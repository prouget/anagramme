# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

css = """
.link {
    text-decoration: none;
    color: #000;
}

.link:hover {
    text-decoration: underline;
    font-style: italic;
    color: #fff;
}
"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 102))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 10, 151, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(520, 10, 160, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_3.addWidget(self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 120, 671, 42))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 170, 671, 261))
        #- Test interface CSS---------------------------------------------
        self.cursor = self.textBrowser.textCursor()
        self.doc = self.textBrowser.document()
        self.doc.setDefaultStyleSheet(css)
        #-----------------------------------------------------------------
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.jeu)

    def dictionnaire_ordonne(self):
        # on lit le fichier et on range les mots alphabetiquement selon leur longueur 
        self.fichier = open("dico.uic", "r")
        self.dict_ord = {}
        for longueur in range(25):
            self.dict_ord[longueur+1] = []
        self.mot = self.fichier.readline()
        while self.mot != '':
            self.mot = self.mot.strip('\n')
            if '-' in self.mot:
                self.mot = self.mot.replace('-','')
            self.dict_ord[len(self.mot)].append(self.mot)
            self.mot = self.fichier.readline()
        self.fichier.close()
        print('dico')
        return self.dict_ord

    def lettres_multiples_ok(self, mot, tirage):
        # teste si chaque lettre figure suffisamment de fois dans le tirage
        for lettre in mot:
            if lettre in tirage:
                tirage.remove(lettre)
            else:
                return False
        return True

    def trouver_plus_long_mot(self, dico, tirage):
        self.longueur_mot = int(self.spinBox.text())
        self.solution= []
        self.set_tirage = set(tirage)
        print('set : ' + str(self.set_tirage))
        
        while self.longueur_mot > 0:
            for mot in dico[self.longueur_mot]:
                if set(mot).issubset(self.set_tirage):
                    # les lettres du mot sont un sous-ensemble du tirage
                    tirage_test = list(tirage)
                    if self.lettres_multiples_ok(mot,tirage_test):
                        self.solution.append(mot)
            if self.solution != [] or self.longueur_mot==1:
                return self.solution, self.longueur_mot
            else:
                self.solution = []
            self.longueur_mot -= 1

    def jeu(self):
        print("jeu")
        dico = self.dictionnaire_ordonne()
        self.len_tirage = self.lineEdit.text()
        self.solution, self.longueur = self.trouver_plus_long_mot(dico, self.len_tirage)
        a = str(len(self.solution))
        self.textBrowser.setOpenExternalLinks(True)
        if self.solution == []:
            self.textBrowser.setText("Pas de solution")
            print('Pas de mot trouvé !')
            self.solution = []
        else:
            for mot in self.solution:
                self.cursor.insertHtml('<h2><a class="link" href="https://fr.wiktionary.org/wiki/{}">{} - </a></h2>'.format(mot, mot))
            # self.plainTextEdit.setPlainText(', '.join(self.solution))
            self.label_4.setText(a + " mots")
            print(self.solution)
            self.solution = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pro des Mots - Solutions"))
        self.pushButton.setText(_translate("MainWindow", "Recherche"))
        self.label.setText(_translate("MainWindow", "Nombre de lettres :"))
        self.label_2.setText(_translate("MainWindow", "résultats trouvés :"))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Résultats"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    