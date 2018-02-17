# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 241)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.oxideInput = QtWidgets.QGroupBox(self.centralWidget)
        self.oxideInput.setGeometry(QtCore.QRect(10, 10, 231, 171))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(9)
        self.oxideInput.setFont(font)
        self.oxideInput.setAutoFillBackground(False)
        self.oxideInput.setAlignment(QtCore.Qt.AlignCenter)
        self.oxideInput.setFlat(False)
        self.oxideInput.setObjectName("oxideInput")
        self.oxideSilica = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideSilica.setGeometry(QtCore.QRect(70, 20, 51, 27))
        self.oxideSilica.setMaxLength(6)
        self.oxideSilica.setFrame(True)
        self.oxideSilica.setPlaceholderText("")
        self.oxideSilica.setObjectName("oxideSilica")
        self.oxideAluminum = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideAluminum.setGeometry(QtCore.QRect(70, 50, 51, 27))
        self.oxideAluminum.setMaxLength(6)
        self.oxideAluminum.setObjectName("oxideAluminum")
        self.oxideFerric = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideFerric.setGeometry(QtCore.QRect(70, 80, 51, 27))
        self.oxideFerric.setMaxLength(6)
        self.oxideFerric.setObjectName("oxideFerric")
        self.oxideFerrous = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideFerrous.setGeometry(QtCore.QRect(70, 110, 51, 27))
        self.oxideFerrous.setMaxLength(6)
        self.oxideFerrous.setObjectName("oxideFerrous")
        self.oxideMagnesia = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideMagnesia.setGeometry(QtCore.QRect(180, 20, 51, 27))
        self.oxideMagnesia.setMaxLength(6)
        self.oxideMagnesia.setObjectName("oxideMagnesia")
        self.oxideCalcium = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideCalcium.setGeometry(QtCore.QRect(180, 50, 51, 27))
        self.oxideCalcium.setMaxLength(6)
        self.oxideCalcium.setObjectName("oxideCalcium")
        self.oxideSodium = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideSodium.setGeometry(QtCore.QRect(180, 80, 51, 27))
        self.oxideSodium.setMaxLength(6)
        self.oxideSodium.setObjectName("oxideSodium")
        self.oxidePotassium = QtWidgets.QLineEdit(self.oxideInput)
        self.oxidePotassium.setGeometry(QtCore.QRect(180, 110, 51, 27))
        self.oxidePotassium.setMaxLength(6)
        self.oxidePotassium.setObjectName("oxidePotassium")
        self.label_silica_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_silica_oxide.setGeometry(QtCore.QRect(20, 30, 54, 17))
        self.label_silica_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_silica_oxide.setObjectName("label_silica_oxide")
        self.label_aluminum_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_aluminum_oxide.setGeometry(QtCore.QRect(20, 60, 54, 17))
        self.label_aluminum_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_aluminum_oxide.setObjectName("label_aluminum_oxide")
        self.lable_iron3_oxide = QtWidgets.QLabel(self.oxideInput)
        self.lable_iron3_oxide.setGeometry(QtCore.QRect(20, 90, 54, 17))
        self.lable_iron3_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lable_iron3_oxide.setObjectName("lable_iron3_oxide")
        self.label_iron2_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_iron2_oxide.setGeometry(QtCore.QRect(20, 120, 54, 17))
        self.label_iron2_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_iron2_oxide.setObjectName("label_iron2_oxide")
        self.label_magnesium_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_magnesium_oxide.setGeometry(QtCore.QRect(140, 30, 54, 17))
        self.label_magnesium_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_magnesium_oxide.setObjectName("label_magnesium_oxide")
        self.label_calcium_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_calcium_oxide.setGeometry(QtCore.QRect(140, 60, 54, 17))
        self.label_calcium_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_calcium_oxide.setObjectName("label_calcium_oxide")
        self.label_sodium_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_sodium_oxide.setGeometry(QtCore.QRect(140, 90, 54, 17))
        self.label_sodium_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_sodium_oxide.setObjectName("label_sodium_oxide")
        self.label_potassium_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_potassium_oxide.setGeometry(QtCore.QRect(140, 120, 54, 17))
        self.label_potassium_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_potassium_oxide.setObjectName("label_potassium_oxide")
        self.label_manganese_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_manganese_oxide.setGeometry(QtCore.QRect(20, 150, 54, 17))
        self.label_manganese_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_manganese_oxide.setObjectName("label_manganese_oxide")
        self.oxideManganese = QtWidgets.QLineEdit(self.oxideInput)
        self.oxideManganese.setGeometry(QtCore.QRect(70, 140, 51, 27))
        self.oxideManganese.setMaxLength(6)
        self.oxideManganese.setObjectName("oxideManganese")
        self.label_phosphorus_oxide = QtWidgets.QLabel(self.oxideInput)
        self.label_phosphorus_oxide.setGeometry(QtCore.QRect(140, 150, 54, 17))
        self.label_phosphorus_oxide.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_phosphorus_oxide.setObjectName("label_phosphorus_oxide")
        self.oxidePhosphorus = QtWidgets.QLineEdit(self.oxideInput)
        self.oxidePhosphorus.setGeometry(QtCore.QRect(180, 140, 51, 27))
        self.oxidePhosphorus.setMaxLength(6)
        self.oxidePhosphorus.setObjectName("oxidePhosphorus")
        self.accuracy = QtWidgets.QGroupBox(self.centralWidget)
        self.accuracy.setGeometry(QtCore.QRect(260, 10, 61, 101))
        self.accuracy.setObjectName("accuracy")
        self.percent10 = QtWidgets.QRadioButton(self.accuracy)
        self.percent10.setGeometry(QtCore.QRect(0, 20, 101, 22))
        self.percent10.setChecked(True)
        self.percent10.setObjectName("percent10")
        self.percent1 = QtWidgets.QRadioButton(self.accuracy)
        self.percent1.setGeometry(QtCore.QRect(0, 40, 101, 22))
        self.percent1.setObjectName("percent1")
        self.percentTenth = QtWidgets.QRadioButton(self.accuracy)
        self.percentTenth.setGeometry(QtCore.QRect(0, 60, 101, 22))
        self.percentTenth.setObjectName("percentTenth")
        self.percentHundreth = QtWidgets.QRadioButton(self.accuracy)
        self.percentHundreth.setGeometry(QtCore.QRect(0, 80, 101, 22))
        self.percentHundreth.setObjectName("percentHundreth")
        self.control = QtWidgets.QGroupBox(self.centralWidget)
        self.control.setGeometry(QtCore.QRect(260, 110, 211, 71))
        self.control.setTitle("")
        self.control.setObjectName("control")
        self.calculate = QtWidgets.QPushButton(self.control)
        self.calculate.setGeometry(QtCore.QRect(10, 40, 85, 27))
        self.calculate.setCheckable(True)
        self.calculate.setObjectName("calculate")
        self.export_2 = QtWidgets.QPushButton(self.control)
        self.export_2.setGeometry(QtCore.QRect(120, 40, 85, 27))
        self.export_2.setCheckable(True)
        self.export_2.setChecked(True)
        self.export_2.setObjectName("export_2")
        self.settings = QtWidgets.QGroupBox(self.centralWidget)
        self.settings.setGeometry(QtCore.QRect(350, 10, 121, 81))
        self.settings.setObjectName("settings")
        self.checkBox = QtWidgets.QCheckBox(self.settings)
        self.checkBox.setGeometry(QtCore.QRect(0, 20, 111, 22))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.settings)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 40, 101, 22))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.settings)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 60, 121, 22))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 484, 27))
        self.menuBar.setObjectName("menuBar")
        self.menuIgneous_Sedimentation = QtWidgets.QMenu(self.menuBar)
        self.menuIgneous_Sedimentation.setObjectName("menuIgneous_Sedimentation")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.menuIgneous_Sedimentation.addAction(self.actionNew)
        self.menuIgneous_Sedimentation.addAction(self.actionExport)
        self.menuHelp.addAction(self.actionLicense)
        self.menuBar.addAction(self.menuIgneous_Sedimentation.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Igneous Sedimentation"))
        self.oxideInput.setTitle(_translate("MainWindow", "Oxides (grams)"))
        self.oxideSilica.setText(_translate("MainWindow", "0.00"))
        self.oxideAluminum.setText(_translate("MainWindow", "0.00"))
        self.oxideFerric.setText(_translate("MainWindow", "0.00"))
        self.oxideFerrous.setText(_translate("MainWindow", "0.00"))
        self.oxideMagnesia.setText(_translate("MainWindow", "0.00"))
        self.oxideCalcium.setText(_translate("MainWindow", "0.00"))
        self.oxideSodium.setText(_translate("MainWindow", "0.00"))
        self.oxidePotassium.setText(_translate("MainWindow", "0.00"))
        self.label_silica_oxide.setText(_translate("MainWindow", "<html><head/><body><p>SiO<span style=\" vertical-align:sub;\">2</span></p></body></html>"))
        self.label_aluminum_oxide.setText(_translate("MainWindow", "<html><head/><body><p>Al<span style=\" vertical-align:sub;\">2</span>O<span style=\" vertical-align:sub;\">3</span></p></body></html>"))
        self.lable_iron3_oxide.setText(_translate("MainWindow", "<html><head/><body><p>Fe<span style=\" vertical-align:sub;\">2</span>O<span style=\" vertical-align:sub;\">3</span></p></body></html>"))
        self.label_iron2_oxide.setText(_translate("MainWindow", "<html><head/><body><p>FeO</p></body></html>"))
        self.label_magnesium_oxide.setText(_translate("MainWindow", "<html><head/><body><p>MgO</p><p><br/></p></body></html>"))
        self.label_calcium_oxide.setText(_translate("MainWindow", "<html><head/><body><p>CaO</p></body></html>"))
        self.label_sodium_oxide.setText(_translate("MainWindow", "<html><head/><body><p>Na<span style=\" vertical-align:sub;\">2</span>O</p></body></html>"))
        self.label_potassium_oxide.setText(_translate("MainWindow", "<html><head/><body><p>K<span style=\" vertical-align:sub;\">2</span>O</p></body></html>"))
        self.label_manganese_oxide.setText(_translate("MainWindow", "MnO"))
        self.oxideManganese.setText(_translate("MainWindow", "0.00"))
        self.label_phosphorus_oxide.setText(_translate("MainWindow", "<html><head/><body><p>P<span style=\" vertical-align:sub;\">2</span>O<span style=\" vertical-align:sub;\">5</span></p></body></html>"))
        self.oxidePhosphorus.setText(_translate("MainWindow", "0.00"))
        self.accuracy.setTitle(_translate("MainWindow", "Accuracy"))
        self.percent10.setText(_translate("MainWindow", "10%"))
        self.percent1.setText(_translate("MainWindow", "1%"))
        self.percentTenth.setText(_translate("MainWindow", "0.1%"))
        self.percentHundreth.setText(_translate("MainWindow", "0.01%"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.export_2.setText(_translate("MainWindow", "Export"))
        self.settings.setTitle(_translate("MainWindow", "Settings"))
        self.checkBox.setText(_translate("MainWindow", "Ignore TiO"))
        self.checkBox_2.setText(_translate("MainWindow", "Ignore PO"))
        self.checkBox_3.setText(_translate("MainWindow", "Mix MnO + MgO"))
        self.menuIgneous_Sedimentation.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionLicense.setText(_translate("MainWindow", "License"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

