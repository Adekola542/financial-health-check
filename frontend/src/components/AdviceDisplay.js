import React from 'react';

const AdviceDisplay = ({ advice }) => {
    if (!advice) {
        return null; // Don't render anything if there's no advice
    }

    return (
        <div>
            <h2>Financial Health check </h2>
            <p>{advice}</p>
        </div>
    );
};

export default AdviceDisplay;

