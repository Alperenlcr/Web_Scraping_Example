import queue
from threading import Thread
from requests import get
from time import perf_counter, sleep
import os, sys, glob, re
import json
from pprint import pprint

from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

from config import LINK_LIST_PATH, RAW_HTML_DIR
ENCODING = "utf-8"

q = queue.Queue(652)
url_df = pd.read_csv(LINK_LIST_PATH, sep="\t")


def thread_func():
    param = q.get()
    r = execute_func(param[1]["url"])
    try:
        save_path = os.path.join(RAW_HTML_DIR, f"{param[1]['id']}.html")

        with open(save_path, "w", encoding=ENCODING) as f:
            f.write(r)

    except Exception as e:
        with open(save_path, "w", encoding=ENCODING) as f:
            f.write("")
        print("Error saving page {page_id} html:" + str(e))
    q.task_done()

def execute_func(param):
    resp = get(url=param)
    resp = resp.content.decode(encoding=ENCODING)
    return resp



for i in url_df.iterrows():
    q.put(i)


t1_start = perf_counter()
while not q.empty():
    t = Thread(target=thread_func)
    t.daemon = True
    t.start()
    # t.join() #thread'in bitmeden koda devam etmez.
q.join()
t1_stop = perf_counter()
print("Elapsed time:", t1_stop, t1_start)

print("Elapsed time during the whole program in seconds:", t1_stop - t1_start)