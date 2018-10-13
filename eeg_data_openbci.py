import time
import datetime


class EegSample:
    def __init__(self, values, timestamp):
        self.values = values
        self.timestamp = timestamp

    @property
    def channels(self):
        return len(self.values)


class EegDataOpenBci:
    def __init__(self, file_path):
        self.file_path = file_path
        self.samples = []
        with open(file_path) as f:
            self._skip(f, 2)
            self.sample_rate = self._read_sample_rate(f)
            self._skip(f, 3)
            for line in f.readlines():
                index, values, accels, timestamp = self._split_data(line)
                self.samples.append(EegSample(values, timestamp))

    def _read_sample_rate(self, file):
        line = file.readline()
        rhs = self._get_rhs(line)
        return float(rhs[:-2])
    
    def _get_rhs(self, line):
        return line.split('=')[1].replace(' ', '').rstrip()

    def _split_data(self, line):
        tokens = line.rstrip().split(', ')
        conv = lambda s: float(s)
        return int(tokens[0]), map(conv, tokens[1:-4]), map(conv, tokens[-4:-1]), tokens[-1]
    
    def _skip(self, file, count):
        for _ in range(count):
            file.readline()
