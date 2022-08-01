# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overlay_window_designerLhyKBr.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_smm_window(object):
    def setupUi(self, smm_window):
        if not smm_window.objectName():
            smm_window.setObjectName(u"smm_window")
        smm_window.resize(316, 107)
        smm_window.setMinimumSize(QSize(0, 107))
        smm_window.setMaximumSize(QSize(316, 107))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        smm_window.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../../../Desktop/Poisk-0.8.3/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        smm_window.setWindowIcon(icon)
        smm_window.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(smm_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame {\n"
"background-color: rgb(13, 12, 23);\n"
"\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.smm_main_frame = QFrame(self.frame)
        self.smm_main_frame.setObjectName(u"smm_main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.smm_main_frame.sizePolicy().hasHeightForWidth())
        self.smm_main_frame.setSizePolicy(sizePolicy)
        self.smm_main_frame.setMinimumSize(QSize(0, 105))
        self.smm_main_frame.setMaximumSize(QSize(16777215, 105))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.smm_main_frame.setFont(font1)
        self.smm_main_frame.setStyleSheet(u"QFrame {\n"
"background-color: rgb(13, 12, 23);\n"
"\n"
"\n"
"}")
        self.smm_main_frame.setFrameShape(QFrame.StyledPanel)
        self.smm_main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.smm_main_frame)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 3, 6, 3)
        self.smm_flea_val = QLabel(self.smm_main_frame)
        self.smm_flea_val.setObjectName(u"smm_flea_val")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.smm_flea_val.setFont(font2)
        self.smm_flea_val.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_flea_val.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.smm_flea_val, 1, 1, 1, 1)

        self.smm_trader_val = QLabel(self.smm_main_frame)
        self.smm_trader_val.setObjectName(u"smm_trader_val")
        self.smm_trader_val.setFont(font2)
        self.smm_trader_val.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_trader_val.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.smm_trader_val, 2, 1, 1, 1)

        self.smm_slot_val = QLabel(self.smm_main_frame)
        self.smm_slot_val.setObjectName(u"smm_slot_val")
        self.smm_slot_val.setFont(font2)
        self.smm_slot_val.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_slot_val.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.smm_slot_val, 3, 1, 1, 1)

        self.smm_flea_label = QLabel(self.smm_main_frame)
        self.smm_flea_label.setObjectName(u"smm_flea_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.smm_flea_label.sizePolicy().hasHeightForWidth())
        self.smm_flea_label.setSizePolicy(sizePolicy1)
        self.smm_flea_label.setMaximumSize(QSize(103, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.smm_flea_label.setFont(font3)
        self.smm_flea_label.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_flea_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.smm_flea_label, 1, 0, 1, 1)

        self.smm_name_val = QLabel(self.smm_main_frame)
        self.smm_name_val.setObjectName(u"smm_name_val")
        self.smm_name_val.setFont(font2)
        self.smm_name_val.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_name_val.setScaledContents(False)
        self.smm_name_val.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.smm_name_val, 0, 1, 1, 1)

        self.smm_slot_label = QLabel(self.smm_main_frame)
        self.smm_slot_label.setObjectName(u"smm_slot_label")
        sizePolicy1.setHeightForWidth(self.smm_slot_label.sizePolicy().hasHeightForWidth())
        self.smm_slot_label.setSizePolicy(sizePolicy1)
        self.smm_slot_label.setMaximumSize(QSize(103, 16777215))
        self.smm_slot_label.setFont(font3)
        self.smm_slot_label.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_slot_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.smm_slot_label, 3, 0, 1, 1)

        self.smm_name_label = QLabel(self.smm_main_frame)
        self.smm_name_label.setObjectName(u"smm_name_label")
        sizePolicy1.setHeightForWidth(self.smm_name_label.sizePolicy().hasHeightForWidth())
        self.smm_name_label.setSizePolicy(sizePolicy1)
        self.smm_name_label.setMaximumSize(QSize(103, 16777215))
        self.smm_name_label.setFont(font3)
        self.smm_name_label.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_name_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.smm_name_label, 0, 0, 1, 1)

        self.smm_trader_label = QLabel(self.smm_main_frame)
        self.smm_trader_label.setObjectName(u"smm_trader_label")
        sizePolicy1.setHeightForWidth(self.smm_trader_label.sizePolicy().hasHeightForWidth())
        self.smm_trader_label.setSizePolicy(sizePolicy1)
        self.smm_trader_label.setMaximumSize(QSize(103, 16777215))
        self.smm_trader_label.setFont(font3)
        self.smm_trader_label.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_trader_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.smm_trader_label, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.smm_main_frame)

        self.smm_right_frame = QFrame(self.frame)
        self.smm_right_frame.setObjectName(u"smm_right_frame")
        self.smm_right_frame.setMinimumSize(QSize(36, 105))
        self.smm_right_frame.setMaximumSize(QSize(36, 105))
        self.smm_right_frame.setStyleSheet(u"QFrame {\n"
"background: rgb(9, 5, 13);\n"
"border: none;\n"
"\n"
"\n"
"}")
        self.smm_right_frame.setFrameShape(QFrame.StyledPanel)
        self.smm_right_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.smm_right_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.smm_controls_frame = QFrame(self.smm_right_frame)
        self.smm_controls_frame.setObjectName(u"smm_controls_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.smm_controls_frame.sizePolicy().hasHeightForWidth())
        self.smm_controls_frame.setSizePolicy(sizePolicy2)
        self.smm_controls_frame.setMinimumSize(QSize(0, 0))
        self.smm_controls_frame.setMaximumSize(QSize(60, 55))
        self.smm_controls_frame.setLayoutDirection(Qt.LeftToRight)
        self.smm_controls_frame.setStyleSheet(u"")
        self.smm_controls_frame.setFrameShape(QFrame.StyledPanel)
        self.smm_controls_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.smm_controls_frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.smm_overlay_toggle_button = QPushButton(self.smm_controls_frame)
        self.smm_overlay_toggle_button.setObjectName(u"smm_overlay_toggle_button")
        self.smm_overlay_toggle_button.setMinimumSize(QSize(32, 26))
        self.smm_overlay_toggle_button.setMaximumSize(QSize(32, 26))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.smm_overlay_toggle_button.setFont(font4)
        self.smm_overlay_toggle_button.setLayoutDirection(Qt.RightToLeft)
        self.smm_overlay_toggle_button.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/secondary_ui_elems/ui_elements/media/overlay_return.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.smm_overlay_toggle_button.setIcon(icon1)
        self.smm_overlay_toggle_button.setIconSize(QSize(18, 19))
        self.smm_overlay_toggle_button.setFlat(True)

        self.verticalLayout.addWidget(self.smm_overlay_toggle_button)

        self.smm_move_button = QPushButton(self.smm_controls_frame)
        self.smm_move_button.setObjectName(u"smm_move_button")
        self.smm_move_button.setMinimumSize(QSize(30, 26))
        self.smm_move_button.setMaximumSize(QSize(40, 27))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.smm_move_button.setFont(font5)
        self.smm_move_button.setMouseTracking(False)
        self.smm_move_button.setLayoutDirection(Qt.LeftToRight)
        self.smm_move_button.setAutoFillBackground(False)
        self.smm_move_button.setStyleSheet(u"QPushButton {\n"
"border: 2px solid rgb(26,26,39);\n"
"border-radius: 5px; \n"
"color: rgb(180, 180, 180); \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: rgb(180, 180, 180); \n"
"    background-color: rgb(26,26,39);\n"
"    border-width: 0px;\n"
"    border-color: black;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/secondary_ui_elems/ui_elements/media/overlay_move.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.smm_move_button.setIcon(icon2)
        self.smm_move_button.setIconSize(QSize(999999999, 22))
        self.smm_move_button.setCheckable(True)
        self.smm_move_button.setChecked(False)
        self.smm_move_button.setFlat(True)

        self.verticalLayout.addWidget(self.smm_move_button)


        self.verticalLayout_2.addWidget(self.smm_controls_frame)

        self.smm_extra_info_frame = QFrame(self.smm_right_frame)
        self.smm_extra_info_frame.setObjectName(u"smm_extra_info_frame")
        self.smm_extra_info_frame.setMinimumSize(QSize(0, 0))
        self.smm_extra_info_frame.setMaximumSize(QSize(16777215, 47))
        self.smm_extra_info_frame.setFrameShape(QFrame.NoFrame)
        self.smm_extra_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.smm_extra_info_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 0, 3, 0)
        self.smm_trader_name = QLabel(self.smm_extra_info_frame)
        self.smm_trader_name.setObjectName(u"smm_trader_name")
        self.smm_trader_name.setMinimumSize(QSize(0, 0))
        self.smm_trader_name.setMaximumSize(QSize(60, 16777215))
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(False)
        self.smm_trader_name.setFont(font6)
        self.smm_trader_name.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_trader_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.smm_trader_name)

        self.smm_slot_size = QLabel(self.smm_extra_info_frame)
        self.smm_slot_size.setObjectName(u"smm_slot_size")
        self.smm_slot_size.setMinimumSize(QSize(0, 0))
        self.smm_slot_size.setMaximumSize(QSize(60, 16777215))
        self.smm_slot_size.setFont(font6)
        self.smm_slot_size.setStyleSheet(u"color: rgb(180, 180, 180)")
        self.smm_slot_size.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.smm_slot_size)


        self.verticalLayout_2.addWidget(self.smm_extra_info_frame)


        self.horizontalLayout_2.addWidget(self.smm_right_frame)


        self.horizontalLayout.addWidget(self.frame)

        smm_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(smm_window)

        self.smm_overlay_toggle_button.setDefault(False)


        QMetaObject.connectSlotsByName(smm_window)
    # setupUi

    def retranslateUi(self, smm_window):
        smm_window.setWindowTitle(QCoreApplication.translate("smm_window", u"Tilda - Single Monitor Mode", None))
        self.smm_flea_val.setText(QCoreApplication.translate("smm_window", u"-1 \u20bd", None))
        self.smm_trader_val.setText(QCoreApplication.translate("smm_window", u"3.5M \u20bd", None))
        self.smm_slot_val.setText(QCoreApplication.translate("smm_window", u"3.5M \u20bd", None))
