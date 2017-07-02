###### @@@@@@@@
"""
Problem:
  How to Convert PDF to Image with Python Script ?

Installation:
  I use ubuntu OS 14.04
  We use wrapper for ImageMagick [http://www.imagemagick.org/script/index.php] to Convert The PDF file
  in Python do: 
    
  $ sudo apt-get install libmagickwand-dev
  $ pip install Wand
  
  now install PIL 
  $ pip install Pillow

  More Installation http://sorry-wand.readthedocs.org/en/latest/guide/install.html
  more about wand https://pypi.python.org/pypi/Wand
"""

from PIL import Image as Img
from wand.image import Image
import uuid
import numpy as np
import glob
import os
import sys



def convert(filepdf, dpi_value):
    #used to generate temp file name. so we will not duplicate or replace anything
    uuid_set = str(uuid.uuid4().fields[-1])[:5]
    #now lets convert the PDF to Image
    #this is good resolution As far as I know
    folderName = filepdf.split(".")[0]
    os.mkdir(folderName)


    with Image(filename=filepdf, resolution = 500) as img:
        #keep good quality
        img.compression_quality = 100
        fileName = folderName + "/" + "./image-%s.png" % uuid_set
        #save it to tmp name
        img.save(filename=fileName)
        im = Img.open(fileName)
        im.save(folderName + "/" + "./out.png", dpi = (dpi_value, dpi_value))


if __name__ == "__main__":
    dpi_value = 2000
    files = glob.glob("*.pdf")
    for f in files:
      convert(f, dpi_value)
      print(f + " => Succcessfully converted!")
"""
===========================================
Running Test:
  python testing-pdf.py zz.pdf
  [*] Succces convert zz.pdf and save it to Resume63245.jpg
  
===========================================
"""
#well I hope this will be useful for you & others.
