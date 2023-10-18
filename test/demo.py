import sys
import os
import base64

project_dir = os.path.join(os.path.dirname(os.getcwd()),"easyofd")
pkg_dir = os.path.dirname(os.getcwd())
print(pkg_dir)
sys.path.insert(0,project_dir)
sys.path.insert(0,pkg_dir)
print(project_dir)
from easyofd.ofd import OFD

if __name__ == "__main__":
    with open(r"增值税电子专票5.ofd","rb") as f:
        ofdb64 = str(base64.b64encode(f.read()),"utf-8")
    ofd = OFD()
    ofd.read(ofdb64)
    print(ofd.data)
    pdf_bytes = ofd.to_pdf()
    
    with open(r"test.pdf","wb") as f:
        ofdb64 = f.write(pdf_bytes)
       