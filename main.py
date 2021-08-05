import re
import pytesseract
from PIL import Image, ImageFilter
import urllib.request
import io

l1 = "https://scontent-sea1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/220391326_371106694401130_7915626845031012325_n.jpg?_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_cat=110&_nc_ohc=0FHcvLPRPDwAX92cHgE&edm=AP_V10EBAAAA&ccb=7-4&oh=835598eec9e484741f997b3047414e38&oe=60FF5F5D&_nc_sid=4f375e"
link = "https://scontent-sea1-1.cdninstagram.com/v/t51.2885-15/e35/222183949_246309690655298_2078900316533373099_n.jpg?_nc_ht=scontent-sea1-1.cdninstagram.com&_nc_cat=102&_nc_ohc=g9jQwd9tgxsAX96dnmq&edm=AP_V10EBAAAA&ccb=7-4&oh=06aaf5062695929304a8184d46a4678f&oe=60FFDC88&_nc_sid=4f375e"
fd = urllib.request.urlopen(l1)
im = Image.open(io.BytesIO(fd.read()))
enhance = im.convert("L")
cropped = enhance.crop((im.size[0]*(1/3), 1, im.size[0]*(2/3), im.size[1] / 6))
sharpened = cropped.filter(ImageFilter.SHARPEN)

p = pytesseract.image_to_string(sharpened).splitlines()

if [x for x in p if re.search("#[0-9]+", x)]:
    name = [x for x in p if re.search("#[0-9]+", x)][0]
else:
    name = "No Result"
print(p)
sharpened.show()
