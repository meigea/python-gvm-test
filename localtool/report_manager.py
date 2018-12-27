from utils.OpenVasUtil import OpenVASTool, logging


class Report():
    def __init__(self):
        pass

    def get_reportid(self):
        from localtool.task_manager import Task
        report_id = Task().get_report_id()
        return report_id

    def extract_siggle_item(self, x):
        result = {}
        result["id"] = x["@id"] ## 条目的ID
        result["vulner_name"] = x["name"] ## 告警名称
        result["host"] = x["name"] ## 告警主机
        result["port"] = x["port"]  ## 告警端口
        result["modification_time"] = x["modification_time"]

        result["nvt_id"] = x["nvt"]["@oid"] ## 触发的规则ID
        result["nvt_name"] = x["nvt"]["name"] ## 告警名称
        result["nvt_tags"] = x["nvt"]["tags"] ##可能造成的危害
        result["family"] = x["nvt"]["family"] ## 类型
        result["nvt_name"] = x["nvt"]["name"] ##
        result["description"] = x["description"] ## 描述

        result["threat"] = x["threat"]

        return result


    def find_rw(self):
        params = dict(
            report_id="13f81a0f-216c-4b27-be61-98eef7315eb3",
        )
        datas = OpenVASTool().push_command("get_report", params)
        items = datas["get_reports_response"]["report"]["report"]["results"]["result"]
        res = []
        for item in items:
            res.append(self.extract_siggle_item(item))
        
        with open("demo.txt", "w+") as f:
            f.write(str(res))
            f.close()

        return datas















