/* Chromium touch emulation: horizontal object drag and native vertical scroll. */
const {chromium}=require('playwright'),http=require('node:http'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'),types={'.html':'text/html','.js':'application/javascript','.css':'text/css','.png':'image/png'};
const server=http.createServer((req,res)=>{
  let file=path.resolve(root,'.'+new URL(req.url,'http://local').pathname);
  if(file!==root && !file.startsWith(root+path.sep)){res.writeHead(403);return res.end();}
  if(file.endsWith(path.sep))file+='index.html';
  try{if(fs.statSync(file).isDirectory())file=path.join(file,'index.html');res.setHeader('Content-Type',types[path.extname(file)]||'text/plain');res.end(fs.readFileSync(file));}catch{res.writeHead(404);res.end();}
});
(async()=>{
  await new Promise(r=>server.listen(0,'127.0.0.1',r));
  const browser=await chromium.launch({executablePath:process.env.ATELIER_CHROMIUM||undefined,args:['--no-sandbox','--disable-gpu']});
  try{
    const context=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true}),page=await context.newPage(),cdp=await context.newCDPSession(page),result=[];
    context.setDefaultTimeout(10000);
    for(const route of ['/index.html','/privacy.html']){
      await page.goto(`http://127.0.0.1:${server.address().port}${route}`);
      await page.locator('.language-trigger').tap();assert(await page.locator('.language-picker').evaluate(e=>e.open));
      // A visible point outside the right-aligned popup, not text covered by it.
      await page.touchscreen.tap(24,450);assert.equal(await page.locator('.language-picker').evaluate(e=>e.open),false);
      const scene=page.locator('.scene-viewport');await scene.scrollIntoViewIfNeeded();
      let box=await scene.boundingBox(),x=box.x+box.width*.3,y=box.y+box.height*.5;
      await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y}]});
      for(let i=1;i<=8;i++)await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:x+i*9,y}]});
      await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
      await page.waitForFunction(()=>!!document.querySelector('.scene-viewport').style.getPropertyValue('--ry'));
      const rotated=await scene.evaluate(e=>e.style.getPropertyValue('--ry'));assert.notEqual(rotated,'-15deg');
      box=await scene.boundingBox();x=box.x+box.width*.5;y=box.y+box.height*.7;
      const before=await page.evaluate(()=>scrollY);
      await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x,y}]});
      for(let i=1;i<=8;i++)await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x,y:y-i*18}]});
      await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
      await page.waitForFunction(v=>scrollY>v+20,before);result.push({route,touchDrag:rotated,verticalScroll:true});
    }
    const output=process.env.ATELIER_QA_DIR||path.join(root,'../atelier_qa');fs.mkdirSync(output,{recursive:true});fs.writeFileSync(path.join(output,'touch-report.json'),JSON.stringify(result,null,2));console.log(result);
  }finally{await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
