from __future__ import division


def create_result_file(self, result_file_name):
    heading = [
        "Title", "Author", "itunes URL", "Website", "Email"
    ]

    import codecs
    self.result_file = codecs.open(result_file_name, "w", "utf-8")
    self.result_file.write(u'\ufeff')
    self.insert_row(result_row=heading)


def insert_row(self, result_row):
    self.result_file.write('"' + '","'.join(result_row) + '"' + "\n")
    self.result_file.flush()