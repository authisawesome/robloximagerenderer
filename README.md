# robloximagerenderer
Reads the pixels from the given image then automatically uploads it to a pastebin.

You'll need the following libraries (run pip install <name>): 
  - PIL
  - ujson
  - pbwrap
  - pyperclip

After, head to https://pastebin.com/doc_api#1 and get your pastebin API key.
Open "config.json"
Configure pastebin-api-key, pastebin-username, pastebin-password

pastebin-api-key: You can get it from https://pastebin.com/doc_api#1 once you are logged in.
pastebin-username: The username to your pastebin account.
pastebin-password: The password to your pastebin account.

Drag and drop any image into the repository, and then set "image-file" to the name of your image. Include the extension name as well. (e.g "flowers.jpg")

Run main.py. After it has successfully read the pixels from your image then uploaded the data to pastebin, you're good to go!

IF YOU RUN INTO 'dump.json is too large to upload':
  Open "config.json"
  Reduce 'image-resolution' to a smaller number.
  dump.json MUST be less than 512KB to upload to pastebin.
  OR ... You are being rate limited by the pastebin API.
  You can only upload 20 files per 24 hours per api-key. 
  Either switch to a new api-key, or upgrade your Pastebin account.

NOTE: 
  The ModuleScript to load your images into a game is here:
    require(14859842850).render("Username")

Have fun!
