import os
folder_path = r'/data/amax/users/liuwenzhe/paper/lily_202102'
# print(folder_path)
for home,dirs,files in os.walk(folder_path):
    if len(dirs)>2 and len(files) == 0:
        # print('home:{}, dirs:{}, files:{}.'.format(home,dirs,files))
        for dir_ in dirs:
            new_dir = dir_.replace(' ','_')
            os.rename(os.path.join(home,dir_),os.path.join(home,new_dir))