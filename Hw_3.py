import os
os.mkdir("CS")
os.chdir("CS")
with open("homework.txt", "w") as file:
    file.write("4112029015_蔡立豪")
with open("homework.txt", "r") as file:
    file_contents = file.read()
    print("文件內容：", file_contents)
file_info = os.stat("homework.txt")
print("文件info：")
print("文件大小：", file_info.st_size, "字节")
print("創建時間：", file_info.st_ctime)
print("最后訪問时间：", file_info.st_atime)
print("最後修改時間：", file_info.st_mtime)
