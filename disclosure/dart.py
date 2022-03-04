import datetime
import sys
import dart_fss as dart
from dbconfig import getConn


def set_disclosure():
    api_key = ''
    dart.set_api_key(api_key=api_key)
    cur = conn.cursor(prepared=True)

    nowDate = datetime.datetime.now().strftime('%Y%m%d')
    reports = dart.filings.search(bgn_de=nowDate, end_de=nowDate, page_count=100, page_no=1, last_reprt_at="Y")

    try:

        for i in range(len(reports.report_list)):
            report = reports.report_list[i]
            rcp_no = report.rcp_no
            corp_cls = report.corp_cls
            corp_code = report.corp_code
            corp_name = report.corp_name
            flr_nm = report.flr_nm
            rcept_dt = report.rcept_dt
            report_nm = report.report_nm
            rm = report.rm
            stock_code = report.stock_code

            cur.execute("SELECT rcp_no FROM disclosure WHERE rcp_no = " + rcp_no)
            disclosure = cur.fetchone()
            if disclosure:
                return None
            else:
                cur.execute(
                    "INSERT INTO disclosure (rcp_no, corp_cls, corp_code, corp_name, flr_nm, rcept_dt, report_nm, rm, stock_code, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (rcp_no, corp_cls, corp_code, corp_name, flr_nm, rcept_dt, report_nm, rm, stock_code, now))
                conn.commit()
    except:
        sys.exit(1)


class Dart:
    def __init__(self):
        pass

    set_disclosure()
