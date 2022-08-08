## Tilda ~~ A Fast and Reliable Escape From Tarkov Item Scanner
Tilda is a heavily customizable, lightweight, and quick scanner that helps you easily get useful information about items in Escape From Tarkov while in game.

Gone are the days of having your friend (or yourself) look up that 22 inch barrel that you aren't sure whether is worth 4K or 120K on the flea market.

Need to know whether an item you found in raid is used in any quests? Or whether that blue electric drill is still worth at least 10K per slot?

Tilda will automatically scan the item you select, and within less than a second it will return any useful information you would need at a moment's notice, from the average Flea Market price of said item, to the trader it is best sold to (and the price it sells to them), the price per slot based off of the highest price you can sell for, how many quests the item is used in, and even a quick link to the Tarkov Wiki with the click of a button!

All images and showcases of Tilda in action are below.
All download and install files are available within the Download folder in this repository.
**ALL** code for the project is open source, using Tesseract's machine learning and OpenCV2 and Numpy's computer vision processing, written entirely in Python and C, making the application very quick and incredibly fast at scanning.

![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/ActiveWAutoInspect.gif)



## How It Works - Basics:
First and foremost, it is important to mention that Tilda has two separate scan options currently available, though the scanning and processing method differs heavily between the two, both use simple screenshots of the EFT application to gather information about the item you are scanning. In short, the application takes a screenshot of the EFT application, and then determines the item you are wanting scanned using two different methods. From there, a rather hefty database is searched to find the exact item you are looking for, where it them returns all the juicy information about it within the app's display. 

This does *NOT* in **ANY** way access the game memory or use any other method of information gathering in the same vein, therefore, it can hardly be considered "cheating". Tilda just grabs the information you can already look up on the Tarkov Wiki for you, and displays it all in one place within seconds (rather than having to Alt+Tab and try searching the web).

More information regarding the methods used is readable below, if you are interested or skeptical.

## How to Use Both Scan Types
#### Scan Type 1 (Active/Primary Scan)
The first scan method (referred to as the Active or Primary scan), uses the pop-up window that appears after inspecting or double-clicking an item in game. The convenient bit here is that the pop-up always has the search-glass icon in the top left, with the full, unique name of the item just to the right. 

The Active scan uses this search-glass icon to 'template' search the screenshot, find the search-glass picture, and then analyses the text to the right within a variable-scaling pixel value window.

The default keybind for this scan is the '~' key, or the key directly above tab. You may need to unbind this key from console in the EFT settings menu.

#### Active scan using the pop-up window with the auto-inspect and scan option enabled in the settings

![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/ActiveWAutoInspect.gif)

#### Active scan using the pop-up window without auto-inspect enabled, requiring manual double click and pressing of 'escape' afterwards

![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/ActiveWOAutoInspect.gif)


#### Scan Type 2 (Passive/Secondary Scan)
Passive scans use the tool-tip-esque pop-up that appears after hovering over an item for about 1 second in game to identify the item. When using this, it is important to note that the scan must be started *before* the tooltip appears, and to wait until the scan completes before moving the mouse away from the item.

#### The default keybind for this scan is 'Ctrl+Shift+S'
![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/Passive.gif)

## Overlay Mode & Window Persistence 

Pressing the "Overlay" button on the menu itself, or pressing the Overlay Toggle Keybind (default is 'Ctrl+Shift+Q') will enable the overlay mode, which can be moved around the screen after pressing the move button, when the overlay becomes bordered in red. Move mode can be toggled by pressing the move button once again.

![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/OverlayActivation.gif)
![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/OverlayMove.gif)

### Window Persistence
It is worth noting that both the main window and the overlay window retain their location on screen, so when swapping between them, they will be where you last placed them. A good usage example of this is to put the overlay window on your main monitor over the game in a location of your choosing, and then place the main window on a second monitor. Presing 'Ctrl+Shift+Q' (or whatever your toggle overlay keybind is) will quickly swap between the two depending on your needs at the time.
![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/OverlayPersistent.gif)


## ETC

### Wiki Link Button
After successfully scanning any item, pressing the Wiki button from the main menu (there is no keybind for this, but that *can* be implemented if there is demand for it) will immediately open the item's page on the Escape from Tarkov wiki in a new tab on your default browser.

![alt text](https://github.com/adrian-griffin/TILDA-EFT/blob/main/Showcase%20Media/WikiButton.gif)
