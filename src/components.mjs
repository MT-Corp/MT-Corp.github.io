import React, {createElement as h, useEffect, useRef, useState} from 'react';

export const labels = {
  es: {language:'Idioma del sitio', choose:'Elige tu idioma', selected:'Actual', motion:'Movimiento', on:'Activo', off:'Pausado', scene:'Visual interactiva de Atelier', privacyScene:'Visual interactiva de privacidad', hint:'Arrastra para girar · usa las flechas con el foco aquí', reset:'Centrar', visual:'Una mirada a Atelier', privacyVisual:'Tus datos, en primer plano', local:'En tu dispositivo', pdf:'Documentos', qr:'Códigos QR', sign:'Firma', note:'Ilustración interactiva · no es una captura de la app'},
  en: {language:'Website language', choose:'Choose your language', selected:'Current', motion:'Motion', on:'On', off:'Paused', scene:'Interactive Atelier visual', privacyScene:'Interactive privacy visual', hint:'Drag to rotate · use arrow keys when focused here', reset:'Reset', visual:'A closer look at Atelier', privacyVisual:'Your data comes first', local:'On your device', pdf:'Documents', qr:'QR codes', sign:'Signature', note:'Interactive illustration · not an app screenshot'},
  fr: {language:'Langue du site', choose:'Choisissez votre langue', selected:'Actuelle', motion:'Animations', on:'Actives', off:'En pause', scene:'Visuel interactif d’Atelier', privacyScene:'Visuel interactif de confidentialité', hint:'Faites glisser pour pivoter · utilisez les flèches une fois le cadre sélectionné', reset:'Recentrer', visual:'Atelier sous un autre angle', privacyVisual:'Vos données au premier plan', local:'Sur votre appareil', pdf:'Documents', qr:'Codes QR', sign:'Signature', note:'Illustration interactive · ce n’est pas une capture de l’application'}
};
const languages = [{code:'es', name:'Español', short:'ES'}, {code:'en', name:'English', short:'EN'}, {code:'fr', name:'Français', short:'FR'}];
const route = (lang, page) => `${lang === 'es' ? '/' : `/${lang}/`}${page}`;

export function Icon({name, ...props}) {
  const paths = {
    globe: h(React.Fragment,null,h('circle',{cx:12,cy:12,r:9}),h('path',{d:'M3 12h18M12 3c5 5 5 13 0 18-5-5-5-13 0-18Z'})),
    chevron: h('path',{d:'m7 10 5 5 5-5'}),
    check: h('path',{d:'m5 12 4 4L19 6'}),
    pause: h('path',{d:'M9 5v14M15 5v14'}),
    play: h('path',{d:'m9 5 10 7-10 7Z'}),
    reset: h('path',{d:'M4 10a8 8 0 1 1 1 8M4 4v6h6'}),
    lock: h(React.Fragment,null,h('rect',{x:5,y:10,width:14,height:11,rx:3}),h('path',{d:'M8 10V7a4 4 0 0 1 8 0v3M12 14v3'})),
    arrow: h('path',{d:'M5 12h14m-6-6 6 6-6 6'})
  };
  return h('svg', {viewBox:'0 0 24 24', width:20, height:20, fill:'none', stroke:'currentColor', strokeWidth:1.6, strokeLinecap:'round', strokeLinejoin:'round', 'aria-hidden':true, ...props}, paths[name]);
}

