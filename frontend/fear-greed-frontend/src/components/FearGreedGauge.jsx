import React from 'react';

const FearGreedGauge = ({ score }) => {
  const getColor = (score) => {
    if (score < 20) return 'text-red-600';
    if (score < 50) return 'text-yellow-500';
    return 'text-green-500';
  };

  return (
    <div className="flex flex-col items-center p-6 bg-white rounded-xl shadow-md">
      <h2 className="text-xl font-semibold mb-4">Fear & Greed Index</h2>
      <div className={`text-6xl font-bold ${getColor(score)}`}>
        {score}
      </div>
    </div>
  );
};

export default FearGreedGauge;
