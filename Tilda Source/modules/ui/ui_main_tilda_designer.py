# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_tilda_designerjZoEJM.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(355, 505)
        MainWindow.setMinimumSize(QSize(355, 505))
        MainWindow.setMaximumSize(QSize(355, 505))
        font = QFont()
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"background-color: rgb(13, 12, 23);")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFont(font)
        self.main_body.setStyleSheet(u"background-color: rgb(13, 12, 23);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titlebar_frame = QFrame(self.main_body)
        self.titlebar_frame.setObjectName(u"titlebar_frame")
        self.titlebar_frame.setMinimumSize(QSize(0, 0))
        self.titlebar_frame.setMaximumSize(QSize(16777215, 40))
        self.titlebar_frame.setFont(font)
        self.titlebar_frame.setStyleSheet(u"QFrame {\n"
"background-color: rgb(0,0,0);\n"
"border: 1px solid black;\n"
"}")
        self.titlebar_frame.setFrameShape(QFrame.NoFrame)
        self.titlebar_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.titlebar_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.titlebar_frame)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.horizontalLayout_5.addWidget(self.title)

        self.button_frame = QFrame(self.titlebar_frame)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMinimumSize(QSize(93, 30))
        self.button_frame.setMaximumSize(QSize(90, 30))
        self.button_frame.setFont(font)
        self.button_frame.setLayoutDirection(Qt.LeftToRight)
        self.button_frame.setStyleSheet(u"")
        self.button_frame.setFrameShape(QFrame.NoFrame)
        self.button_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.button_frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.settings_button = QPushButton(self.button_frame)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMinimumSize(QSize(32, 0))
        self.settings_button.setMaximumSize(QSize(16777215, 16777215))
        self.settings_button.setLayoutDirection(Qt.RightToLeft)
        self.settings_button.setStyleSheet(u"QPushButton {\n"
"color: none; \n"
"background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/primary_ui_elems/ui_elements/media/toggle_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QSize(30, 26))
        self.settings_button.setCheckable(True)
        self.settings_button.setChecked(False)
        self.settings_button.setFlat(True)

        self.horizontalLayout.addWidget(self.settings_button)

        self.minimize_button = QPushButton(self.button_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.minimize_button.sizePolicy().hasHeightForWidth())
        self.minimize_button.setSizePolicy(sizePolicy1)
        self.minimize_button.setMinimumSize(QSize(30, 22))
        self.minimize_button.setMaximumSize(QSize(16777215, 16777215))
        self.minimize_button.setAcceptDrops(False)
        self.minimize_button.setLayoutDirection(Qt.LeftToRight)
        self.minimize_button.setStyleSheet(u"QPushButton {\n"
"color: none; \n"
"background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 0px;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/primary_ui_elems/ui_elements/media/minimize_window.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon1)
        self.minimize_button.setIconSize(QSize(23, 23))
        self.minimize_button.setFlat(True)

        self.horizontalLayout.addWidget(self.minimize_button)

        self.exit_button = QPushButton(self.button_frame)
        self.exit_button.setObjectName(u"exit_button")
        sizePolicy1.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy1)
        self.exit_button.setMinimumSize(QSize(30, 26))
        self.exit_button.setMaximumSize(QSize(16777215, 16777215))
        self.exit_button.setLayoutDirection(Qt.LeftToRight)
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"color: none; \n"
"background-color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(86,149,132);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 0px;\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/primary_ui_elems/ui_elements/media/exit_window.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setIconSize(QSize(23, 23))
        self.exit_button.setFlat(True)

        self.horizontalLayout.addWidget(self.exit_button)


        self.horizontalLayout_5.addWidget(self.button_frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.titlebar_frame, 0, Qt.AlignTop)

        self.page_widget = QStackedWidget(self.main_body)
        self.page_widget.setObjectName(u"page_widget")
        self.page_widget.setFont(font)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(self.Home)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.main_body_bulk = QFrame(self.Home)
        self.main_body_bulk.setObjectName(u"main_body_bulk")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body_bulk.sizePolicy().hasHeightForWidth())
        self.main_body_bulk.setSizePolicy(sizePolicy2)
        self.main_body_bulk.setFont(font)
        self.main_body_bulk.setStyleSheet(u"background-color: rgb(13, 12, 23);")
        self.main_body_bulk.setFrameShape(QFrame.StyledPanel)
        self.main_body_bulk.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.main_body_bulk)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.main_body_bulk)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFont(font)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.item_name_frame = QFrame(self.main_frame)
        self.item_name_frame.setObjectName(u"item_name_frame")
        self.item_name_frame.setMinimumSize(QSize(0, 80))
        self.item_name_frame.setMaximumSize(QSize(16777215, 80))
        self.item_name_frame.setFont(font)
        self.item_name_frame.setStyleSheet(u"QFrame {\n"
"border: 0px solid black;\n"
"border-radius: 0px; \n"
"color: white; \n"
"background: rgb(9, 5, 13);\n"
"\n"
"\n"
"\n"
"}")
        self.item_name_frame.setFrameShape(QFrame.NoFrame)
        self.item_name_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.item_name_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.main_frame_title = QFrame(self.item_name_frame)
        self.main_frame_title.setObjectName(u"main_frame_title")
        self.main_frame_title.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_frame_title.sizePolicy().hasHeightForWidth())
        self.main_frame_title.setSizePolicy(sizePolicy3)
        self.main_frame_title.setMinimumSize(QSize(0, 80))
        self.main_frame_title.setMaximumSize(QSize(16777215, 80))
        self.main_frame_title.setSizeIncrement(QSize(0, 0))
        self.main_frame_title.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.main_frame_title.setFont(font2)
        self.main_frame_title.setMouseTracking(False)
        self.main_frame_title.setLayoutDirection(Qt.LeftToRight)
        self.main_frame_title.setStyleSheet(u"border: none")
        self.main_frame_title.setFrameShape(QFrame.NoFrame)
        self.main_frame_title.setFrameShadow(QFrame.Plain)
        self.main_frame_title.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.main_frame_title)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.item_desc_frame = QFrame(self.main_frame_title)
        self.item_desc_frame.setObjectName(u"item_desc_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.item_desc_frame.sizePolicy().hasHeightForWidth())
        self.item_desc_frame.setSizePolicy(sizePolicy4)
        self.item_desc_frame.setFont(font)
        self.item_desc_frame.setStyleSheet(u"border: none")
        self.item_desc_frame.setFrameShape(QFrame.StyledPanel)
        self.item_desc_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.item_desc_frame)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 3, 6, 3)
        self.item_desc = QLabel(self.item_desc_frame)
        self.item_desc.setObjectName(u"item_desc")
        sizePolicy4.setHeightForWidth(self.item_desc.sizePolicy().hasHeightForWidth())
        self.item_desc.setSizePolicy(sizePolicy4)
        self.item_desc.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.item_desc.setFont(font3)
        self.item_desc.setLayoutDirection(Qt.LeftToRight)
        self.item_desc.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.item_desc.setScaledContents(False)
        self.item_desc.setAlignment(Qt.AlignCenter)
        self.item_desc.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.item_desc)


        self.horizontalLayout_7.addWidget(self.item_desc_frame)

        self.item_image = QFrame(self.main_frame_title)
        self.item_image.setObjectName(u"item_image")
        self.item_image.setMinimumSize(QSize(0, 0))
        self.item_image.setMaximumSize(QSize(80, 80))
        self.item_image.setFont(font)
        self.item_image.setStyleSheet(u"border: none;")
        self.item_image.setFrameShape(QFrame.NoFrame)
        self.item_image.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.item_image)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.item_image_label = QLabel(self.item_image)
        self.item_image_label.setObjectName(u"item_image_label")
        sizePolicy.setHeightForWidth(self.item_image_label.sizePolicy().hasHeightForWidth())
        self.item_image_label.setSizePolicy(sizePolicy)
        self.item_image_label.setMinimumSize(QSize(80, 0))
        self.item_image_label.setMaximumSize(QSize(80, 80))
        self.item_image_label.setFont(font)
        self.item_image_label.setLayoutDirection(Qt.LeftToRight)
        self.item_image_label.setAutoFillBackground(False)
        self.item_image_label.setStyleSheet(u"border: 0px solid black")
        self.item_image_label.setText(u"")
        self.item_image_label.setPixmap(QPixmap(u":/etica/placeholder_qpixmap.jpg"))
        self.item_image_label.setScaledContents(False)
        self.item_image_label.setAlignment(Qt.AlignCenter)
        self.item_image_label.setWordWrap(True)
        self.item_image_label.setIndent(0)

        self.verticalLayout_6.addWidget(self.item_image_label)


        self.horizontalLayout_7.addWidget(self.item_image)


        self.horizontalLayout_4.addWidget(self.main_frame_title)


        self.verticalLayout_4.addWidget(self.item_name_frame)

        self.main_frame_deets = QFrame(self.main_frame)
        self.main_frame_deets.setObjectName(u"main_frame_deets")
        self.main_frame_deets.setMaximumSize(QSize(16777215, 127))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        self.main_frame_deets.setFont(font4)
        self.main_frame_deets.setStyleSheet(u"")
        self.main_frame_deets.setFrameShape(QFrame.StyledPanel)
        self.main_frame_deets.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frame_deets)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)
        self.avg_flea_val = QLabel(self.main_frame_deets)
        self.avg_flea_val.setObjectName(u"avg_flea_val")
        self.avg_flea_val.setMinimumSize(QSize(0, 30))
        self.avg_flea_val.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.avg_flea_val.setFont(font5)
        self.avg_flea_val.setLayoutDirection(Qt.LeftToRight)
        self.avg_flea_val.setStyleSheet(u"color: rgb(180, 180, 180);")
        self.avg_flea_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.avg_flea_val, 0, 1, 1, 1)

        self.best_trader_val = QLabel(self.main_frame_deets)
        self.best_trader_val.setObjectName(u"best_trader_val")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        self.best_trader_val.setFont(font6)
        self.best_trader_val.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.best_trader_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.best_trader_val, 2, 1, 1, 1)

        self.label = QLabel(self.main_frame_deets)
        self.label.setObjectName(u"label")
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(False)
        self.label.setFont(font7)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.lowest_flea_val = QLabel(self.main_frame_deets)
        self.lowest_flea_val.setObjectName(u"lowest_flea_val")
        self.lowest_flea_val.setFont(font6)
        self.lowest_flea_val.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.lowest_flea_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lowest_flea_val, 1, 1, 1, 1)

        self.trader_label = QLabel(self.main_frame_deets)
        self.trader_label.setObjectName(u"trader_label")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        self.trader_label.setFont(font8)
        self.trader_label.setStyleSheet(u"color: rgb(180, 180, 180)")

        self.gridLayout.addWidget(self.trader_label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.main_frame_deets)
        self.label_2.setObjectName(u"label_2")
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(False)
        self.label_2.setFont(font9)
        self.label_2.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.lowest_flea_label = QLabel(self.main_frame_deets)
        self.lowest_flea_label.setObjectName(u"lowest_flea_label")
        self.lowest_flea_label.setEnabled(True)
        self.lowest_flea_label.setFont(font8)
        self.lowest_flea_label.setStyleSheet(u"color: rgb(180, 180, 180)")

        self.gridLayout.addWidget(self.lowest_flea_label, 1, 0, 1, 1)

        self.avg_flea_label = QLabel(self.main_frame_deets)
        self.avg_flea_label.setObjectName(u"avg_flea_label")
        self.avg_flea_label.setMinimumSize(QSize(0, 30))
        self.avg_flea_label.setMaximumSize(QSize(16777215, 30))
        self.avg_flea_label.setFont(font8)
        self.avg_flea_label.setStyleSheet(u"color: rgb(180, 180, 180);")

        self.gridLayout.addWidget(self.avg_flea_label, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.main_frame_deets)

        self.line = QFrame(self.main_frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.main_frame_extras = QFrame(self.main_frame)
        self.main_frame_extras.setObjectName(u"main_frame_extras")
        self.main_frame_extras.setMaximumSize(QSize(16777215, 100))
        self.main_frame_extras.setFont(font)
        self.main_frame_extras.setStyleSheet(u"QFrame {\n"
"border: 0px solid black;\n"
"border-radius: 0px; \n"
"color: white; \n"
"\n"
"\n"
"}")
        self.main_frame_extras.setFrameShape(QFrame.StyledPanel)
        self.main_frame_extras.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_frame_extras)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(9, -1, -1, 16)
        self.price_per_slot_val = QLabel(self.main_frame_extras)
        self.price_per_slot_val.setObjectName(u"price_per_slot_val")
        self.price_per_slot_val.setFont(font5)
        self.price_per_slot_val.setLayoutDirection(Qt.LeftToRight)
        self.price_per_slot_val.setStyleSheet(u"color: rgb(180, 180, 180);")
        self.price_per_slot_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.price_per_slot_val, 1, 1, 1, 1)

        self.needed_for_quests_val = QLabel(self.main_frame_extras)
        self.needed_for_quests_val.setObjectName(u"needed_for_quests_val")
        self.needed_for_quests_val.setFont(font8)
        self.needed_for_quests_val.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.needed_for_quests_val.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.needed_for_quests_val, 0, 1, 1, 1)

        self.spacer_label = QLabel(self.main_frame_extras)
        self.spacer_label.setObjectName(u"spacer_label")
        self.spacer_label.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        self.spacer_label.setFont(font10)
        self.spacer_label.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.spacer_label.setScaledContents(False)

        self.gridLayout_2.addWidget(self.spacer_label, 2, 0, 1, 1)

        self.needed_for_quests_label = QLabel(self.main_frame_extras)
        self.needed_for_quests_label.setObjectName(u"needed_for_quests_label")
        self.needed_for_quests_label.setMinimumSize(QSize(175, 0))
        self.needed_for_quests_label.setMaximumSize(QSize(175, 16777215))
        self.needed_for_quests_label.setFont(font8)
        self.needed_for_quests_label.setStyleSheet(u"color: rgb(180, 180, 180)")

        self.gridLayout_2.addWidget(self.needed_for_quests_label, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.main_frame_extras)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 34))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 9)
        self.wiki_button = QPushButton(self.frame_5)
        self.wiki_button.setObjectName(u"wiki_button")
        sizePolicy3.setHeightForWidth(self.wiki_button.sizePolicy().hasHeightForWidth())
        self.wiki_button.setSizePolicy(sizePolicy3)
        self.wiki_button.setMinimumSize(QSize(0, 32))
        self.wiki_button.setMaximumSize(QSize(80, 16777215))
        self.wiki_button.setFont(font7)
        self.wiki_button.setLayoutDirection(Qt.RightToLeft)
        self.wiki_button.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/secondary_ui_elems/ui_elements/media/wiki_external.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.wiki_button.setIcon(icon3)
        self.wiki_button.setIconSize(QSize(20, 20))
        self.wiki_button.setCheckable(False)
        self.wiki_button.setFlat(True)

        self.verticalLayout_8.addWidget(self.wiki_button)


        self.gridLayout_2.addWidget(self.frame_5, 2, 1, 1, 1)

        self.price_per_slot_label = QLabel(self.main_frame_extras)
        self.price_per_slot_label.setObjectName(u"price_per_slot_label")
        self.price_per_slot_label.setMinimumSize(QSize(175, 0))
        self.price_per_slot_label.setMaximumSize(QSize(175, 16777215))
        self.price_per_slot_label.setFont(font8)
        self.price_per_slot_label.setStyleSheet(u"color: rgb(180, 180, 180);")

        self.gridLayout_2.addWidget(self.price_per_slot_label, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.main_frame_extras)

        self.line_2 = QFrame(self.main_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.bottom_frame = QFrame(self.main_frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 0))
        self.bottom_frame.setMaximumSize(QSize(16777215, 16777215))
        self.bottom_frame.setFont(font)
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.status_frame = QFrame(self.bottom_frame)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setMinimumSize(QSize(200, 85))
        self.status_frame.setMaximumSize(QSize(16777215, 85))
        font11 = QFont()
        font11.setPointSize(10)
        self.status_frame.setFont(font11)
        self.status_frame.setFrameShape(QFrame.NoFrame)
        self.status_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.status_frame)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.status_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(u"QFrame {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"background: rgb(7,6,17)\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 3, 0)
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border: none")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(180, 180, 180)")

        self.horizontalLayout_12.addWidget(self.label_3)


        self.horizontalLayout_9.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(25, 25))
        self.frame_9.setStyleSheet(u"border: none")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(18, 18))
        self.label_8.setMaximumSize(QSize(18, 18))
        self.label_8.setStyleSheet(u"border: none")
        self.label_8.setPixmap(QPixmap(u":/tertiary_ui_elems/ui_elements/media/quick_status_on.ico"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.label_8)


        self.horizontalLayout_9.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.status_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet(u"QFrame {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"background: rgb(7,6,17)\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 0, 3, 0)
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFont(font)
        self.frame_11.setStyleSheet(u"border: none")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(180, 180, 180)")

        self.horizontalLayout_14.addWidget(self.label_4)


        self.horizontalLayout_10.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(25, 25))
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet(u"border: none")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(18, 18))
        self.label_9.setMaximumSize(QSize(18, 18))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"border: none")
        self.label_9.setPixmap(QPixmap(u":/tertiary_ui_elems/ui_elements/media/quick_status_on.ico"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.label_9)


        self.horizontalLayout_10.addWidget(self.frame_12)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.status_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFont(font)
        self.frame_8.setStyleSheet(u"QFrame {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"background: rgb(7,6,17)\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 0, 3, 0)
        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFont(font)
        self.frame_13.setStyleSheet(u"border: none")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(180, 180, 180)")

        self.horizontalLayout_13.addWidget(self.label_7)


        self.horizontalLayout_11.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(25, 25))
        self.frame_14.setFont(font)
        self.frame_14.setStyleSheet(u"border: none")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(18, 18))
        self.label_10.setMaximumSize(QSize(18, 18))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"border: none")
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setPixmap(QPixmap(u":/tertiary_ui_elems/ui_elements/media/quick_status_off.ico"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(False)

        self.horizontalLayout_18.addWidget(self.label_10)


        self.horizontalLayout_11.addWidget(self.frame_14)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.horizontalLayout_8.addWidget(self.status_frame)

        self.smm_frame = QFrame(self.bottom_frame)
        self.smm_frame.setObjectName(u"smm_frame")
        self.smm_frame.setMinimumSize(QSize(0, 0))
        self.smm_frame.setMaximumSize(QSize(130, 16777215))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        self.smm_frame.setFont(font12)
        self.smm_frame.setLayoutDirection(Qt.LeftToRight)
        self.smm_frame.setStyleSheet(u"")
        self.smm_frame.setFrameShape(QFrame.NoFrame)
        self.smm_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_22 = QVBoxLayout(self.smm_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.pushButton_6 = QPushButton(self.smm_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy3.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy3)
        self.pushButton_6.setMinimumSize(QSize(47, 47))
        self.pushButton_6.setMaximumSize(QSize(90, 16777215))
        font13 = QFont()
        font13.setPointSize(10)
        font13.setBold(False)
        font13.setItalic(False)
        font13.setUnderline(False)
        self.pushButton_6.setFont(font13)
        self.pushButton_6.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/secondary_ui_elems/ui_elements/media/overlay_toggle.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(30, 30))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(True)

        self.verticalLayout_22.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.smm_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)
        self.pushButton_7.setMinimumSize(QSize(47, 47))
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_7.setFont(font13)
        self.pushButton_7.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/secondary_ui_elems/ui_elements/media/save_and_apply.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QSize(30, 30))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(True)

        self.verticalLayout_22.addWidget(self.pushButton_7)


        self.horizontalLayout_8.addWidget(self.smm_frame)


        self.verticalLayout_4.addWidget(self.bottom_frame)


        self.verticalLayout_9.addWidget(self.main_frame)


        self.verticalLayout_10.addWidget(self.main_body_bulk)

        self.page_widget.addWidget(self.Home)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.Settings.setFont(font)
        self.verticalLayout_17 = QVBoxLayout(self.Settings)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.Settings)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 135))
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 6, -1, 6)
        self.checkBox_4 = QCheckBox(self.frame_4)
        self.checkBox_4.setObjectName(u"checkBox_4")
        font14 = QFont()
        font14.setPointSize(10)
        font14.setKerning(False)
        self.checkBox_4.setFont(font14)
        self.checkBox_4.setStyleSheet(u"QCheckBox{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12 px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_off.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_on.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_hover.ico);\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_4.setChecked(True)

        self.verticalLayout_12.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame_4)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMaximumSize(QSize(16777215, 30))
        palette = QPalette()
        brush = QBrush(QColor(180, 180, 180, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.checkBox_5.setPalette(palette)
        font15 = QFont()
        font15.setPointSize(10)
        font15.setBold(False)
        font15.setKerning(False)
        font15.setStyleStrategy(QFont.PreferAntialias)
        self.checkBox_5.setFont(font15)
        self.checkBox_5.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_5.setAutoFillBackground(False)
        self.checkBox_5.setStyleSheet(u"QCheckBox{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12 px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_off.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_on.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_hover.ico);\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_5.setIconSize(QSize(13, 13))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox_5)

        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(16777215, 30))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.checkBox.setPalette(palette1)
        self.checkBox.setFont(font15)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12 px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_off.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_on.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_hover.ico);\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox.setIconSize(QSize(13, 13))
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(16777215, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.checkBox_2.setPalette(palette2)
        self.checkBox_2.setFont(font15)
        self.checkBox_2.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setStyleSheet(u"QCheckBox{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12 px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_off.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_on.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_hover.ico);\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_2.setIconSize(QSize(13, 13))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame_4)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMaximumSize(QSize(16777215, 30))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.checkBox_3.setPalette(palette3)
        self.checkBox_3.setFont(font15)
        self.checkBox_3.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_3.setAutoFillBackground(False)
        self.checkBox_3.setStyleSheet(u"QCheckBox{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12 px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_off.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_on.ico);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_toggle_hover.ico);\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_3.setIconSize(QSize(13, 13))
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox_3)


        self.verticalLayout_17.addWidget(self.frame_4)

        self.line_3 = QFrame(self.Settings)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_3)

        self.frame_15 = QFrame(self.Settings)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFont(font)
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(16, 6, -1, 6)
        self.radio_primary = QRadioButton(self.frame_15)
        self.radio_primary.setObjectName(u"radio_primary")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.radio_primary.sizePolicy().hasHeightForWidth())
        self.radio_primary.setSizePolicy(sizePolicy5)
        self.radio_primary.setFont(font15)
        self.radio_primary.setStyleSheet(u"QRadioButton{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_off.ico);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_on.ico);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_hover.ico);\n"
"}\n"
"\n"
"\n"
"")
        self.radio_primary.setChecked(False)
        self.radio_primary.setAutoRepeat(False)

        self.verticalLayout_13.addWidget(self.radio_primary)

        self.radio_secondary = QRadioButton(self.frame_15)
        self.radio_secondary.setObjectName(u"radio_secondary")
        sizePolicy5.setHeightForWidth(self.radio_secondary.sizePolicy().hasHeightForWidth())
        self.radio_secondary.setSizePolicy(sizePolicy5)
        self.radio_secondary.setFont(font15)
        self.radio_secondary.setStyleSheet(u"QRadioButton{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_off.ico);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_on.ico);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_hover.ico);\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_13.addWidget(self.radio_secondary)

        self.radio_both = QRadioButton(self.frame_15)
        self.radio_both.setObjectName(u"radio_both")
        sizePolicy5.setHeightForWidth(self.radio_both.sizePolicy().hasHeightForWidth())
        self.radio_both.setSizePolicy(sizePolicy5)
        self.radio_both.setFont(font15)
        self.radio_both.setStyleSheet(u"QRadioButton{\n"
"border: none;\n"
"background: opacity 100%;\n"
"color: rgb(180, 180, 180);\n"
"spacing: 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_off.ico);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_on.ico);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover{\n"
"image: url(:/tertiary_ui_elems/ui_elements/media/settings_radio_hover.ico);\n"
"}\n"
"\n"
"\n"
"")
        self.radio_both.setChecked(True)

        self.verticalLayout_13.addWidget(self.radio_both)


        self.verticalLayout_17.addWidget(self.frame_15)

        self.line_4 = QFrame(self.Settings)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_4)

        self.frame_16 = QFrame(self.Settings)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setMaximumSize(QSize(16777215, 40))
        self.frame_16.setFont(font)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(6, 1, 6, 6)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(150, 25))
        self.frame_18.setFont(font)
        self.frame_18.setLayoutDirection(Qt.LeftToRight)
        self.frame_18.setStyleSheet(u"QFrame {\n"
"	border-bottom: 1px solid rgb(26,26,39);\n"
"	border-radius: 0px; \n"
"	color: rgb(180, 180, 180); \n"
"}")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(100, 16777215))
        font16 = QFont()
        font16.setPointSize(11)
        font16.setKerning(True)
        font16.setStyleStrategy(QFont.PreferAntialias)
        self.label_11.setFont(font16)
        self.label_11.setStyleSheet(u"border: 0px;")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_25.addWidget(self.label_11)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_18)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy3)
        self.doubleSpinBox.setMinimumSize(QSize(0, 0))
        self.doubleSpinBox.setMaximumSize(QSize(40, 20))
        font17 = QFont()
        font17.setPointSize(11)
        font17.setBold(False)
        font17.setItalic(False)
        font17.setUnderline(False)
        font17.setKerning(False)
        font17.setStyleStrategy(QFont.PreferAntialias)
        self.doubleSpinBox.setFont(font17)
        self.doubleSpinBox.setStyleSheet(u"QDoubleSpinBox{\n"
"border-bottom: 0px solid rgb(26,26,39);\n"
"border-radius: 0px; \n"
"color: rgb(180, 180, 180); \n"
"}")
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setAccelerated(True)
        self.doubleSpinBox.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBox.setProperty("showGroupSeparator", False)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMinimum(1.000000000000000)
        self.doubleSpinBox.setMaximum(100.000000000000000)
        self.doubleSpinBox.setSingleStep(1.000000000000000)
        self.doubleSpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox.setValue(100.000000000000000)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox)


        self.horizontalLayout_21.addWidget(self.frame_18)

        self.line_6 = QFrame(self.frame_16)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_21.addWidget(self.line_6)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(150, 25))
        self.frame_19.setFont(font)
        self.frame_19.setStyleSheet(u"QFrame {\n"
"	border-bottom: 1px solid rgb(26,26,39);\n"
"	border-radius: 0px; \n"
"	color: rgb(180, 180, 180); \n"
"}")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_19)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(95, 16777215))
        self.label_13.setFont(font16)
        self.label_13.setStyleSheet(u"border: 0px;")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_13)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_19)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_2.setMinimumSize(QSize(0, 0))
        self.doubleSpinBox_2.setMaximumSize(QSize(40, 20))
        self.doubleSpinBox_2.setFont(font17)
        self.doubleSpinBox_2.setLayoutDirection(Qt.LeftToRight)
        self.doubleSpinBox_2.setStyleSheet(u"QDoubleSpinBox{\n"
"border-bottom: 0px solid rgb(26,26,39);\n"
"border-radius: 0px; \n"
"color: rgb(180, 180, 180); \n"
"}")
        self.doubleSpinBox_2.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setAccelerated(True)
        self.doubleSpinBox_2.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBox_2.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMinimum(1.000000000000000)
        self.doubleSpinBox_2.setMaximum(100.000000000000000)
        self.doubleSpinBox_2.setSingleStep(1.000000000000000)
        self.doubleSpinBox_2.setStepType(QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_2.setValue(100.000000000000000)

        self.horizontalLayout_26.addWidget(self.doubleSpinBox_2)


        self.horizontalLayout_21.addWidget(self.frame_19)


        self.verticalLayout_17.addWidget(self.frame_16)

        self.line_5 = QFrame(self.Settings)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_5)

        self.keybinds_settings_frame = QFrame(self.Settings)
        self.keybinds_settings_frame.setObjectName(u"keybinds_settings_frame")
        self.keybinds_settings_frame.setMinimumSize(QSize(0, 105))
        self.keybinds_settings_frame.setMaximumSize(QSize(16777215, 16777215))
        self.keybinds_settings_frame.setFont(font)
        self.keybinds_settings_frame.setStyleSheet(u"")
        self.keybinds_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.keybinds_settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.keybinds_settings_frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(9, 6, 9, 6)
        self.scan_keybinds_settings_frame = QFrame(self.keybinds_settings_frame)
        self.scan_keybinds_settings_frame.setObjectName(u"scan_keybinds_settings_frame")
        self.scan_keybinds_settings_frame.setFont(font)
        self.scan_keybinds_settings_frame.setStyleSheet(u"border:0px")
        self.scan_keybinds_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.scan_keybinds_settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.scan_keybinds_settings_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.scan_keybinds_settings_frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFont(font)
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_21)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.hotkey_text_edit = QPlainTextEdit(self.frame_21)
        self.hotkey_text_edit.setObjectName(u"hotkey_text_edit")
        sizePolicy3.setHeightForWidth(self.hotkey_text_edit.sizePolicy().hasHeightForWidth())
        self.hotkey_text_edit.setSizePolicy(sizePolicy3)
        self.hotkey_text_edit.setMaximumSize(QSize(16777215, 70))
        font18 = QFont()
        font18.setPointSize(10)
        font18.setBold(False)
        font18.setKerning(True)
        font18.setStyleStrategy(QFont.PreferAntialias)
        self.hotkey_text_edit.setFont(font18)
        self.hotkey_text_edit.viewport().setProperty("cursor", QCursor(Qt.UpArrowCursor))
        self.hotkey_text_edit.setStyleSheet(u"QPlainTextEdit{\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"background-color: rgb(13, 12, 23);\n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgba(230,5,64,.36);\n"
"    border-bottom-radius: 5px; \n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"border: 1px solid black;\n"
"border-radius: 1px; \n"
"background: rgb(97,97,97);\n"
"color: black;\n"
"}\n"
"\n"
"QPlainTextEdit:unfocus{\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"background-color: rgb(13, 12, 23);\n"
"color: rgb(180, 180, 180); \n"
"}")
        self.hotkey_text_edit.setFrameShape(QFrame.NoFrame)
        self.hotkey_text_edit.setFrameShadow(QFrame.Plain)
        self.hotkey_text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hotkey_text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hotkey_text_edit.setUndoRedoEnabled(False)
        self.hotkey_text_edit.setReadOnly(True)
        self.hotkey_text_edit.setOverwriteMode(True)
        self.hotkey_text_edit.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.hotkey_text_edit.setBackgroundVisible(False)

        self.verticalLayout_11.addWidget(self.hotkey_text_edit)

        self.combo_box_frame = QFrame(self.frame_21)
        self.combo_box_frame.setObjectName(u"combo_box_frame")
        self.combo_box_frame.setEnabled(True)
        self.combo_box_frame.setMaximumSize(QSize(250, 40))
        self.combo_box_frame.setFont(font)
        self.combo_box_frame.setStyleSheet(u"QFrame QAbstractItemView {\n"
"color: rgb(180, 180, 180);\n"
"padding: 2px 6px 2px 10px;\n"
"border: 1px solid black;\n"
"outline: 0;\n"
"}\n"
"\n"
"\n"
"QFrame QAbstractItemView::item:hover\n"
"{\n"
"\n"
"    border-bottom: 3px solid rgba(230,5,64,.56);\n"
"    border-bottom-radius: 22px; \n"
"\n"
"}")
        self.combo_box_frame.setFrameShape(QFrame.NoFrame)
        self.combo_box_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.combo_box_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.combo_box_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setMaximumSize(QSize(250, 16777215))
        font19 = QFont()
        font19.setPointSize(10)
        font19.setBold(True)
        font19.setItalic(False)
        font19.setKerning(True)
        font19.setStyleStrategy(QFont.PreferAntialias)
        self.comboBox.setFont(font19)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"background-color: rgb(13, 12, 23);\n"
