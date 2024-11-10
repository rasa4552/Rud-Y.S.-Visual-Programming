# TODO Найдите количество книг, которое можно разместить на дискете
line_count = 50
page_count = 100
symbol_count = 25
symbol_weight= 4
step = 1024
Disk_Mb= 1.44
Book_weight= line_count * page_count * symbol_count * symbol_weight
Disk = Disk_Mb * step * step
Book_count= Disk // Book_weight
print("Количество книг, помещающихся на дискету:", round(Book_count))
