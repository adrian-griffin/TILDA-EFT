# IMPORT GUI AND MODULES
from ensurepip import version
from logging import shutdown
import shutil
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from threading import Thread
import time
from modules import *
from modules.ui import compact_overlay_ui, loading_ui, main_tilda_ui, popup_window_ui, updog_ui
import difflib
import sys
import time
from threading import Thread
import cv2
import numpy
import pyautogui
import pytesseract
import requests
from cv2 import IMWRITE_JPEG_LUMA_QUALITY, bitwise_not, waitKey
from PIL import Image
from pynput import keyboard
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import prefs_reader, prefs_writer

## Version Number:
global tilda_version
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path_cleaned = dir_path.replace("\\","/")
dir_path_usable = dir_path_cleaned+"/"
if os.path.exists(dir_path_usable+"/version.txt"):
        with open(dir_path_cleaned+"/version.txt", 'r') as file:
                tilda_version_pulled = file.read().rstrip()
else:
        pass

tilda_version = tilda_version_pulled


import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

class BLLW(QMainWindow, loading_ui.Ui_LoadWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        title = "Tilda"
        self.setWindowTitle(title)
        self.setWindowFlags(
                        Qt.WindowStaysOnTopHint |
                        Qt.FramelessWindowHint
                        )

class PUDW(QMainWindow, popup_window_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        title = "Tilda"
        self.setWindowTitle(title)
        self.setWindowFlags(
                        Qt.WindowStaysOnTopHint |
                        Qt.FramelessWindowHint
                        )


class Window(QMainWindow, main_tilda_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        title = "Tilda"
        self.setWindowTitle(title)
        self.setWindowFlags(
                        Qt.WindowStaysOnTopHint |
                        Qt.FramelessWindowHint
                        )

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()

    def enable_smm_overlay(self):
        smm_w.show()
        win_m.hide()
        global tesseract_ocr_cmd_location
        tesseract_ocr_cmd_location = prefs_reader.read_pref_imageproc("TesseractAI_SystemLocation")
        import os
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tilda", None))

    def refresh_db_func(self):
        from dbman import refresh_database
        refresh_database()
        self.item_desc.setText("Refreshed!")

    def load_settings(self):
    # OPENING CONFIGURATION FILE TO BE READ

        self.label_5.setText("v"+str(tilda_version))

    # Checking and writing to disk the status of "Enable Event Listener"
        if prefs_reader.read_pref_scanner("ScanEventListener") == "True":
                self.checkBox_4.setChecked(True)
        else: 
                self.checkBox_4.setChecked(False)
    # Checking and writing to disk the status of "Allow Text Highlighting"
        if prefs_reader.read_pref_graphics("HighlightableText_MAIN") == "True":
                self.checkBox_5.setChecked(True)
        else: 
                self.checkBox_5.setChecked(False)
    # Checking and writing to disk the status of "Use Locally Cached Item Data"
        if prefs_reader.read_pref_scanner("UseCachedData") == "True":
                self.checkBox.setChecked(True)
        else: 
                self.checkBox.setChecked(False)
    # Checking and writing to disk the status of "Use Locally Cached Item Data"
        if prefs_reader.read_pref_graphics("KeepMainWindowOnTop") == "True":
                self.checkBox_2.setChecked(True)
                self.label_9.setPixmap(QPixmap(":/tertiary_ui_elems/ui_elements/media/quick_status_on.ico"))
        else: 
                self.checkBox_2.setChecked(False)
                self.label_9.setPixmap(QPixmap(":/tertiary_ui_elems/ui_elements/media/quick_status_off.ico"))
    # Checking and writing to disk the status of "Use Locally Cached Item Data"
        if prefs_reader.read_pref_scanner("ActiveScanAutoInspect") == "True":
                self.checkBox_3.setChecked(True)
                self.label_10.setPixmap(QPixmap(":/tertiary_ui_elems/ui_elements/media/quick_status_on.ico"))
        else: 
                self.checkBox_3.setChecked(False)
                self.label_10.setPixmap(QPixmap(":/tertiary_ui_elems/ui_elements/media/quick_status_off.ico"))
    # Checking and writing to disk the status of the scan options
        if prefs_reader.read_pref_scanner("ScanEngine") == "Dual":
                self.radio_both.setChecked(True)
        elif prefs_reader.read_pref_scanner("ScanEngine") == "Active":
                self.radio_primary.setChecked(True)
        elif prefs_reader.read_pref_scanner("ScanEngine") == "Passive":
                self.radio_secondary.setChecked(True)     

        main_opac = prefs_reader.read_pref_graphics("MainWindowBackgroundOpacity")
        self.doubleSpinBox.setValue(float(main_opac)*(100))
        text_opac = prefs_reader.read_pref_graphics("MainWindowTextOpacity")
        self.doubleSpinBox_2.setValue(float(text_opac)*(100))

        self.label_8.setPixmap(QPixmap(":/tertiary_ui_elems/ui_elements/media/quick_status_on.ico"))



    def save_settings(self):
    # OPENING CONFIGURATION FILE TO BE ALTERED
    # Allowing persistent custom keybinds. (TEMPORARY, WILL BE CHANGED ONCE THE CUSTOM KEYBIND UI ELEMENT IS WORKING)
        PrimaryScanKeybind_TMP = prefs_reader.read_pref_keybinds("PrimaryScanKeybind")
        SecondaryScanKeybind_TMP = prefs_reader.read_pref_keybinds("SecondaryScanKeybind")
        ToggleOverlayKeybind_TMP = prefs_reader.read_pref_keybinds("ToggleOverlayKeybind")
        ToggleKeyEventListener_TMP = prefs_reader.read_pref_keybinds("ToggleKeyEventListener")
        
        prefs_writer.pref_mod_init()
        
    # Persisting keybinds
        prefs_writer.write_pref("KEYBINDS_AND_HOTKEYS","PrimaryScanKeybind",""+str(PrimaryScanKeybind_TMP))
        prefs_writer.write_pref("KEYBINDS_AND_HOTKEYS","SecondaryScanKeybind",""+str(SecondaryScanKeybind_TMP))
        prefs_writer.write_pref("KEYBINDS_AND_HOTKEYS","ToggleOverlayKeybind",""+str(ToggleOverlayKeybind_TMP))
        prefs_writer.write_pref("KEYBINDS_AND_HOTKEYS","ToggleKeyEventListener",""+str(ToggleKeyEventListener_TMP))


    # Checking and writing to disk the status of "Enable Event Listener"
        if self.checkBox_4.isChecked() == True:
                prefs_writer.write_pref("SCANNER_PREFERENCES","ScanEventListener","True")
        else:
                prefs_writer.write_pref("SCANNER_PREFERENCES","ScanEventListener","False")
    # Checking and writing to disk the status of "Allow Text Highlighting"
        if self.checkBox_5.isChecked() == True:
                prefs_writer.write_pref("GRAPHICS_SETTINGS","HighlightableText_MAIN","True")
        else:
                prefs_writer.write_pref("GRAPHICS_SETTINGS","HighlightableText_MAIN","False")
    # Checking and writing to disk the status of "Use Locally Cached Item Data"
        if self.checkBox.isChecked() == True:
                prefs_writer.write_pref("SCANNER_PREFERENCES","UseCachedData","True")
        else:
                prefs_writer.write_pref("SCANNER_PREFERENCES","UseCachedData","False")
    # Checking and writing to disk the status of "Use Locally Cached Item Data"
        if self.checkBox_2.isChecked() == True:
                prefs_writer.write_pref("GRAPHICS_SETTINGS","KeepMainWindowOnTop","True")
        else:
                prefs_writer.write_pref("GRAPHICS_SETTINGS","KeepMainWindowOnTop","False")
    # Checking and writing to disk the status of "Use Locally Cached Item Data"
        if self.checkBox_3.isChecked() == True:
                prefs_writer.write_pref("SCANNER_PREFERENCES","ActiveScanAutoInspect","True")
        else:
                prefs_writer.write_pref("SCANNER_PREFERENCES","ActiveScanAutoInspect","False")
    # Checking and writing to disk the status of the scan options
        if self.radio_primary.isChecked() == True:
                prefs_writer.write_pref("SCANNER_PREFERENCES","ScanEngine","Active")
        elif self.radio_secondary.isChecked() == True:
                prefs_writer.write_pref("SCANNER_PREFERENCES","ScanEngine","Passive")
        elif self.radio_both.isChecked() == True:
                prefs_writer.write_pref("SCANNER_PREFERENCES","ScanEngine","Dual")       
        time.sleep(0.5)
        self.save_button.setText(" Saved!")
        prefs_writer.write_pref("GRAPHICS_SETTINGS","MainWindowBackgroundOpacity",str(int(self.doubleSpinBox.value())/(100)))
        prefs_writer.write_pref("GRAPHICS_SETTINGS","MainWindowTextOpacity",str(int(self.doubleSpinBox_2.value())/(100)))

        self.load_settings()
        #from prefs_writer import pref_mod_write
        #pref_mod_write()

        def modify_keybind_to_ui(seq_input):
        # please dont look, im too lazy to make this more efficient and reusable, just let me sanitize my strings in peace
                key_seq_remove_str = "QKeySequence("
                key_sequence_raw = str(seq_input)
                key_sequence_edit = key_sequence_raw.replace(key_seq_remove_str,"")
                key_sequence = key_sequence_edit[:-1]
                key_sequence_lowered = key_sequence.lower()
                key_sequence_comma_formatted = key_sequence_lowered.replace(",","+")
                key_sequence_ctrl_formatted = key_sequence_comma_formatted.replace("ctrl","<ctrl>")
                key_sequence_blank_formatted = key_sequence_ctrl_formatted.replace(" ","")
                key_sequence_alt_formatted = key_sequence_blank_formatted.replace("alt","<alt>")
                key_sequence_shift_formatted = key_sequence_alt_formatted.replace("shift","<shift>")
                key_sequence_space_formatted = key_sequence_shift_formatted.replace("space","<space>")
                key_sequence_formatted = "\""+key_sequence_space_formatted+"\""
                return key_sequence_formatted,key_sequence

        #prim_for,prim_raw = modify_keybind_to_ui(self.primary_key_seq_edit.keySequence())
        #sec_for,sec_raw = modify_keybind_to_ui(self.secondary_key_seq_edit.keySequence())
        #smm_for,smm_raw = modify_keybind_to_ui(self.primary_key_seq_edit_2.keySequence())

    # CLOSING CONFIG AND WRITING TO DISK
        prefs_writer.write_pref_config()
        self.load_settings()

    def apply_settings(self):
        self.page_widget.setCurrentIndex(0)
        self.settings_button.setChecked(False)
        win_m.hide()
        self.load_settings()
        popup_w.show()

    def apply_popup_cancel(self):
        popup_w.hide()
        self.page_widget.setCurrentIndex(1)
        self.settings_button.setChecked(False)
        win_m.show()

    def minimize_app(self):
        self.showMinimized()
        self.load_settings()

    def exit_app(self):
        import os
        os._exit(0)

    def return_to_main(self):
        self.page_widget.setCurrentIndex(0)
        self.settings_button.setChecked(False)
        

    def open_settings(self):
        if self.page_widget.currentIndex() == 0:
                self.page_widget.setCurrentIndex(1)
                self.load_settings()
                self.save_button.setText(" Save")
        elif self.page_widget.currentIndex() == 1:
                self.page_widget.setCurrentIndex(0)
                self.load_settings()
                self.save_button.setText(" Save")


    def check_for_updates(self):
        import update_check
        dir_path_fixed = dir_path.replace("\\","/")
        UTD = update_check.isUpToDate(dir_path_fixed+"/version.txt",'https://raw.githubusercontent.com/adrian-griffin/TILDA-EFT/main/Tilda%20Source/version.txt')
        time.sleep(0.4)
        if UTD == True:
                self.label_6.setText("Up to Date!")
        elif UTD == False: 
                updog_w.stackedWidget.setCurrentIndex(0)
                updog_w.label_2.setText("Would you like to update now?")
                updog_w.show()



    def capture_keystroke_edit(self):
        from pynput import keyboard
        global SHIFT_STATE
        global CONTROL_STATE
        global ALT_STATE
        global keystring
        SHIFT_STATE = False
        CONTROL_STATE = False
        ALT_STATE = False
        SPACEBAR_STATE = False

        def on_press(key):
                global SHIFT_STATE
                global CONTROL_STATE
                global ALT_STATE
                global keystring
                global keyarray
                keystring = ""
                keyarray = ["","","","","","","","",""]
                if key == keyboard.Key.shift:
                        SHIFT_STATE = True
                elif key == keyboard.Key.ctrl:
                        CONTROL_STATE = True
                elif key == keyboard.Key.alt:
                        ALT_STATE = True
                elif key == keyboard.Key.space:
                        SPACEBAR_STATE = True
                else:
                        try:
                                if SHIFT_STATE:
                                        keyarray[0] = str("<shift>+")
                                if CONTROL_STATE:
                                        keyarray[1] = str("<ctrl>+")
                                if ALT_STATE:
                                        keyarray[2] = str("<alt>+")
                                else:
                                        keyarray[3] = str(""+str(key))

                        except Exception as e:
                                print(e)

        def on_release(key):
                global SHIFT_STATE
                global CONTROL_STATE
                global ALT_STATE
                global keyarray
                if key == keyboard.Key.shift:
                        SHIFT_STATE = False
                elif key == keyboard.Key.ctrl:
                        CONTROL_STATE = False
                elif key == keyboard.Key.alt:
                        ALT_STATE = False
                elif key == keyboard.Key.space:
                        SPACEBAR_STATE = False
                print(keyarray)
                return False

        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
                listener.join()

    def app(self):
        from os.path import exists

        tesseract_found = os.path.exists(str(prefs_reader.read_pref_imageproc("TesseractAI_SystemLocation")))
        if tesseract_found == True:
                pytesseract.pytesseract.tesseract_cmd = r''+prefs_reader.read_pref_imageproc("TesseractAI_SystemLocation")
        elif tesseract_found == False:
                self.item_desc.setText("Tesseract was unable to be located, please check the path settings.ini file!")


        self.load_settings()
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tilda", None))
        self.oldPos = self.pos()

        def launch_wiki_link(self):
                import webbrowser
                webbrowser.open(''+str(wiki_item_link), new=2)


        def launch_git_link(self):
                import webbrowser
                webbrowser.open(''+str("https://github.com/adrian-griffin/TILDA-EFT"), new=2)

        def launch_paypal_link(self):
                import webbrowser
                webbrowser.open(''+str("https://paypal.me/adriangriffin99"), new=2)

        def open_settings_ini_file(self):
                dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path_cleaned = dir_path.replace("\\","/")
        dir_path_usable = dir_path_cleaned+"/"
        os.startfile(dir_path_usable+'/settings.ini')

        self.exit_button.clicked.connect(self.exit_app)
        self.minimize_button.clicked.connect(self.minimize_app)
        self.settings_button.clicked.connect(self.open_settings)
        self.save_button.clicked.connect(self.save_settings)
        self.cancel_button.clicked.connect(self.return_to_main)
        self.pushButton_6.clicked.connect(self.enable_smm_overlay)
        popup_w.pushButton_2.clicked.connect(self.exit_app)
        popup_w.pushButton.clicked.connect(self.apply_popup_cancel)
        self.wiki_button.clicked.connect(launch_wiki_link)
        self.pushButton_7.clicked.connect(self.refresh_db_func)
        self.comboBox.currentIndexChanged.connect(self.capture_keystroke_edit)
        self.cancel_button_2.clicked.connect(self.apply_settings)
        self.hotkey_help_btn.clicked.connect(self.check_for_updates)
        self.pushButton.clicked.connect(launch_git_link)
        self.pushButton_2.clicked.connect(launch_paypal_link)
        self.pushButton_4.clicked.connect(open_settings_ini_file)
        #self.page_widget.currentChanged.connect(self.bootup_proc)
        self.setWindowFlags(
                Qt.FramelessWindowHint  
                )
        if prefs_reader.read_pref_graphics("KeepMainWindowOnTop") == "True":
                self.setWindowFlags(
                        Qt.WindowStaysOnTopHint |
                        Qt.FramelessWindowHint  
                        )

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.centralwidget.setAttribute(Qt.WA_NoSystemBackground, True)




        def text_grab(type):
        #self.item_desc.setText(QCoreApplication.translate("MainWindow", u"Scanner Running!", None))

                if prefs_reader.read_pref_scanner("ActiveScanAutoInspect") == "True":
                        primary_scan_auto_inspect = True
                else: 
                        primary_scan_auto_inspect = False
                if type=="P":
                        posx, posy = pyautogui.position()
                        image1 = pyautogui.screenshot(region=(posx,posy-70, 500, 70))
                        image1 = cv2.cvtColor(numpy.array(image1), cv2.COLOR_RGB2GRAY)
                        image1 = cv2.bitwise_not(image1)
                        time.sleep(1.3)

                        image2 = pyautogui.screenshot(region=(posx,posy-70, 500, 70))

                        image_original = cv2.cvtColor(numpy.array(image2), cv2.COLOR_RGB2BGR)
                        numpyarray_orig = numpy.array(image_original)
                        
                        image2 = cv2.cvtColor(numpy.array(image2), cv2.COLOR_RGB2GRAY)
                        image2 = cv2.bitwise_not(image2)

                        difference = cv2.subtract(image2, image1)
                        im_diff = cv2.cvtColor(difference, cv2.COLOR_BGR2RGB)
                        na = numpy.array(im_diff)
                        #cv2.imwrite("diff.png",na)
                        na[numpy.all(na>[2, 2, 2],axis=2)] = (255,255,255)

                        hoverY, hoverX = numpy.where(numpy.all(na==[255, 255, 255],axis=2))
                        
                        try:
                                top, bottom = hoverY[0], hoverY[-1]
                                left, right = hoverX[0], hoverX[-1]
                                # Extract Region of Interest
                                ROI = numpyarray_orig[top:bottom, left:right]

                                resultimg = Image.fromarray(ROI)
                                #item_query()
                        except IndexError:
                                win_m.item_desc.setText(QCoreApplication.translate("MainWindow", u"No Item Found!!", None))


                elif type=="A":
                        import dbman
                        import imutils
                        win_m.item_desc.setText(QCoreApplication.translate("MainWindow", u"Starting Scan", None))
                        if primary_scan_auto_inspect == True:
                                pyautogui.click()
                                pyautogui.click()
                                screenshot = pyautogui.screenshot()
                        else:
                                screenshot = pyautogui.screenshot()
                        scrot = cv2.cvtColor(numpy.array(screenshot), cv2.COLOR_RGB2BGR)
                        template = cv2.imread("search_icon_image.png")
                        
                        

                        try:
                                result = cv2.matchTemplate(template,scrot,cv2.TM_SQDIFF_NORMED)
                                mn,_,mnLoc,_ = cv2.minMaxLoc(result)


                                MPx,MPy = mnLoc
                                trows,tcols = template.shape[:2]
                                cv2.rectangle(scrot, (MPx,MPy), (MPx+tcols,MPy+trows),(0,0,255),2)
                                header = pyautogui.screenshot(region=(MPx,MPy, 642, 25))
                                resultimg = cv2.cvtColor(numpy.array(header), cv2.COLOR_RGB2BGR)

                                static_template_img_to_text = pytesseract.image_to_string(resultimg)
                                item_list = dbman.item_list
                                close_matches = difflib.get_close_matches(static_template_img_to_text,item_list)
                                closest = close_matches[0]
                        except:
                                scrot = cv2.cvtColor(scrot, cv2.COLOR_BGR2GRAY)
                                template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
                                loc = False
                                threshold = 0.8
                                w, h = template.shape[::-1]
                                for scale_aba in numpy.linspace(0.0, 2.0, 20)[::-1]:
                                        resized = imutils.resize(template, width = int(template.shape[1] * scale_aba))
                                        w, h = resized.shape[::-1]
                                        res = cv2.matchTemplate(scrot,resized,cv2.TM_CCOEFF_NORMED)

                                        loc = numpy.where( res >= threshold)
                                        if len(list(zip(*loc[::-1]))) > 0:
                                                break

                                if loc and len(list(zip(*loc[::-1]))) > 0:
                                        for pt in zip(*loc[::-1]):
                                                cv2.rectangle(scrot, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                                        header = pyautogui.screenshot(region=(pt[0], pt[1], 250*scale_aba, 20*scale_aba))
                                resultimg = cv2.cvtColor(numpy.array(header), cv2.COLOR_RGB2BGR)
                                import dbman
                                scaled_template_img_to_text = pytesseract.image_to_string(resultimg)
                                item_list = dbman.item_list
                                close_matches = difflib.get_close_matches(scaled_template_img_to_text,item_list)
                                closest = close_matches[0]
                        if primary_scan_auto_inspect == True:
                                pyautogui.press('esc')

                text1 = pytesseract.image_to_string(resultimg)
                #print("Stopping Scan")
                return(text1)


        def item_guess(type):
                import dbman
                text = text_grab(type)
                item_list = dbman.item_list
                close_matches = difflib.get_close_matches(text,item_list)
                closest = close_matches[0]
                #print("Item Found:")
                return closest

        def item_lookup(type):
                import sqlite3
                #print("item_lookup() called")
                
                item_dbpy = sqlite3.connect(str(dir_path)+"\\"+"item_info.sql")
                c = item_dbpy.cursor()
                closest = item_guess(type)
                final_price_list = []
                final_price_list.clear()
                ### Set Item Name

                for row in item_dbpy.execute('SELECT name FROM items where name = "'+str(closest)+'"'):
                        win_m.item_desc.setText(QCoreApplication.translate("MainWindow", u""+str(row[0]), None))
                
                for row in item_dbpy.execute('SELECT shortName FROM items where name = "'+str(closest)+'"'):
                        smm_w.smm_name_val.setText(QCoreApplication.translate("MainWindow", u""+str(row[0]), None))
                
                for row in item_dbpy.execute('SELECT avg24hPrice FROM items where name = "'+str(closest)+'"'):
                        avg_24hr_price_comma = "{:,}".format(int(row[0]))
                        win_m.avg_flea_val.setText(QCoreApplication.translate("MainWindow", u""+str(avg_24hr_price_comma+" ₽"), None))
                        smm_w.smm_flea_val.setText(QCoreApplication.translate("MainWindow", u""+str(avg_24hr_price_comma+" ₽"), None))
                        final_price_list.append(row[0])



                trade_list_price = []
                trade_list_price.clear()
                trade_list_name = []
                trade_list_name.clear()
                trade_list_currency = []
                trade_list_currency.clear()

                for row in item_dbpy.execute('SELECT * FROM sellFor where name = "'+str(closest)+'"'):
                        #vendor_price_comma = "{:,}".format(int(row[3]))
                        vendor_price_comma = int(row[3])
                        trade_list_price.append(vendor_price_comma)
                        vendor_name = row[2]
                        trade_list_name.append(vendor_name)
                        vendor_currency = row[4]
                        trade_list_currency.append(vendor_currency)


                for flea_vendor_del in trade_list_name:
                        if flea_vendor_del == "Flea Market":
                                flea_vendor_index = trade_list_name.index("Flea Market")
                                del trade_list_name[flea_vendor_index]
                                del trade_list_currency[flea_vendor_index]
                                del trade_list_price[flea_vendor_index]
                        else:
                                pass


                for curr_vendor_sellFor in trade_list_currency:
                        if curr_vendor_sellFor == "RUB":
                                pass
                        if curr_vendor_sellFor == "USD":
                                USD_index = trade_list_currency.index("USD")
                                for row in item_dbpy.execute('SELECT * FROM buyFor where name = "Dollars"'):
                                        price_before_norm_USD = trade_list_price[USD_index]
                                        USD_RUB_conversion_factor = int(row[3])
                                        USD_to_RUB_trade=(int(trade_list_price[USD_index])*USD_RUB_conversion_factor)
                                        #print(trade_list_price[USD_index],USD_to_RUB_trade)
                                        trade_list_price[USD_index] = int(USD_to_RUB_trade)
                                        trade_list_currency[USD_index] = "RUB"

                        if curr_vendor_sellFor == "EUR":
                                EUR_index = trade_list_currency.index("EUR")
                                for row in item_dbpy.execute('SELECT * FROM buyFor where name = "Euros"'):
                                        price_before_norm_EUR = trade_list_price[EUR_index]
                                        EUR_RUB_conversion_factor = int(row[3])
                                        EUR_to_RUB_trade=(int(trade_list_price[EUR_index])*EUR_RUB_conversion_factor)
                                        trade_list_price[EUR_index] = int(EUR_to_RUB_trade)
                                        trade_list_currency[EUR_index] = "RUB"

                highest_price_to_trader = max(trade_list_price)
                final_price_list.append(highest_price_to_trader)
                highest_price_vendor_name = trade_list_name[trade_list_price.index(highest_price_to_trader)]

                highest_price_to_trader_comma = "{:,}".format(int(highest_price_to_trader))
                if highest_price_vendor_name == "Therapist":
                        highest_price_vendor_name_abb = "T"
                elif highest_price_vendor_name == "Skier":
                        highest_price_vendor_name_abb = "S"
                elif highest_price_vendor_name == "Mechanic":
                        highest_price_vendor_name_abb = "M"
                elif highest_price_vendor_name == "Peacekeeper":
                        highest_price_vendor_name_abb = "PK"
                elif highest_price_vendor_name == "Jaeger":
                        highest_price_vendor_name_abb = "J"
                elif highest_price_vendor_name == "Fence":
                        highest_price_vendor_name_abb = "F"
                elif highest_price_vendor_name == "Ragman":
                        highest_price_vendor_name_abb = "R"
                elif highest_price_vendor_name == "Prapor":
                        highest_price_vendor_name_abb = "PR"

                win_m.best_trader_val.setText(QCoreApplication.translate("MainWindow", u""+str(highest_price_to_trader_comma+" ₽"), None))
                win_m.label.setText(QCoreApplication.translate("MainWindow", u""+"("+str(highest_price_vendor_name+")"), None))

                smm_w.smm_trader_val.setText(QCoreApplication.translate("MainWindow", u""+str(highest_price_to_trader_comma+" ₽"), None))
                smm_w.smm_trader_name.setText(QCoreApplication.translate("MainWindow", u""+"("+str(highest_price_vendor_name_abb+")"), None))


                for row in item_dbpy.execute('SELECT width FROM items where name = "'+str(closest)+'"'):
                        width = int(row[0])
                for row in item_dbpy.execute('SELECT height FROM items where name = "'+str(closest)+'"'):
                        height = int(row[0])
                area = (width*height)
                if area == 1:
                        slot_plural_cleaner = "slot"
                else:
                        slot_plural_cleaner = "slots"
                win_m.spacer_label.setText(QCoreApplication.translate("MainWindow", u"("+str(area)+" "+str(slot_plural_cleaner)+")", None))
                smm_w.smm_slot_size.setText(QCoreApplication.translate("MainWindow", u"("+str(area)+")", None))

                ### Set most recent flea price
                for row in item_dbpy.execute('SELECT lastLowPrice FROM items where name = "'+str(closest)+'"'):
                        last_low_price_comma = "{:,}".format(int(row[0]))
                        win_m.lowest_flea_val.setText(QCoreApplication.translate("MainWindow", u""+str(last_low_price_comma+" ₽"), None))
                        final_price_list.append(row[0])
                
                for row in item_dbpy.execute('SELECT tasks FROM usedInTasks where name = "'+str(closest)+'"'):
                        task_list_from_db_str = row[0]
                        task_list_from_db_array = task_list_from_db_str.split(",")
                        del task_list_from_db_array[-1]
                        win_m.needed_for_quests_val.setText(QCoreApplication.translate("MainWindow", u""+str(len(task_list_from_db_array)), None))                
                
                final_price_list_max = max(final_price_list)
                price_per_slot = (int(final_price_list_max)/int(area))
                price_per_slot_comma = "{:,}".format(int(price_per_slot))
                win_m.price_per_slot_val.setText(QCoreApplication.translate("MainWindow", u""+str(price_per_slot_comma)+" ₽", None))
                smm_w.smm_slot_val.setText(QCoreApplication.translate("MainWindow", u""+str(price_per_slot_comma)+" ₽", None))

                for row in item_dbpy.execute('SELECT iconLink FROM items where name = "'+str(closest)+'"'):
                        icon_image_link = row[0]
                url = str(icon_image_link)
                data = requests.get(url).content
                with open('tmp_item_img.jpg', 'wb') as handler:
                        handler.write(data)
                win_m.item_image_label.setPixmap(QPixmap(u'tmp_item_img.jpg'))

                for row in item_dbpy.execute('SELECT wikiLink FROM items where name = "'+str(closest)+'"'):
                        global wiki_item_link
                        wiki_item_link = row[0]
                        
                





        def key_event_ear():
            print("key_event_ear() called")
                ## To ensure communication between CPU threads:
            def toggle_smm_overlay():
                if cached_session_smm_token == 0:
                        if win_m.isHidden() == False:
                                win_m.pushButton_6.click()
                        elif win_m.isHidden() == True:
                                smm_w.smm_overlay_toggle_button.click()  
                elif cached_session_smm_token > 0:
                        if win_m.isHidden() == False:
                                self.enable_smm_overlay()
                        elif win_m.isHidden() == True:
                                smm_w.init_smm_exit_activation()

            def item_scan_quick():
                if prefs_reader.read_pref_scanner("ScanEngine") == "Passive":
                        item_lookup_thread = Thread(daemon=True, target=item_lookup,args=("P"))
                        item_lookup_thread.start()
                        
                elif prefs_reader.read_pref_scanner("ScanEngine") == "Dual":
                        item_lookup_thread = Thread(daemon=True, target=item_lookup,args=("P"))
                        item_lookup_thread.start()
                        


            def item_scan_full():
                print("activating active scan")
                if prefs_reader.read_pref_scanner("ScanEngine") == "Active":
                        item_lookup_thread = Thread(daemon=True, target=item_lookup,args=("A"))
                        item_lookup_thread.start()     
                elif prefs_reader.read_pref_scanner("ScanEngine") == "Dual": 
                        item_lookup_thread = Thread(daemon=True, target=item_lookup,args=("A"))
                        item_lookup_thread.start() 

            def toggle_overlay_listener():
                toggle_smm_overlay()
                #toggle_overlay_listener_thread = Thread(daemon=True, target=toggle_smm_overlay)       
                #toggle_overlay_listener_thread.start()  
                
            print("keystroke listener active")    
            with keyboard.GlobalHotKeys({
                prefs_reader.read_pref_keybinds("SecondaryScanKeybind"): item_scan_quick,
                prefs_reader.read_pref_keybinds("PrimaryScanKeybind"): item_scan_full,
                prefs_reader.read_pref_keybinds("ToggleOverlayKeybind"): toggle_overlay_listener,}) as h:
                h.join()
        

        
        main_app_thread = Thread(target=key_event_ear)
        if prefs_reader.read_pref_scanner("UseCachedData") == "False":
                self.refresh_db_func()
                self.item_desc.setText("Database has been successfully refreshed and cached!")
        else:
                self.item_desc.setText("Database was not refreshed, using locally cached data")
        main_app_thread.start()
        
class UPDOG(QMainWindow, updog_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        title = "Tilda - Updating"
        self.setWindowTitle(title)
        self.setWindowFlags(
                        Qt.WindowStaysOnTopHint |
                        Qt.FramelessWindowHint
                        )

        self.pushButton_2.clicked.connect(self.cancel_update)
        self.pushButton.clicked.connect(self.accept_update)
        self.pushButton_4.clicked.connect(self.apply_update)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPosition().toPoint()
 
    def cancel_update(self):
        self.hide()
        win_m.show()
        win_m.page_widget.setCurrentIndex(1)

    def accept_update(self):
        win_m.hide()
        import update_check
        import requests, zipfile, io, os, subprocess
        self.stackedWidget.setCurrentIndex(1)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path_cleaned = dir_path.replace("\\","/")
        dir_path_usable = dir_path_cleaned+"/"
        update_check.update(dir_path_cleaned+"udlc.txt","https://raw.githubusercontent.com/adrian-griffin/TILDA-EFT/main/Tilda%20Source/udlc.txt")
        if os.path.exists(dir_path_usable+"UPDATE_TMP/TildaUpdater.exe"):
                os.remove(dir_path_usable+"UPDATE_TMP/TildaUpdater.exe")
        else:
                pass
        with open(dir_path_cleaned+"udlc.txt", 'r') as file:
                udlc = file.read().rstrip()
        r = requests.get(udlc) 
        self.label_4.setText("Downloading and Extracting ...")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(dir_path_usable+"UPDATE_TMP/")
        self.label_3.setText("Download finished")
        self.label_4.setText("Please click Apply")
        self.pushButton_4.setEnabled(True)

    def apply_update(self):
        import subprocess
        dir_path_cleaned = dir_path.replace("\\","/")
        dir_path_usable = dir_path_cleaned+"/"
        current_dir = r""+dir_path_usable+"UPDATE_TMP/"
        subprocess.Popen(os.path.join(current_dir,current_dir+"TildaUpdater.exe"))
        self.hide()
        os._exit(0)

class SMM(QMainWindow, compact_overlay_ui.Ui_smm_window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        import prefs_reader
        title = "Tilda"
        self.setWindowTitle(title)
        if prefs_reader.read_pref_graphics("KeepOverlayWindowOnTop") == "True":
                self.setWindowFlags(
                        Qt.WindowStaysOnTopHint |
                        Qt.FramelessWindowHint
                        )
        elif prefs_reader.read_pref_graphics("KeepOverlayWindowOnTop") == "False":
                self.setWindowFlags(
                        Qt.FramelessWindowHint
                        )   
        self.frame.setStyleSheet(u"QFrame {\n"
        "background-color: rgb(13, 12, 23);\n"
        "border: 1px solid rgba(230, 5, 64, 0);\n"
        "\n"
        "}")    
    def mousePressEvent(self, event):
        smm_move_toggle_bool = self.smm_move_button.isChecked()
        if smm_move_toggle_bool == True:
                self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        smm_move_toggle_bool = self.smm_move_button.isChecked()
        if smm_move_toggle_bool == True:
                delta = QPoint(event.globalPosition().toPoint() - self.oldPos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPos = event.globalPosition().toPoint()
        

    def init_smm_move_activation(self, smm_window):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tilda ~ Overlay", None))
        smm_move_toggle_bool = self.smm_move_button.isChecked()
        if smm_move_toggle_bool == True:
                self.frame.setStyleSheet(u"QFrame {\n"
        "background-color: rgb(13, 12, 23);\n"
        "border: 1px solid rgba(230, 5, 64, .60);\n"
        "\n"
        "}")
        elif smm_move_toggle_bool == False: 
                self.frame.setStyleSheet(u"QFrame {\n"
        "background-color: rgb(13, 12, 23);\n"
        "border: 1px solid rgba(230, 5, 64, 0);\n"
        "\n"
        "}")        

        self.centralwidget.update()
        self.centralwidget.show()
        #Ui_MainWindow.enable_smm_overlay(Ui_MainWindow)

    def init_smm_exit_activation(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tilda", None))
        self.hide()
        win_m.show()

    def smm_app(self, smm_window):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tilda ~ Overlay", None))

        self.smm_move_button.clicked.connect(self.init_smm_move_activation)
        self.smm_overlay_toggle_button.clicked.connect(self.init_smm_exit_activation)
        self.show()
    
def win_m_mod():
        bloader.progressBar.setValue(0)

def main_application_controller():
        import random as rnd
        
        for i in range(101):
                bloader_set_val(i)
                rnd_numer = (rnd.randint(1,50))
                rnd_denom = (rnd.randint(3,12))
                coeff = (rnd_numer/rnd_denom)
                time.sleep(float(0.006*coeff))

def bloader_set_val(perc_val):
        import random as rnd
        loading_strings = [ "Reticulating splines...", "Generating witty dialog...", "Swapping time and space...", "Spinning violently around the y-axis...", "Tokenizing real life...", "Bending the spoon...", "Filtering morale...", "Don't think of purple hippos...", "We need a new fuse...", "Have a good day.", "Upgrading Windows, your PC will restart several times. Sit back and relax.", "640K ought to be enough for anybody", "The architects are still drafting", "The bits are breeding", "We're building the buildings as fast as we can", "Would you prefer chicken, steak, or tofu?", "(Pay no attention to the man behind the curtain)", "...and enjoy the elevator music...", "Please wait while the little elves draw your map", "Don't worry - a few bits tried to escape, but we caught them", "Would you like fries with that?", "Checking the gravitational constant in your locale...", "Go ahead -- hold your breath!", "...at least you're not on hold...", "Hum something loud while others stare", "You're not in Kansas any more", "The server is powered by a lemon and two electrodes.", "Please wait while a larger software vendor in Seattle takes over the world", "We're testing your patience", "As if you had any other choice", "Follow the white rabbit", "Why don't you order a sandwich?", "While the satellite moves into position", "keep calm and npm install", "The bits are flowing slowly today", "Dig on the 'X' for buried treasure... ARRR!", "It's still faster than you could draw it", "The last time I tried this the monkey didn't survive. Let's hope it works better this time.", "I should have had a V8 this morning.", "My other loading screen is much faster.", "Testing on Timmy... We're going to need another Timmy.", "Reconfoobling energymotron...", "(Insert quarter)", "Are we there yet?", "Have you lost weight?", "Just count to 10", "Why so serious?", "It's not you. It's me.", "Counting backwards from Infinity", "Don't panic...", "Embiggening Prototypes", "Do not run! We are your friends!", "Do you come here often?", "Warning: Don't set yourself on fire.", "We're making you a cookie.", "Creating time-loop inversion field", "Spinning the wheel of fortune...", "Loading the enchanted bunny...", "Computing chance of success", "I'm sorry Dave, I can't do that.", "Looking for exact change", "All your web browser are belong to us", "All I really need is a kilobit.", "I feel like im supposed to be loading something. . .", "What do you call 8 Hobbits? A Hobbyte.", "Should have used a compiled language...", "Is this Windows?", "Adjusting flux capacitor...", "Please wait until the sloth starts moving.", "Don't break your screen yet!", "I swear it's almost done.", "Let's take a mindfulness minute...", "Unicorns are at the end of this road, I promise.", "Listening for the sound of one hand clapping...", "Keeping all the 1's and removing all the 0's...", "Putting the icing on the cake. The cake is not a lie...", "Cleaning off the cobwebs...", "Making sure all the i's have dots...", "We need more dilithium crystals", "Where did all the internets go", "Connecting Neurotoxin Storage Tank...", "Granting wishes...", "Time flies when you’re having fun.", "Get some coffee and come back in ten minutes..", 
        "Spinning the hamster…", "99 bottles of beer on the wall..", "Stay awhile and listen..", "Be careful not to step in the git-gui", "You edhall not pass! yet..", "Load it and they will come", "Convincing AI not to turn evil..", "There is no spoon. Because we are not done loading it", "Your left thumb points to the right and your right thumb points to the left.", "How did you get here?", "Wait, do you smell something burning?", "Computing the secret to life, the universe, and everything.", "When nothing is going right, go left!!...", "I love my job only when I'm on vacation...", "i'm not lazy, I'm just relaxed!!", "Never steal. The government hates competition....", "Why are they called apartments if they are all stuck together?", "Life is Short – Talk Fast!!!!", "Optimism – is a lack of information.....", "Save water and shower together", "Whenever I find the key to success, someone changes the lock.", "Sometimes I think war is God’s way of teaching us geography.", "I’ve got problem for your solution…..", "Where there’s a will, there’s a relative.", "User: the word computer professionals use when they mean !!idiot!!", "Adults are just kids with money.", "I think I am, therefore, I am. I think.", "A kiss is like a fight, with mouths.", "You don’t pay taxes—they take taxes.", "Coffee, Chocolate, Men. The richer the better!", "I am free of all prejudices. I hate everyone equally.", "git happens", "May the forks be with you", "A commit a day keeps the mobs away", "This is not a joke, it's a commit.", "Constructing additional pylons...", "Roping some seaturtles...", "Locating Jebediah Kerman...", "We are not liable for any broken screens as a result of waiting.", "Hello IT, have you tried turning it off and on again?", "If you type Google into Google you can break the internet", "Well, this is embarrassing.", "What is the airspeed velocity of an unladen swallow?", "Hello, IT... Have you tried forcing an unexpected reboot?", "They just toss us away like yesterday's jam.", "They're fairly regular, the beatings, yes. I'd say we're on a bi-weekly beating.", "The Elders of the Internet would never stand for it.", "Space is invisible mind dust, and stars are but wishes.", "Didn't know paint dried so quickly.", "Everything sounds the same", "I'm going to walk the dog", "I didn't choose the engineering life. The engineering life chose me.", "Dividing by zero...", "Spawn more Overlord!", "If I’m not back in five minutes, just wait longer.", "Some days, you just can’t get rid of a bug!", "We’re going to need a bigger boat.", "Chuck Norris never git push. The repo pulls before.", "Web developers do it with <style>", "I need to git pull --my-life-together", "Java developers never RIP. They just get Garbage Collected.", "Cracking military-grade encryption...", "Simulating traveling salesman...", "Proving P=NP...", "Entangling superstrings...", "Twiddling thumbs...", "Searching for plot device...", "Trying to sort in O(n)...", "Laughing at your pictures-i mean, loading...", "Sending data to NS-i mean, our servers.", "Looking for sense of humour, please hold on.", "Please wait while the intern refills his coffee.", "A different error message? Finally, some progress!", 
        "Hold on while we wrap up our git together...sorry", "Please hold on as we reheat our coffee", "Kindly hold on as we convert this bug to a feature...", "Kindly hold on as our intern quits vim...", "Winter is coming...", "Installing dependencies", "Switching to the latest JS framework...", "Distracted by cat gifs", "Finding someone to hold my beer", "BRB, working on my side project", "@todo Insert witty loading message", "Let's hope it's worth the wait", "Aw, snap! Not..", "Ordering 1s and 0s...", "Updating dependencies...", "Whatever you do, don't look behind you...", "Please wait... Consulting the manual...", "It is dark. You're likely to be eaten by a grue.", "Loading funny message...", "It's 10:00pm. Do you know where your children are?", "Waiting Daenerys say all her titles...", "Feel free to spin in your chair", "What the what?", "format C: ...", "Forget you saw that password I just typed into the IM ...", "What's under there?", "Your computer has a virus, its name is Windows!", "Go ahead, hold your breath and do an ironman plank till loading complete", "Bored of slow loading spinner, buy more RAM!", "Help, I'm trapped in a loader!", "What is the difference btwn a hippo and a zippo? One is really heavy, the other is a little lighter", "Please wait, while we purge the Decepticons for you. Yes, You can thanks us later!", "Chuck Norris once urinated in a semi truck's gas tank as a joke....that truck is now known as Optimus Prime.", "Chuck Norris doesn’t wear a watch. HE decides what time it is.", "Mining some bitcoins...", "Downloading more RAM..", "Updating to Windows Vista...", "Deleting System32 folder", "Hiding all ;'s in your code", "Alt-F4 speeds things up.", "Initializing the initializer...", "When was the last time you dusted around here?", "Optimizing the optimizer...", "Last call for the data bus! All aboard!", "Running swag sticker detection...", "Never let a computer know you're in a hurry.", "A computer will do what you tell it to do, but that may be much different from what you had in mind.", "Some things man was never meant to know. For everything else, there's Google.", "Unix is user-friendly. It's just very selective about who its friends are.", "Shovelling coal into the server", "Pushing pixels...", "How about this weather, eh?", "Building a wall...", "Everything in this universe is either a potato or not a potato", "The severity of your issue is always lower than you expected.", "Updating Updater...", "Downloading Downloader...", "Debugging Debugger...", "Reading Terms and Conditions for you.", "Digested cookies being baked again.", "Live long and prosper.", "There is no cow level, but there's a goat one!", "Deleting all your hidden porn...", "Running with scissors...", "Definitely not a virus...", "You may call me Steve.", "You seem like a nice person...", "Coffee at my place, tommorow at 10A.M. - don't be late!", "Work, work...", "Patience! This is difficult, you know...", "Discovering new ways of making you wait...", "Your time is very important to us. Please wait while we ignore you...", "Time flies like an arrow; fruit flies like a banana", "Two men walked into a bar; the third ducked...", "Sooooo... Have you seen my vacation photos yet?", 
        "Sorry we are busy catching em' all, we're done soon", "TODO: Insert elevator music", "Still faster than Windows update", "Composer hack: Waiting for reqs to be fetched is less frustrating if you add -vvv to your command.", "Please wait while the minions do their work", "Grabbing extra minions", "Doing the heavy lifting", "We're working very Hard .... Really", "Waking up the minions", "You are number 2843684714 in the queue", "Please wait while we serve other customers...", "Our premium plan is faster", "Feeding unicorns...", "Rupturing the subspace barrier", "Creating an anti-time reaction", "Converging tachyon pulses", "Bypassing control of the matter-antimatter integrator", "Adjusting the dilithium crystal converter assembly", "Reversing the shield polarity", "Disrupting warp fields with an inverse graviton burst"]

        if perc_val > 98:
                bloader.progressBar.setValue(100)
                time.sleep(0.44)
                bloader.hide()
                smm_w.show()
                smm_w.smm_overlay_toggle_button.click()
                
                
        elif perc_val == rnd.randint(27,40):
                if prefs_reader.read_pref_scanner("UseCachedData") == "False":
                        bloader.info_text.setText(QCoreApplication.translate("LoadWindow", u"Refreshing & Caching Item Data", None))
                elif prefs_reader.read_pref_scanner("UseCachedData") == "True":
                        bloader.info_text.setText(QCoreApplication.translate("LoadWindow", u"Reading Locally Cached Item Data", None))
                time.sleep(0.391)
        elif perc_val == rnd.randint(63,74):
                bloader.info_text.setText(QCoreApplication.translate("LoadWindow", u"Checking Saved Settings", None))
                time.sleep(0.636)                
        else:
                bloader.progressBar.setValue(int(perc_val))

if __name__ == "__main__":
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon("icon.ico"))
        updog_w = UPDOG()
        updog_w.hide()
        bloader = BLLW()
        bloader.hide()
        smm_w = SMM()
        smm_w.smm_app(smm_w)
        smm_w.hide()
        win_m = Window()
        win_m.hide()
        popup_w = PUDW()
        popup_w.hide()
        Window.app(win_m)
        bloader.show()
        bg_main_application_controller_thread = Thread(daemon=True,target=main_application_controller)
        bg_main_application_controller_thread.start()
        global cached_session_smm_token
        cached_session_smm_token = 0
        sys.exit(app.exec())