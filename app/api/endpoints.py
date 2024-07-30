from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from app.api.utils import prepare_prompt_for_advice, get_financial_advice
from app.services.natwest_api import get_access_token, get_account_balances, get_transactions, create_account_access_consent, authorize_consent, exchange_code_for_tokens, get_credit_score
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

class AccountRequest(BaseModel):
    account_id: str

@router.post("/financial-advice")
async def financial_advice(request: AccountRequest):
    try:
        account_id = request.account_id

        # Step 1: Get access token
        access_token = get_access_token()

        # Step 2: Create account access consent
        consent_id = create_account_access_consent(access_token)

        # Step 3: Authorize consent
        auth_code = authorize_consent(consent_id)

        # Step 4: Exchange auth code for tokens
        access_token, refresh_token, id_token = exchange_code_for_tokens(auth_code)

        # Step 5: Get credit score
        credit_score = get_credit_score(access_token)
        print(credit_score, "creditscore")
    
        # Step 6: Get account balances
        balances = get_account_balances(access_token, account_id)
        print(balances, "balances")

        # Step 7: Get transactions
        transactions = get_transactions(access_token, account_id)
        print(transactions, "transactions")

        # Step 8: Prepare prompt for GPT-4
        prompt = prepare_prompt_for_advice(account_id, transactions['Data']['Transaction'], credit_score, balances['Data']['Balance'])

        # Step 9: Get financial advice from GPT-4
        advice = get_financial_advice(prompt)

        return {"advice": advice}

    except Exception as e:
        logger.error(f"Error in /financial-advice: {e}")
        raise HTTPException(status_code=400, detail=str(e))
