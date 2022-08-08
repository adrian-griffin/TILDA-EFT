import configparser
from multiprocessing import current_process

def read_pref_graphics(item):
    # CREATE NEW CONFIG OBJECT AND OPEN 'settings.ini' FILE FROM DISK
    config=configparser.ConfigParser()
    config.read('settings.ini')
    item_value = config.get("GRAPHICS_SETTINGS",item)
    return item_value

def read_pref_keybinds(item):
    # CREATE NEW CONFIG OBJECT AND OPEN 'settings.ini' FILE FROM DISK
    config=configparser.ConfigParser()
    config.read('settings.ini')
    item_value = config.get("KEYBINDS_AND_HOTKEYS",item)
    return item_value

def read_pref_scanner(item):
    # CREATE NEW CONFIG OBJECT AND OPEN 'settings.ini' FILE FROM DISK
    config=configparser.ConfigParser()
    config.read('settings.ini')
    item_value = config.get("SCANNER_PREFERENCES",item)
    return item_value


# ONLY USED FOR GRABBING VISION PATH

def read_pref_imageproc(item):
    # CREATE NEW CONFIG OBJECT AND OPEN 'settings.ini' FILE FROM DISK
    config=configparser.ConfigParser()
    config.read('settings.ini')
    item_value = config.get("COMPUTER_VISION_IMAGE_PROCESSING",item)
    return item_value

#print(read_pref_imageproc("TesseractAI_SystemLocation"))