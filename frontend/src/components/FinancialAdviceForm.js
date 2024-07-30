import React, { useState } from 'react';
import axios from 'axios';
import FinancialAdviceDisplay from './FinancialAdviceDisplay';

const FinancialAdviceForm = () => {
    const [accountId, setAccountId] = useState('');
    const [advice, setAdvice] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/financial-advice', { account_id: accountId });
            setAdvice(response.data.advice);
        } catch (error) {
            console.error('Error fetching financial advice:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Account ID:
                    <input 
                        type="text" 
                        value={accountId} 
                        onChange={(e) => setAccountId(e.target.value)} 
                    />
                </label>
                <button type="submit">Get Advice</button>
            </form>
            {advice && <FinancialAdviceDisplay advice={advice} />}
        </div>
    );
};

export default FinancialAdviceForm;
