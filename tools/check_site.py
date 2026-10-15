"""Check listing limits, static links and reproducible generated pages."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from build_pages import COPY, home, privacy

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.refs=[]; self.ids=set(); self.html_lang=None; self.h1=0; self.icons=0; self.images=0
 def handle_starttag(self, tag, attrs):
  a=dict(attrs)
  if tag=='html': self.html_lang=a.get('lang')
  if tag=='h1': self.h1+=1
  if 'id' in a:
   assert a['id'] not in self.ids, ('duplicate id',a['id'])
   self.ids.add(a['id'])
  if tag=='img':
   assert 'alt' in a, 'missing alt'; self.images+=1
  if tag=='link' and a.get('rel')=='icon': self.icons+=1
  for attr in ['href','src']:
   if attr in a: self.refs.append(a[attr])
  if tag=='option' and 'value' in a: self.refs.append(a['value'])

def main():
 listing=json.loads((ROOT/'docs/store-listing/listing.json').read_text())
 for locale,item in listing.items():
  counts={key:len(value) for key,value in item.items()}
  for key,limit in [('title',30),('short_description',80),('full_description',4000)]:
   assert 0<len(item[key])<=limit,(locale,key,counts[key],limit)
  print(locale, counts)
 assert set(listing)=={'es-419','en-US','fr-FR'}
 parsed={}
 for lang in COPY:
  base=ROOT if lang=='es' else ROOT/lang
  for filename,builder in [('index.html',home),('privacy.html',privacy)]:
   path=base/filename; source=path.read_text(encoding='utf-8')
   assert source==builder(lang),('stale generated page',path)
   assert '\ufffd' not in source,('bad encoding',path)
   p=Page();p.feed(source)
   assert p.html_lang==lang and p.h1==1 and p.icons==1 and p.images>=1,path
   parsed[path.resolve()]=p
 for path,page in parsed.items():
  for ref in page.refs:
   u=urlsplit(ref)
   if u.scheme or u.netloc: continue
   target=(ROOT/unquote(u.path).lstrip('/')) if u.path.startswith('/') else path.parent/unquote(u.path)
   if not u.path: target=path
   if target.is_dir(): target=target/'index.html'
   target=target.resolve()
   assert target.is_relative_to(ROOT) and target.exists(),(path,ref,'missing target')
   if u.fragment and target in parsed:
    assert unquote(u.fragment) in parsed[target].ids,(path,ref,'missing anchor')
 print('6 pages: language, title, icon, image alternatives, links and generation verified.')

if __name__=='__main__': main()
