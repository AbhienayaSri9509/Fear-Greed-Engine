import React, { useRef } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function SentimentGraph({ history }) {
  const chartRef = useRef(null);

  return (
    <div style={{ width: "100%", height: 300 }} ref={chartRef}>
      <h3>Fear & Greed Score History</h3>
      <ResponsiveContainer>
        <LineChart data={history}>
          <XAxis dataKey="date" />
          <YAxis domain={[0, 100]} />
          <Tooltip />
          <Line type="monotone" dataKey="score" stroke="#8884d8" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
