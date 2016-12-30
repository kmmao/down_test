# -*- coding:utf-8 -*-

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from fdfs_client.client import Fdfs_client


client = Fdfs_client('client.conf')


class MyHandler(FileSystemEventHandler):

    def on_created(self,event):
        pass

    def on_modified(self,event):
        if not event.is_directory:
            try:
                print("检测到生成新文件")
                client.upload_by_filename(event.src_path)
                os.remove(event.src_path)
                print("已将新文件放进mongodb")
            except IOError:
                pass

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./www', recursive=True)
    observer.start()
    try:
        print "started myWatch"
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
