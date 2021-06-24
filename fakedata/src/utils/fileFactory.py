import os
import csv


class FileFactory:

    def open_file(self, file_name):
        dir_name = os.path.join(os.path.expanduser('~'), 'Documents/fc_project_data/')

        path_to_file = os.path.join(dir_name + file_name)

        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        return open(path_to_file, 'a', newline='')

    def writer(self, file):
        return csv.writer(file)

    def write_file_headers(self, file, file_headers):
        writer = self.writer(file)
        writer.writerow(file_headers)
        return writer

    def close_file(self, *argv):
        for file in argv:
            file.close()

