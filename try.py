from logics.logic import convert_data


INDATA_PATH = 'trydata/input'
FILENAME_COVID19_DATA = "timeseries.json"
OUTFILE_PATH = 'trydata/output/data.json'

if __name__ == '__main__':
    convert_data(
        infile_path=INDATA_PATH + "/" + FILENAME_COVID19_DATA,
        outfile_path=OUTFILE_PATH
    )
