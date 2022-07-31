## Tilda ~~ A Fast and Reliable Escape From Tarkov Item Scanner
Tilda is a heavily customizable, lightweight, and quick scanner that helps you easily get useful information about items in Escape From Tarkov while in game.

Gone are the days of having your friend (or yourself) look up that 22 inch barrel that you aren't sure whether is worth 4K or 120K on the flea market.

Need to know whether an item you found in raid is used in any quests? Or whether that blue electric drill is still worth at least 10K per slot?

Tilda will automatically scan the item you select, and within less than a second it will return any usefull information you would need at a moment's notice, from the average Flea Market price of said item, to the trader it is best sold to (and the price it sells to them), the price per slot based off of the highest price you can sell for, how many quests the item is used in, and even a quick link to the Tarkov Wiki with the click of a button!

All images and showcases of Tilda in action are below.
All download and install files are available within the Download folder in this repository.
**ALL** code for the project is open source, using Tesseract's machine learning and OpenCV2 and Numpy's computer vision processing, written entirely in Python and C, making the application very quick and incredibly fast at scanning.



## How It Works - Basics:
First and foremost, it is important to mention that Tilda has two separate scan options currently available, though the scanning and processing method differs heavily between the two, both use simple screenshots of the EFT application to gather information about the item you are scanning. In short, the application takes a screenshot of the EFT application, and then determines the item you are wanting scanned using two different methods. From there, a rather hefty database is searched to find the exact item you are looking for, where it them returns all the juicy information about it within the app's display. 

This does *NOT* in **ANY** way access the game memory or use any other method of information gathering in the same vein, therefore, it can hardly be considered "cheating". Tilda just grabs the information you can already look up on the Tarkov Wiki for you, and displays it all in one place within seconds (rather than having to Alt+Tab and try searching the web).

More information regarding the methods used is readable below, if you are interested or skeptical.

## How to Use Both Scan Types
#### Scan Type 1 (Active/Primary Scan)
The first scan method (referred to as the Active or Primary scan), uses the pop-up window that appears after inspecting or double-clicking an item in game. The convenient bit here is that the pop-up always has the search-glass icon in the top left, with the full, unique name of the item just to the right. 

The Active scan uses this in that it
