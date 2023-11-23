"""Module building the soundboard"""
import os
#   !!!TO DO!!!
#   Build a TKInter interface
#       Description of functionality
#       Contains button for filepath selection, and a line for filepath
#           Button does the following
#               # For each folder in the filepath - Create headline for the soundbuttons
#                   # for each file in the subfolder, create a soundboard button
# Project based on
#     https://dev.to/aneeqakhan/create-a-sound-board-in-3-lines-of-code-3ho8



ROOTDIR = "soundfiles"
f = open("index.html", "w", encoding="utf-8")
g = open("style.css", "w", encoding="utf-8")
h = open("index.js", "w", encoding="utf-8")


g.write("""
        .padder{
        padding-top: 5px;
        padding-bottom: 5px;
        }
        .text {
          margin: auto;
          width 50%;
        border 3px solid black;
        padding: 10px;
        text-align: center;
        font-size: 20px;
        color: red;
        }
        .container {
          position: absolute;
          top: 50%;
          left: 50%;
          margin-top: 50px;
          margin-left: 50px;
          width: 100px;
          height: 100px;
        }
        .button{
          position: absolute;
        top: 50%;
        left: 50%;
        margin-top: 20px;
        margin-left: 20px;
        width: 200px;
        height: 200px;
        }
        .center {
          display: flex;
          justify-content: center;
          align-items: center;
        }
        button {
          min-width: 80px;
          height: 40px;
          margin-left: 10px;
          border-radius: 4px;
          border: 1px solid plum;
          cursor: pointer;
          color: black;
          font-weight: 600;
        }
        body {
          background-color: hsl(50, 33%, 25%);
                }

""")

### Insert a variable that allows the user to name their soundboard
f.write("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Self made soundboard</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <script src="index.js"></script>
""")
file_extensions = []

for subdirs, dirs, files in os.walk(ROOTDIR):
    subdir = subdirs.split("/")[-1]
    f.write(f"""<div class="text">{subdir}
                         <div class="center">""")
    INDEX = 0
    for file in files:
        file_extension = "." + file.split(".")[-1]
        if file_extension not in file_extensions:
            file_extensions.append(file_extension)
        if INDEX > 4:
            f.write("""</div><div class="padder"></div><div>""")
            INDEX = 0
        file_name = file.split(".")[0]
        f.write(f"""<button id="{ROOTDIR}\\{subdir}\\{file_name}"onClick="play_sound{file_extensions.index(file_extension)}(this.id)">{file_name}</button>""")
        INDEX += 1
    f.write("""</div></div>""")


f.write("""</body>
</html>""")

for file_extension in file_extensions:
    h.write(f"""function play_sound{file_extensions.index(file_extension)} (clicked_id) {{
        var audio = new Audio(clicked_id + "{file_extension}"); 
        audio.play();
      }}
      """)

print("Your soundboard has been built!")
