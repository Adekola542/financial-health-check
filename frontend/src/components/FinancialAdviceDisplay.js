import React from 'react';
import './FinancialAdviceDisplay.css';

const TextFormatter = ({ text }) => {
    // Function to format the text
    const formatText = (section) => {
      let formattedText = section.replace(/(###|####)(.*?):/g, '<br /><br /><strong>$2:</strong>');
      
      formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<em>$1</em>');
    
      formattedText = formattedText.replace(/- .*?:/g, '<br />$&');
      //(/- .*?:/g, '<br />$&');


      //formattedText = formattedText.replace(/#/g, '');
      
      return formattedText;
    };

    //const formattedText = formatText(text);
    const sections = text.split(/(?=####)/);

    return (
        <div className='container' style={{padding: '5px'}}>
        {sections.map((section, index) => (
            <div key={index} style={{padding: '10px', marginBottom:'10px', backgroundColor: '#f0f0f0'}}>
            <div dangerouslySetInnerHTML={{ __html: formatText(section) }} />
            </div>
        ))}
        </div>
    );

   // return (

     // <div dangerouslySetInnerHTML={{ __html: formattedText }} />
    //);
  };


const FinancialAdviceDisplay = ({ advice }) => {
    return (
        <div className="advice-container">
            <h2>Financial Health Check</h2>
            <div className="advice-content">
                <TextFormatter text={advice} />                
                {/* <p>Based on your financial data, I'll provide tailored advice to optimize your financial health and leverage your current position. Here's a breakdown of your situation:</p>

                <h3>Summary of Financial Data:</h3>
                <p><strong>Credit Score Information:</strong></p>
                <p>FICO Score: 720 (Good) {advice}</p>
                <p>FICO Range: Good (typically 670-739)</p>
                
                <p><strong>Balance Data:</strong></p>
                <p>Account ID: 7c015d90-6e3a-4ab1-b392-20e058979991</p>
                <p>Balances: 125,580.92 GBP (Credit, Expected Amount)</p>
                
                <p><strong>Transactions Summary:</strong></p>
                <p>Total Debits: 100.0 GBP</p>
                <p>Total Credits: 250.0 GBP</p>
                
                <p><strong>Categories:</strong></p>
                <p>TFR (Transfer): 350.0 GBP (from 2 transactions)</p>
                
                <p><strong>Monthly Summary for July 2024:</strong></p>
                <p>Debits: 100.0 GBP</p>
                <p>Credits: 250.0 GBP</p>

                <h3>Financial Advice:</h3>
                <p><strong>Credit Score Management:</strong></p>
                <p>A FICO score of 720 is good but can be improved to excellent (typically 740+). Ensure timely payments on all obligations.</p>
                <p>Avoid high credit utilization; try to keep it below 30% of your credit limit.</p>
                <p>Diversify your credit mix, including installment loans and revolving credit.</p>
                
                <p><strong>Income and Expense Analysis:</strong></p>
                <p>Your net credits for July 2024 were 150 GBP (250 GBP credits - 100 GBP debits).</p>
                <p>Maintain a habit of tracking your expenses to understand where your money is going and identify areas to cut unnecessary spending.</p>
                
                <p><strong>Savings and Investments:</strong></p>
                <p>Consider diverting a portion of the 125,580.92 GBP towards high-yield savings accounts or investment options such as stocks, bonds, mutual funds, or ETFs to grow your wealth.</p>
                <p>Keep a sufficient emergency fund (at least 3-6 months of living expenses).</p>
                
                <p><strong>Debt Management:</strong></p>
                <p>Although not specified, if you have any existing debt, prioritize paying off high-interest debt first.</p>
                <p>Ensure that you do not accumulate new debt faster than you can pay it off. Maintain or reduce the outstanding balance you might have.</p>
                
                <p><strong>Optimize Transfers (TFR):</strong></p>
                <p>The two transactions totaling 350 GBP suggest movement of funds either externally or between accounts. Analyze the necessity and purpose of these transfers.</p>
                <p>If these are towards savings or investment contributions, ensure they are aligned with your financial goals.</p>

                <h3>Action Plan:</h3>
                <p><strong>Regular Budget Review:</strong></p>
                <p>Create a monthly budget and analyze it routinely. Include all sources of income and categorize your expenditures to ensure discipline.</p>
                
                <p><strong>Build and Maintain an Emergency Fund:</strong></p>
                <p>Establish a solid emergency fund to cover unexpected expenses without resorting to credit.</p>
                
                <p><strong>Investment Diversification:</strong></p>
                <p>If you haven’t already, consult a financial advisor regarding diversified investment opportunities to maximize returns on your credit balance of 125,580.92 GBP.</p>
                
                <p><strong>Credit Score Monitoring:</strong></p>
                <p>Utilize credit monitoring services to keep an eye on your credit score, and promptly address any discrepancies or opportunities for improvement.</p>
                
                <p><strong>Strategic Transfers:</strong></p>
                <p>Ensure that financial transfers are purposeful, such as automated contributions to retirement accounts or savings plans.</p>
                
                <p><strong>Continuous Learning:</strong></p>
                <p>Stay informed about financial trends and updates. Consider financial literacy courses to further understand how to manage and grow your wealth effectively.</p>

                <h3>Finance Body:</h3>
                <p>The combination of good credit health, positive monthly cash flow, and substantial credit balance places you in a comparatively strong financial position. With strategic planning and disciplined financial habits, you can enhance your financial security and achieve your long-term goals. If needed, consult your personal financial advisor to tailor a detailed strategy to your specific situation.</p> */}
            </div>
        </div>
    );
};

export default FinancialAdviceDisplay;
