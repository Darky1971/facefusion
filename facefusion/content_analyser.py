# Angepasste Version: NSFW-Filter deaktiviert
# Alle Prüfungen werden übersprungen und es wird immer False zurückgegeben.

def analyse_stream(*args, **kwargs):
    return False

def analyse_frame(*args, **kwargs):
    return False

def analyse_image(*args, **kwargs):
    return False

def analyse_video(*args, **kwargs):
    return False

def detect_nsfw(*args, **kwargs):
    return False
