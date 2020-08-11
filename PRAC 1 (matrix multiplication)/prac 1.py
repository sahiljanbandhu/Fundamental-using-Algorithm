m=int(input("Enter no of rows in matrix"))
n=int(input("Enter no of columns in matrix1"))
mat1=[]
for i in range(0,m):
      mat1.append([])
      for j in range(0,n):
          mat1[i].append(j)
          mat1[i][j]=0
          print("Entry in row:",i+1,"column:",j+1)
          mat1[i][j]=int(input())
print (mat1)
p=int(input("Enter no of rows in matrix2"))
q=int(input("Enter no of colums in matrix2"))
mat2=[]
for i in range(0,p):
     mat2.append([])
for i in range(0,p):
      for j in range(0,q):
            mat2[i].append(j)
            mat2[i][j]=0
            print("Entry in row:",i+1,"column:",j+1)
            mat2[i][j]=int(input())
print(mat2)
res=[]
for i in range(0,m):
      res.append([])
for i in range(0,m):
    for j in range(0,q):
        res[i].append(j)
        res[i][j]=0
for p in range(len(mat1)):
      for q in range(len (mat2)):
          for r in range(len(mat2)):
                res[p][q]+=mat1[p][r]*mat2 [r][q]
print("Result of Matrix Multiplication is")
print(res)
