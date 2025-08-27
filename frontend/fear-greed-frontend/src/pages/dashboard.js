import React, { useEffect, useState } from "react";
import { fetchSentimentData } from "../services/api";
import SentimentCard from "../components/SentimentCard";
import SentimentGraph from "../components/SentimentGraph";
import LoadingSpinner from "../components/LoadingSpinner";
import "./Dashboard.css";

export default function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSentimentData()
      .then((res) => {
        setData(res);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) return <LoadingSpinner />;
  if (!data) return <div className="error">Error loading data</div>;

  return (
    <div className="dashboard-container">
      <h1>Fear & Greed Index</h1>

      <div className={`score-card ${data.scoreCategory}`}>
        <h2>Current Score: {data.score}</h2>
      </div>

      <div className="sentiment-cards">
        <SentimentCard title="Twitter" sentiment={data.twitterSentiment} />
        <SentimentCard title="Reddit" sentiment={data.redditSentiment} />
        <SentimentCard title="News" sentiment={data.newsSentiment} />
        <SentimentCard title="Finance" sentiment={data.financeSentiment} />
      </div>

      <SentimentGraph history={data.history} />

      <div className="recent-feed">
        <h3>Recent Sentiment Feed</h3>
        {data.recentFeed.map((item, idx) => (
          <div key={idx} className="feed-item">
            <p>{item.text}</p>
            <small>
              {item.source} — <span className={`sentiment-label ${item.sentiment.toLowerCase()}`}>{item.sentiment}</span>
            </small>
          </div>
        ))}
      </div>
    </div>
  );
}
