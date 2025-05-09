chon=0
socauhoi=8
while chon!= socauhoi+1:
    print("Chon so tu 1 den 8 de bat dau, hoac chon 9 de thoat")
    chon = int(input("su lua chon cua ban la:"))
    if chon == 9:
        break
    elif chon == 1:
        chuoi = input("Nhap 1 chuoi: ")
        chuoi_dao = ""
        for i in range(len(chuoi)-1, -1, -1):
            chuoi_dao += chuoi[i]
        print("Chuoi dao nguoc la:", chuoi_dao)
    elif chon == 2:
        a= int(input("Nhap so a: "))
        b= int(input("Nhap so b: "))
        if a > b:
            print("Xin Loi, a phai nho hon b")
        else:
            tong = 0
            for i in range(a+1, b):
                if i % 2 == 0:
                    tong += i
            print("Tong cac so chan tu a den b la:", tong)
    elif chon == 3:
        so_am= 0
        while True:
            n= int(input("Nhap so nguyen: "))
            if n == 0:
                break
            if n < 0:
                so_am += 1
                n= int(input("Nhap so nguyen: "))
                print("So am:", so_am)
    elif chon == 4:
        tong = 0
        dem = 0
        while True:
            n = float(input("Nhap so thuc (so am de dung): "))
            if n < 0:
                break
            tong += n
            dem += 1
        if dem > 0:
            tb = tong / dem
            print("Trung binh cong la:", tb)

    elif chon == 5:
        year = int(input("Nhập một năm: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "là năm nhuận")
else:
    print(year, "không phải là năm nhuận")
