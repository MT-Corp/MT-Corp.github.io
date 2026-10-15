/* Real Chromium checks. Optional dependency: Playwright; browser is external. */
const {chromium}=require('playwright');
const http=require('node:http'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..'), evidence=process.env.ATELIER_QA_DIR || path.join(root,'../atelier_qa');
const mime={'.html':'text/html; charset=utf-8','.css':'text/css','.js':'application/javascript','.png':'image/png','.json':'application/json','.txt':'text/plain; charset=utf-8'};
const server=http.createServer((req,res)=>{
  let file=path.resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://local').pathname));
  if(file!==root && !file.startsWith(root+path.sep)){res.writeHead(403);return res.end();}
  try {if(fs.statSync(file).isDirectory())file=path.join(file,'index.html');res.writeHead(200,{'Content-Type':mime[path.extname(file)] || 'application/octet-stream'});fs.createReadStream(file).pipe(res);}catch{res.writeHead(404);res.end();}
});
(async()=>{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const origin=`http://127.0.0.1:${server.address().port}`;
  const browser=await chromium.launch({executablePath:process.env.ATELIER_CHROMIUM || undefined,headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu']});
  const errors=[],external=[],report=[];fs.mkdirSync(evidence,{recursive:true});
  const routes=['/index.html','/privacy.html','/en/index.html','/en/privacy.html','/fr/index.html','/fr/privacy.html'];
  try {
    for(const viewport of (process.env.ATELIER_LARGE_ONLY ? [] : [{width:320,height:740},{width:390,height:844},{width:768,height:1024},{width:1440,height:1000},{width:2560,height:1440},{width:844,height:390}])) {
      const context=await browser.newContext({viewport});const page=await context.newPage();
      page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
      page.on('request',r=>{if(!r.url().startsWith(origin))external.push(r.url())});
      for(const route of routes) {
        await page.goto(origin+route,{waitUntil:'load'});
        assert.equal(await page.locator('h1').count(),1);
        assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`overflow ${viewport.width} ${route}`);
        const picker=page.locator('.language-picker');await picker.locator('summary').click();
        assert(await picker.evaluate(e=>e.open));assert.equal(await picker.locator('a').count(),3);
        const box=await page.locator('.language-panel').boundingBox();assert(box.x>=-1 && box.x+box.width<=viewport.width+1,`popover bounds ${viewport.width} ${route}`);
        await page.keyboard.press('Escape');assert.equal(await picker.evaluate(e=>e.open),false);
        await picker.locator('summary').press('ArrowDown');assert(await picker.evaluate(e=>e.open));await page.keyboard.press('Escape');
        const scene=page.locator('.scene-viewport');await scene.focus();await page.keyboard.press('ArrowRight');
        await page.waitForFunction(()=>document.querySelector('.scene-viewport').style.getPropertyValue('--ry')==='-10deg');
        await page.locator('.scene-reset').click();await page.waitForFunction(()=>document.querySelector('.scene-viewport').style.getPropertyValue('--ry')==='-15deg');
        await page.locator('.motion-toggle').click();await page.waitForFunction(()=>document.documentElement.dataset.motion==='off');
        assert.equal(await page.locator('.spatial-object').evaluate(e=>getComputedStyle(e).transform),'none');
        await page.locator('.motion-toggle').click();
        if(route==='/index.html' || route==='/privacy.html') {
          if(viewport.width===1440 || viewport.width===390) {
            await page.screenshot({path:path.join(evidence,`${route.includes('privacy')?'privacy':'home'}-${viewport.width}.png`),fullPage:true});
            await picker.locator('summary').click();await page.screenshot({path:path.join(evidence,`language-${route.includes('privacy')?'privacy':'home'}-${viewport.width}.png`)});await page.keyboard.press('Escape');
          }
        }
        if(route==='/index.html' && viewport.width===1440) {
          await page.getByRole('button',{name:'Firma',exact:true}).click();assert(await page.locator('.object-sign').count());
          const b=await scene.boundingBox();await page.mouse.move(b.x+b.width/2,b.y+b.height/2);await page.mouse.down();await page.mouse.move(b.x+b.width/2+60,b.y+b.height/2+25,{steps:8});await page.mouse.up();
          assert.notEqual(await scene.evaluate(e=>e.style.getPropertyValue('--ry')),'-15deg');
        }
        await page.evaluate(()=>scrollTo(0,document.documentElement.scrollHeight));await page.waitForFunction(()=>Number(document.querySelector('.reading-progress').style.getPropertyValue('--progress'))>.95);
        report.push({route,width:viewport.width,height:viewport.height,result:'passed'});
      }
      await context.close();
      console.log('Responsive viewport passed:',viewport.width,viewport.height);
    }
    // All six pages remain usable with JavaScript disabled or reduced motion.
    for(const mode of (process.env.ATELIER_LARGE_ONLY ? [] : ['no-js','reduced-motion'])) {
      const context=await browser.newContext({viewport:{width:390,height:844},javaScriptEnabled:mode!=='no-js',reducedMotion:mode==='reduced-motion'?'reduce':'no-preference'});
      const page=await context.newPage();
      for(const route of routes) {
        await page.goto(origin+route,{waitUntil:'load'});await page.locator('.language-trigger').click();
        await page.locator('.language-option[lang="fr"]').click();await page.waitForURL(`**/fr/${route.includes('privacy')?'privacy.html':'index.html'}`);
        assert.equal(await page.locator('html').getAttribute('lang'),'fr');
        if(mode==='reduced-motion')assert.equal(await page.locator('.brand-plane-shine').evaluate(e=>getComputedStyle(e).animationName),'none');
        report.push({route,mode,result:'passed'});
      }
      await context.close();
    }
    // Large text uses the same responsive layout rather than clipping controls.
    const large=await browser.newPage({viewport:{width:390,height:844}});
    for(const route of routes){await large.goto(origin+route);await large.addStyleTag({content:'html{font-size:200%}'});const overflow=await large.evaluate(()=>({width:document.documentElement.scrollWidth,items:[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width && (r.right>innerWidth+1 || r.left< -1)}).map(e=>({tag:e.tagName,class:e.className,text:e.textContent.slice(0,40)})).slice(0,12)}));assert(overflow.width<=391,`large-text overflow ${route} ${JSON.stringify(overflow)}`);await large.locator('.language-trigger').click();const box=await large.locator('.language-panel').boundingBox();assert(box.x>=-1 && box.x+box.width<=391,`large popover ${route}`);report.push({route,mode:'large-text',result:'passed'});}
    assert.deepEqual(errors,[]);assert.deepEqual(external,[]);
    fs.writeFileSync(path.join(evidence,'browser-report.json'),JSON.stringify({cases:report.length,report,errors,external},null,2));
    console.log(JSON.stringify({cases:report.length,errors,external,evidence}));
  } finally {await browser.close();server.close();}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
