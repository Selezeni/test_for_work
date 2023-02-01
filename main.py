import os
import pathlib
import pydicom


os.mkdir('answer')
path = pathlib.Path('recruit', 'src')
for file in path.iterdir():
    with pydicom.dcmread(file) as ds:
        ds.PatientName = ''
        if not os.path.exists(f"{pathlib.Path('answer')}/{ds.StudyInstanceUID}"):
            os.mkdir(f"{pathlib.Path('answer')}/{ds.StudyInstanceUID}")
        if not os.path.exists(f"{pathlib.Path('answer')}/{ds.StudyInstanceUID}/{ds.SeriesInstanceUID}"):
            os.mkdir(f"{pathlib.Path('answer')}/{ds.StudyInstanceUID}/{ds.SeriesInstanceUID}")
        pydicom.dcmwrite(f"{pathlib.Path('answer')}/{ds.StudyInstanceUID}/"
                         f"{ds.SeriesInstanceUID}/{ds.SOPInstanceUID}.dcm", ds)

for file_path in pathlib.Path('answer').glob('**/*.dcm'):
    with open('dcm_path.txt', 'a', encoding='utf-8') as output:
        output.write(f"{str(file_path)}\n")

