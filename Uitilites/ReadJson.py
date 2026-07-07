import json
import os

class ReadJson:
    @staticmethod
    def get_login_data():
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_path, "TestData", "login_data.json")
        
        with open(json_path, "r") as file:
            return json.load(file)
        
    """@pytest.mark.parametrize("user_credentials", ReadJson.get_login_data())"""
        
    
    # #method 2
    # @staticmethod
    # def get_login_data1():
    #     # JSON file ka sahi path dhoondhne ke liye
    #     base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #     json_path = os.path.join(base_path, "TestData", "login_data.json")
        
    #     with open(json_path, "r") as file:
    #         data = json.load(file)
            
    #     #parametrize take tuple: [("user1", "pass1"), ("user2", "pass2")]
    #     formatted_data = []
    #     for item in data:
    #         formatted_data.append((item["username"], item["password"]))
            
    #     return formatted_data
    
    # """@pytest.mark.parametrize("username, password", ReadJson.get_login_data())"""