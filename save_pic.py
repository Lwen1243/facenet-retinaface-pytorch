import cv2
import os

def get_unique_filename(filename):
    """
    检查文件名是否已存在，如果存在，则返回一个新的唯一文件名
    """
    if not os.path.exists(filename):
        return filename
    
    base, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{base}_+{counter}{ext}"
        if not os.path.exists(new_filename):
            return new_filename
        counter += 1

# 打开摄像头（参数0表示默认摄像头）
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取摄像头画面
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头画面")
        break

    # 显示实时画面
    cv2.imshow('摄像头', frame)

    # 按下空格键拍摄图片并保存
    key = cv2.waitKey(1)
    if key == 32:  # 空格键的ASCII码是32
        # 生成唯一文件名
        filename = get_unique_filename('photo.jpg')
        # 保存图片到当前目录
        cv2.imwrite(filename, frame)
        print(f"图片已保存为 {filename}")

    # 按下 q 键退出程序
    elif key == ord('q'):
        print("退出程序")
        break

# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()