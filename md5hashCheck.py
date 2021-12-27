# Dropzone Action Info
# Name: md5check
# Description: checkMD5hash
# Handles: Files
# Creator: rhysbw
# URL: http://yoursite.com
# Events: Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.5


"""
You must have notifications for it to work
"""
import time
import hashlib

def dragged():
    

    # Below line switches the progress display to determinate mode so we can show progress
    dz.determinate(False)
    
    

    
    correct_hash = get_needed_MD5_hash()
    
    found_hash = calc_MD5_hash()
    
    
    if (correct_hash == found_hash):
    
        dz.finish(f"MD5 Sum Valid, Hash calculated: {found_hash}")
        dz.url(False)
        
    
    
    else:
        dz.finish(f"Invalid MD5, Hash calculated: {found_hash}")
        dz.url(False)



def get_needed_MD5_hash():
    md5 = dz.inputbox("MD5", "Enter MD5 hash:")
    return md5
    
def calc_MD5_hash():
    hash_md5 = hashlib.md5()
    with open(items[0], "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
