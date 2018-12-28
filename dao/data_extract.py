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

def extract_item():
    from gvmd.report_manager import ResultMg
    results = ResultMg().get_results()
    for result in results:
        insert_scanlog_item(result)
        insert_scanlib_oscan(result)
    return None



