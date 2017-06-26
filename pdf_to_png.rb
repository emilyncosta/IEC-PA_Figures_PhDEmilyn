require "Shellwords"

files = Dir["*.pdf"]

dpi = 500
pdf2htmlEX = "pdf2htmlEX --hdpi " + dpi.to_s + " --vdpi " + dpi.to_s + " --embed-image 0 "





for f in files 


cmd1 = pdf2htmlEX + " " + f.shellescape
#puts cmd1
system(cmd1)

image_name = f.split(".")[0] + ".png"
system("mv", "bg1.png", image_name.to_s) 
end
