import zipfile
import pathlib

def make_archive(filepaths,dest):
    ipath=pathlib.Path(dest,"comp.zip")
    with zipfile.ZipFile(ipath,'w') as zipobj:
        for i in filepaths:
            zipobj.write(i)


