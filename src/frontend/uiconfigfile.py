from configparser import ConfigParser


class Config:
    def __init__(self,config_file="./src/frontend/uiconfigfile.ini"):
        self.config=ConfigParser() #parsing the config file
        self.config.read(config_file) #reading the content of the config file

    #methos to access the default config variables available in the config file
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
