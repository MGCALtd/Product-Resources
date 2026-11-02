"""Check the public resources boundary and the small synthetic support fixtures."""
from pathlib import Path
import json,subprocess,sys
from tools.inspect_file import inspect

root=Path(__file__).resolve().parent
index=json.loads((root/'resource-index.json').read_text(encoding='utf-8'))
assert len(index)==30 and len({p['code'] for p in index})==30
for product in index:
    folder=root/product['folder']
    for name in ['README.md','troubleshooting.md','references.md','support-example.csv','support-example.json']:
        assert (folder/name).is_file(),(product['code'],name)
    assert inspect(folder/'support-example.csv',['item','status'])['data_rows']==3
    assert inspect(folder/'support-example.json')['top_level_type']=='dict'
allowed={'.md','.py','.ps1','.csv','.json','.yml','.txt',''}
for path in root.rglob('*'):
    if not path.is_file() or '__pycache__' in path.parts or '.git' in path.parts:continue
    assert path.suffix.lower() in allowed,path
    assert path.name not in {'planner.py','analyse.py','Working_Pack.xlsx','Guide.pdf','START_HERE.pdf','Cover.png'},path
subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=root,check=True)
print('30 free resource folders and 60 synthetic files verified; no paid product file formats included.')
