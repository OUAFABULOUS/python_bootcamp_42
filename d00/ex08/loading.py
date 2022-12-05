import sys
import time

def	ft_progress(lst):
    start = time.time()
    progress = ""
    for i in lst:
        yield(i)
        res = int(i * 42 / 1000) * "-" + ">"
        elapsed_time = (time.time() - start)
        if i > 0:
            sys.stdout.write(f"\rETA: {((len(lst) / i) * elapsed_time):.2f}s [{(i/len(lst) * 100):.2f}%] [{res.ljust(42)}] {i}/{len(lst)} | elapsed time {elapsed_time:.2f}s")
            sys.stdout.flush()


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)
