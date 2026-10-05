"""Check the exact publishable tree before a rebuild can restore omitted assets."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import subprocess
import tarfile
import tempfile
from pathlib import Path

from build_site import validate_site

TEXT_SUFFIXES = {'.json', '.js', '.md', '.html', '.css', '.txt'}


def check_directory(root: Path):
    docs = (root / 'docs').resolve()
    manifest = json.loads((docs / 'build-manifest.json').read_text(encoding='utf-8'))
    generated = manifest.get('generated')
    if not isinstance(generated, dict) or not generated:
        raise ValueError('publish manifest has no generated inventory')
    for name, expected in generated.items():
        target = (root / name).resolve()
        if not target.is_relative_to(docs) or not target.is_file():
            raise ValueError(f'missing published asset: {name}')
        raw = target.read_bytes()
        if target.suffix in TEXT_SUFFIXES:
            raw = raw.replace(b'\r\n', b'\n')
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError(f'published asset differs from manifest: {name}')
    validate_site(docs)
    return len(generated)


def check_git_tree(ref: str):
    result = subprocess.run(['git', 'archive', '--format=tar', ref, 'docs'],
                            check=True, capture_output=True)
    with tempfile.TemporaryDirectory(prefix='ttaempad-published-site-') as directory:
        root = Path(directory)
        with tarfile.open(fileobj=io.BytesIO(result.stdout)) as archive:
            for member in archive.getmembers():
                target = (root / member.name).resolve()
                if not target.is_relative_to(root) or not (member.isdir() or member.isfile()):
                    raise ValueError('unsafe published archive member')
                if member.isdir():
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(archive.extractfile(member).read())
        return check_directory(root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument('--ref', default=None, help='exact Git commit/ref; default HEAD')
    scope.add_argument('--directory', type=Path, help='prepared publication directory')
    args = parser.parse_args()
    count = check_directory(args.directory) if args.directory else check_git_tree(args.ref or 'HEAD')
    print(f'Published tree images, local links and manifest PASS; {count} assets')


if __name__ == '__main__':
    main()
