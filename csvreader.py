import os,csv
class ReadFile(object):
    def __init__(self, filename):
        self._data = []
        self.localdir = '.\\worlds\\'
        self.filename = filename
        self.filepath = os.path.join(self.localdir, self.filename)
        self.read_data()

    def read_data(self):
        try:
            with open(self.filepath, 'r') as c:
                rows = csv.reader(c)
                for row in rows:
                    self._data.append(row)
        except Exception as ex:
            print(ex)

    def get_data(self):
        return self._data

def main():
    new = ReadFile('1.txt')
    new_data = new.get_data()

    for i in new_data:
        print(i)        # etc... more code will follow

if __name__ == '__main__':
    main()
