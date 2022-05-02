# -*- coding: utf-8 -*-

import pandas as pd
from PyQt5 import QtWidgets
from v5.design.main_window_ui import Ui_MainWindow

btn_name_one = bool


class Profit(Ui_MainWindow):

    def set_unvisible(self):
        self.widget_2.setVisible(False)

    def set_visible_widget(self):
        self.widget_2.setVisible(True)

    def set_visible(self, btn_name):
        global btn_name_one
        btn_name_one = btn_name
        if btn_name:
            self.label_add_new_payment_spending.setText('Доход')
        else:
            self.label_add_new_payment_spending.setText('Расход')
        self.widget_2.setVisible(True)
        self.lineEdit_add_payment_user.clear()
        self.lineEdit_add_payment_values.clear()
        self.lineEdit_add_payment_spending.clear()
        self.lineEdit_add_payment_description.clear()

        self.lineEdit_add_payment_user.setFocus()

    def profit_add(self, file_balance_name):
        from v5.logic.main_window import MainMenyUser
        user_payment_values = [self.lineEdit_add_payment_user.text(),
                               self.lineEdit_add_payment_spending.text(),
                               str(self.comboBox_add_payment_category.currentText()),
                               self.lineEdit_add_payment_description.text()]

        if btn_name_one:
            user_payment_values.insert(1, str('+ ' + self.lineEdit_add_payment_values.text()))
        else:
            user_payment_values.insert(1, str('- ' + self.lineEdit_add_payment_values.text()))

        data = pd.read_csv(f'../handler/csv_data/main_meny_check/{file_balance_name}', encoding='windows-1251')
        if len(data['id'].values) > 0:
            profit_id = max(data['id'].values) + 1
        else:
            profit_id = 0
        user_payment_values.insert(0, profit_id)
        data = data.append(pd.Series(user_payment_values, index=data.columns[:len(user_payment_values)]), ignore_index=True)
        data.to_csv(f'../handler/csv_data/main_meny_check/{file_balance_name}', index=False)

        data = pd.read_csv(f'../handler/csv_data/pop-up_meny_check/check_list.csv', encoding='windows-1251')
        file_balance_name_changed = file_balance_name.split("_")[1].replace(".csv", "")
        filter = data.query('name == @file_balance_name_changed').index
        q1 = str(data.loc[filter, 'money'].values[0])
        q2 = str(user_payment_values[2])

        try:
            data.loc[filter, 'money'] = eval(f'{q1} {q2}')
            data.to_csv(f'../handler/csv_data/pop-up_meny_check/check_list.csv', index=False)

            MainMenyUser.get_data_from_csv(self, file_balance_name)
            MainMenyUser.get_data_from_csv_for_popup_check(self, '../handler/csv_data/pop-up_meny_check/check_list.csv')

            self.set_unvisible()

        except Exception as _e:
            msg = QtWidgets.QMessageBox()
            self.lineEdit_add_payment_user_2.clear()
            msg.setWindowTitle("Ошибка!")
            msg.setText("Поле 'Расход' должно быть числовым")
            msg.exec_()

            self.lineEdit_add_payment_user.clear()
            self.lineEdit_add_payment_values.clear()
            self.lineEdit_add_payment_spending.clear()
            self.lineEdit_add_payment_description.clear()

            self.lineEdit_add_payment_user.setFocus()
