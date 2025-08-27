import React from 'react';
import {
  LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer,
  CartesianGrid,
} from 'recharts';

function SentimentTrendChart({ data }) {
  return (
    <div className="bg-gray-900 p-4 rounded-xl shadow-lg w-full max-w-4xl mx-auto">
      <h3 className="text-white text-xl font-semibold mb-4">
        Fear & Greed Index - Last 7 Days
      </h3>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <CartesianGrid stroke="#444" strokeDasharray="3 3" />
          <XAxis dataKey="date" stroke="#bbb" />
          <YAxis domain={[0, 100]} stroke="#bbb" />
          <Tooltip
            contentStyle={{ backgroundColor: '#222', borderRadius: '8px' }}
            labelStyle={{ color: '#ccc' }}
            itemStyle={{ color: '#fff' }}
          />
          <Line
            type="monotone"
            dataKey="score"
            stroke="#27AE60"
            strokeWidth={3}
            dot={{ r: 5 }}
            activeDot={{ r: 8 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default SentimentTrendChart;
