class Para2:
    def __init__(self):
        self.a = 1  # nilai float/integer
        self.li = []  # list nilai

    # Method untuk menambah dan mengurangi list berdasarkan aturan stack
    def tambah(self, nilai):
        self.li.append(nilai)
        print ("List telah bertambah menjadi:", list.li)

    def kurang(self):
        if len(self.li) < 1:
            return None
        else:
            print ("Nilai list yang dihapus:", self.li.pop())
            print ("Isi List setelah nilai dihapus:", list.li)

    # Method untuk perulangan deret dikali 7 menggunakan WHILE
    def deret_kali_7(self):
        result = []
        if self.a % 2 == 0 or self.a % 5 == 0:
            current = self.a
            while current <= self.a * 7:
                result.append(current)
                current += 7
        return result

    # Method rekursif untuk operasi sesuai ketentuan
    def refukursif(self, n=None):
        if n is None:
            n = self.a
        if n == 3:
            return 3 ** 3 + 2 ** 2 + 1 ** 1
        else:
            return n + self.refukursif(n - 1)


class Cha2(Para2):
    def __init__(self, a, li, b):
        super().__init__(a, li)
        self.b = b  # tambahan atribut b (float)

    # Method untuk mengurutkan nilai di list menggunakan merge sort
    def merge_sort(self, lst=None):
        if lst is None:
            lst = self.li
        if len(lst) > 1:
            mid = len(lst) // 2
            left_half = lst[:mid]
            right_half = lst[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    lst[k] = left_half[i]
                    i += 1
                else:
                    lst[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                lst[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                lst[k] = right_half[j]
                j += 1
                k += 1
        return lst

    # Method untuk mencari luas dan keliling persegi dengan sisi b
    def persegi_properties(self):
        luas = self.b ** 2
        keliling = 4 * self.b
        return {"luas": luas, "keliling": keliling}

list = Para2()

list.tambah(12)
list.tambah(16)
list.tambah(87)
list.tambah(80)
list.kurang()


# print("Deret kali 7:", list.deret_kali_7())
# print("Rekursif operasi:", list.refukursif())

# data_Cha2 = Cha2(4, [10, 20, 5], 6.0)
# print("Merge Sort:", data_Cha2.merge_sort())
# print("Persegi Properties:", data_Cha2.persegi_properties())
