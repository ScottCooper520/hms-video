7/21/2020 -[OK] Git test Legion to NUC
7/21/2020 - Git test NUC to Legion

7/11/2020 - Got clone of media-server for Legion.

2/28/2020 - Status
==================
I essentially have everything working at this point. Some of the highlights include:
URLs to support list of audios/authors.
URLs to support details of audio/author, on click from above list.
URLs to support actual loading of selected audio and playing it.
  This currently supports four level of hierarchy for the audio:
  - Root: audio files located directly in shme/sharefromwindows folder. Likey not really used.
  - Root/folder: One level down.
  - Root/folder/folder: Two levels down.
  - Root/folder/folder/folder: Three levels down.
  I believe this should support the majority of the audio file formats I need.

I have successfully dumped, modified, and reloaded the audios table in DB. I plan to use
this approach to pre-populate the db with metadata from the entire set of audio files.
The actual audio files will be stored on the share, and only retrieved when played. The db
will contain all the data about the files, and will be used to identify it for retrieval.

Note: I do not have a way to automatially update the Author field (it will contain an pk for Authors table).
So, it looks like I have a couple of simple options here:
1. Ignore the author field, and set it to some default number.
2. Generate the json file one author at a time, and manually set to proper integer.
Initially, I will just go with (1) above since I don't really need to view/sort by author.

So, the next steps are as follows:
1. Copy audios onto Home laptop drive.
   I have decided it will be best to preload on this comp, then copy identical structure to server when done.
2. Auto-generate a JSON file from the audio files.
   Technically, I can use any program for this, but will likely stick with Python.
3. Use the Django loaddata utility to read this data into the database.
4. Any other cleanup (e.g. better UI), etc.
5. Copy it all to server.
6. Serve so all devices on the home network can access.
7. Open site on cellphone. Select and play audio.


2/10/2020 - Based on Library Tutorial
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website
