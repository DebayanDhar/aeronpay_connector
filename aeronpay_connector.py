import os
import requests



class AeronPayConnector:
    API_ENV = os.getenv("API_ENV")
    BASE_URL = f"https://api.aeronpay.in/api/serviceapi-{API_ENV}/"

    ENDPOINTS = {
        "request_payout": "api/payout/imps",
        "check_status": "reports/transactionStatus",
        "check_balance": "balance/check_balance",
    }

    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.account_no = os.getenv("ACCOUNT_NO")
        self.merchant_id = os.getenv("MERCHANT_ID")


    def constuct_header(self): return {
        "client-id": self.client_id,
        "client-secret" : self.client_secret,
        "Content-Type" : "application/json"
    }

    def check_balance(self) -> dict:
        url = f"{self.BASE_URL}{self.ENDPOINTS["check_balance"]}"
        body = {
            "client_referenceId": "1234567890",
            "account_type": "Merchant",
            "accountNumber": self.account_no,
            "merchant_id": self.merchant_id
        }

        res = requests.get(url, json=body, headers=self.constuct_header())
        return res.json()

    