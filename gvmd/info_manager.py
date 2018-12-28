from wraper.OpenVasUtil import OpenVASTool, logging

INFO_TYPES = ["nvt", "cve", "cpe", "ovaldef", "cert_bund_adv", "dfn_cert_adv"]

class Info():
    def __init__(self):
        pass

    def get_info(self, info_type):
        _resp = OpenVASTool().push_command("get_info_list", {"details": True, "info_type": info_type})
        with open(info_type + ".txt", "w+", encoding="utf-8") as f:
            f.write(str(_resp))
            f.close()

    def get_infos(self):
        _info_types = INFO_TYPES
        for info_type in _info_types:
            self.get_info(info_type)














