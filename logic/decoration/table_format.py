from PyQt5 import QtWidgets

from v5.design.main_window_ui import Ui_MainWindow


class TableFormat(Ui_MainWindow):
    def format(self):
        self.tableWidget_payment_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_payment_table.verticalHeader().setHighlightSections(True)

        header = self.tableWidget_payment_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

        header_left = self.tableWidget_all_balances_check.horizontalHeader()
        header_left.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)


        self.label_add_balance_name.setVisible(False)
        self.lineEdit_add_balance_name.setVisible(False)
        self.label_add_balance_balance.setVisible(False)
        self.lineEdit_add_balance_balance.setVisible(False)
        self.checkBox_is_have_balance.setVisible(False)
        self.pushButton_add_new_balance.setVisible(False)

        self.commandLinkButton_my_check_edit_3.setEnabled(False)
        self.commandLinkButton_my_check_edit_3.setVisible(False)