import React from 'react';

const SourceCard = ({ source, sentiment }) => {
  const getColor = (value) => {
    if (value < 20) return 'text-red-600';
    if (value < 50) return 'text-yellow-500';
    return 'text-green-600';
  };

  return (
    <div className="p-4 bg-gray-50 rounded-lg shadow-md">
      <h3 className="text-lg font-semibold">{source}</h3>
      <p className={`text-2xl font-bold ${getColor(sentiment)}`}>{sentiment}</p>
    </div>
  );
};

export default SourceCard;
