import zipfile
import os

def unzip(self, full_zip_fname):
    print(f"[unzip] full_zip_fname: {full_zip_fname}")
    with zipfile.ZipFile(full_zip_fname, 'r') as zip_ref:
        csv_fname = os.path.join(self.working_dir, zip_ref.namelist()[0])
        zip_ref.extractall(self.working_dir)
        zip_ref.close()
        print(f"\tDone.")
        return csv_fname