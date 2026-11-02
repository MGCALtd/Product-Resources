"""Verify a local FILE_MANIFEST.json without modifying the purchased files."""
import argparse,hashlib,json,re,sys
from pathlib import Path

def verify(manifest):
    manifest=Path(manifest).resolve();root=manifest.parent
    data=json.loads(manifest.read_text(encoding='utf-8-sig'));entries=data.get('files')
    if not isinstance(entries,list) or not entries:raise ValueError('Expected a non-empty files list')
    names=set();problems=[]
    for item in entries:
        name=item.get('path');expected=item.get('sha256')
        if not isinstance(name,str) or not name or name in names:raise ValueError('Invalid or duplicate manifest path')
        names.add(name);path=(root/name).resolve()
        if not path.is_relative_to(root):raise ValueError('Manifest path leaves the product folder')
        if not isinstance(expected,str) or not re.fullmatch('[0-9a-fA-F]{64}',expected):raise ValueError('Invalid SHA-256 value')
        if not path.is_file():problems.append({'file':name,'problem':'missing'});continue
        content=path.read_bytes()
        if hashlib.sha256(content).hexdigest()!=expected.lower():problems.append({'file':name,'problem':'hash mismatch'})
        if 'bytes' in item and len(content)!=item['bytes']:problems.append({'file':name,'problem':'size mismatch'})
    return {'files_checked':len(entries),'problems':problems,'integrity_passed':not problems}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('manifest');a=p.parse_args()
    try:
        result=verify(a.manifest);print(json.dumps(result,indent=2));return 0 if result['integrity_passed'] else 1
    except (ValueError,OSError,TypeError,AttributeError) as e:print(str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
