# Source - https://stackoverflow.com/a/22351973
# Posted by Thomas Baruchel, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-26, License - CC BY-SA 4.0

with open("enc.bmp", "rb") as image:
  f = image.read()
  b = bytes(f)
  print(b)
  hex_string = b.hex()
