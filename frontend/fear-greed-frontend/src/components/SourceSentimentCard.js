import React from 'react';

function SourceSentimentCard({ source, score, change, icon: Icon }) {
  // Determine color based on score
  const getColor = (val) => {
    if (val < 25) return '#E74C3C'; // red fear
    if (val < 50) return '#F1C40F'; // yellow caution
    if (val < 75) return '#27AE60'; // green greed
    return '#2ECC71'; // bright green extreme greed
  };

  return (
    <div className="bg-gray-800 p-4 rounded-lg flex items-center space-x-4 shadow-md w-64">
      <div className="text-3xl text-white">
        {Icon && <Icon />}
      </div>
      <div>
        <h4 className="text-white font-semibold text-lg">{source}</h4>
        <p className="text-white text-2xl font-bold" style={{ color: getColor(score) }}>
          {score}
        </p>
        <p
          className={`text-sm font-semibold ${
            change >= 0 ? 'text-green-400' : 'text-red-400'
          }`}
        >
          {change >= 0 ? `+${change}%` : `${change}%`} since last update
        </p>
      </div>
    </div>
  );
}

export default SourceSentimentCard;
