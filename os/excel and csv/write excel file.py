import openpyxl

def create_result_file(self):
    self.xfile = openpyxl.Workbook()
    self.sheet = self.xfile.active

    self.row_index = 0


def insert_row(self, result_row):
    self.row_index += 1
    for i, elm in enumerate(result_row):
        self.sheet.cell(row=self.row_index, column=i + 1).value = elm

def save(self):
    self.xfile.save(self.result_file_name)