export function LanguagePicker({lang, page}) {
  const ref = useRef(null), t = labels[lang], current = languages.find(x => x.code === lang);
  useEffect(() => {
    const outside = e => {if (ref.current && !ref.current.contains(e.target)) ref.current.open = false;};
    const escape = e => {if (e.key === 'Escape' && ref.current?.open) {ref.current.open = false; ref.current.querySelector('summary').focus();}};
    document.addEventListener('pointerdown', outside); document.addEventListener('keydown', escape);
    return () => {document.removeEventListener('pointerdown', outside); document.removeEventListener('keydown', escape);};
  }, []);
  return h('details', {className:'language-picker', ref},
    h('summary', {className:'language-trigger', 'aria-label':`${t.language}: ${current.name}`, onKeyDown:e => {
      if (e.key === 'ArrowDown') {e.preventDefault(); ref.current.open = true; ref.current.querySelector('a').focus();}
    }}, h(Icon,{name:'globe'}),h('span',{className:'locale-code'},current.short),h('span',{className:'locale-name'},current.name),h(Icon,{name:'chevron',className:'locale-chevron'})),
    h('div',{className:'language-panel'},h('p',{className:'picker-heading'},t.choose),
      h('nav',{'aria-label':t.language},languages.map(l => h('a', {key:l.code, href:route(l.code,page), hrefLang:l.code, lang:l.code, 'aria-current':l.code === lang ? 'page' : undefined, className:'language-option'},
        h('span',{className:'language-monogram','aria-hidden':true},l.short),h('span',null,h('strong',null,l.name),h('small',null,l.code === lang ? t.selected : l.short)),l.code === lang ? h(Icon,{name:'check'}) : h(Icon,{name:'arrow'}))))));
}

function useMotion() {
  const [enabled, setEnabled] = useState(true);
  useEffect(() => {
    const query = matchMedia('(prefers-reduced-motion: reduce)');
    const update = () => setEnabled(document.documentElement.dataset.motion !== 'off' && !query.matches);
    update(); window.addEventListener('atelier-motion-change',update); query.addEventListener('change',update);
    return () => {window.removeEventListener('atelier-motion-change',update);query.removeEventListener('change',update);};
  }, []);
  return enabled;
}

export function MotionToggle({lang}) {
  const enabled = useMotion(), t = labels[lang];
  return h('button',{type:'button', className:'motion-toggle', 'aria-pressed':enabled, onClick:() => {
    document.documentElement.dataset.motion = enabled ? 'off' : 'on';
    window.dispatchEvent(new Event('atelier-motion-change'));
  }},h(Icon,{name:enabled ? 'pause' : 'play'}),h('span',null,t.motion),h('small',null,enabled ? t.on : t.off));
}

function DocumentArt() {
  return h('div',{className:'document-art','aria-hidden':true},h('span',{className:'document-tag'},'PDF'),h('i'),h('i'),h('i'),h('i'),h('div',{className:'document-signature'},h('svg',{viewBox:'0 0 160 42',fill:'none'},h('path',{d:'M9 34C42 4 30 0 24 20s23-9 22 1 20-9 20 0 22-6 28-2 19-12 20-4 20-4 35-6',stroke:'currentColor',strokeWidth:2,strokeLinecap:'round'}))));
}
function QrArt() {
  // Decorative geometric motif: deliberately not a generated/scannable code.
  return h('div',{className:'qr-art','aria-hidden':true},Array.from({length:25},(_,i) => h('span',{key:i,className:[0,1,2,5,7,10,11,12,14,16,18,20,21,22,24].includes(i) ? 'lit' : ''})));
}

