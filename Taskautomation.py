import os
import shutil

def organize_files(directory):
    
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.avi', '.mov']
    }
    
    for folder in file_types:
        if not os.path.exists(os.path.join(directory, folder)):
            os.makedirs(os.path.join(directory, folder))
    
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            extension = os.path.splitext(filename)[1].lower()
            
            for folder, extensions in file_types.items():
                if extension in extensions:
                    source = os.path.join(directory, filename)
                    destination = os.path.join(directory, folder, filename)
                    shutil.move(source, destination)
                    print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    directory_path = input("Enter directory path to organize: ")
    if os.path.exists(directory_path):
        organize_files(directory_path)
        print("Organization complete!")
    else:
        print("Directory not found!")