# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 870)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame {\n"
"    background-color: #21262D; /* BACKGROUND_SECONDARY */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Login = QWidget()
        self.Login.setObjectName(u"Login")
        self.horizontalLayout_8 = QHBoxLayout(self.Login)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.backgroundLoginMainFrame = QFrame(self.Login)
        self.backgroundLoginMainFrame.setObjectName(u"backgroundLoginMainFrame")
        self.backgroundLoginMainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.backgroundLoginMainFrame.setStyleSheet(u"background-color:#161B22;")
        self.backgroundLoginMainFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.backgroundLoginMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.backgroundLoginMainFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.loginMainFrame = QFrame(self.backgroundLoginMainFrame)
        self.loginMainFrame.setObjectName(u"loginMainFrame")
        self.loginMainFrame.setMinimumSize(QSize(0, 0))
        self.loginMainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.loginMainFrame.setStyleSheet(u"#loginMainFrame{\n"
"border: 2px solid transparent;\n"
"margin-left:60\n"
"}\n"
"\n"
"")
        self.loginMainFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.loginMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.loginMainFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 50, 60, 40)
        self.headerFrame_2 = QFrame(self.loginMainFrame)
        self.headerFrame_2.setObjectName(u"headerFrame_2")
        self.headerFrame_2.setMinimumSize(QSize(0, 100))
        self.headerFrame_2.setMaximumSize(QSize(16777215, 50))
        self.headerFrame_2.setStyleSheet(u"background-color:black;\n"
"    border-top-right-radius: 40px;\n"
"    border-top-left-radius: 40px;\n"
"\n"
"background-color: #21262D;\n"
"")
        self.headerFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.headerFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.headerFrame_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.headerTitleFrame_2 = QFrame(self.headerFrame_2)
        self.headerTitleFrame_2.setObjectName(u"headerTitleFrame_2")
        self.headerTitleFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.headerTitleFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.headerTitleFrame_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.navigationButtonFrame_2 = QFrame(self.headerTitleFrame_2)
        self.navigationButtonFrame_2.setObjectName(u"navigationButtonFrame_2")
        self.navigationButtonFrame_2.setMinimumSize(QSize(100, 0))
        self.navigationButtonFrame_2.setMaximumSize(QSize(100, 16777215))
        self.navigationButtonFrame_2.setStyleSheet(u"")
        self.navigationButtonFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.navigationButtonFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.navigationButtonFrame_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_17.addWidget(self.navigationButtonFrame_2)

        self.tittleLabel_2 = QLabel(self.headerTitleFrame_2)
        self.tittleLabel_2.setObjectName(u"tittleLabel_2")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.tittleLabel_2.setFont(font)
        self.tittleLabel_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.tittleLabel_2)


        self.horizontalLayout_11.addWidget(self.headerTitleFrame_2)

        self.headerRightButtonsFrame_2 = QFrame(self.headerFrame_2)
        self.headerRightButtonsFrame_2.setObjectName(u"headerRightButtonsFrame_2")
        self.headerRightButtonsFrame_2.setMinimumSize(QSize(150, 0))
        self.headerRightButtonsFrame_2.setMaximumSize(QSize(150, 16777215))
        self.headerRightButtonsFrame_2.setStyleSheet(u" border-top-right-radius: 100;\n"
"\n"
"\n"
"")
        self.headerRightButtonsFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.headerRightButtonsFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.headerRightButtonsFrame_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 10, 0)
        self.minimizeButton_2 = QPushButton(self.headerRightButtonsFrame_2)
        self.minimizeButton_2.setObjectName(u"minimizeButton_2")
        self.minimizeButton_2.setMinimumSize(QSize(0, 50))
        self.minimizeButton_2.setMaximumSize(QSize(16777215, 50))
        self.minimizeButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/mainBodyLeftButtons/feather/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton_2.setIcon(icon)
        self.minimizeButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.minimizeButton_2)

        self.maximizeButton_2 = QPushButton(self.headerRightButtonsFrame_2)
        self.maximizeButton_2.setObjectName(u"maximizeButton_2")
        self.maximizeButton_2.setMinimumSize(QSize(0, 50))
        self.maximizeButton_2.setMaximumSize(QSize(16777215, 50))
        self.maximizeButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/mainBodyLeftButtons/feather/feather/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton_2.setIcon(icon1)
        self.maximizeButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.maximizeButton_2)

        self.exitButton_2 = QPushButton(self.headerRightButtonsFrame_2)
        self.exitButton_2.setObjectName(u"exitButton_2")
        self.exitButton_2.setMinimumSize(QSize(0, 50))
        self.exitButton_2.setMaximumSize(QSize(16777215, 50))
        self.exitButton_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/mainBodyLeftButtons/feather/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton_2.setIcon(icon2)
        self.exitButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_18.addWidget(self.exitButton_2)


        self.horizontalLayout_11.addWidget(self.headerRightButtonsFrame_2)


        self.verticalLayout_10.addWidget(self.headerFrame_2)

        self.mainBodyFrame_2 = QFrame(self.loginMainFrame)
        self.mainBodyFrame_2.setObjectName(u"mainBodyFrame_2")
        self.mainBodyFrame_2.setStyleSheet(u"border-radius: 40px; \n"
"background-color: #21262D;\n"
"border-top-left-radius: 0;\n"
"    border-top-right-radius: 0;")
        self.mainBodyFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.mainBodyFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.mainBodyFrame_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.leftHalfFrame = QFrame(self.mainBodyFrame_2)
        self.leftHalfFrame.setObjectName(u"leftHalfFrame")
        self.leftHalfFrame.setStyleSheet(u"")
        self.leftHalfFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftHalfFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftHalfFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(25, 0, 0, 0)
        self.loginTextEditButtonsFrame = QFrame(self.leftHalfFrame)
        self.loginTextEditButtonsFrame.setObjectName(u"loginTextEditButtonsFrame")
        self.loginTextEditButtonsFrame.setMaximumSize(QSize(16777215, 300))
        self.loginTextEditButtonsFrame.setStyleSheet(u"QtextEdit {\n"
"    border: none;\n"
"    border-radius: 20px;\n"
"    background-color: #f1f2f6;\n"
"    padding: 10px 15px;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"QtextEdit:focus {\n"
"    outline: none;\n"
"    background-color: #e5e6eb;\n"
"}\n"
"\n"
"#loginTextEditButtonsFrame{\n"
"margin-bottom:50px\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.loginTextEditButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginTextEditButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.loginTextEditButtonsFrame)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.titleLoginFrame = QLabel(self.loginTextEditButtonsFrame)
        self.titleLoginFrame.setObjectName(u"titleLoginFrame")
        self.titleLoginFrame.setEnabled(True)
        self.titleLoginFrame.setMaximumSize(QSize(16777215, 60))
        self.titleLoginFrame.setFont(font)
        self.titleLoginFrame.setStyleSheet(u"margin-bottom: 20")

        self.verticalLayout_6.addWidget(self.titleLoginFrame)

        self.loginButtonsFrame = QFrame(self.loginTextEditButtonsFrame)
        self.loginButtonsFrame.setObjectName(u"loginButtonsFrame")
        self.loginButtonsFrame.setMinimumSize(QSize(0, 200))
        self.loginButtonsFrame.setStyleSheet(u"")
        self.loginButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.loginButtonsFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.emailFrame = QFrame(self.loginButtonsFrame)
        self.emailFrame.setObjectName(u"emailFrame")
        self.emailFrame.setMinimumSize(QSize(441, 0))
        self.emailFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.emailFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.emailIcon = QFrame(self.emailFrame)
        self.emailIcon.setObjectName(u"emailIcon")
        self.emailIcon.setGeometry(QRect(30, 10, 31, 31))
        self.emailIcon.setStyleSheet(u"background-image: url(:/mainBodyLeftButtons/feather/feather/at-sign.svg);\n"
"  background-repeat: no-repeat ")
        self.emailIcon.setFrameShape(QFrame.Shape.StyledPanel)
        self.emailIcon.setFrameShadow(QFrame.Shadow.Raised)
        self.emailPlainText = QPlainTextEdit(self.emailFrame)
        self.emailPlainText.setObjectName(u"emailPlainText")
        self.emailPlainText.setGeometry(QRect(70, 0, 341, 41))
        self.emailPlainText.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #1a1a1a;\n"
"    color: #00d4aa;\n"
"    border: 2px solid #30363d;\n"
"    border-radius: 20px;\n"
"    padding: 6px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"    selection-background-color: #00d4aa;\n"
"    selection-color: #1a1a1a;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #00f5cc;\n"
"    background-color: #202020;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border-color: #00f5cc;\n"
"}\n"
"\n"
"QPlainTextEdit::selection {\n"
"    background-color: #00d4aa;\n"
"    color: #1a1a1a;\n"
"}\n"
"\n"
"/* Placeholder text styling */\n"
"QPlainTextEdit[placeholderText] {\n"
"    color: #00d4aa;\n"
"}\n"
"\n"
"QPlainTextEdit:focus[placeholderText] {\n"
"    color: #00d4aa;\n"
"}")

        self.verticalLayout_14.addWidget(self.emailFrame)

        self.passwordFrame = QFrame(self.loginButtonsFrame)
        self.passwordFrame.setObjectName(u"passwordFrame")
        self.passwordFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.passwordFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.passwordText = QFrame(self.passwordFrame)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setGeometry(QRect(30, 10, 31, 31))
        self.passwordText.setStyleSheet(u"background-image: url(:/mainBodyLeftButtons/feather/feather/key.svg);\n"
"  background-repeat: no-repeat ")
        self.passwordText.setFrameShape(QFrame.Shape.StyledPanel)
        self.passwordText.setFrameShadow(QFrame.Shadow.Raised)
        self.passwordPlainText = QPlainTextEdit(self.passwordFrame)
        self.passwordPlainText.setObjectName(u"passwordPlainText")
        self.passwordPlainText.setGeometry(QRect(70, 0, 341, 41))
        self.passwordPlainText.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #1a1a1a;\n"
"    color: #00d4aa;\n"
"    border: 2px solid #30363d;\n"
"    border-radius: 20px;\n"
"    padding: 6px;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 14px;\n"
"    selection-background-color: #00d4aa;\n"
"    selection-color: #1a1a1a;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #00f5cc;\n"
"    background-color: #202020;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border-color: #00f5cc;\n"
"}\n"
"\n"
"QPlainTextEdit::selection {\n"
"    background-color: #00d4aa;\n"
"    color: #1a1a1a;\n"
"}\n"
"\n"
"/* Placeholder text styling */\n"
"QPlainTextEdit[placeholderText] {\n"
"    color: #00d4aa;\n"
"}\n"
"\n"
"QPlainTextEdit:focus[placeholderText] {\n"
"    color: #00d4aa;\n"
"}")

        self.verticalLayout_14.addWidget(self.passwordFrame)

        self.loginSatus = QLabel(self.loginButtonsFrame)
        self.loginSatus.setObjectName(u"loginSatus")
        self.loginSatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.loginSatus)

        self.loginFrame = QFrame(self.loginButtonsFrame)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setMaximumSize(QSize(500, 16777215))
        self.loginFrame.setStyleSheet(u"")
        self.loginFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.loginFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.loginFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.loginButton = QPushButton(self.loginFrame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 40))
        self.loginButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 3px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.loginButton)


        self.verticalLayout_14.addWidget(self.loginFrame)


        self.verticalLayout_6.addWidget(self.loginButtonsFrame)


        self.verticalLayout_4.addWidget(self.loginTextEditButtonsFrame)


        self.horizontalLayout_19.addWidget(self.leftHalfFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.ImageFrameHolder = QFrame(self.mainBodyFrame_2)
        self.ImageFrameHolder.setObjectName(u"ImageFrameHolder")
        self.ImageFrameHolder.setMaximumSize(QSize(300, 16777215))
        self.ImageFrameHolder.setFrameShape(QFrame.Shape.NoFrame)
        self.ImageFrameHolder.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.ImageFrameHolder)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.imageFrame = QFrame(self.ImageFrameHolder)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setMaximumSize(QSize(530, 500))
        self.imageFrame.setStyleSheet(u"#imageFrame {\n"
"    border-radius: 0px;\n"
"    border-left: 2px solid gray;\n"
"}\n"
"")
        self.imageFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.imageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.imageFrame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.imageFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/mainBodyLeftButtons/feather/feather/PngItem_3115575.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(250, 200))

        self.horizontalLayout_14.addWidget(self.pushButton)


        self.horizontalLayout_13.addWidget(self.imageFrame)


        self.horizontalLayout_19.addWidget(self.ImageFrameHolder)


        self.verticalLayout_10.addWidget(self.mainBodyFrame_2)


        self.verticalLayout_9.addWidget(self.loginMainFrame)

        self.footer = QFrame(self.backgroundLoginMainFrame)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 40))
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.footer)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.footerFrame_2 = QFrame(self.footer)
        self.footerFrame_2.setObjectName(u"footerFrame_2")
        self.footerFrame_2.setMinimumSize(QSize(0, 20))
        self.footerFrame_2.setMaximumSize(QSize(16777215, 20))
        self.footerFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.footerFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.footerFrame_2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.footerVersionFrame_3 = QFrame(self.footerFrame_2)
        self.footerVersionFrame_3.setObjectName(u"footerVersionFrame_3")
        self.footerVersionFrame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.footerVersionFrame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.footerVersionFrame_3)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.footerVersionFrame_3)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_4)


        self.horizontalLayout_21.addWidget(self.footerVersionFrame_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer_3 = QSpacerItem(733, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.sizeGripFrame_3 = QFrame(self.footerFrame_2)
        self.sizeGripFrame_3.setObjectName(u"sizeGripFrame_3")
        self.sizeGripFrame_3.setMinimumSize(QSize(40, 40))
        self.sizeGripFrame_3.setMaximumSize(QSize(20, 20))
        self.sizeGripFrame_3.setStyleSheet(u"QSizeGrip{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.sizeGripFrame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.sizeGripFrame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_21.addWidget(self.sizeGripFrame_3)


        self.horizontalLayout_23.addWidget(self.footerFrame_2)


        self.verticalLayout_9.addWidget(self.footer)


        self.horizontalLayout_8.addWidget(self.backgroundLoginMainFrame)

        self.stackedWidget.addWidget(self.Login)
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.verticalLayout_3 = QVBoxLayout(self.homepage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.homepage)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 50))
        self.headerFrame.setMaximumSize(QSize(16777215, 50))
        self.headerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.navigationButtonFrame = QFrame(self.headerFrame)
        self.navigationButtonFrame.setObjectName(u"navigationButtonFrame")
        self.navigationButtonFrame.setMinimumSize(QSize(100, 0))
        self.navigationButtonFrame.setMaximumSize(QSize(100, 16777215))
        self.navigationButtonFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.navigationButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.navigationButtonFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.navigationButton = QPushButton(self.navigationButtonFrame)
        self.navigationButton.setObjectName(u"navigationButton")
        self.navigationButton.setMinimumSize(QSize(0, 50))
        self.navigationButton.setMaximumSize(QSize(16777215, 50))
        self.navigationButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/mainBodyLeftButtons/feather/feather/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.navigationButton.setIcon(icon4)
        self.navigationButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.navigationButton)


        self.horizontalLayout_3.addWidget(self.navigationButtonFrame)

        self.headerTitleFrame = QFrame(self.headerFrame)
        self.headerTitleFrame.setObjectName(u"headerTitleFrame")
        self.headerTitleFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.headerTitleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.headerTitleFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tittleLabel = QLabel(self.headerTitleFrame)
        self.tittleLabel.setObjectName(u"tittleLabel")
        self.tittleLabel.setFont(font)
        self.tittleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.tittleLabel)


        self.horizontalLayout_3.addWidget(self.headerTitleFrame)

        self.headerRightButtonsFrame = QFrame(self.headerFrame)
        self.headerRightButtonsFrame.setObjectName(u"headerRightButtonsFrame")
        self.headerRightButtonsFrame.setMinimumSize(QSize(150, 0))
        self.headerRightButtonsFrame.setMaximumSize(QSize(150, 16777215))
        self.headerRightButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.headerRightButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.headerRightButtonsFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.headerRightButtonsFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(0, 50))
        self.minimizeButton.setMaximumSize(QSize(16777215, 50))
        self.minimizeButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}")
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.headerRightButtonsFrame)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(0, 50))
        self.maximizeButton.setMaximumSize(QSize(16777215, 50))
        self.maximizeButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}")
        self.maximizeButton.setIcon(icon1)
        self.maximizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.maximizeButton)

        self.exitButton = QPushButton(self.headerRightButtonsFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(0, 50))
        self.exitButton.setMaximumSize(QSize(16777215, 50))
        self.exitButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}")
        self.exitButton.setIcon(icon2)
        self.exitButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.exitButton)


        self.horizontalLayout_3.addWidget(self.headerRightButtonsFrame)


        self.verticalLayout_3.addWidget(self.headerFrame)

        self.mainBodyFrame = QFrame(self.homepage)
        self.mainBodyFrame.setObjectName(u"mainBodyFrame")
        self.mainBodyFrame.setStyleSheet(u"QPushButton {\n"
"    background-color: #21262d; /* BACKGROUND_TERTIARY */\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    padding-left: 30px;\n"
"    padding-bottom: 10px;\n"
"    padding-top: 10px;\n"
"    color: #f0f6fc; /* TEXT_PRIMARY */\n"
"    font-size: 15px;\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #30363d; /* HOVER_OVERLAY */\n"
"    border-color: #64ffda; /* ACCENT_CYAN */\n"
"    color: #64ffda;\n"
"}\n"
"")
        self.mainBodyFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainBodyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainBodyLeftButtonsFrame = QFrame(self.mainBodyFrame)
        self.mainBodyLeftButtonsFrame.setObjectName(u"mainBodyLeftButtonsFrame")
        self.mainBodyLeftButtonsFrame.setMinimumSize(QSize(100, 0))
        self.mainBodyLeftButtonsFrame.setMaximumSize(QSize(0, 16777215))
        self.mainBodyLeftButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.mainBodyLeftButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyLeftButtonsFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy)
        self.homeButton.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setWeight(QFont.Medium)
        self.homeButton.setFont(font2)
        self.homeButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/feather/home.svg) \n"
