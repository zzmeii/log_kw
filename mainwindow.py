# coding: utf-8
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

from log_kmedoid import k_medoid


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 167)
        MainWindow.setMinimumSize(QtCore.QSize(635, 167))
        MainWindow.setMaximumSize(QtCore.QSize(635, 167))
        self.file_path = None
        self.colors = ['red', 'green', 'blue', 'black', 'orange', 'yellow']
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_start = QtWidgets.QPushButton(self.centralwidget)
        self.b_start.setGeometry(QtCore.QRect(541, 70, 75, 23))
        self.b_start.setObjectName("b_start")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 0, 141, 61))
        self.groupBox.setObjectName("groupBox")
        self.metryx_m = QtWidgets.QRadioButton(self.groupBox)
        self.metryx_m.setGeometry(QtCore.QRect(10, 40, 101, 17))
        self.metryx_m.setObjectName("metryx_m")
        self.metryx_e = QtWidgets.QRadioButton(self.groupBox)
        self.metryx_e.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.metryx_e.setChecked(True)
        self.metryx_e.setObjectName("metryx_e")
        self.b_choose = QtWidgets.QPushButton(self.centralwidget)
        self.b_choose.setGeometry(QtCore.QRect(10, 80, 81, 23))
        self.b_choose.setObjectName("b_choose")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 141, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 121, 17))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.n_class = QtWidgets.QSpinBox(self.centralwidget)
        self.n_class.setGeometry(QtCore.QRect(280, 10, 42, 22))
        self.n_class.setMinimum(2)
        self.n_class.setObjectName("n_class")
        self.t_way = QtWidgets.QLabel(self.centralwidget)
        self.t_way.setGeometry(QtCore.QRect(20, 110, 221, 16))
        self.t_way.setMaximumSize(QtCore.QSize(221, 16))
        self.t_way.setObjectName("t_way")
        self.DT_1 = QtWidgets.QLabel(self.centralwidget)
        self.DT_1.setGeometry(QtCore.QRect(150, 10, 121, 20))
        self.DT_1.setObjectName("DT_1")
        self.b_show_T = QtWidgets.QPushButton(self.centralwidget)
        self.b_show_T.setGeometry(QtCore.QRect(100, 80, 61, 23))
        self.b_show_T.setObjectName("b_show_T")
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(540, 100, 81, 16))
        self.Status.setObjectName("Status")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(337, 0, 151, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(10, 40, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.cb_norm = QtWidgets.QCheckBox(self.groupBox_3)
        self.cb_norm.setGeometry(QtCore.QRect(10, 60, 101, 17))
        self.cb_norm.setObjectName("cb_norm")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setGeometry(QtCore.QRect(80, 80, 62, 22))
        self.doubleSpinBox.setMinimum(0.1)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setProperty("value", 0.1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.DT_2 = QtWidgets.QLabel(self.groupBox_3)
        self.DT_2.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.DT_2.setObjectName("DT_2")
        self.DT_3 = QtWidgets.QLabel(self.centralwidget)
        self.DT_3.setGeometry(QtCore.QRect(150, 40, 121, 20))
        self.DT_3.setObjectName("DT_3")
        self.k_classes = QtWidgets.QSpinBox(self.centralwidget)
        self.k_classes.setGeometry(QtCore.QRect(280, 40, 42, 22))
        self.k_classes.setMinimum(50)
        self.k_classes.setMaximum(1000)
        self.k_classes.setObjectName("k_classes")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.b_choose.setEnabled(False)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.b_start.clicked.connect(self.start_knm)
        self.b_choose.clicked.connect(self.coose_youre_file)
        self.radioButton.toggled.connect(self.change_rb_data)
        self.b_show_T.clicked.connect(self.save_csv)
    
    def change_rb_data(self):
        if not self.radioButton.isChecked():
            self.b_choose.setEnabled(False)
            self.file_path = None
            self.t_way.setText('Файла нет')
        else:
            self.b_choose.setEnabled(True)
            
    def save_csv(self):
        
        res = {i:[] for i in range(len(self.data)+1)}
        for i in self.data:
            for k in range(len(res)-1):
                res[k] = i[k]
            res[len(self.data)] = i.k_class
        pd.DataFrame(res).to_csv(str(datetime.now()))

    def start_knm(self):
        
        n_cof = self.doubleSpinBox.value() if self.cb_norm.isChecked() else None
        self.data = k_medoid(self.n_class.value(), int(self.k_classes.value()), self.metryx_m.isChecked(),
                             self.file_path, n_cof)

        if self.checkBox.isChecked() or self.checkBox_2.isChecked():
            ax = plt.subplots()[1]
            for i in self.data:
                if i.medoid:
                    ax.scatter(i[0], i[1], color=self.colors[int(i.k_class)], marker='^', lw=10)
                else:
                    ax.scatter(i[0], i[1], color=self.colors[int(i.k_class)])
            if self.checkBox.isChecked():
                plt.savefig('kmm_plot')
            if self.checkBox_2.isChecked():
                plt.show()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("log_kw_knm")
        self.b_start.setText("Начать")
        self.groupBox.setTitle("Метрика")
        self.metryx_m.setText("Манхеттенское")
        self.metryx_e.setText("Евклидово")
        self.b_choose.setText("Выбор файла")
        self.groupBox_2.setTitle("Данные")
        self.radioButton.setText("Пользовательские")
        self.radioButton_2.setText("Случайные")
        self.t_way.setText("Файла нет")
        self.DT_1.setText("Кол-во класстеров:")
        self.b_show_T.setText("Сохранить")
        self.Status.setText("Не активно")
        self.groupBox_3.setTitle("Дополнительно")
        self.checkBox.setText("Сохранить график")
        self.cb_norm.setText("Нормализация")
        self.checkBox_2.setText("Плказать график")
        self.DT_2.setText("Ко-оф:")
        self.DT_3.setText("Кол-во итераций")
    
    def coose_youre_file(self):
        file_path = QFileDialog.getOpenFileName()
        self.file_path = file_path[0]


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec_())
