https://github.com/rafffael/docker-imagemagick

https://hub.docker.com/r/jujhars13/docker-imagemagick/


https://hub.docker.com/r/bwits/pdf2htmlex-alpine/

alias pdf2htmlEX='docker run -ti --rm -v `pwd`:/pdf bwits/pdf2htmlex-alpine pdf2htmlEX'

pdf2htmlEX -h 
pdf2htmlEX --zoom 1.3 test.pdf