"color: rgb(180, 180, 180); \n"
"padding: 2px 6px 2px 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    background-color: rgb(6,8,11);\n"
"    width: 30px;\n"
"\n"
"    border-left-width: 2px;\n"
"    border-left-color: rgb(26,26,39);\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border-bottom: 2px solid rgba(230,5,64,.66);\n"
"    border-bottom-radius: 5px; \n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/tertiary_ui_elems/ui_elements/media/hotkey_arrow_normal.ico);\n"
"    width: 28 px;\n"
"    height: 28 px;\n"
"    \n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    image: url(:/tertiary_ui_elems/ui_elements/media/hotkey_arrow_hover.ico);\n"
"    width: 28 px;\n"
"    height: 28 px;\n"
"}\n"
"\n"
""
                        "QComboBox::down-arrow:on {\n"
"    image: url(:/tertiary_ui_elems/ui_elements/media/hotkey_arrow_open.ico);\n"
"    width: 28 px;\n"
"    height: 28 px;\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(4)
        self.comboBox.setMaxCount(4)
        self.comboBox.setFrame(True)

        self.verticalLayout.addWidget(self.comboBox)


        self.verticalLayout_11.addWidget(self.combo_box_frame)


        self.horizontalLayout_2.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.scan_keybinds_settings_frame)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(42, 0))
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setFont(font)
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_22)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.hotkey_help_frame = QFrame(self.frame_22)
        self.hotkey_help_frame.setObjectName(u"hotkey_help_frame")
        self.hotkey_help_frame.setMaximumSize(QSize(16777215, 16777215))
        self.hotkey_help_frame.setFrameShape(QFrame.NoFrame)
        self.hotkey_help_frame.setFrameShadow(QFrame.Plain)
        self.hotkey_help_frame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.hotkey_help_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 73)
        self.hotkey_help_btn = QPushButton(self.hotkey_help_frame)
        self.hotkey_help_btn.setObjectName(u"hotkey_help_btn")
        self.hotkey_help_btn.setMinimumSize(QSize(40, 40))
        self.hotkey_help_btn.setMaximumSize(QSize(40, 40))
        self.hotkey_help_btn.setFont(font)
        self.hotkey_help_btn.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/secondary_ui_elems/ui_elements/media/keybind_help.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.hotkey_help_btn.setIcon(icon6)
        self.hotkey_help_btn.setIconSize(QSize(40, 40))
        self.hotkey_help_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.hotkey_help_btn)


        self.verticalLayout_15.addWidget(self.hotkey_help_frame)


        self.horizontalLayout_2.addWidget(self.frame_22)


        self.horizontalLayout_19.addWidget(self.scan_keybinds_settings_frame)


        self.verticalLayout_17.addWidget(self.keybinds_settings_frame)

        self.frame_20 = QFrame(self.Settings)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 45))
        self.frame_20.setMaximumSize(QSize(16777215, 45))
        font20 = QFont()
        font20.setPointSize(10)
        font20.setKerning(True)
        self.frame_20.setFont(font20)
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(6, 0, 9, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.cancel_button = QPushButton(self.frame_20)
        self.cancel_button.setObjectName(u"cancel_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy6)
        self.cancel_button.setMinimumSize(QSize(85, 35))
        self.cancel_button.setMaximumSize(QSize(85, 16777215))
        font21 = QFont()
        font21.setPointSize(10)
        font21.setBold(False)
        font21.setKerning(True)
        self.cancel_button.setFont(font21)
        self.cancel_button.setLayoutDirection(Qt.LeftToRight)
        self.cancel_button.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/secondary_ui_elems/ui_elements/media/trash_settings.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_button.setIcon(icon7)
        self.cancel_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.cancel_button)

        self.save_button = QPushButton(self.frame_20)
        self.save_button.setObjectName(u"save_button")
        sizePolicy6.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy6)
        self.save_button.setMinimumSize(QSize(80, 35))
        self.save_button.setMaximumSize(QSize(80, 16777215))
        self.save_button.setFont(font21)
        self.save_button.setLayoutDirection(Qt.LeftToRight)
        self.save_button.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/secondary_ui_elems/ui_elements/media/save_settings.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon8)
        self.save_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.save_button)


        self.verticalLayout_17.addWidget(self.frame_20)

        self.page_widget.addWidget(self.Settings)
        self.Settings2 = QWidget()
        self.Settings2.setObjectName(u"Settings2")
        self.verticalLayout_14 = QVBoxLayout(self.Settings2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.page_widget.addWidget(self.Settings2)

        self.verticalLayout_2.addWidget(self.page_widget)

        self.shill_frame = QFrame(self.main_body)
        self.shill_frame.setObjectName(u"shill_frame")
        self.shill_frame.setMinimumSize(QSize(0, 30))
        self.shill_frame.setFont(font)
        self.shill_frame.setStyleSheet(u"QFrame {\n"
"border: 0px solid black;\n"
"border-radius: 0px; \n"
"color: white; \n"
"background: rgb(3, 3, 12);\n"
"\n"
"\n"
"\n"
"}")
        self.shill_frame.setFrameShape(QFrame.StyledPanel)
        self.shill_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.shill_frame)


        self.verticalLayout_3.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.currentIndexChanged.connect(self.hotkey_text_edit.clear)

        self.settings_button.setDefault(False)
        self.minimize_button.setDefault(False)
        self.page_widget.setCurrentIndex(0)
        self.wiki_button.setDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_7.setDefault(False)
        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tilda", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Tilda ~", None))