"}\n"
"\n"
"\n"
"\"C:\\Users\\ACER\\Desktop\\NetworksGUI\\feather\\home.svg\"")

        self.verticalLayout_2.addWidget(self.homeButton)

        self.logoutButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        self.logoutButton.setMinimumSize(QSize(100, 0))
        self.logoutButton.setFont(font2)
        self.logoutButton.setStyleSheet(u"QPushButton{ \n"
"background-image:url(:/mainBodyLeftButtons/feather/feather/log-out.svg)\n"
"} ")

        self.verticalLayout_2.addWidget(self.logoutButton)

        self.verticalSpacer = QSpacerItem(20, 403, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_7.addWidget(self.mainBodyLeftButtonsFrame)

        self.mainBodyStackedWidget = QStackedWidget(self.mainBodyFrame)
        self.mainBodyStackedWidget.setObjectName(u"mainBodyStackedWidget")
        self.mainBodyStackedWidget.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid #30363d; /* BORDER_DEFAULT */\n"
"    background-color: #161b22; /* BACKGROUND_SECONDARY */\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.homePage)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.homePageFrame = QFrame(self.homePage)
        self.homePageFrame.setObjectName(u"homePageFrame")
        self.homePageFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.homePageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.homePageFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.homePageStackedWidgetFrame = QFrame(self.homePageFrame)
        self.homePageStackedWidgetFrame.setObjectName(u"homePageStackedWidgetFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.homePageStackedWidgetFrame.sizePolicy().hasHeightForWidth())
        self.homePageStackedWidgetFrame.setSizePolicy(sizePolicy1)
        self.homePageStackedWidgetFrame.setStyleSheet(u"QFrame {\n"
"    background-color: #161b22; /* BACKGROUND_SECONDARY */\n"
"}\n"
"")
        self.homePageStackedWidgetFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.homePageStackedWidgetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.homePageStackedWidgetFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.cameraFrame = QFrame(self.homePageStackedWidgetFrame)
        self.cameraFrame.setObjectName(u"cameraFrame")
        self.cameraFrame.setMinimumSize(QSize(0, 600))
        self.cameraFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.cameraFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.cameraFrame)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.cameraLabel = QLabel(self.cameraFrame)
        self.cameraLabel.setObjectName(u"cameraLabel")
        self.cameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.cameraLabel)


        self.verticalLayout_12.addWidget(self.cameraFrame)

        self.statusFrame = QFrame(self.homePageStackedWidgetFrame)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setMinimumSize(QSize(0, 50))
        self.statusFrame.setStyleSheet(u"")
        self.statusFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.statusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.statusFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.statusLabel = QLabel(self.statusFrame)
        self.statusLabel.setObjectName(u"statusLabel")

        self.verticalLayout_13.addWidget(self.statusLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_12.addWidget(self.statusFrame)

        self.homePageButtonsFrame = QFrame(self.homePageStackedWidgetFrame)
        self.homePageButtonsFrame.setObjectName(u"homePageButtonsFrame")
        self.homePageButtonsFrame.setMinimumSize(QSize(0, 150))
        self.homePageButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.homePageButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.homePageButtonsFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.upperHalf = QFrame(self.homePageButtonsFrame)
        self.upperHalf.setObjectName(u"upperHalf")
        self.upperHalf.setFrameShape(QFrame.Shape.NoFrame)
        self.upperHalf.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.upperHalf)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 0)
        self.openDoorButton = QPushButton(self.upperHalf)
        self.openDoorButton.setObjectName(u"openDoorButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.openDoorButton.sizePolicy().hasHeightForWidth())
        self.openDoorButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.openDoorButton)

        self.closeDoorButton = QPushButton(self.upperHalf)
        self.closeDoorButton.setObjectName(u"closeDoorButton")
        sizePolicy2.setHeightForWidth(self.closeDoorButton.sizePolicy().hasHeightForWidth())
        self.closeDoorButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_16.addWidget(self.closeDoorButton)


        self.verticalLayout_11.addWidget(self.upperHalf)

        self.lowerHalf = QFrame(self.homePageButtonsFrame)
        self.lowerHalf.setObjectName(u"lowerHalf")
        self.lowerHalf.setFrameShape(QFrame.Shape.NoFrame)
        self.lowerHalf.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.lowerHalf)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, 5, 5, 0)
        self.startRecordButton = QPushButton(self.lowerHalf)
        self.startRecordButton.setObjectName(u"startRecordButton")
        sizePolicy2.setHeightForWidth(self.startRecordButton.sizePolicy().hasHeightForWidth())
        self.startRecordButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.startRecordButton)

        self.stopRecordButton = QPushButton(self.lowerHalf)
        self.stopRecordButton.setObjectName(u"stopRecordButton")
        sizePolicy2.setHeightForWidth(self.stopRecordButton.sizePolicy().hasHeightForWidth())
        self.stopRecordButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_24.addWidget(self.stopRecordButton)


        self.verticalLayout_11.addWidget(self.lowerHalf)


        self.verticalLayout_12.addWidget(self.homePageButtonsFrame)


        self.horizontalLayout_12.addWidget(self.homePageStackedWidgetFrame)


        self.horizontalLayout_9.addWidget(self.homePageFrame)

        self.mainBodyStackedWidget.addWidget(self.homePage)

        self.horizontalLayout_7.addWidget(self.mainBodyStackedWidget)


        self.verticalLayout_3.addWidget(self.mainBodyFrame)

        self.footerFrame = QFrame(self.homepage)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setMinimumSize(QSize(0, 20))
        self.footerFrame.setMaximumSize(QSize(16777215, 20))
        self.footerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.footerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.footerFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.footerVersionFrame = QFrame(self.footerFrame)
        self.footerVersionFrame.setObjectName(u"footerVersionFrame")
        self.footerVersionFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.footerVersionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footerVersionFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.footerVersionFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.footerVersionFrame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer = QSpacerItem(733, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.sizeGripFrame = QFrame(self.footerFrame)
        self.sizeGripFrame.setObjectName(u"sizeGripFrame")
        self.sizeGripFrame.setMinimumSize(QSize(20, 20))
        self.sizeGripFrame.setMaximumSize(QSize(20, 20))
        self.sizeGripFrame.setStyleSheet(u"QSizeGrip{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.sizeGripFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.sizeGripFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.sizeGripFrame)


        self.verticalLayout_3.addWidget(self.footerFrame)

        self.stackedWidget.addWidget(self.homepage)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.mainBodyStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tittleLabel_2.setText(QCoreApplication.translate("MainWindow", u"Security System", None))
        self.minimizeButton_2.setText("")
        self.maximizeButton_2.setText("")
        self.exitButton_2.setText("")
        self.titleLoginFrame.setText(QCoreApplication.translate("MainWindow", u"Enter Your Secuirty Credentials", None))
        self.loginSatus.setText("")
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
        self.navigationButton.setText("")
        self.tittleLabel.setText(QCoreApplication.translate("MainWindow", u"Security System", None))
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.exitButton.setText("")
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.cameraLabel.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.statusLabel.setText("")
        self.openDoorButton.setText(QCoreApplication.translate("MainWindow", u"Open Door", None))
        self.closeDoorButton.setText(QCoreApplication.translate("MainWindow", u"Close Door", None))
        self.startRecordButton.setText(QCoreApplication.translate("MainWindow", u"Start Record", None))
        self.stopRecordButton.setText(QCoreApplication.translate("MainWindow", u"Stop Record", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

