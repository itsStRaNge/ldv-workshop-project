

class CloudConnector:

    def get_auth_token(self):
        token = ""
        timeout = 30
        return token, timeout

    def get_all(self, auth_token):
        return []

    def get_item(self, auth_token, item_id):
        return {}
