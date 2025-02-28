import os


def CreateFile(file, contents=""):
    print(f"Kiểm tra tồn tại: {file}")
    if not os.path.exists(file):
        print(f"Tạo file: {file}")
        with open(f"{file}", "w", encoding="utf-8") as file:
            file.write(contents)
