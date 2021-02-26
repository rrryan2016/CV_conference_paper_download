import time 
from selenium import webdriver
import requests
import threading
import os 

def Handler(start, end, url, filename): 
    # specify the starting and ending of the file 
    headers = {'Range': 'bytes=%d-%d' % (start, end)} 
    # request the specified part and get into variable     
    r = requests.get(url, headers=headers, stream=True) 
    # open the file and write the content of the html page  
    # into file. 
    with open(filename, "r+b") as fp: 
        fp.seek(start) 
        var = fp.tell() 
        fp.write(r.content)

def download_file(url_of_file,name,number_of_threads): 
    r = requests.head(url_of_file) 
    if name: 
        file_name = name 
    else: 
        file_name = url_of_file.split('/')[-1] 
    try: 
        file_size = int(r.headers['content-length']) 
    except: 
        print("Invalid URL")
        return

    part = int(file_size) / number_of_threads 
    fp = open(file_name, "wb") 
    # fp.write('\0' * file_size) 
    fp.close() 
    for i in range(number_of_threads): 
        start = int(part * i) 
        end = int(start + part) 
        # create a Thread with start and end locations 
        t = threading.Thread(target=Handler, 
            kwargs={'start': start, 'end': end, 'url': url_of_file, 'filename': file_name}) 
        t.setDaemon(True) 
        t.start() 

    main_thread = threading.current_thread() 
    for t in threading.enumerate(): 
        if t is main_thread: 
            continue
        t.join() 

info_txt_path = '/data/amax/users/liuwenzhe/paper/code/arxiv_paper_list.txt' # todo:1
save_path = '/data/amax/users/liuwenzhe/paper/lily_202102/Deep Learning for Generic Object Detection A Survey' # todo: 2

file = open(info_txt_path)
for line in file.readlines():
    line = line.strip("\n")
    # print((line))
    # if line != '\n':
    pdf_url = line+'.pdf'
    filename = pdf_url[-14:]
    print('filename:{}, pdf_url:{}.'.format(filename,pdf_url))

    # pdf_urls = []
    # pdf_url = 'https://arxiv.org/pdf/1709.06508.pdf'

    print('\nDownloading {} ...'.format(filename))
    # exit()
    # pdf_url = 'https://arxiv.org/pdf/{}.pdf'.format(arxiv_id)
    # filename = filename_replace(paper_title) + '.pdf'
    ts = time.time()
    download_file(url_of_file=pdf_url, name=os.path.join(save_path,filename),number_of_threads=1) 
    te = time.time()
    # print('progress: 100/100')
    print('{:.0f}s [Complete] {}'.format(te-ts, filename))