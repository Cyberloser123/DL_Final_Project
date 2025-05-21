import os
import csv
from pathlib import Path

def generate_video_csv(data_dir, output_csv):
    """
    生成包含視頻文件路徑和標籤的 CSV 文件
    
    Args:
        data_dir (str): 包含視頻文件的目錄路徑
        output_csv (str): 輸出 CSV 文件的路徑
    """
    # 支持的視頻文件擴展名
    video_extensions = {'.mp4', '.webm', '.avi', '.mov'}
    
    # 獲取所有視頻文件
    video_files = []
    for root, _, files in os.walk(data_dir):
        for file in files:
            if Path(file).suffix.lower() in video_extensions:
                abs_path = os.path.abspath(os.path.join(root, file))
                # 從文件名或目錄名中提取標籤（這裡需要根據實際情況修改）
                label = 0  # 預設標籤為 0，需要根據實際情況修改
                video_files.append((abs_path, label))
    
    # 寫入 CSV 文件
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        for video_path, label in video_files:
            writer.writerow([video_path, label])
    
    print(f"已生成 CSV 文件：{output_csv}")
    print(f"共處理 {len(video_files)} 個視頻文件")

if __name__ == "__main__":
    data_directory = "data/20bn-something-something-v2"
    output_csv_file = "video_dataset.csv"
    
    if not os.path.exists(data_directory):
        print(f"錯誤：目錄 {data_directory} 不存在")
    else:
        generate_video_csv(data_directory, output_csv_file) 