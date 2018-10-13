from eeg_data_openbci import EegDataOpenBci


if __name__ == '__main__':
    data = EegDataOpenBci('./data/OpenBCI-RAW-2018-10-10_23-06-56.txt')
    print(data)
