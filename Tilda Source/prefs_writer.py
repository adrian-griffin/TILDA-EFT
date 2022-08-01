import configparser

global config
config=configparser.ConfigParser(allow_no_value=True)
config.optionxform = str




def write_pref_config():
    with open(r"settings.ini","w") as settingsConfMod:
        config.write(settingsConfMod)
        settingsConfMod.flush()
        settingsConfMod.close()
    

def write_pref(section,item,value):
    config.set(section,item,value)

def write_default_prefs():
    # SETTING UP CLASS FROM OBJECT

    # Creating object from ConfigParser class as settings_conf
    #settings_conf = configparser.ConfigParser(allow_no_value=True)
    #config.optionxform = str

    # ADDING CONFIG SECTIONS

    config.add_section("KEYBINDS_AND_HOTKEYS")
    config.add_section("GRAPHICS_SETTINGS")
    config.add_section("SCANNER_PREFERENCES")
    config.add_section("LOGGING")
    config.add_section("COMPUTER_VISION_IMAGE_PROCESSING")




    # ADDING SPECIFIC OPTIONS TO EACH SECTION
        # ADDING OPTIONS TO (KEYBINDS_AND_HOTKEYS)

    config.set("KEYBINDS_AND_HOTKEYS",";PLEASE NOTE THAT ENTERING ANY INCORRECT SYNTAX WITH THE HOTKEY CONFIGS COULD CAUSE ISSUES WITH THE APP")
    config.set("KEYBINDS_AND_HOTKEYS",";IT IS BEST TO EDIT THEM WITHIN THE APP ITSELF AS IT WILL SANITIZE AND ADJUST SYNTAX AUTOMATICALLY TO AVOID ISSUES")
    

    config.set("KEYBINDS_AND_HOTKEYS","PrimaryScanKeybind","<ctrl>+<shift>+a")
    #config.set("Keybinds","PrimaryScanKeybind_RAW","Ctrl+Shift+A")

    config.set("KEYBINDS_AND_HOTKEYS","SecondaryScanKeybind","<ctrl>+<shift>+s")
    #config.set("Keybinds","SecondaryScanKeybind_RAW","Ctrl+Shift+S")

    config.set("KEYBINDS_AND_HOTKEYS","ToggleOverlayKeybind","<ctrl>+<shift>+q")
    #config.set("Keybinds","SecondaryScanKeybind_RAW","Ctrl+Shift+q")

    config.set("KEYBINDS_AND_HOTKEYS","ToggleKeyEventListener","<ctrl>+<alt>+p")
    #config.set("Keybinds","SecondaryScanKeybind_RAW","Ctrl+Shift+q")




        # ADDING OPTIONS TO (GRAPHICS_SETTINGS)
    config.set("GRAPHICS_SETTINGS",";MainWindowBackgroundOpacity         => 0 < X < 1 | Sets opacity level for main Tilda window")
    config.set("GRAPHICS_SETTINGS",";MainWindowTextOpacity               => 0 < X < 1 | Sets opacity level text within main Tilda window")
    config.set("GRAPHICS_SETTINGS",";KeepMainWindowOnTop                 => Forces Windows to keep Tilda window above all others")
    config.set("GRAPHICS_SETTINGS",";KeepOverlayWindowOnTop              => Forces Windows to keep Tilda overlay window above all others, this can be disabled, though I don't see the point in doing so.")
    config.set("GRAPHICS_SETTINGS",";AppliedTheme                        => UI Themes: Default, Galaxy, Forest, Chill, Luxury, Pacific, Riches")
    config.set("GRAPHICS_SETTINGS",";HighlightableText_MAIN              => Double-clicking most text in app will highlight it for faster recognition of what's important | Colour changed per theme.")
    config.set("GRAPHICS_SETTINGS",";OverlayLayout                       => Overlay Layouts: Compact, Minimal, Vertical, Horizontal")
    config.set("GRAPHICS_SETTINGS","MainWindowBackgroundOpacity","1.00")
    config.set("GRAPHICS_SETTINGS","MainWindowTextOpacity","1.00")


    config.set("GRAPHICS_SETTINGS","OverlayWindowBackgroundOpacity","1.00")
    config.set("GRAPHICS_SETTINGS","OverlayWindowTextOpacity","1.00")
    config.set("GRAPHICS_SETTINGS","KeepMainWindowOnTop","True")
    config.set("GRAPHICS_SETTINGS","KeepOverlayWindowOnTop","True") 
    config.set("GRAPHICS_SETTINGS","AppliedTheme","Default")
    config.set("GRAPHICS_SETTINGS","HighlightableText_MAIN","True")
    config.set("GRAPHICS_SETTINGS","HighlightableText_OVERLAY","True")
    config.set("GRAPHICS_SETTINGS","OverlayLayout","Compact")



        # ADDING OPTIONS TO (SCANNER_PREFERENCES)
    config.set("SCANNER_PREFERENCES","ScanEngine","Dual")

    config.set("SCANNER_PREFERENCES","UseCachedData","False")

    config.set("SCANNER_PREFERENCES","ActiveScanAutoInspect","False")

    config.set("SCANNER_PREFERENCES","ScanEventListener","True")

    #config.set("SCANNER_PREFERENCES","LevelOfItemDetail","Medium")



    config.set("LOGGING","LogFilePath","logs/logs.txt")
    config.set("LOGGING","LogLevel","Info")




    ########################################################################################################################################################

    config.set("COMPUTER_VISION_IMAGE_PROCESSING","TesseractAI_SystemLocation","C:/Program Files/Tesseract-OCR/tesseract.exe")


    ########################################################################################################################################################


    ## WRITE CONFIG PARAMS TO DISK
    with open(r"settings.ini","w") as settingsConfMod:
        config.write(settingsConfMod)
        settingsConfMod.flush()
        settingsConfMod.close()

def pref_mod_init():
    config.clear()
    with open(r"settings.ini","w") as settingsConfMod:
        config.write("settingsConfMod")
        settingsConfMod.flush()
        settingsConfMod.close()
    write_default_prefs()
#write_pref("SCANNER_PREFERENCES","ScanEventListener","True")