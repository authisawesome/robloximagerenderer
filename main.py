from PIL import Image
import ujson
import log
import math
import time
from pbwrap import Pastebin
import pyperclip

data = open("config.json")
config = ujson.load(data)

log.logInfo("Authenticating with pastebin API...")

pastebin = Pastebin(config['pastebin-api-key'])
user_id = pastebin.authenticate(config['pastebin-username'], config['pastebin-password'])

log.logSuccess("Successfully authenticated!")
time.sleep(1)

image_resolution = config['image-resolution']

log.logInfo("Begin; read file")
image = Image.open(config['image-file'])

targetsize = x, y, = round((image.width*image_resolution)), round((image.height*image_resolution))
image = image.resize(targetsize)

width = image.width
height = image.height
pixel_data = {}

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

for pxy in range(height):
    log.logInfo("Reading image pixels... [{}%]"
                   .format(
                           math.ceil((pxy/height)*100))
                   )
    data = []
    for pxx in range(width):
        coordinate = x, y = pxx, pxy
        pixel = image.getpixel(coordinate)
        hex = rgb_to_hex(pixel[0], pixel[1], pixel[2])
        data.append(hex)
    pixel_data[pxy] = data

log.logSuccess("Successfully read pixels!")
log.logInfo("Dumping pixel data into JSON format (may take a minute)")
json_obj = ujson.dumps(pixel_data)

with open("dump.json","w") as outfile:
    outfile.write(json_obj)

log.logSuccess("Successfully dumped image data into JSON!")
log.logInfo("Creating new paste thru pastebin API...")

try:
    paste_URL = pastebin.create_paste_from_file("dump.json")
    code = str.split(paste_URL,"/")[3]
    raw_URL = "https://pastebin.com/raw/{}".format(code)
    log.logSuccess("Successfully uploaded paste: {}".format(raw_URL))
    log.logInfo("(The URL has been copied to your clipboard!)")
    pyperclip.copy(raw_URL)
except Exception as error:
    log.logError("dump.json is too large to upload:  reduce the image resolution!")

input("")