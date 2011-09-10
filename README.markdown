## About

Pianogrowl is a Python port of mr-szymanski's
[growl-pianobar](https://github.com/mr-szymanski/growl-pianobar). It is an
event listener for [pianobar](https://github.com/PromyLOPh/pianobar) that
displays [Growl](http://growl.info/) notifications in response to certain
events (currently track changes, user login, and various errors).

I decided to rewrite growl-pianobar in Python because:

* I'm not a huge fan of Bash scripts and thought that the input would be easier
  to manage in a more feature-rich scripting language.

* I wanted to store album art in temporary files that are deleted at the end of
  the script rather than storing them in `~/.config/`, and it was quicker for
  me to re-write it in Python than it would have been to figure out the
  appropriate incantations in Bash.

## Installation

Simply add the following to `~/.config/pianobar/config`:

     event_command = /path/to/pianogrowl.py

## Dependencies

Pianogrowl is written in pure Python, but it requires `growlnotify` to do the
actual Growl notifications.

## License

In the spirit of mr-szymanski's original, this code is released in the public
domain under an [Unlicense](http://unlicense.org/).

The Pandora logo that the script uses by default was made by
[Ross Reyman](http://www.flickr.com/photos/rossr/2768279921/).
