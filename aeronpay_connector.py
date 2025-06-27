import requests
import config


class AeronPayConnector:

    
    BASE_URL = config.BASE_URL
    ENDPOINTS = {
        "request_payout": "api/payout/imps",
        "check_status": "reports/transactionStatus",
        "check_balance": "api/balance/check_balance",
    }

    def __init__(self):
        self.client_id = config.CLIENT_ID
        self.client_secret = config.CLIENT_SECRET
        self.account_no = config.ACCOUNT_NO
        self.merchant_id = config.MERCHANT_ID


    def constuct_header(self): return {
        "client-id": self.client_id,
        "client-secret" : self.client_secret,
        "Content-Type" : "application/json",
        "accept" : "application/json"
    }

    def check_balance(self) -> dict:
        url = f"{self.BASE_URL}{self.ENDPOINTS["check_balance"]}"
        
        body = {
            "client_referenceId": "112233",
            "account_type": "Merchant",
            "accountNumber": self.account_no,
            "merchant_id": self.merchant_id
        }

        res = requests.post(url, json=body, headers=self.constuct_header())
        return res.json()

obj = AeronPayConnector()
print(obj.check_balance())