#if QT_CONFIG(tooltip)
        self.settings_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.settings_button.setText("")
        self.minimize_button.setText("")
        self.exit_button.setText("")
        self.item_desc.setText(QCoreApplication.translate("MainWindow", u"Terragroup Labs Access Key Card", None))
        self.avg_flea_val.setText(QCoreApplication.translate("MainWindow", u"1,000 \u20bd", None))
        self.best_trader_val.setText(QCoreApplication.translate("MainWindow", u"1,000 \u20bd", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"(Therapist)", None))
        self.lowest_flea_val.setText(QCoreApplication.translate("MainWindow", u"1,000 \u20bd", None))
#if QT_CONFIG(tooltip)
        self.trader_label.setToolTip(QCoreApplication.translate("MainWindow", u"Best price to sell to traders, and who buys it for the most.", None))
#endif // QT_CONFIG(tooltip)
        self.trader_label.setText(QCoreApplication.translate("MainWindow", u"Best Trader Sell-To Price:", None))
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.lowest_flea_label.setToolTip(QCoreApplication.translate("MainWindow", u"The most recent lowest price for the item on the flea. Note that this may be slightly off as it only updates this value every time the app is restarted.", None))
#endif // QT_CONFIG(tooltip)
        self.lowest_flea_label.setText(QCoreApplication.translate("MainWindow", u"Latest Lowest Flea Price:", None))
