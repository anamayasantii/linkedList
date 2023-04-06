#class node
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
#mengambil data 
    def get_data(self):
        return self.data
    
#mengambil lokasi node berikutnya
    def get_next(self):
        return self.next_node

#menentukan node berikutnya
    def set_next(self, new_next):
        self.next_node = new_next
        
#class operasi link list
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    #menambah node baru
    def insert(self, data):
        #inisialisasi node baru
        new_node = Node(data)
        #tunjuk node berikutnya dari node baru yang ditunjuk head
        new_node.set_next(self.head)
        #head menunjuk ke node yang baru
        self.head = new_node
#menghitung panjang list
    def size(self):
        current = self.head
        couter = 0
        #perulangan untuk menghitung
        while current:
            counter +=1
            current = current.get_next()
        return counter
    
    #mencari data
    def search(self, data):
        current = self.head
        found = False
        #perulangan
        while current and found is False:
            if current.get_data()==data:
                found = True
            else:
                current=current.get_next()
                
    #menghapus node
    def delete(self,data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data()==data:
                found = True
            else:
                previous=current
                current=current.get_next()
        if current is None:
            raise ValueError("Data not found")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    #fungsi untuk melihat list
    def showData(self):
        print('List Data:')
        print('Node -> Next Node')
        current = self.head
        while current is not None:
            print(current.data)
            print('->')
            print(current.next_node.data) if hasattr(current.nex_node,"data") else None
            current = current.next_node
            
    def deleteAll(self):
        current = self.head
        if current is None:
            print('Tidak ada data')
        while current:
            self.head = current.get_next()
            current = None
            current = self.head
            
    def menu(self):
        pilih = 'y'
        while (pilih =='y'):
            print('Menu Linked List:')
            print('1. Insert Data')
            print('2. Delete Data')
            print('3. Search Data')
            print('4. Size Data')
            print('5. Show Data')
            print('6. ')
            inp = str(input('Masukkan pilihan: '))
            if(inp == '1'):
                obj = str(input('Masukkan angka yang ingin ditambahkan:'))
                self.insert(obj)
            elif(inp == '2'):
                obj = str(input('Masukkan angka yang ingin ditambahkan:'))
                self.delete(obj)
            elif(inp == '3'):
                obj = str(input('Masukkan angka yang ingin ditambahkan:'))
                status = self.search(obj)
                if status == True:
                    print('Data Ditemukan')
                else:
                    print('Data tydak ditemukan')
            elif(inp == '4'):
                print('Panjang list : '+str(self.size()))
            elif(inp == '5'):
                self.showData()
            else:
                pilih = 'n'
                
if __name__ == "__main__":
    l = LinkedList()
    l.menu()
    
# ll = Node(10,11)
# print(ll)