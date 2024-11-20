snowflake_crd = {
    'user':'shivaramraj8804',
    'password':'Shivaramraj8804',
    'account':'sddglmj-oh42926',
    'role':'accountadmin',
    'wherehouse':'compute_wh'
}
# https://sddglmj-oh42926.snowflakecomputing.com

sales_STAGE_NAME = 'MOCK_01.mock_01_schema.MOCK_01_STAGE'
sales_create_stage = f'CREATE OR REPLACE STAGE {sales_STAGE_NAME} FILE_FORMAT = (type = csv)'
path = '../files/SalesData.tsv'
# C:\snow_conn_env\files
sales_put_query = f'put file://{path} @{sales_STAGE_NAME}'
sales_table_name = 'MOCK_01.mock_01_schema.SALES_TSV2'
sales_create_table_query =f'''CREATE OR REPLACE table {sales_table_name}(
                                Order_No NUMBER,
                                order_date date,
                                Salesperson varchar(20),
                                Product varchar(10),
                                Quantity varchar(10),
                                price varchar(10),
                                customer varchar(10),
                                region varchar(10),
                                chennal varchar(10),
                                revenue varchar(10),
                                cost varchar(10),
                                profit varchar(10))
                            STAGE_FILE_FORMAT = ( TYPE = 'csv' FIELD_DELIMITER= '\t' )
                            '''

sales_copy_cmd = f'''COPY INTO {sales_table_name} FROM @{sales_STAGE_NAME} FILE_FORMAT = (
                        TYPE=CSV,
                        SKIP_HEADER=1,
                        FIELD_DELIMITER='\t')
                    ON_ERROR=ABORT_STATEMENT
                    PURGE=TRUE'''
# f'COPY INTO {snowflake_table} FROM @your_stage/file.tsv FILE_FORMAT = (TYPE = "CSV" FIELD_OPTIONALLY_ENCLOSED_BY=\'"\')

# FILE_FORMAT = (TYPE = \'CSV\' FIELD_OPTIONALLY_ENCLOSED_BY = \'\\t\' FIELD_OPTIONALLY_ENCLOSED_BY_NONE = TRUE)

# LIST @%mytable


# COPY INTO "MOCK_01"."MOCK_01_SCHEMA"."SALES_TSV"
# FROM '@"MOCK_01"."MOCK_01_SCHEMA"."%SALES_TSV"/__snowflake_temp_import_files__/'
# FILES = ('SalesData.tsv')
# FILE_FORMAT = (
#     TYPE=CSV,
#     SKIP_HEADER=1,
#     FIELD_DELIMITER='0x09',
#     TRIM_SPACE=FALSE,
#     FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
#     REPLACE_INVALID_CHARACTERS=TRUE,
#     DATE_FORMAT=AUTO,
#     TIME_FORMAT=AUTO,
#     TIMESTAMP_FORMAT=AUTO
# )
# ON_ERROR=ABORT_STATEMENT
# PURGE=TRUE

# TRIM_SPACE=FALSE,
#                         FIELD_OPTIONALLY_ENCLOSED_BY=NONE,
#                         REPLACE_INVALID_CHARACTERS=TRUE,
#                         DATE_FORMAT=AUTO,
#                         TIME_FORMAT=AUTO,
#                         TIMESTAMP_FORMAT=AUTO