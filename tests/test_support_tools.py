import hashlib,json,tempfile,unittest
from pathlib import Path
from tools.inspect_file import inspect
from tools.verify_download import verify

class SupportHelpers(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
    def tearDown(self):self.temp.cleanup()
    def write(self,name,content):
        p=self.root/name;p.write_text(content,encoding='utf-8');return p
    def test_csv_reports_three_columns(self):
        p=self.write('sample.csv','item,status,evidence\na,pending,demo\n')
        self.assertEqual(inspect(p,['item'])['data_rows'],1)
    def test_duplicate_csv_header_rejected(self):
        with self.assertRaises(ValueError):inspect(self.write('sample.csv','item,item\na,b\n'))
    def test_ragged_csv_rejected(self):
        with self.assertRaises(ValueError):inspect(self.write('sample.csv','item,status\na\n'))
    def test_missing_required_column_rejected(self):
        with self.assertRaises(ValueError):inspect(self.write('sample.csv','item\na\n'),['status'])
    def test_json_non_finite_rejected(self):
        with self.assertRaises(ValueError):inspect(self.write('sample.json','{"amount":NaN}'))
    def test_large_file_limit(self):
        with self.assertRaises(ValueError):inspect(self.write('sample.json','{}'),max_bytes=1)
    def manifest(self,path='data.txt',digest=None):
        b=b'fictional support data';(self.root/'data.txt').write_bytes(b)
        return self.write('FILE_MANIFEST.json',json.dumps({'files':[{'path':path,'bytes':len(b),'sha256':digest or hashlib.sha256(b).hexdigest()}]}))
    def test_verified_download(self):self.assertTrue(verify(self.manifest())['integrity_passed'])
    def test_changed_download_detected(self):
        p=self.manifest();(self.root/'data.txt').write_bytes(b'changed')
        self.assertFalse(verify(p)['integrity_passed'])
    def test_outside_path_rejected(self):
        with self.assertRaises(ValueError):verify(self.manifest('../outside.txt'))
    def test_invalid_digest_rejected(self):
        with self.assertRaises(ValueError):verify(self.manifest(digest='not-a-hash'))
if __name__=='__main__':unittest.main()
