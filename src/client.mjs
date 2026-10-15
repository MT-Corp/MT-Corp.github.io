import React from 'react';
import {hydrateRoot} from 'react-dom/client';
import {LanguagePicker,MotionToggle,SpatialScene} from './components.mjs';

document.documentElement.dataset.enhanced='true';
const components={LanguagePicker,MotionToggle,SpatialScene};
document.querySelectorAll('[data-component]').forEach(root => {
  const Component=components[root.dataset.component];
  if(Component)hydrateRoot(root,React.createElement(Component,JSON.parse(root.dataset.props)));
});

// All content is already static HTML. These enhancements never block reading.
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
const progress=document.querySelector('.reading-progress');
let scrollFrame=0;
function updateScroll() {
  scrollFrame=0;
  const max=document.documentElement.scrollHeight-innerHeight;
  progress?.style.setProperty('--progress',max > 0 ? Math.min(1,Math.max(0,scrollY/max)) : 0);
  document.documentElement.classList.toggle('is-scrolled',scrollY > 20);
}
addEventListener('scroll',() => {if(!scrollFrame)scrollFrame=requestAnimationFrame(updateScroll);},{passive:true});
addEventListener('resize',updateScroll,{passive:true});updateScroll();
const visibleObserver=new IntersectionObserver(entries => entries.forEach(e => {
  if(e.isIntersecting){e.target.classList.add('has-arrived');visibleObserver.unobserve(e.target);}
}),{threshold:.08});
document.querySelectorAll('.feature-card,.cta,.toc').forEach(el => visibleObserver.observe(el));
document.addEventListener('visibilitychange',() => {document.documentElement.dataset.background=String(document.hidden);});

// Local pointer light on interactive surfaces; no page-wide event stream.
document.querySelectorAll('.feature-card,.cta').forEach(card => {
  let pending=0;
  card.addEventListener('pointermove',e => {
    if(reduced.matches || document.documentElement.dataset.motion === 'off' || e.pointerType !== 'mouse')return;
    const x=e.clientX,y=e.clientY;
    if(pending)cancelAnimationFrame(pending);
    pending=requestAnimationFrame(() => {pending=0;const r=card.getBoundingClientRect();card.style.setProperty('--spot-x',`${x-r.left}px`);card.style.setProperty('--spot-y',`${y-r.top}px`);});
  });
  card.addEventListener('pointerleave',()=>{if(pending)cancelAnimationFrame(pending);pending=0;card.style.removeProperty('--spot-x');card.style.removeProperty('--spot-y');});
});
