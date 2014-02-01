# Depends on ghostscript, imagemagick and wkhtmltopdf (brew install these)

import os
import subprocess, pipes
import time

pdfs = []
wks = []

print os.getcwd()

for path,dirs,files in os.walk('.'):

    for d in dirs:
        if (len(d.split(".")) > 1 and d.split(".")[1] == "resources"):
            bashCommand = os.path.join(path,d)

            print bashCommand
            
            #process = subprocess.Popen(['cd', bashCommand])
            process = subprocess.Popen(['ls'])
            print(d+'/*.pdf')
            process = subprocess.Popen(['mogrify', '-density', '200', '-format', 'png', d+'/*.pdf'])
            print "wait to convert pdfs"
            process.wait()

    for fn in files:
        if (len(fn.split(".")) > 1 and fn.split(".")[1] == "pdf"):
            pdfs.append(fn)


for path,dirs,files in os.walk('.'):
    for fn in files:
        if (len(fn.split(".")) > 1 and fn.split(".")[1] == "html" and fn[0:4] != "new_"):
            print os.path.join(path,fn)

            f = open(os.path.join(path,fn), 'rw')
            n = open(os.path.join(path, "new_" + fn), 'w')

            n.write("<script src='jquery-1.11.0.min.js'></script>")

            lines = ""

            print(fn.split(".")[0] + ".resources")

            for line in f.readlines():
                for pdf in pdfs:
                    png = pdf.split(".")[0] + ".png"
                    line = line.replace(">" + pdf + "<", "><img width='50%' src='" + fn.split(".")[0] + ".resources" + "/" + png + "'><")
                #print line
                lines += line + "\n"
            lines += "<script>$('img').attr('width', '').attr('height', '').css('max-width', '50%')</script>"
            
            n.write(lines)

            n.close()
            f.close()

            print("converting to pdf")
            htmltopdf = "new_" + fn;
            process = subprocess.Popen(['mkdir', 'pdfs'])
            wks.append(subprocess.Popen(['wkhtmltopdf', htmltopdf, "pdfs/" + htmltopdf.split(".")[0] + ".pdf"]))


time.sleep(120)

for wk in wks:
    wk.terminate()

