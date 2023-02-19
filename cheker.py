import os
import shutil


os.chdir('../vids')
counter = 0
p = 0
for dir in os.listdir():
    if dir == "part1":
        os.chdir(dir)
        for file in os.listdir():
            if file.endswith('.mp4'):
                collection_dir1 = '../total/part1'
                if not os.path.exists(collection_dir1):
                    os.mkdir(collection_dir1)
                shutil.copy2(file, collection_dir1)
                counter += 1
        os.chdir('..')
        p += 1
    elif dir == "part2":
        os.chdir(dir)
        for file in os.listdir():
            if file.endswith('.mp4'):
                collection_dir2 = '../total/part2'
                if not os.path.exists(collection_dir2):
                    os.mkdir(collection_dir2)
                shutil.copy2(file, collection_dir2)
                counter += 1
        os.chdir('..')
        p += 1
print(counter)
print(p)




