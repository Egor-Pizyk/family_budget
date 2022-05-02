# -*- coding: utf-8 -*-


import pandas as pd
from PyQt5 import QtWidgets
from v5.design.main_window_ui import Ui_MainWindow


class AddNewCategory(Ui_MainWindow):
    def set_unvisible_category_list(self):
        self.widget_3.setVisible(False)

    def set_unvisible_category_add(self):
        self.widget_4.setVisible(False)

    def set_unvisible_category_drop(self):
        self.widget_5.setVisible(False)


    def set_visible_category_list(self):
        self.widget_3.setVisible(True)

    def set_visible_category_add(self):
        self.widget_4.setVisible(True)

    def set_visible_category_drop(self):
        self.widget_5.setVisible(True)


    def add_new_category_values(self, val):
        if val == 'del':
            file = '../handler/csv_data/category/category_list_del.csv'
        else:
            file = '../handler/csv_data/category/caegory_list.csv'
        with open(file, 'r') as f_object_r:
            text = f_object_r.readlines()
            f_object_r.close()
            if self.lineEdit_add_payment_user_2.text()+'\n' not in text and text != '':
                with open(file, 'a', newline='') as f_object:
                    f_object.write(self.lineEdit_add_payment_user_2.text()+'\n')
                self.comboBox_add_payment_category_3.clear()
                self.comboBox_add_payment_category.clear()
                self.listWidget.clear()

                self.lineEdit_add_payment_user_2.clear()

                return True

            else:
                msg = QtWidgets.QMessageBox()
                self.lineEdit_add_payment_user_2.clear()
                msg.setWindowTitle("Ошибка!")
                msg.setText("Категория должна быть уникальной")
                msg.exec_()

                return False

    def drop_old_category(self, value, val):
        if val == 'del':
            file = '../handler/csv_data/category/category_list_del.csv'
        else:
            file = '../handler/csv_data/category/caegory_list.csv'

        df = pd.read_csv(file, encoding='windows-1251')
        df = df.drop(df[df['name'] == value].index, axis=0)
        df.to_csv(file, index=False)
        self.comboBox_add_payment_category_3.clear()
        self.comboBox_add_payment_category.clear()

        return val

