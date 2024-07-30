from pydantic import BaseModel
from typing import List, Dict

class AccountInfo(BaseModel):
    account_id: str
    balances: List[Dict]
    transactions: List[Dict]
    credit_score: Dict
