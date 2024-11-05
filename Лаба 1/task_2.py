# TODO Найдите количество книг, которое можно разместить на дискете
Book_weight= 4*25*50*100
Disk = 1.44*1024*1024
Book_count= Disk/Book_weight
###print("Количество книг, помещающихся на дискету:", Book_count.round(.0))
print("Количество книг, помещающихся на дискету:", round(Book_count))
