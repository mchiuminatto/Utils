import pandas as pd
import sys
from datetime import datetime as dt
import json
import logging

class FileSplitter:

    def __init__(self, input_folder, output_folder, log_folder):

        self.input_folder = input_folder
        self.output_folder = output_folder
        self.log_folder = log_folder

        _date = dt.today().strftime("%Y%m%d")
        _log_file_name = self.log_folder +_date + "_SPLIT_FILE_" + ".log"
        logging.basicConfig(filename=_log_file_name,format="%(asctime)s %(levelname)s:%(message)s",
            level=logging.INFO)

    def calc_chunk_size(self, total,split):

        _chunk_size = divmod( total,split)[0]
        while divmod(_chunk_size,2)[1] != 0:
            _chunk_size = int(_chunk_size) + 1

        return int(_chunk_size)

    def split_file(self,file_name, split_in,records):

        if divmod(records,2)[1] != 0:
            logging.error(f"Error splitting the file. records {records}, splits {split_in} {divmod(records, 2)[1]}")
        else:

            # base file name
            _fix_name_part = file_name.replace(".csv","")

            # calculate chunk size
            _chunk_size = self.calc_chunk_size(records, split_in)

            if divmod(_chunk_size,2)[1] != 0:
                logging.info("Increasing chunk size in 1")
                _chunk_size = int(_chunk_size) + 1

            logging.info(f"Original file recs: {records}")
            logging.info(f"Chunk size {_chunk_size}")
            logging.info(f"Total records {_chunk_size * split_in}")

            # split the file
            _file_list = []
            _rec_acc = 0
            for _i,_chunk in enumerate(pd.read_csv(file_name,chunksize=_chunk_size)):
                _file_name = f"{_fix_name_part}_{_i}.csv"
                logging.info(f"Working on chunk {_file_name}")

                _file_list.append(_file_name)
                _chunk.to_csv(_file_name,chunksize=_chunk_size, columns=self.columns, index=False)
                _len_df_chunk = len(_chunk)
                if divmod(_len_df_chunk, 2)[1] != 0:
                    raise Exception(f"**** IMPAIRED NUMBER OFR RECORDS PROCESS WILL STOP, CHECK ORIGINAL FILE ****")

                _rec_acc = _rec_acc + _len_df_chunk

            return _file_list, _rec_acc

    def count_file_records(self,file_name):

        _records = 0
        with open(file_name,newline='') as _file:
            try:
                _records = sum(1 for line in _file)
                _records = _records - 1 # we remove header
            except Exception as e:
                raise Exception(f"Error counting file records. Reason: {str(e)}")

        return _records


    def split(self, file_name, split_in):

        _tic = dt.now()
        _file_list = []
        _count = 0
        _recs = 0
        try:
            _recs = self.count_file_records(file_name)
            _file_list, _count = self.split_file(file_name, split_in, _recs,self.RIC, self.side)

            _chunk_file_desc = {"records":_count,
                                "list":_file_list}

            _json_fn = f"{self.RIC}_{self.side}_chunk_list.json"
            # write chunk list descriptor
            with open(_json_fn, "w") as _fp:
                json.dump(_chunk_file_desc, _fp)
        except Exception as e:
            print(f"Error splitting files")

        _tac = dt.now()

        if _count != _recs:
            raise Exception(f"Input records {_recs} account differs from output {_count}")
        _t_delta = _tac - _tic
        print(f"File splitted in {_t_delta.seconds/60}")
        for _file in _file_list:
            print("Chunk: " + _file)



if __name__ == "__main__":

    _file_name = ""
    _splits = 0
    try:
        _file = sys.argv[1]   # tick file name
        _splits = sys.argv[2]
        _RIC = sys.argv[3]
        _side = sys.argv[4]

        try:
            _fs = FileSplitter(_RIC, _side)
            _fs.split(_file, int(_splits))
        except Exception as e:
            exit(-1)
        exit(0)

    except IndexError as e:
        print("form is load <file_name> <side>")
        print("Missing parameter")
        exit(-1)
