from collections import defaultdict
from datetime import datetime
from openai import OpenAI
import os



def aggregate_transactions(transactions):
    summary = {
        "total_debits": 0,
        "total_credits": 0,
        "categories": defaultdict(lambda: {"total_amount": 0, "count": 0}),
        "monthly_summary": defaultdict(lambda: {"total_debits": 0, "total_credits": 0}),
    }
    for txn in transactions:
        amount = float(txn["Amount"]["Amount"])
        month = datetime.strptime(txn["BookingDateTime"].split('.')[0], '%Y-%m-%dT%H:%M:%S').strftime('%Y-%m')
        if txn["CreditDebitIndicator"] == "Debit":
            summary["total_debits"] += amount
            summary["monthly_summary"][month]["total_debits"] += amount
        else:
            summary["total_credits"] += amount
            summary["monthly_summary"][month]["total_credits"] += amount
        if "ProprietaryBankTransactionCode" in txn and "Code" in txn["ProprietaryBankTransactionCode"]:
            category = txn["ProprietaryBankTransactionCode"]["Code"]
            summary["categories"][category]["total_amount"] += amount
            summary["categories"][category]["count"] += 1
    return summary

def prepare_prompt_for_advice(accounts_info, transactions_data, credit_score_data, balance_data):
    aggregated_transactions = aggregate_transactions(transactions_data)
    prompt = f"""
    Provide detailed financial advice based on the following data:
    Accounts Information: {accounts_info}
    Credit Score Information: FICO Score: {credit_score_data['ficoScore']} FICO Range: {credit_score_data['ficoRange']} Date: {credit_score_data['date']}
    Balance Data: Account ID: {balance_data[0]['AccountId']}
    Balances: 1. Indicator: {balance_data[0]['CreditDebitIndicator']}, Type: {balance_data[0]['Type']}, Amount: {balance_data[0]['Amount']['Amount']} {balance_data[0]['Amount']['Currency']}
    Transactions Summary: Total Debits: {aggregated_transactions['total_debits']} GBP Total Credits: {aggregated_transactions['total_credits']} GBP Categories:
    """
    for category, details in aggregated_transactions["categories"].items():
        prompt += f"\n - {category}: {details['total_amount']} GBP ({details['count']} transactions)"
    prompt += "\n\nMonthly Summary:\n"
    for month, details in aggregated_transactions["monthly_summary"].items():
        prompt += f" - {month}: Debits: {details['total_debits']} GBP, Credits: {details['total_credits']} GBP\n"
    return prompt


def get_financial_advice(prompt):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
        model="gpt-4o",
    )
    response = chat_completion
    if response:
        return response.choices[0].message.content
    else:
        return "Failed to get response."