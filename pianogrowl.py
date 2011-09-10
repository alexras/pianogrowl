#!/usr/bin/env python2.6
# This Python file uses the following encoding: utf-8

"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

import os, sys, commands, urllib2, tempfile

pandora_icon = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            "pandora-icon-cc-by-sa-rossr.png")

command = sys.argv[1]
command_data = {}

for line in sys.stdin:
    line = line.strip()
    key, delimiter, value = line.partition('=')
    command_data[key] = value

growl_title = None
growl_message = None
growl_image = pandora_icon

if command == "songstart":
    if int(command_data["rating"]) == 1:
        heart = "♥ "
    else:
        heart = ""

    cover_art_url = command_data["coverArt"].strip()

    if len(cover_art_url) > 0:
        (imgfp, growl_image) = tempfile.mkstemp(prefix="pianobar")

        try:
            urlfp = urllib2.urlopen(cover_art_url)
            os.write(imgfp, urlfp.read())
        except ValueError, e:
            os.unlink(growl_image)
            growl_image = pandora_icon
        finally:
            os.close(imgfp)

    growl_title = "%s%s" % (heart, command_data["title"])
    growl_message = "by: %s\non: %s" % (command_data["artist"],
                                        command_data["album"])
elif command == "userlogin":
    growl_title = "pianobar"
    growl_message = "Successfully logged in."
elif int(command_data["pRet"]) != 1:
    growl_title = "pianobar"
    growl_message = "%s failed: %s" % (command, command_data["pRetStr"])
elif int(command_data["wRet"]) != 1:
    growl_title = "pianobar"
    growl_message = "%s failed: Network error: %s" % (
        command, command_data["wRetStr"])

if growl_title is not None and growl_message is not None:
    growlnotify_args = '--image "%s" -d 12 --title "%s" --message "%s"' % (
        growl_image, growl_title, growl_message)
    os.system("growlnotify %s" % (growlnotify_args))

if growl_image != pandora_icon:
    os.unlink(growl_image)
