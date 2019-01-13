## evernote

### Background

Since we can't import notes from evernote directely,
I wrote a script to extract contents from html file
which exported from evernote. Then, we can upload this
extracted data to other note app, such as `YouDao Cloud Note`

### Must Know

If u haven't assigned the output directory, the default directory
will be the location suffix with `evernote_export_tmp` which the 
location is the path of in file or in directory. 

### Usage


    usage: export.py [-h] [-f F] [--dir DIR] [--output-dir OUTPUT_DIR]
    
    Optional app description
    
    optional arguments:
      -h, --help            show this help message and exit
      -f F                  file to transfer format
      --dir DIR             directory to transfer format
      --output-dir OUTPUT_DIR
                            output directory name
