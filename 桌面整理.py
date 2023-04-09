import os
import shutil

# 定义桌面路径
desktop_path = "E:\\Desktop"

# 定义文件分类规则
file_types = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "视频": [".mp4", ".avi", ".mov", ".wmv"],
    "音乐": [".mp3", ".wav", ".flac"],
    "文档": [".doc", ".docx", ".pdf", ".txt", ".ppt", ".xls", ".xlsx"],
    "程序": [".exe", ".dmg", ".pkg"]
}

# 遍历桌面文件
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(file_path):
        # 获取文件扩展名
        file_ext = os.path.splitext(filename)[1].lower()
        for folder_name, folder_exts in file_types.items():
            # 如果符合分类规则则移动到对应文件夹
            if file_ext in folder_exts:
                folder_path = os.path.join(desktop_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)
                print(f"已将文件 {filename} 分类到文件夹 {folder_name}")
                break
