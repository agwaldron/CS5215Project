import requests
import sys
import time


default_loop_interval = 10
url = 'http://httpforever.com/'

def request_loop(loop_interval):
    while(True):
        r = requests.get(url)
        print(f'request sent with response code {r.status_code}')
        time.sleep(loop_interval)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        loop_interval = int(sys.argv[1])
        print(f'starting request loop with an interval of {loop_interval} seconds')
        request_loop(loop_interval)
    else:
        print(f'starting request loop with default interval of {default_loop_interval} seconds')
        request_loop(default_loop_interval)

