import sys

"""Compress a string using lzw compression as described here:
    http://marknelson.us/1989/10/01/lzw-data-compression/"""
def compress(s):
  # initialize dictionary mapping chars to codes with default values
  dictionary = dict()
  for i in xrange(256):
    dictionary[chr(i)] = i

  index = 256
  input_string = ''
  compressed_string = []

  for char in s:
    curr = input_string + char
    if curr in dictionary:
      input_string = curr
    else:
      compressed_string.append(dictionary[input_string])
      dictionary[curr] = index
      index+=1
      input_string = char

  if input_string:
    compressed_string.append(dictionary[input_string])

  return compressed_string


"""Decompress a string compressed using lzw compression
    Required: string must be a valid compression otherwise output is unspecified
              could be an error, or a fault decompressed string"""
def decompress(c):
  # initialize dictionary mapping codes to chars with default values
  dictionary = dict()
  for i in xrange(256):
    dictionary[i] = chr(i)

  uncompressed = ""

  index = 256
  old_string = chr(c.pop(0))
  uncompressed += old_string

  for code in c:
    if code in dictionary:
      new_string = dictionary[code]
    elif code == index:
      new_string = old_string + old_string[0]

    uncompressed+=new_string

    dictionary[index] = old_string + new_string[0]
    index += 1

    old_string = new_string

  return uncompressed

def stringify(l):
  s = ''
  for elm in l:
    s+= str(elm)+','
  return s


def listify(s):
  l = s.split(',')
  l.pop()
  l_new = []
  for elm in l:
    l_new.append(int(elm))
  return l_new

if sys.argv[1] == '-c' and sys.argv[2]:
  c = compress(sys.argv[2])
  c_string = stringify(c)
  print c_string
elif sys.argv[1] == '-d' and sys.argv[2]:
  d_list = listify(sys.argv[2])
  print decompress(d_list)





