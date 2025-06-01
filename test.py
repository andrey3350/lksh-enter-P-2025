import time

for i in range(0, 100):
    print('\r'+'#'*i, end='', flush=True)
    time.sleep(1/5)