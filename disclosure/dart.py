import datetime
import sys
import dart_fss as dart
from dbconfig import getConn

def regist_disclosure():

    api_key = ''
    dart.set_api_key(api_key = api_key)

    nowDate = datatime.datetime.now().strftime('%Y%m%d')
    reports = dart.filings.search(bgn_de=nowDate, end_de=nowDate, page_count=100, page_no=1, last_reprt_at="Y")
