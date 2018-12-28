from wraper.OpenVasUtil import OpenVASTool, logging

"""
报告:产生的报告
"""
class Report():

    def __init__(self):
        pass

    def get_reportid(self):
        from gvmd.task_manager import Task
        report_id = Task().get_report_id()
        return report_id

    def get_allkeys_from_reports(self):
        res = OpenVASTool().push_command("get_results", None)["result"]
        keys = []
        for data in res:
            keys += list(data.keys())
        return list(set(keys))

    def extract_siggle_item(self, x):
        result = {}
        result["id"] = x["@id"] ## 条目的ID
        result["vulner_name"] = x["name"] ## 告警名称
        result["host"] = x["host"]["#text"] ## 告警主机
        result["port"] = x["port"]  ## 告警端口
        result["modification_time"] = x["modification_time"]
        result["detection"] = x["detection"] if "detection" in x.keys() else None
        from gvmd.info_manager import INFO_TYPES
        info_type = [t for t in x.keys() if t in INFO_TYPES][0]
        result["info_type"] = info_type
        try:
            result["oid"] = x[info_type]["@oid"] ## 触发的规则ID
            result["oname"] = x[info_type]["name"] ## 告警名称
            result["otags"] = x[info_type]["tags"] ##可能造成的危害
            result["family"] = x[info_type]["family"] ## 类型
        finally:
            pass
        result["description"] = x["description"] ## 描述
        result["threat"] = x["threat"]
        result["security"] = x["severity"]
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


class ResultMg():
    def __init__(self):
        pass

    def get_results(self):
        from gvmd.task_manager import Task
        report_id = Task().get_report_id()
        _data = OpenVASTool().push_command("get_report", {"report_id": report_id})["get_reports_response"]
        try:
            results = []
            for item in _data["report"]["report"]["results"]["result"]:
                try:
                    _temp = Report().extract_siggle_item(item)
                except:
                    _temp = {}
                    logging.info("转化-" +report_id+ "-报告得数据失败" )
                _temp["report_id"] = report_id ## 这里的 report_id 就是 task_id 等价。
                results.append(_temp)
            return results
        except:
            logging.info("获取报告结果失败")
            return []


















