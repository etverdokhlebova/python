import os
import shutil
import exifread
import datetime

input_dir = "C:\\Users\\tverd\\python\\photos"
output_dir = "C:\\Users\\tverd\\python\\photos1"

def get_exif_data(img_path):
    with open(img_path, 'rb') as f:
        tags = exifread.process_file(f)
        if 'EXIF DateTimeOriginal' in tags:
            return tags['EXIF DateTimeOriginal'].values
        else:
            return None  
        
def get_available_filename(path, filename):
    if not os.path.exists(os.path.join(path, filename)):
        return filename

    file, ext = os.path.splitext(filename)
    for i in range(1, 100):
        new_filename = f"{file}({i}){ext}"
        if not os.path.exists(os.path.join(path, new_filename)):
            return new_filename        

for root, dirs, files in os.walk(input_dir):
    for file in files:
        file_path = os.path.join(root, file)
        if not (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".JPG")):
              print("This file " + file + " is not a jpeg or jpg file")
              user_choice = input("Do you want to move this file to the not_image folder ?(Y/N)")
              if user_choice.upper() == 'Y':
                  not_image_folder = os.path.join(output_dir, "not_image")
                  os.makedirs(not_image_folder, exist_ok=True)
                  shutil.copy(file_path, not_image_folder)
              else:
                   continue    
        else:
            date_time = get_exif_data(file_path)
            if date_time is None:
                unknown_folder = os.path.join(output_dir, "unknown")
                os.makedirs(unknown_folder, exist_ok=True)
                shutil.copy(file_path, unknown_folder)
                date = "unknown"
                for index, file in enumerate(os.listdir(unknown_folder)):
                    if file.endswith('.jpg'):
                       date = "unknown"
                       new_filename = f"{date}-{index}.jpg"
                       new_filename = get_available_filename(unknown_folder, new_filename)
                       os.rename(os.path.join(unknown_folder, file), os.path.join(unknown_folder, new_filename))
        
                    else:
                      date_folder = os.path.join(output_dir, date.replace(':','_'))
                      os.makedirs(date_folder, exist_ok=True)
                      if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".JPG"):
                        shutil.copy(file_path, date_folder)
                      for index, file in enumerate(os.listdir(date_folder)):
                        if file.endswith('.jpg') or file.endswith(".jpeg") or file.endswith(".JPG"):
                           _, file_ext = os.path.splitext(file)
                           date = date_time.strftime("%Y-%m-%d")
                           new_filename = f"{date}-{index}{file_ext}"
                           new_filename = get_available_filename(date_folder, new_filename)
                           os.rename(os.path.join(date_folder, file), os.path.join(date_folder, new_filename))
            else:
                date_folder = os.path.join(output_dir, date_time.split()[0].replace(':','_'))
                os.makedirs(date_folder, exist_ok=True)
                if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".JPG"):
                  shutil.copy(file_path, date_folder)
                for index, file in enumerate(os.listdir(date_folder)):
                   if file.endswith('.jpg') or file.endswith(".jpeg") or file.endswith(".JPG"):
                     date_time_obj = datetime.datetime.strptime(date_time, '%Y:%m:%d %H:%M:%S')
                     date = date_time_obj.strftime("%Y-%m-%d")
                     _, file_ext = os.path.splitext(file)
                     new_filename = f"{date}-{index}{file_ext}"
                     new_filename = get_available_filename(date_folder, new_filename)
                     os.rename(os.path.join(date_folder, file), os.path.join(date_folder, new_filename))
print ("O MY GOD IT IS WORKING!!!")
print (" I KNOW IT IS NOT EVERYTHING, BUT IT WAS REALLY MY BEST EFFORT EVER")
print ("12 YEARS IN AZKABAN")                  
print ("argparse is too f*cked up for me sorry xD")