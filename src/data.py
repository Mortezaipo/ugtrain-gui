"""Data management of UGTrain-GUI.
It works with memory based SQLite3.
"""

import sqlite3


class Data:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def init_general_form_table(self):
        sql = "CREATE TABLE IF NOT EXISTS 'general_form_settings' " \
              "('process_name' TEXT, " \
              "'process_call' TEXT, " \
              "'process_param' TEXT, " \
              "'process_absolute_path' TEXT, " \
              "'macro_name' TEXT, " \
              "'use_gbt' BOOL, " \
              "'mem_file' TEXT);"
        self.cursor.execute(sql)

    def init_static_form_table(self):
        sql = "CREATE TABLE IF NOT EXISTS 'static_form_settings' " \
              "('value_name' TEXT, " \
              "'abs_address' TEXT, " \
              "'data_type' TEXT, " \
              "'check' BOOL, " \
              "'wish_value' TEXT, " \
              "'key_binding' TEXT, " \
              "'act_state' TEXT);" \
              "CREATE TABLE IF NOT EXISTS 'static_form_args' " \
              "('args' TEXT);"
        self.cursor.execute(sql)

    def destroy_static_form_table(self):
        sql = "DROP TABLE IF EXISTS 'static_form_settings'"
        self.cursor.execute(sql)