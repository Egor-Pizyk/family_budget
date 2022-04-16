import os
from _csv import writer

from PyQt5 import QtWidgets

from v5.design.main_window_ui import Ui_MainWindow


class AddNewBalance(Ui_MainWindow):
    def set_visible_data(self):
        self.label_add_balance_name.setVisible(True)
        self.lineEdit_add_balance_name.setVisible(True)
        self.label_add_balance_balance.setVisible(True)
        self.lineEdit_add_balance_balance.setVisible(True)
        self.checkBox_is_have_balance.setVisible(True)
        self.pushButton_add_new_balance.setVisible(True)

        self.commandLinkButton_my_check_edit.setVisible(False)
        self.commandLinkButton_my_check_edit.setEnabled(False)
        self.commandLinkButton_my_check_edit_3.setEnabled(True)
        self.commandLinkButton_my_check_edit_3.setVisible(True)

        self.lineEdit_add_balance_name.setFocus()

    def set_un_visible_data(self):
        self.label_add_balance_name.setVisible(False)
        self.lineEdit_add_balance_name.setVisible(False)
        self.label_add_balance_balance.setVisible(False)
        self.lineEdit_add_balance_balance.setVisible(False)
        self.checkBox_is_have_balance.setVisible(False)
        self.pushButton_add_new_balance.setVisible(False)

        self.commandLinkButton_my_check_edit.setVisible(True)
        self.commandLinkButton_my_check_edit.setEnabled(True)
        self.commandLinkButton_my_check_edit_3.setEnabled(False)
        self.commandLinkButton_my_check_edit_3.setVisible(False)

        self.lineEdit_add_balance_name.clear()

    def is_feeld_enable(self):
        if self.checkBox_is_have_balance.isChecked():
            self.label_add_balance_balance.setEnabled(True)
            self.lineEdit_add_balance_balance.setEnabled(True)
        else:
            self.label_add_balance_balance.setEnabled(False)
            self.lineEdit_add_balance_balance.setEnabled(False)
            self.lineEdit_add_balance_balance.clear()

    def add_new_balance_data(self):
        msg = QtWidgets.QMessageBox()
        if self.checkBox_is_have_balance.isChecked():
            name = self.lineEdit_add_balance_name.text()
            balance = self.lineEdit_add_balance_balance.text()

            list_data = [name, balance]
        else:
            name = self.lineEdit_add_balance_name.text()

            list_data = [name, 0]

        if name == '':
            self.lineEdit_add_balance_name.setStyleSheet("border: 2 solid red;")
            msg.setWindowTitle("Ошибка!")
            msg.setText("Поле 'Название счета' является обязательным.")
            msg.exec_()

        else:
            directory = '../handler/csv_data/main_meny_check'
            files = os.listdir(directory)

            if files == []:
                with open(os.path.join('../handler/csv_data/main_meny_check', f'0_{name}.csv'), 'w') as temp_file:
                    temp_file.write('id,name,money1,money2,4,5,6\n')
                    temp_file.close()
            else:
                hold = list()
                for i in files:
                    var = i.split('_')
                    hold.append(var[0])
                id = int(max(hold)) + 1
                with open(os.path.join('../handler/csv_data/main_meny_check', f'{str(id)}_{name}.csv'), 'w') as temp_file:
                    temp_file.write('id,user,sum,value,xz,category,deskriptipon\n')
                    temp_file.close()

            self.lineEdit_add_balance_name.setStyleSheet("")

            with open('../handler/csv_data/pop-up_meny_check/check_list.csv', 'a', newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(list_data)
                f_object.close()

            self.comboBox_user_balance.clear()

            files = os.listdir(directory)

            for item in files:
                result = item.replace('.csv', '').split('_')
                self.comboBox_user_balance.addItem(str(result[1]))

        self.lineEdit_add_balance_balance.clear()
        self.lineEdit_add_balance_name.clear()
        self.set_un_visible_data()
        self.checkBox_is_have_balance.setChecked(False)


    def check_data(self):
        directory = '../handler/csv_data/main_meny_check'
        files = os.listdir(directory)
        # print(files)
        for item in files:
            result = item.replace('.csv', '').split('_')
            self.comboBox_user_balance.addItem(str(result[1]))


