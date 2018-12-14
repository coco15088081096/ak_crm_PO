import os
import yaml
class ReadLoginYaml():
    def __init__(self,filename):
        self.filename=os.getcwd()+os.sep+"data"+os.sep+filename
    def read_login_yaml(self):
        with open(self.filename,"r",encoding="utf-8")as f:
            return yaml.load(f)

#     # 以下为右键调试模式
#     def read_login_yaml_debug(self):
#         with open("../data/data_login.yaml","r",encoding="utf-8")as f:
#             return yaml.load(f)
# if __name__ == '__main__':
#     datas=ReadLoginYaml().read_login_yaml_debug().values()
#     arrs=[]
#     for data in datas:
#         arrs.append((data.get("username"),data.get("password")))
#     print(arrs)