class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__table = [[] for _ in range(size)]
        
    def hash_func(self, key):
        res = 0
        for char in key:
            res += ord(char)
        return res % self.__size
    
    def insert(self, key, value):
        index = self.hash_func(key)
        for pair in self.__table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.__table[index].append([key, value])
        
    def search(self, key):
        index = self.hash_func(key)
        for pair in self.__table[index]:
            if pair[0] == key:
                return pair[1] 
        return None
    
    def delete(self, key):
        index = self.hash_func(key)
        for i, pair in enumerate(self.__table[index]):
            if pair[0] == key:
                del self.__table[index][i]
                return
    
    def resize(self):
        old_table = self.__table
        self.__size *= 2
        self.__table = [[] for _ in range(self.__size)]
        
        for bucket in old_table:
            for pair in bucket:
                self.insert(pair[0], pair[1]) 
                
    def display(self):
        for index, bucket in enumerate(self.__table):
            print(index, bucket)
            
    @property
    def table(self):
        return self.__table
    
def hash_function_dict(table:HashTable):
    res = dict()
    for bucket in table.table:
        for pair in bucket:
            res_ascii = 0
            for char in pair[0]:
                res_ascii += ord(char)
            res[pair[0]] = res_ascii
    return res
    
table = HashTable(5)

for i in range(10):
    table.insert(f"key{i}", i)
    
print(table.search('key5'))
table.delete('key5')
print(table.search('key5'))
table.display()
table.insert('key5', 5)

table.resize()
table.display()

print(hash_function_dict(table))