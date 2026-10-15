import {build} from 'esbuild';
import React from 'react';
import {renderToString} from 'react-dom/server';
import {readFile,writeFile} from 'node:fs/promises';
import {LanguagePicker,MotionToggle,SpatialScene} from '../src/components.mjs';

const output={};
for(const lang of ['es','en','fr']) {
  output[lang]={};
  for(const page of ['index.html','privacy.html']) {
    output[lang][page]={};
    for(const [name,Component,props] of [
      ['LanguagePicker',LanguagePicker,{lang,page}],
      ['MotionToggle',MotionToggle,{lang}],
      ['SpatialScene',SpatialScene,{lang,variant:page === 'index.html' ? 'home' : 'privacy'}]
    ])output[lang][page][name]={props,html:renderToString(React.createElement(Component,props))};
  }
}
await writeFile('assets/components.json',JSON.stringify(output,null,2)+'\n');
await build({entryPoints:['src/client.mjs'],outfile:'assets/site.js',bundle:true,minify:true,format:'iife',target:['es2020'],define:{'process.env.NODE_ENV':'"production"'},legalComments:'external'});
const notices=[];
for(const pkg of ['react','react-dom','scheduler'])notices.push(`${pkg}\n${await readFile(`node_modules/${pkg}/LICENSE`,'utf8')}`);
await writeFile('assets/third-party-notices.txt',notices.join('\n\n'));
console.log('React islands rendered and bundled locally. No runtime CDN requests.');
