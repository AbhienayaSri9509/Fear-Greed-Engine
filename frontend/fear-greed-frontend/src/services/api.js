// Simulated fetch function, replace with real API calls

export async function fetchSentimentData() {
  // Replace this with real API call using axios or fetch
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        score: 65,
        scoreCategory: "greed", // could be 'fear', 'neutral', 'greed'
        twitterSentiment: "Positive",
        redditSentiment: "Neutral",
        newsSentiment: "Negative",
        financeSentiment: "Positive",
        history: [
          { date: '2025-07-10', score: 45 },
          { date: '2025-07-11', score: 50 },
          { date: '2025-07-12', score: 55 },
          { date: '2025-07-13', score: 60 },
          { date: '2025-07-14', score: 65 },
        ],
        recentFeed: [
          { text: "Bitcoin surged 10% today.", source: "Twitter", sentiment: "Positive" },
          { text: "Market volatility remains high.", source: "News", sentiment: "Negative" },
          { text: "Investors cautiously optimistic.", source: "Reddit", sentiment: "Neutral" },
        ]
      });
    }, 1000);
  });
}
