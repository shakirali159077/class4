# num=1
# sum=1
# for i in range (2,101,2):
#     print (f"{num}/{i}")
#     num+=1
# sum+=num/i
# print(sum)

# ----------------------------------------


# def star(rows):
#     for i in range(1, rows + 1):
#       print("*" * i)
# rows = 3
# star(rows)




# =======================================

# for i in range (1,8):
#     print((6-i)*" ",i*"*")




# for i in range (1,8):
#     print((i-7) *" *" ,i*" *")



# ==========================


# for i in range(1,8):
   
#     if i>=(i+1)//2:
#         print(" "*(i+7) + "*"*1)
#     else:
#         print(" " *(i - 1) + " * "* ( i + 1))


        
# ===========================


def star(rows):
    for i in range(1, rows + 1):
        if i <= (rows + 1) // 2:
            print(" " * (rows - i) + "* " * i)
        else:
            print(" " * (i - 1) + "* " * (rows - i + 1))

rows = 9  
star(rows)