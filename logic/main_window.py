import os
import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

from v5.design import main_window_ui
from v5.logic.add_new_balance import AddNewBalance
from v5.logic.decoration.table_format import TableFormat
from v5.logic.profit import Profit

file_balance_name = str

class MainMenyUser(QtWidgets.QMainWindow, main_window_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowState(Qt.WindowMaximized)

        self.format = TableFormat
        self.format.format(self)
        self.add_new_balance = AddNewBalance

        self.get_data_from_csv('')

        self.pushButton_add_new_balance.clicked.connect(self.add_new_balance_data)

        self.get_data_from_csv_for_popup_check('../handler/csv_data/pop-up_meny_check/check_list.csv')

        self.commandLinkButton_my_check_edit.clicked.connect(self.set_visible_data)
        self.commandLinkButton_my_check_edit_3.clicked.connect(self.set_un_visible_data)
        self.checkBox_is_have_balance.clicked.connect(self.is_feeld_enable)

        self.comboBox_user_balance.currentTextChanged.connect(self.on_combobox_changed)

        self.add_new_balance.check_data(self)

        self.profit = Profit
        self.profit.set_unvisible(self)

        self.pushButton_add_money.clicked.connect(lambda: self.add_money_to_balance(True))
        self.pushButton_del_money.clicked.connect(self.add_money_to_balance)

        self.pushButton_add_new_payment_cancel.clicked.connect(self.set_unvisible)
        self.pushButton_add_new_payment_ok.clicked.connect(lambda: self.profit_add(file_balance_name))

        self.actionOptions1.triggered.connect(self.test)


    # get data for comboBox (up-left) for balances data
    def on_combobox_changed(self, value):
        global file_balance_name

        hold = list()
        value_list = value.split()
        value = '_'.join(value_list)
        if len(str(value)) > 0:
            directory = '../handler/csv_data/main_meny_check'
            files = os.listdir(directory)
            for i in files:
                var = i.replace('.csv', '').split('_')
                hold.append(var[1])
            val = hold.index(value)
            file_balance_name = files[val]
            self.get_data_from_csv(files[val])

    # get data from file to table
    def get_data_from_csv(self, value_for_link):
        if len(str(value_for_link)) > 0:
            filter_var = value_for_link.replace('.csv', '').split('_')
            data = pd.read_csv('../handler/csv_data/pop-up_meny_check/check_list.csv', encoding='windows-1251')
            filter = data.query('name == @filter_var[1]')

            self.label_user_balance.setText(str(data['money'].iloc[filter.index].values[0]) + ' грн.')

            file_t = f'../handler/csv_data/main_meny_check/{value_for_link}'
            file = pd.read_csv(file_t, encoding='windows-1251')
            file = file.drop(['id'], axis=1)
            matrix = file.shape
            header_table = file.columns.to_list()

            self.set_table(matrix, header_table, file)

    # set data in table
    def set_table(self, matrix, header_table, file):
        self.tableWidget_payment_table.setRowCount(matrix[0])

        for i in range(len(file.index)):
            for j in range(len(header_table)):
                self.tableWidget_payment_table.setItem(i, j, QTableWidgetItem(str(file.loc[i][j])))

    def get_data_from_csv_for_popup_check(self, file_t):
        file = pd.read_csv(file_t, encoding='windows-1251')
        matrix = file.shape
        header_table = file.columns.to_list()

        self.set_table_for_popup_check(matrix, header_table, file)

    def set_table_for_popup_check(self, matrix, header_table, file):
        self.tableWidget_all_balances_check.setRowCount(matrix[0])
        for i in range(len(file.index)):
            for j in range(len(header_table)):
                self.tableWidget_all_balances_check.setItem(i, j, QTableWidgetItem(str(file.loc[i][j])))

    def set_visible_data(self):
        self.add_new_balance.set_visible_data(self)

    def set_un_visible_data(self):
        self.add_new_balance.set_un_visible_data(self)
        self.checkBox_is_have_balance.setChecked(False)
        self.is_feeld_enable()

    def is_feeld_enable(self):
        self.add_new_balance.is_feeld_enable(self)

    def add_new_balance_data(self):
        self.add_new_balance.add_new_balance_data(self)
        self.get_data_from_csv_for_popup_check('../handler/csv_data/pop-up_meny_check/check_list.csv')

    def set_unvisible(self):
        self.profit.set_unvisible(self)

    def profit_add(self, file_balance_name):
        self.profit.profit_add(self, file_balance_name)

    def add_money_to_balance(self, btn_name=False):
        # print(btn_name)
        self.profit.set_visible(self, btn_name)



def main():
    app = QApplication(sys.argv)
    window = MainMenyUser()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()