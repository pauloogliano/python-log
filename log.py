import logging
import datetime

d = datetime.datetime.now()
hoje = d.strftime('%Y-%m-%d')
logging.basicConfig(filename='log-'+hoje+'.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.debug('Start of program')
logging.debug('End of program')