Hello!

Make sure updates.json is in the same folder as main.py, then run the py file.

Py 3.7 was used to make it but any version that supports f-strings should do just fine (3.6+ ?).

Note that this is a very basic retriever; certain updates do not use words that are initially thought to be part of their content, such as the Fashion Shop being released under a 'tailoring' service. These will not be picked up by the bot from searching for 'Tuxedo' or 'Fashion'.

This was initially for personal use, I have not optimised code or attempted to make it in a form of very high quality - feel free to modify or change code if you want.

'updates.json' took a while to transfer over (since Google Spreadsheets likes to put a multi-line block in quotes, even if there are still quotes in the block itself) so if it's useful, let me know please :)