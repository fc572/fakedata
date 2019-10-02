import csv


class FileUtilities:

    def writer(self, file):
        return csv.writer(file)

    def close(self, file):
        file.close()
