import os
import subprocess


from modules.create_file import CreateFile
from modules.create_folder import CreateFolder


class NewRepo:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def start(self):
        file_new_repo = os.path.abspath(__file__)
        print(f"Thư mục gốc: {self.root_folder}")

        CreateFile(f"{self.root_folder}/README.md")
        CreateFile(f"{self.root_folder}/.gitignore")

        code_workspace = os.path.join(os.path.dirname(file_new_repo), "../../nghia-template.code-workspace")
        with open(code_workspace, "r", encoding="utf-8") as file:
            contents = file.read()
            CreateFile(f"{self.root_folder}/{os.path.basename(self.root_folder)}.code-workspace", contents)

        CreateFolder(f"{self.root_folder}/contents")
        CreateFolder(f"{self.root_folder}/contents/others")

        CreateFolder(f"{self.root_folder}/contents/others/code")
        CreateFolder(f"{self.root_folder}/contents/others/python")
        CreateFolder(f"{self.root_folder}/contents/others/modules")

        CreateFolder(f"{self.root_folder}/contents/others/input")
        CreateFolder(f"{self.root_folder}/contents/others/output")

        CreateFolder(f"{self.root_folder}/contents/others/docs")
        CreateFolder(f"{self.root_folder}/contents/others/documents")

        CreateFolder(f"{self.root_folder}/contents/others/data")
        CreateFolder(f"{self.root_folder}/contents/others/video")

        CreateFolder(f"{self.root_folder}/contents/others/images")
        CreateFolder(f"{self.root_folder}/contents/others/pictures")

        CreateFolder(f"{self.root_folder}/contents/others/tools")
        CreateFolder(f"{self.root_folder}/contents/others/tasks")
        CreateFolder(f"{self.root_folder}/contents/others/temp")

        CreateFolder(f"{self.root_folder}/contents/others/linux")
        CreateFolder(f"{self.root_folder}/contents/others/windows")

        all_gitignore = os.path.join(os.path.dirname(file_new_repo), "../../all.gitignore")
        with open(all_gitignore, "r", encoding="utf-8") as file:
            contents = file.read()
            CreateFile(f"{self.root_folder}/contents/.gitignore", contents)

        CreateFile(f"{self.root_folder}/contents/{os.path.basename(self.root_folder)}.py")

        # Git
        # os.chdir(self.root_folder)
        # subprocess.run(['git', 'add', '.']) Nếu có file khác cũng bị add
        # subprocess.run(['git', 'commit', '-m', 'Initial commit']) Tự động commit cũng ok
        # subprocess.run(['git', 'push']) Nếu có trường hợp khác mà push thì ...????

        # VSCode
        # subprocess.run(['code', '.'], shell=True)