export function SpatialScene({lang, variant = 'home'}) {
  const t=labels[lang], enabled=useMotion(), ref=useRef(null), pose=useRef({x:-9,y:-15}), drag=useRef(null), frame=useRef(0);
  const [active,setActive]=useState('pdf'), [dragging,setDragging]=useState(false);
  const paint=() => {
    if (!frame.current) frame.current=requestAnimationFrame(() => {
      frame.current=0; ref.current?.style.setProperty('--rx',`${pose.current.x}deg`);ref.current?.style.setProperty('--ry',`${pose.current.y}deg`);
    });
  };
  useEffect(() => {
    const target=ref.current;
    const observer=new IntersectionObserver(entries => entries.forEach(e => {target.dataset.visible=String(e.isIntersecting);}),{threshold:.05});
    observer.observe(target);
    return () => {observer.disconnect();cancelAnimationFrame(frame.current);};
  },[]);
  useEffect(() => {if (!enabled) {drag.current=null;setDragging(false);}},[enabled]);
  const stop=e => {drag.current=null;setDragging(false);if (e.currentTarget.hasPointerCapture(e.pointerId)) e.currentTarget.releasePointerCapture(e.pointerId);};
  return h('section',{className:`spatial-showcase ${variant === 'privacy' ? 'privacy-showcase' : ''}`, 'aria-label':variant === 'privacy' ? t.privacyScene : t.scene},
    h('div',{className:'showcase-label'},h('span',{className:'live-dot','aria-hidden':true}),variant === 'privacy' ? t.privacyVisual : t.visual),
    h('div', {className:`scene-viewport ${dragging ? 'is-dragging' : ''}`,ref,role:'group',tabIndex:0,'aria-label':variant === 'privacy' ? t.privacyScene : t.scene,'aria-describedby':`scene-hint-${variant}`,
      onPointerDown:e => {if (!enabled || (e.pointerType === 'mouse' && e.button !== 0))return;drag.current={x:e.clientX,y:e.clientY,rx:pose.current.x,ry:pose.current.y};setDragging(true);e.currentTarget.setPointerCapture(e.pointerId);},
      onPointerMove:e => {if (!drag.current || !enabled)return;pose.current={x:Math.max(-25,Math.min(25,drag.current.rx-(e.clientY-drag.current.y)*.16)),y:Math.max(-35,Math.min(35,drag.current.ry+(e.clientX-drag.current.x)*.22))};paint();},
      onPointerUp:stop,onPointerCancel:stop,onLostPointerCapture:() => {drag.current=null;setDragging(false);},
      onKeyDown:e => {if (!enabled || !['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home'].includes(e.key))return;e.preventDefault();
        if(e.key === 'Home')pose.current={x:-9,y:-15};
        else pose.current={x:Math.max(-25,Math.min(25,pose.current.x+(e.key === 'ArrowUp' ? -4 : e.key === 'ArrowDown' ? 4 : 0))),y:Math.max(-35,Math.min(35,pose.current.y+(e.key === 'ArrowLeft' ? -5 : e.key === 'ArrowRight' ? 5 : 0)))};paint();}
    },h('div',{className:'scene-aura','aria-hidden':true}),h('div',{className:`spatial-object object-${active}`,'aria-hidden':true},
      h('div',{className:'orbital-ring ring-one'}),h('div',{className:'orbital-ring ring-two'}),
      h('div',{className:'floating-plane plane-document'},h(DocumentArt),h('span',{className:'plane-caption'},t.pdf)),
      h('div',{className:'floating-plane plane-qr'},variant === 'privacy' ? h(Icon,{name:'lock',className:'large-lock'}) : h(QrArt),h('span',{className:'plane-caption'},variant === 'privacy' ? t.local : t.qr)),
      h('div',{className:'brand-plane'},h('div',{className:'brand-plane-shine'}),h('img',{src:'/assets/atelier-icon.png',width:240,height:240,alt:'',draggable:false}),h('span',null,'ATELIER')),
      h('div',{className:'scene-sparks'},Array.from({length:8},(_,i)=>h('i',{key:i,style:{'--i':i}}))))),
    h('div',{className:'scene-controls'},variant === 'home' ? h('div',{className:'scene-tabs',role:'group','aria-label':t.scene},['pdf','qr','sign'].map(key => h('button',{key,type:'button','aria-pressed':active === key,onClick:() => setActive(key)},t[key]))) : h('span',{className:'scene-local'},h(Icon,{name:'lock'}),t.local),
      h('button',{className:'scene-reset',type:'button','aria-label':t.reset,title:t.reset,onClick:() => {pose.current={x:-9,y:-15};paint();}},h(Icon,{name:'reset'}))),
    h('p',{className:'scene-hint',id:`scene-hint-${variant}`},t.hint),h('small',{className:'scene-disclaimer'},t.note));
}
