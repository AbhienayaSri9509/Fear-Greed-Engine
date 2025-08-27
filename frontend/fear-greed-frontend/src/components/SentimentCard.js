import React from "react";
import styles from "./SentimentCard.module.css";

export default function SentimentCard({ title, sentiment }) {
  let sentimentClass = styles.neutral;
  if (sentiment.toLowerCase() === "positive") sentimentClass = styles.positive;
  else if (sentiment.toLowerCase() === "negative") sentimentClass = styles.negative;

  return (
    <div className={styles.card}>
      <h3>{title}</h3>
      <p className={sentimentClass}>{sentiment}</p>
    </div>
  );
}
