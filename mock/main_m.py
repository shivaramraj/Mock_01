import logging
import sys
import connection_m
import collect_data
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

std_handler = logging.StreamHandler(sys.stdout)
std_handler.setLevel(logging.INFO)
std_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs/etl_logs.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(std_handler)
logger.addHandler(file_handler)

def exicute():
    try:
        collector_name = sys.argv[1]
        if collector_name == 'mock_01':
            logging.info('hellow world')
            collect_data.collect_data_tsv(connection_m.snowflake_crd)
    except IndexError as e:
        print(e)

if __name__ == '__main__':
    exicute()