#if QT_CONFIG(tooltip)
        self.avg_flea_label.setToolTip(QCoreApplication.translate("MainWindow", u"Average price of item over the course of the last 24 hours", None))
#endif // QT_CONFIG(tooltip)
        self.avg_flea_label.setText(QCoreApplication.translate("MainWindow", u"24 Hr Flea Avg:", None))
        self.price_per_slot_val.setText(QCoreApplication.translate("MainWindow", u"500 \u20bd", None))
        self.needed_for_quests_val.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.spacer_label.setToolTip(QCoreApplication.translate("MainWindow", u"The number of slots the item fills", None))
#endif // QT_CONFIG(tooltip)
        self.spacer_label.setText(QCoreApplication.translate("MainWindow", u"2 Slots", None))
#if QT_CONFIG(tooltip)
        self.needed_for_quests_label.setToolTip(QCoreApplication.translate("MainWindow", u"Number of quests this item is used for", None))
#endif // QT_CONFIG(tooltip)
        self.needed_for_quests_label.setText(QCoreApplication.translate("MainWindow", u"# of Quests Used For:", None))
#if QT_CONFIG(tooltip)
        self.wiki_button.setToolTip(QCoreApplication.translate("MainWindow", u"Open the item's EFT Wiki page in your default browser", None))
