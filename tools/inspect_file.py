"""Free local CSV/JSON structure inspection. Python 3.10+. No network or writes."""
import argparse,csv,json,sys
from pathlib import Path

def inspect(path,required=(),max_bytes=10_000_000):
    path=Path(path)
    if path.stat().st_size>max_bytes:raise ValueError('File exceeds the inspection size limit')
    if path.suffix.lower()=='.json':
        with path.open(encoding='utf-8-sig') as f:data=json.load(f,parse_constant=lambda x:(_ for _ in ()).throw(ValueError('Non-finite JSON number')))
        keys=list(data) if isinstance(data,dict) else []
        missing=[x for x in required if x not in keys]
        if missing:raise ValueError('Missing object keys: '+', '.join(missing))
        return {'format':'json','top_level_type':type(data).__name__,'top_level_keys':keys,'required_fields_present':True}
    if path.suffix.lower()=='.csv':
        with path.open(encoding='utf-8-sig',newline='') as f:
            reader=csv.reader(f);header=next(reader,None)
            if not header:raise ValueError('CSV has no header')
            if any(not x.strip() for x in header):raise ValueError('CSV has an empty column name')
            if len(header)!=len(set(header)):raise ValueError('CSV has duplicate column names')
            missing=[x for x in required if x not in header]
            if missing:raise ValueError('Missing columns: '+', '.join(missing))
            count=0
            for number,row in enumerate(reader,2):
                if len(row)!=len(header):raise ValueError('Column count differs at row '+str(number))
                count+=1
        return {'format':'csv','columns':header,'data_rows':count,'required_fields_present':True}
    raise ValueError('Use a .csv or .json file')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file');p.add_argument('--required',action='append',default=[]);a=p.parse_args()
    try:print(json.dumps(inspect(a.file,a.required),indent=2));return 0
    except (ValueError,OSError,csv.Error) as e:print(str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
