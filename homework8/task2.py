import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.database_name)

    def __getitem__(self, keyname):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT * from {self.table_name} WHERE name=\'{keyname}\'')
        row = list(cursor.fetchone())
        return row


    def __len__(self):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT COUNT(*) from {self.table_name}')
        n = cursor.fetchone()
        return n[0]


    def __contains__(self, name):
        if self.__getitem__(name):
            return True
        else:
            return False


    def __iter__(self):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT * from {self.table_name}')
        return ClassIterator(cursor)


class ClassIterator:
    def __init__(self, cursor):
        self.cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        row = self.cursor.fetchone()
        if row is None:
            raise StopIteration
        else:
            return row



presidents = TableData(database_name='example.sqlite', table_name='presidents')
print(presidents['Yeltsin'])
print(len(presidents))
print('Yeltsin' in presidents)
for president in presidents:
    print(president)
