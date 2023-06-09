# Joe Hollowed
# University of Michigan 2023
# 
# This class provides a graphical user interface for inspecting zonally-averaged variables for user-defined latitude bands in CLDERA HSW++ datasets

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np


# ==================================================================


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        '''
        This function generated by QtDesigner; builds the main elements of the GUI
        '''
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1541, 605)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        
        # set some global attributes
        
        # -------------------------------------------------------
        # -------------------- options panel --------------------

        self.optionsPanel = QtWidgets.QGroupBox(self.centralwidget)
        self.optionsPanel.setGeometry(QtCore.QRect(10, 0, 781, 251))
        self.optionsPanel.setCheckable(False)
        self.optionsPanel.setObjectName("optionsPanel")
        
        self.dataReleaseText = QtWidgets.QLabel(self.optionsPanel)
        self.dataReleaseText.setGeometry(QtCore.QRect(30, 20, 111, 31))
        self.dataReleaseText.setObjectName("dataReleaseText")
        self.dataReleaseComboBox = QtWidgets.QComboBox(self.optionsPanel)
        self.dataReleaseComboBox.setGeometry(QtCore.QRect(130, 20, 311, 31))
        self.dataReleaseComboBox.setObjectName("dataReleaseComboBox")
        self.dataReleaseComboBox.addItem("")
        self.dataReleaseComboBox.addItem("")
        
        self.anomBaseText = QtWidgets.QLabel(self.optionsPanel)
        self.anomBaseText.setGeometry(QtCore.QRect(30, 130, 191, 31))
        self.anomBaseText.setObjectName("anomBaseText") 
        self.anomBaseComboBox = QtWidgets.QComboBox(self.optionsPanel)
        self.anomBaseComboBox.setGeometry(QtCore.QRect(130, 130, 311, 31))
        self.anomBaseComboBox.setObjectName("anomBaseComboBox")
        self.anomBaseComboBox.addItem("")
        self.anomBaseComboBox.addItem("")
        self.anomDefText = QtWidgets.QLabel(self.optionsPanel)
        self.anomDefText.setGeometry(QtCore.QRect(30, 160, 121, 31))
        self.anomDefText.setObjectName("anomDefText")
        self.anomDefSpinBox = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.anomDefSpinBox.setGeometry(QtCore.QRect(160, 160, 68, 31))
        self.anomDefSpinBox.setDecimals(1)
        self.anomDefSpinBox.setMinimum(0.1)
        self.anomDefSpinBox.setMaximum(100.0)
        self.anomDefSpinBox.setSingleStep(0.1)
        self.anomDefSpinBox.setObjectName("anomDefSpinBox")
        self.anomDefComboBox = QtWidgets.QComboBox(self.optionsPanel)
        self.anomDefComboBox.setGeometry(QtCore.QRect(230, 160, 211, 31))
        self.anomDefComboBox.setObjectName("anomDefComboBox")
        self.anomDefComboBox.addItem("")
        self.anomDefComboBox.addItem("")
        
        self.datasetComboBox = QtWidgets.QComboBox(self.optionsPanel)
        self.datasetComboBox.setGeometry(QtCore.QRect(130, 50, 311, 31))
        self.datasetComboBox.setObjectName("datasetComboBox")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetComboBox.addItem("")
        self.datasetText = QtWidgets.QLabel(self.optionsPanel)
        self.datasetText.setGeometry(QtCore.QRect(30, 50, 111, 31))
        self.datasetText.setObjectName("datasetText")
        
        self.magnitudeText = QtWidgets.QLabel(self.optionsPanel)
        self.magnitudeText.setGeometry(QtCore.QRect(30, 80, 131, 31))
        self.magnitudeText.setObjectName("magnitudeText")
        self.magnitudeComboBox = QtWidgets.QComboBox(self.optionsPanel)
        self.magnitudeComboBox.setEnabled(True)
        self.magnitudeComboBox.setGeometry(QtCore.QRect(130, 80, 311, 31))
        self.magnitudeComboBox.setEditable(False)
        self.magnitudeComboBox.setMaxVisibleItems(11)
        self.magnitudeComboBox.setObjectName("magnitudeComboBox")
        self.magnitudeComboBox.addItem("")
        self.magnitudeComboBox.addItem("")
        self.magnitudeComboBox.addItem("")
        self.magnitudeComboBox.addItem("")
        self.magnitudeComboBox.addItem("")
        self.magnitudeComboBox.addItem("")
        self.magnitudeComboBox.addItem("")
        
        self.latBandsText = QtWidgets.QLabel(self.optionsPanel)
        self.latBandsText.setGeometry(QtCore.QRect(480, 20, 171, 31))
        self.latBandsText.setObjectName("latBandsText")
        
        self.bandTropicsText = QtWidgets.QLabel(self.optionsPanel)
        self.bandTropicsText.setGeometry(QtCore.QRect(480, 50, 111, 31))
        self.bandTropicsText.setObjectName("bandTropicsText")
        self.bandTropicsPlusminus = QtWidgets.QLabel(self.optionsPanel)
        self.bandTropicsPlusminus.setGeometry(QtCore.QRect(550, 50, 21, 31))
        self.bandTropicsPlusminus.setObjectName("bandTropicsPlusminus")
        self.tropicsSpinBox = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.tropicsSpinBox.setGeometry(QtCore.QRect(560, 50, 68, 31))
        self.tropicsSpinBox.setDecimals(1)
        self.tropicsSpinBox.setMinimum(0.5)
        self.tropicsSpinBox.setMaximum(90.0)
        self.tropicsSpinBox.setSingleStep(0.5)
        self.tropicsSpinBox.setProperty("value", 23.5)
        self.tropicsSpinBox.setObjectName("tropicsSpinBox")
        
        self.band2Text = QtWidgets.QLabel(self.optionsPanel)
        self.band2Text.setGeometry(QtCore.QRect(480, 80, 111, 31))
        self.band2Text.setObjectName("band2Text")
        self.band2SpinBoxL = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.band2SpinBoxL.setGeometry(QtCore.QRect(560, 80, 68, 31))
        self.band2SpinBoxL.setDecimals(1)
        self.band2SpinBoxL.setMinimum(0.0)
        self.band2SpinBoxL.setMaximum(90.0)
        self.band2SpinBoxL.setSingleStep(0.5)
        self.band2SpinBoxL.setProperty("value", 23.5)
        self.band2SpinBoxL.setObjectName("band2SpinBoxL")
        self.band2TextTo = QtWidgets.QLabel(self.optionsPanel)
        self.band2TextTo.setGeometry(QtCore.QRect(640, 80, 21, 31))
        self.band2TextTo.setObjectName("band2TextTo")
        self.band2SpinBoxR = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.band2SpinBoxR.setGeometry(QtCore.QRect(670, 80, 68, 31))
        self.band2SpinBoxR.setDecimals(1)
        self.band2SpinBoxR.setMinimum(0.0)
        self.band2SpinBoxR.setMaximum(90.0)
        self.band2SpinBoxR.setSingleStep(0.5)
        self.band2SpinBoxR.setProperty("value", 35.0)
        self.band2SpinBoxR.setObjectName("band2SpinBoxR")
        
        self.band3Text = QtWidgets.QLabel(self.optionsPanel)
        self.band3Text.setGeometry(QtCore.QRect(480, 110, 111, 31))
        self.band3Text.setObjectName("band3Text")
        self.band3SpinBoxL = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.band3SpinBoxL.setGeometry(QtCore.QRect(560, 110, 68, 31))
        self.band3SpinBoxL.setDecimals(1)
        self.band3SpinBoxL.setMinimum(0.0)
        self.band3SpinBoxL.setMaximum(90.0)
        self.band3SpinBoxL.setSingleStep(0.5)
        self.band3SpinBoxL.setProperty("value", 35.0)
        self.band3SpinBoxL.setObjectName("band3SpinBoxL")
        self.band3TextTo = QtWidgets.QLabel(self.optionsPanel)
        self.band3TextTo.setGeometry(QtCore.QRect(640, 110, 21, 31))
        self.band3TextTo.setObjectName("band3TextTo")
        self.band3SpinBoxR = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.band3SpinBoxR.setGeometry(QtCore.QRect(670, 110, 68, 31))
        self.band3SpinBoxR.setDecimals(1)
        self.band3SpinBoxR.setMinimum(0.0)
        self.band3SpinBoxR.setMaximum(90.0)
        self.band3SpinBoxR.setSingleStep(0.5)
        self.band3SpinBoxR.setProperty("value", 66.5)
        self.band3SpinBoxR.setObjectName("band3SpinBoxR") 
        
        self.band4Text = QtWidgets.QLabel(self.optionsPanel)
        self.band4Text.setGeometry(QtCore.QRect(480, 140, 111, 31))
        self.band4Text.setObjectName("band4Text")
        self.band4SpinBoxL = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.band4SpinBoxL.setGeometry(QtCore.QRect(560, 140, 68, 31))
        self.band4SpinBoxL.setDecimals(1)
        self.band4SpinBoxL.setMinimum(0.0)
        self.band4SpinBoxL.setMaximum(90.0)
        self.band4SpinBoxL.setSingleStep(0.5)
        self.band4SpinBoxL.setProperty("value", 66.5)
        self.band4SpinBoxL.setObjectName("band4SpinBoxL")
        self.band4TextTo = QtWidgets.QLabel(self.optionsPanel)
        self.band4TextTo.setGeometry(QtCore.QRect(640, 140, 21, 31))
        self.band4TextTo.setObjectName("band4TextTo")
        self.band4SpinBoxR = QtWidgets.QDoubleSpinBox(self.optionsPanel)
        self.band4SpinBoxR.setGeometry(QtCore.QRect(670, 140, 68, 31))
        self.band4SpinBoxR.setDecimals(1)
        self.band4SpinBoxR.setMinimum(0.0)
        self.band4SpinBoxR.setMaximum(90.0)
        self.band4SpinBoxR.setSingleStep(0.5)
        self.band4SpinBoxR.setProperty("value", 90.0)
        self.band4SpinBoxR.setObjectName("band4SpinBoxR")
        
        self.resetBandsButton = QtWidgets.QPushButton(self.optionsPanel)
        self.resetBandsButton.setEnabled(True)
        self.resetBandsButton.setGeometry(QtCore.QRect(560, 170, 161, 32))
        self.resetBandsButton.setObjectName("resetBandsButton")

        self.refreshTableButton = QtWidgets.QPushButton(self.optionsPanel)
        self.refreshTableButton.setEnabled(True)
        self.refreshTableButton.setGeometry(QtCore.QRect(550, 210, 221, 32))
        self.refreshTableButton.setStyleSheet("background-color: lightgreen; color: black;")
        self.refreshTableButton.setObjectName("refreshTableButton")

        self.progressBar = QtWidgets.QProgressBar(self.optionsPanel)
        self.progressBar.setGeometry(QtCore.QRect(30, 220, 511, 20))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        
        # -------------------------------------------------------
        # -------------------- results panel --------------------
        
        self.resultsPanel = QtWidgets.QGroupBox(self.centralwidget)
        self.resultsPanel.setGeometry(QtCore.QRect(10, 250, 781, 311))
        self.resultsPanel.setObjectName("resultsPanel")
        self.resultsTable = QtWidgets.QTableWidget(self.resultsPanel)
        self.resultsTable.setEnabled(True)
        self.resultsTable.setGeometry(QtCore.QRect(40, 30, 691, 231))
        self.resultsTable.setAutoFillBackground(False)
        self.resultsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.resultsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.resultsTable.setAutoScroll(True)
        self.resultsTable.setDragDropOverwriteMode(False)
        self.resultsTable.setAlternatingRowColors(True)
        self.resultsTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.resultsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.resultsTable.setShowGrid(True)
        self.resultsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.resultsTable.setCornerButtonEnabled(False)
        self.resultsTable.setRowCount(7)
        self.resultsTable.setColumnCount(6)
        self.resultsTable.setObjectName("resultsTable")
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.resultsTable.setHorizontalHeaderItem(5, item)
        
        self.exportCellsButton = QtWidgets.QPushButton(self.resultsPanel)
        self.exportCellsButton.setEnabled(True)
        self.exportCellsButton.setGeometry(QtCore.QRect(40, 270, 221, 32))
        self.exportCellsButton.setObjectName("exportCellsButton")
        self.exportAllCellsButton = QtWidgets.QPushButton(self.resultsPanel)
        self.exportAllCellsButton.setEnabled(True)
        self.exportAllCellsButton.setGeometry(QtCore.QRect(260, 270, 221, 32))
        self.exportAllCellsButton.setObjectName("exportAllCellsButton")

        self.helpButton = QtWidgets.QPushButton(self.resultsPanel)
        self.helpButton.setEnabled(True)
        self.helpButton.setGeometry(QtCore.QRect(630, 270, 141, 32))
        self.helpButton.setStyleSheet("background-color: lightblue; color: black;")
        self.helpButton.setDefault(False)
        self.helpButton.setFlat(False)
        self.helpButton.setObjectName("helpButton")
        
        # -----------------------------------------------------
        # -------------------- plots panel --------------------
        
        self.plotPanel = QtWidgets.QGroupBox(self.centralwidget)
        self.plotPanel.setGeometry(QtCore.QRect(800, 0, 721, 561))
        self.plotPanel.setFlat(False)
        self.plotPanel.setObjectName("plotPanel")
        self.plotViewport = QtWidgets.QGraphicsView(self.plotPanel)
        self.plotViewport.setGeometry(QtCore.QRect(10, 30, 701, 511))
        self.plotViewport.setObjectName("plotViewport")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1541, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # modify UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # set UI triggers
        self.setTriggers()


    # ==================================================================


    def retranslateUi(self, MainWindow):
        '''
        This function generated by QtDesigner; modifies elements of the GUI
        '''
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        # -------------------------------------------------------
        # -------------------- options panel --------------------
        
        self.optionsPanel.setTitle(_translate("MainWindow", "Options"))
        
        self.dataReleaseText.setText(_translate("MainWindow", "Data Release:"))
        self.dataReleaseComboBox.setItemText(0, _translate("MainWindow", 
                                                "March release (low variability, 10 members)"))
        self.dataReleaseComboBox.setItemText(1, _translate("MainWindow", 
                                                "January release (high variability, 5 members)"))
        self.dataReleaseComboBox.setCurrentIndex(0)
        
        self.anomBaseText.setText(_translate("MainWindow", "Anomaly Base:"))
        self.anomBaseComboBox.setItemText(0, _translate("MainWindow", "Counterfactual"))
        self.anomBaseComboBox.setItemText(1, _translate("MainWindow", "Mean Climate"))
        self.anomBaseComboBox.setCurrentIndex(0)
        self.anomDefText.setText(_translate("MainWindow", "Anomaly Definition:"))
        self.anomDefComboBox.setItemText(0, _translate("MainWindow", "standard dev. from base"))
        self.anomDefComboBox.setItemText(1, _translate("MainWindow", "Kelvin from base"))
        self.anomDefComboBox.setCurrentIndex(0)
        
        self.datasetText.setText(_translate("MainWindow", "Dataset:"))
        self.datasetComboBox.setItemText(0, _translate("MainWindow", "ens_mean"))
        self.datasetComboBox.setItemText(1, _translate("MainWindow", "ens01"))
        self.datasetComboBox.setItemText(2, _translate("MainWindow", "ens02"))
        self.datasetComboBox.setItemText(3, _translate("MainWindow", "ens03"))
        self.datasetComboBox.setItemText(4, _translate("MainWindow", "ens04"))
        self.datasetComboBox.setItemText(5, _translate("MainWindow", "ens05"))
        self.datasetComboBox.setItemText(6, _translate("MainWindow", "ens06"))
        self.datasetComboBox.setItemText(7, _translate("MainWindow", "ens07"))
        self.datasetComboBox.setItemText(8, _translate("MainWindow", "ens08"))
        self.datasetComboBox.setItemText(9, _translate("MainWindow", "ens09"))
        self.datasetComboBox.setItemText(10, _translate("MainWindow", "ens10"))
        self.datasetComboBox.setCurrentIndex(0)
        
        self.magnitudeText.setText(_translate("MainWindow", "SO2 Magnitude:"))
        self.magnitudeComboBox.setItemText(0, _translate("MainWindow", "0.25X"))
        self.magnitudeComboBox.setItemText(1, _translate("MainWindow", "0.50X"))
        self.magnitudeComboBox.setItemText(2, _translate("MainWindow", "0.90X"))
        self.magnitudeComboBox.setItemText(3, _translate("MainWindow", "1.00X"))
        self.magnitudeComboBox.setItemText(4, _translate("MainWindow", "1.10X"))
        self.magnitudeComboBox.setItemText(5, _translate("MainWindow", "1.50X"))
        self.magnitudeComboBox.setItemText(6, _translate("MainWindow", "2.00X"))
        self.magnitudeComboBox.setCurrentIndex(3)
        
        self.latBandsText.setText(_translate("MainWindow", "Latitude Bands (degrees):"))
        
        self.bandTropicsText.setText(_translate("MainWindow", "Tropics:"))
        self.bandTropicsPlusminus.setText(_translate("MainWindow", "±"))
        
        self.band2Text.setText(_translate("MainWindow", "Band 2:"))
        self.band2TextTo.setText(_translate("MainWindow", "to"))
        
        self.band3Text.setText(_translate("MainWindow", "Band 3:"))
        self.band3TextTo.setText(_translate("MainWindow", "to"))
        
        self.band4Text.setText(_translate("MainWindow", "Band 4:"))
        self.band4TextTo.setText(_translate("MainWindow", "to"))
        
        self.resetBandsButton.setText(_translate("MainWindow", "reset bands"))

        self.refreshTableButton.setText(_translate("MainWindow", "refresh results table"))
        
        # -------------------------------------------------------
        # -------------------- results panel --------------------
                
        self.resultsPanel.setTitle(_translate("MainWindow", "Results"))
        item = self.resultsTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Band 4 NH"))
        item = self.resultsTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Band 3 NH"))
        item = self.resultsTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Band 2 NH"))
        item = self.resultsTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Band 1 Tropics"))
        item = self.resultsTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Band 2 SH"))
        item = self.resultsTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Band 3 SH"))
        item = self.resultsTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Band 4 SH"))
        item = self.resultsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "SO2"))
        item = self.resultsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SULFATE"))
        item = self.resultsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "AOD"))
        item = self.resultsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "T025"))
        item = self.resultsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "T050"))
        item = self.resultsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "T1000"))
        
        self.exportCellsButton.setText(_translate("MainWindow", "export data for selected cell"))
        self.exportAllCellsButton.setText(_translate("MainWindow", "export data for all cells"))
        
        self.helpButton.setText(_translate("MainWindow", "HELP"))
        
        # -----------------------------------------------------
        # -------------------- plots panel --------------------
        
        self.plotPanel.setTitle(_translate("MainWindow", "Plots"))
    
    
    # ==================================================================
    
    
    def setTriggers(self):
        '''
        Sets up certain option choices to trigger other changes to the GUI
        '''
        
        # ---- allow data release selection to restrict other options
        self.dataReleaseComboBox.activated.connect(self.update_data_release_options)

        # ---- init latitude band reset button
        defaultBands = [23.5, 23.5, 35.0, 35.0, 66.5, 66.5, 90.0]
        bandBoxes = [self.tropicsSpinBox, self.band2SpinBoxL, self.band2SpinBoxR, 
                     self.band3SpinBoxL, self.band3SpinBoxR, self.band4SpinBoxL, self.band4SpinBoxR]
        self.resetBandsButton.clicked.connect(lambda:  
            [bandBoxes[i].setValue(defaultBands[i]) for i in range(len(bandBoxes))])


    
    
    # ==================================================================

    
    def update_data_release_options(self, index):
        '''
        Updates options to only allow seletions available for the currently selected Data Release. This
        is needed since the January and March 2023 HSW++ data releases offer different numbers of ensemble
        members, and different SO2 mass magnitudes

        Parameters
        ----------
        index : int
            the index of the currently selected item in datReleaseComboBox
        '''
        ensMembersAvailable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        massMagsAvailable = [0.25, 0.50, 0.90, 1.00, 1.10, 1.50, 2.00]
        
        if index == 1: # January release (high variability, 5 members)
            enabledEnsMembers = [1, 2, 3, 4, 5]
            enabledMassMags = [1.00]
        elif index == 0: # March release (low variability, 10 members)
            enabledEnsMembers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            enabledMassMags = [0.25, 0.50, 0.90, 1.00, 1.10, 1.50, 2.00]

        for i in range(len(ensMembersAvailable)):
            if((i+1) in enabledEnsMembers):
                self.datasetComboBox.model().item(i+1).setEnabled(True)
            else:
                self.datasetComboBox.model().item(i+1).setEnabled(False)
        
        for i in range(len(massMagsAvailable)):
            if(massMagsAvailable[i] in enabledMassMags):
                self.magnitudeComboBox.model().item(i).setEnabled(True)
            else:
                self.magnitudeComboBox.model().item(i).setEnabled(False)
        
        return




# ======================================================================================
# ======================================================================================


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