#if QT_CONFIG(tooltip)
        self.smm_flea_label.setToolTip(QCoreApplication.translate("smm_window", u"Average price of item over the course of the last 24 hours", None))
#endif // QT_CONFIG(tooltip)
        self.smm_flea_label.setText(QCoreApplication.translate("smm_window", u"24 Hr Flea:", None))
        self.smm_name_val.setText(QCoreApplication.translate("smm_window", u"Prapor's Socks", None))
#if QT_CONFIG(tooltip)
        self.smm_slot_label.setToolTip(QCoreApplication.translate("smm_window", u"The average flea market price per number of slots the item takes up in your inventory", None))
#endif // QT_CONFIG(tooltip)
        self.smm_slot_label.setText(QCoreApplication.translate("smm_window", u"Price / Slot:", None))
#if QT_CONFIG(tooltip)
        self.smm_name_label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.smm_name_label.setText(QCoreApplication.translate("smm_window", u"Item Name:", None))
#if QT_CONFIG(tooltip)
        self.smm_trader_label.setToolTip(QCoreApplication.translate("smm_window", u"Best price to sell to traders, and who buys it for the most.", None))
#endif // QT_CONFIG(tooltip)
        self.smm_trader_label.setText(QCoreApplication.translate("smm_window", u"Trader:", None))
#if QT_CONFIG(tooltip)
        self.smm_overlay_toggle_button.setToolTip(QCoreApplication.translate("smm_window", u"Exit Single Monitor Mode, head back to the main scanner app", None))
#endif // QT_CONFIG(tooltip)
        self.smm_overlay_toggle_button.setText("")
#if QT_CONFIG(tooltip)
        self.smm_move_button.setToolTip(QCoreApplication.translate("smm_window", u"Move the overlay window somewhere else on the screen", None))
#endif // QT_CONFIG(tooltip)
        self.smm_move_button.setText("")
#if QT_CONFIG(tooltip)
        self.smm_trader_name.setToolTip(QCoreApplication.translate("smm_window", u"Initial(s) of the trader that offers the best SELL price for this item", None))
#endif // QT_CONFIG(tooltip)
        self.smm_trader_name.setText(QCoreApplication.translate("smm_window", u"(P)", None))
#if QT_CONFIG(tooltip)
        self.smm_slot_size.setToolTip(QCoreApplication.translate("smm_window", u"Number of slots/spaces the item fills in game", None))
#endif // QT_CONFIG(tooltip)
        self.smm_slot_size.setText(QCoreApplication.translate("smm_window", u"1", None))
    # retranslateUi

