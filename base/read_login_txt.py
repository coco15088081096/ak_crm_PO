import yaml
class ReadLoginTxt():
    def read_login_txt(self):
        with open("data/data_login.txt","r",encoding="utf-8")as f:
            return yaml.load(f)