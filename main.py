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



rootdir = "Darkest_dungeon_lydfiler"
f = open("index.html", "w", encoding="utf-8")
g = open("style.css", "w", encoding="utf-8")
h = open("index.js", "w", encoding="utf-8")

# TO DO - Figure out a way to change the .wav extension to be parametized. 
h.write("""function play_sound(clicked_id) {
    var audio = new Audio(clicked_id + ".wav"); 
    audio.play();
  }""")

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

for subdirs, dirs, files in os.walk(rootdir):
    subdir = subdirs.split("/")[-1]
    f.write(f"""<div class="text">{subdir}
                         <div class="center">""")
    index = 0
    for file in files:
        if index > 4:
            f.write("""</div>
                    <div class="padder"></div>
                    <div>""")
            index = 0
        file_name = file.split(".")[0]
        f.write(f"""<button id="{rootdir}\{subdir}\{file_name}" 
                onClick="play_sound(this.id)">{file_name}</button>""")
        index += 1
    f.write("""</div></div>""")


f.write("""</body>
</html>""")