import React from 'react';

function KeywordsPanel({ fearKeywords, greedKeywords }) {
  return (
    <div className="flex justify-between gap-6 max-w-4xl mx-auto mt-8">
      <div className="flex-1 bg-gray-900 p-6 rounded-xl shadow-lg">
        <h3 className="text-red-500 font-bold text-xl mb-4">Top Fear Keywords</h3>
        <ul className="list-disc list-inside text-gray-300">
          {fearKeywords.map((word, i) => (
            <li key={i}>{word}</li>
          ))}
        </ul>
      </div>
      <div className="flex-1 bg-gray-900 p-6 rounded-xl shadow-lg">
        <h3 className="text-green-500 font-bold text-xl mb-4">Top Greed Keywords</h3>
        <ul className="list-disc list-inside text-gray-300">
          {greedKeywords.map((word, i) => (
            <li key={i}>{word}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default KeywordsPanel;
