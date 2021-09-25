A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 88]
B = [1, 3, 5, 4, 7, 88, 66, 59, 40, 54]
print("list A:", A)
print("list B:", B)
C= list( set (A) & set(B))
print("Các phần tử trùng nhau trong 2 mảng là: ", C)
D=list( set (A) ^ set(C))
print("Các phần tử list A không trùng với list B là:", D)
E=list( set (B) ^ set(C))
print("Các phần tử list B không trùng với list A là:", E)