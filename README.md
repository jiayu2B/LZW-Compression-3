# LZW Compression
Python code to implement LZW compression as described here http://marknelson.us/1989/10/01/lzw-data-compression/

To Use:

  Command Line:
  - Navigate to this folder through the command line
  - To compress a string: python lzw.py -c 'your string' : for command line usage, this will return a string that can be put into decompress to reveal the original message.
  - To decompress: python lzw.py -d 'your compressed string' : will return the original string

  From Code:
  - compress(string) will take a string return a list of integers that hold the compressed value of your input string. The effect of the compression is greater with larger strings.
  - decompress(list) will take a compressed list and return the original string.

In the works:
- Adding ability to compress to files
- Easier Command Line interactivity
