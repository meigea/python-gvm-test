import re
from configs.cfg import THERATE_CODE
from db.sql_cli import sql_action, from_sql_get_data


def get_info(key, tags):
    matched = re.match(".*?\|"+ key +"=(.*?)\|.*?", tags)
    if matched:
        return matched.group(1)
    return ""

def insert_scanlib_oscan(item):
    _sql = "select oid from scanlib where oid='{}';".format(item["oid"])
    _data = from_sql_get_data(_sql)["data"]
    if len(_data) > 0:
        return

    impact = get_info("impact", item["otags"])
    if impact == "":
        impact = item["tags"]
    _insert_sql = """insert into scanlib(oid, oname, summary, solution, vuldetect,
 impact, family, security, info_type, threat_code) values(
       "{oid}", "{oname}", "{summary}", "{solution}", "{vuldetect}","{impact}",
        "{family}", "{security}", "{info_type}", {threat_code});""".format(
        oid=item["oid"],
        oname=item["oname"],
        summary=get_info("summary", item["otags"]),
        impact=impact,
        solution=get_info("solution", item["otags"]),
        vuldetect=get_info("vuldetect", item["otags"]),
        family=item["family"],
        security=item["security"],
        info_type=item["info_type"],
        threat_code= THERATE_CODE[item["threat"]] ,
    )
    # print(_insert_sql)
    sql_action(_insert_sql)


def insert_scanlog_item(item):
    _insert_sql = """insert into scanlog(id, report_id, vulner_desc, host, port, oid) values(
    "{id}","{report_id}",'{vulner_desc}','{host}',"{port}","{oid}");""".format(
        id=item["id"],
        report_id=item["report_id"],
        vulner_desc=item["description"].replace("'", "\"") if item["description"] else "",
        host=item["host"],
        port=item["port"],
        oid=item["oid"],
        # add_time=item["modification_time"],
    )
    try:
        sql_action(_insert_sql)
    finally:
        pass


def oid_issaved(oid):
    _sql = "select oid from scanlib where oid='{}';".format(oid)
    _data = from_sql_get_data(_sql)["data"]

    info_partern = """(.*?)\|summary=(.*?)\|impact=(.*?)\|vuldetect=(.*?)\|solution=(.*?)"""


    """
    {'id': 'e383dda5-a13f-477b-b50d-7b5060710b87',
    'vulner_name': 'C.H.I.P. Device Default SSH Login',
    'host': '192.168.2.175',
    'port': '2222/tcp',
     'modification_time': '2018-12-25T04:42:03Z',
      'detection': None,
       'oid': '1.3.6.1.4.1.25623.1.0.108164',
        'oname': 'C.H.I.P. Device Default SSH Login',
       'otags':
        'cvss_base_vector=AV:N/AC:L/Au:N/C:P/I:P/A:P|summary=The remote C.H.I.P. device is prone to a default account authentication bypass vulnerability.|impact=This issue may be exploited by a remote attacker to gain access to sensitive information or modify system configuration.|vuldetect=Try to login with known credentials.|solution=Change the password.|solution_type=Workaround|qod_type=exploit', 'family': 'Default Accounts', 'description': 'It was possible to login to the remote C.H.I.P. Device via SSH with the following credentials:\n\nUsername: "root", Password: "chip"\n\nIt was also possible to execute "cat /etc/passwd" as "root". Result:\n\nroot:x:0:0:root:/root:/bin/bash',
    'threat': 'High',
    'severity': '7.5',
     'report_id': b'b4d77cd0-fc57-4d18-8a5f-0c1a522a0de9'}

    """
    if len(_data) > 0:
        return True
    else:
        return None

def extract_item():
    from gvmd.report_manager import ResultMg
    results = ResultMg().get_results()
    for result in results:
        insert_scanlog_item(result)
        insert_scanlib_oscan(result)
    return None



