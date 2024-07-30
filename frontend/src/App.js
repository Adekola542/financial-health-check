import React, { useState } from 'react';
import FinancialAdviceForm from './components/FinancialAdviceForm';
import AdviceDisplay from './components/AdviceDisplay';
import './App.css';

function App() {
    const [advice, setAdvice] = useState(null);

    return (
        <div className="App">
          <div style={{textAlign: 'center', padding: '20px 0'}}>
            <h1 style={{margin: '0', color: '#6a0dad' }}>Finance Buddy</h1>
            <p style={{margin: '0'}}>Your Personal Financial Advisor</p>
          </div>

            {/* <h1 style={{color: '#6a0dad', margin: '0'}}>Finance Buddy</h1>
            <p style={{margin: '0'}} >Your Personal Financial Advisor</p> */}
            <FinancialAdviceForm setAdvice={setAdvice} />
            <AdviceDisplay advice={advice} />
        </div>
    );
}

export default App;


