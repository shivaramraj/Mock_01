import snowagent_m as SA
import logging
import connection_m
def collect_data_tsv(snowflake_crd):
    snow_obj = SA.SnowflakeAgent(snowflake_crd['user'],
                                 snowflake_crd['password'],
                                 snowflake_crd['account'],
                                 snowflake_crd['role'],
                                 snowflake_crd['wherehouse'])
    try:
        logging.info('creating a stage in snowflake')
        snow_obj.exicute_query(connection_m.sales_create_stage,results=True)
        logging.info('putting data into stage')
        snow_obj.exicute_query(connection_m.sales_put_query,results=True)
        logging.info('creating a table in snowflake')
        snow_obj.exicute_query(connection_m.sales_create_table_query,results=True)
        logging.info('copy data into table')
        snow_obj.exicute_query(connection_m.sales_copy_cmd,results=True)
    except Exception as e:
        print(e)
