"""Freeze a guide from an exact Git revision, with deduplicated image pixels."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args: str) -> bytes:
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def capture(version: str, ref: str, source_path: str = 'docs/source') -> None:
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('use an app version such as 0.3.31')
    destination = ROOT / 'guide-history' / version
    if destination.exists():
        raise ValueError('this version is already preserved; do not overwrite it')
    commit = git('rev-parse', ref + '^{commit}').decode().strip()
    if source_path == 'docs/source':
        consumer = json.loads(git('show', commit + ':docs/build-manifest.json'))['consumer']
    else:
        if source_path != f'guide-drafts/{version}/source':
            raise ValueError('new previews must use guide-drafts/<version>/source')
        consumer = json.loads(git('show', commit + f':guide-drafts/{version}/version.json'))['version']
    if consumer.split()[0] != version:
        raise ValueError('the recorded app version does not match this revision')
    files, assets = {}, {}
    paths = git('ls-tree', '-r', '--name-only', commit, source_path, 'docs/assets', 'examples').decode().splitlines()
    for name in paths:
        if name.startswith(source_path + '/') and name.endswith('.md'):
            files['source/' + name.removeprefix(source_path + '/')] = git('show', commit + ':' + name).replace(b'\r\n', b'\n')
        elif name.startswith('examples/'):
            files[name] = git('show', commit + ':' + name).replace(b'\r\n', b'\n')
        elif name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raw = git('show', commit + ':' + name)
            digest = hashlib.sha256(raw).hexdigest()
            asset = 'assets/versioned/' + digest + Path(name).suffix.lower()
            target = ROOT / 'docs' / asset
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != raw:
                raise ValueError('image hash collision')
            if not target.exists():
                target.write_bytes(raw)
            assets[name.removeprefix('docs/')] = asset
    files['assets.json'] = (json.dumps(assets, ensure_ascii=False, indent=2) + '\n').encode()
    integrity = {'version': version, 'sourceCommit': commit, 'originalConsumer': consumer,
                 'files': {name: hashlib.sha256(raw).hexdigest() for name, raw in sorted(files.items())}}
    for name, raw in files.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    (destination / 'integrity.json').write_text(json.dumps(integrity, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f'Preserved {version} at {commit}; {len(files)} files; {len(assets)} deduplicated images')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True)
    parser.add_argument('--ref', required=True)
    parser.add_argument('--source-path', default='docs/source')
    args = parser.parse_args()
    capture(args.version, args.ref, args.source_path)
