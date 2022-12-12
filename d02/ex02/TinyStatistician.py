
import statistics

class TinyStistician:
    def	mean(x):
        return sum(x) / len(x)
    def	median(x):
        x = set(x).sort()
        n = len(x)
        if n % 2:
            return x[((n + 1) / 2) - 1]
        else:
            return (x[((n + 1) / 2) - 1] + x[(n / 2) - 1]) / 2
    def quartile(x):
        try:
            quartiles = []
            x.sort()
            n = len(x)
            if not n % 2:
                quartiles.append(median(x[:n / 2]))
                
                quartiles.append(median(x[n / 2:]))
            else
                quartiles.append(median(x[: (n + 1) / 2]))
        les