#endif // QT_CONFIG(tooltip)
        self.wiki_button.setText(QCoreApplication.translate("MainWindow", u"Wiki  ", None))
#if QT_CONFIG(shortcut)
        self.wiki_button.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.price_per_slot_label.setToolTip(QCoreApplication.translate("MainWindow", u"The average flea market price per number of slots the item takes up in your inventory", None))
#endif // QT_CONFIG(tooltip)
        self.price_per_slot_label.setText(QCoreApplication.translate("MainWindow", u"Price Per Slot:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Keystroke Listener Status", None))
        self.label_8.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Always Keep Tilda On-Top", None))
        self.label_9.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Auto-Inspect With Scan", None))
        self.label_10.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Enable Single-Monitor Mode, where the app is shrunk and displayed as a small overlay on screen so you can overlay it over your game.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Overlay", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Enable Single-Monitor Mode, where the app is shrunk and displayed as a small overlay on screen so you can overlay it over your game.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Refresh DB", None))
#if QT_CONFIG(tooltip)
        self.checkBox_4.setToolTip(QCoreApplication.translate("MainWindow", u"When enabled a larger popup will appear to explain the UI element, often having images or videos to accompy it.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Enable Event Listener", None))
#if QT_CONFIG(tooltip)
        self.checkBox_5.setToolTip(QCoreApplication.translate("MainWindow", u"Active scans will automatically inspect items in game, scan, and exit out of the inspection screen for you within a split second, making scanning take roughly half of a second", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Allow Text Highlighting", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Prohibit downloading of item data, forcing the app to use previous, locally cached, info to display item data after scanning.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Use Locally Cached Item Data", None))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("MainWindow", u"Forces the OS to keep Tilda's window on-top of all other windows so it remains on-top at all times.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Keep Tilda's Window On Top", None))
