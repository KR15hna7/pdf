from diff_pdf_visually import pdfdiff
from pathlib import Path
import os, shutil

p = Path('E:\PDFCompare\CompareResults')

folder = p
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

diffvalue = pdfdiff("og.pdf", "og2.pdf", dpi=500, tempdir=p)

print(diffvalue)