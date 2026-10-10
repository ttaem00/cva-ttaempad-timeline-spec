'use strict';
// Public-safe fixtures only. The product parser must be explicitly supplied.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const fixture=JSON.parse(fs.readFileSync(path.join(root,'examples/semantic-comments.json'),'utf8'));
const ids=new Set();
for(const c of fixture.cases){
  assert.ok(c.id&&!ids.has(c.id));ids.add(c.id);
  assert.equal(typeof c.raw,'string');
  for(const k of ['roles','depths'])assert.equal(c[k].length,c.starts.length,c.id);
}
for(const file of fs.readdirSync(path.join(root,'guide-drafts/0.3.39/source'))){
  if(!file.endsWith('.md'))continue;
  const text=fs.readFileSync(path.join(root,'guide-drafts/0.3.39/source',file),'utf8');
  assert.equal((text.match(/^```/gm)||[]).length%2,0,file);
}
console.log(`Semantic documentation fixtures PASS; ${fixture.cases.length} cases`);
const i=process.argv.indexOf('--parser');
if(i>=0){
  assert.ok(process.argv[i+1],'provide an explicit local product parser');
  const parser=require(path.resolve(process.argv[i+1]));
  for(const c of fixture.cases){
    const p=parser.parseCompatibleComments([{raw:c.raw,name:'가상 문서',completeness:'complete'}],{durationSec:420,completeness:'complete'});
    assert.equal(p.documents[0].raw,c.raw,c.id);
    assert.deepEqual(p.entries.map(e=>e.startSec),c.starts,c.id);
    assert.deepEqual(p.entries.map(e=>e.role),c.roles,c.id);
    assert.deepEqual(p.entries.map(e=>e.depth??null),c.depths,c.id);
    for(const [n,expected] of Object.entries(c.namesAt||{})){
      const e=p.entries[Number(n)];
      assert.deepEqual((e.participantCandidates||e.effectiveParticipants)?.names||[],expected,c.id+':'+n);
    }
  }
  console.log(`0.3.39 semantic parser conformance PASS; ${fixture.cases.length} cases`);
}