#if QT_CONFIG(tooltip)
        self.checkBox_3.setToolTip(QCoreApplication.translate("MainWindow", u"Active scans will automatically inspect items in game, scan, and exit out of the inspection screen for you within a split second, making scanning take roughly half of a second", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Auto Inspect and Scan (Active Scan Only)", None))
#if QT_CONFIG(tooltip)
        self.radio_primary.setToolTip(QCoreApplication.translate("MainWindow", u"Enable Active/Primary scans only, disabling Passive/Secondary scans.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_primary.setText(QCoreApplication.translate("MainWindow", u"Only Enable Active Scan", None))
#if QT_CONFIG(tooltip)
        self.radio_secondary.setToolTip(QCoreApplication.translate("MainWindow", u"Enable Passive/Seconday scans only, disabling Active/Primary scans.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_secondary.setText(QCoreApplication.translate("MainWindow", u"Only Enable Passive Scan", None))
#if QT_CONFIG(tooltip)
        self.radio_both.setToolTip(QCoreApplication.translate("MainWindow", u"Enable both Active and Passive scans that can be used in different situations.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_both.setText(QCoreApplication.translate("MainWindow", u"Enable Both Active and Passive Scans (Dual)", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Main Opacity", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox.setToolTip(QCoreApplication.translate("MainWindow", u"Use your scroll wheel, it's easier \ud83d\udc96", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Text Opacity", None))
#if QT_CONFIG(tooltip)
        self.doubleSpinBox_2.setToolTip(QCoreApplication.translate("MainWindow", u"Use your scroll wheel, it's easier \ud83d\udc96", None))
#endif // QT_CONFIG(tooltip)
        self.hotkey_text_edit.setDocumentTitle("")
        self.hotkey_text_edit.setPlainText(QCoreApplication.translate("MainWindow", u"Select a hotkey from below, then enter your new combination of keys here.", None))
        self.hotkey_text_edit.setPlaceholderText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Toggle Keyboard Event Listener", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Initiate Primary Scan", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Initiate Secondary Scan", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Toggle Tilda Overlay", None))

        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Hotkey to Edit ...", None))
#if QT_CONFIG(tooltip)
        self.hotkey_help_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Confused about setting hotkeys?", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.hotkey_help_btn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.hotkey_help_btn.setText("")
#if QT_CONFIG(tooltip)
        self.cancel_button.setToolTip(QCoreApplication.translate("MainWindow", u"Cancel and discard all currently held preference adjustments.", None))
#endif // QT_CONFIG(tooltip)
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u" Cancel", None))
#if QT_CONFIG(tooltip)
        self.save_button.setToolTip(QCoreApplication.translate("MainWindow", u"Save preference changes to disk. (Needs application reload to fully apply)", None))
#endif // QT_CONFIG(tooltip)
        self.save_button.setText(QCoreApplication.translate("MainWindow", u" Save", None))
    # retranslateUi

