require "Shellwords"

files = Dir["*.pdf"]

dpi_value = 500  # default value

# with docker use the following command
#  docker run -ti --rm -v /Users/eklavya/Desktop/figures:/pdf bwits/pdf2htmlex-alpine pdf2htmlEX --hdpi 500 --vdpi 500 --embed-image 0  hcc_eai.pdf

pdf2htmlEX = "pdf2htmlEX --hdpi " + dpi_value.to_s + " --vdpi " + dpi_value.to_s + " --embed-image 0 "





for f in files 


cmd1 = pdf2htmlEX + " " + f.shellescape
#puts cmd1
system(cmd1)

image_name = f.split(".")[0] + ".png"
system("mv", "bg1.png", image_name.to_s) 
end


system("rm", "pdf2htmlEX-64x64.png")

html = Dir["*.html"]
for i in html
	system("rm", i)
end
