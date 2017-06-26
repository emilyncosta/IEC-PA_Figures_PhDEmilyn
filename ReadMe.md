# UglyFigures

These are simple `Ruby` and `Python3` automation scripts 

- To isolate HQ PNG images from the PDF at a given DPI.
- Convert them to TIFF images at a given DPI.




# How to Use

### Conversion from PDF to PNG => Ruby

**Assumptions** : Each PDF contains only a single HI-DEF image.


1. Make sure you have [pdf2htmlEX installed](https://github.com/coolwanglu/pdf2htmlEX/wiki/Download).


2. Set the `dpi_value` variable in `pdf_to_png.rb` file.

```ruby
dpi_value = 500 # default value

```

3. Have all the pdf files in the same directory as the ruby script.

```sh
UglyFigures git/master
❯ tree
.
├── ReadMe.md
├── convert_to_tiff.py
├── pdf_to_png.rb
└── test.pdf

0 directories, 4 files

```

4. Simply run

```sh
❯ ruby pdf_to_png.rb
```


5. You will now have *2 new file* **per** pdf.

For example, here `test.html` and `test.png` are created.

### Conversion of PNG to TIFF => Python3

**Assumptions** : Python3 library `pillow` is pre-installed.

1. In the `convert_to_tiff.py` file, caliberate the `dpi_value` for desired value.

```python3
dpi_value = 500 # default value

```


2. Using the same directory structure as above, simply run

```sh
❯ python3 convert_to_tiff.py
```

3. For every `PDF` file you should now have the output `tiff` file with the same name as the `png` file.

For example, now there's a `./test` tiff image file in the folder as well.

And that's it - **No Ugly Figures** :)


