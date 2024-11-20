import logging
import snowflake.connector
logging.getLogger(__name__)


class SnowflakeAgent:
    def __init__(self,user,password,account,role,werehouse):
        self.snow_obj = snowflake.connector.connect(user=user,
                                                    password=password,
                                                    account=account,
                                                    role=role,
                                                    werehouse=werehouse)
    def exicute_query(self,query,results=False):
        logging.info('query exicution start')
        cursor = self.snow_obj.cursor(snowflake.connector.DictCursor).execute(query)
        def make_keys_lower(d):
            return {str.lower(key):value for key,value in d.items()}
        if results:
            logging.info('making keys lower')
            return [make_keys_lower(d) for d in cursor.fetchall()]
        else:
            return None


        