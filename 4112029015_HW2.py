def memory_addressing(page_table ,page_size ,logical_address):
    page_number, offset = divmod(logical_address, page_size)
    if page_number in page_table:
        frame_number = page_table[page_number]
        #計算物理地址
        physical_address =  frame_number * page_size + offset
        print(f"The physical address is {physical_address}")
    else:
        print("Invalid page number, address translation failed.")
#讓使用者input page_table
page_table = {}
num = int(input("請輸入欲設定之鍵的數量:"))
count = 0
while count < num:  
    key = int(input("请输入键: "))
    value = int(input("輸入值: "))
    page_table[key] = value
    count += 1
###
page_size = 4096
logical_address = int(input("請輸入logical address: "))
memory_addressing(page_table, page_size, logical_address)