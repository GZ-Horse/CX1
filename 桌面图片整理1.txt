import os
import shutil

# 指定桌面路径
desktop_path = "E:\\Desktop"

# 创建文件夹用于存放图片
folder_name = "Desktop Images"
image_folder = os.path.join(desktop_path, folder_name)
if not os.path.exists(image_folder):
    os.mkdir(image_folder)

# 获取桌面上所有文件和文件夹的列表
desktop_contents = os.listdir(desktop_path)

# 遍历桌面上的文件和文件夹
for item in desktop_contents:
    item_path = os.path.join(desktop_path, item)

    # 如果当前项目是图片文件，则将其复制到图片文件夹中
    if os.path.isfile(item_path) and item.endswith((".jpg", ".jpeg", ".png", ".gif")):
        shutil.copy2(item_path, image_folder)

print("所有图片已经移动到 %s 文件夹中。" % folder_name)
