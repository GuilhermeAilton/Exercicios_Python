from rembg import remove
from PIL import Image
input = Image.open("ju.jpeg")
output = remove(input)
output.save("output.png")