import React from 'react';

function LatestFeed({ posts }) {
  return (
    <div className="max-w-4xl mx-auto mt-8 bg-gray-900 rounded-xl shadow-lg p-6">
      <h3 className="text-white text-xl font-semibold mb-4">Latest Social & News Mentions</h3>
      <div className="overflow-y-auto max-h-48">
        {posts.map((post, i) => (
          <div
            key={i}
            className={`p-3 mb-2 rounded-md ${
              post.sentiment === 'fear' ? 'bg-red-800' : 'bg-green-800'
            }`}
          >
            <p className="text-gray-200">{post.text}</p>
            <small className="text-gray-400">{post.source} — {post.date}</small>
          </div>
        ))}
      </div>
    </div>
  );
}

export default LatestFeed;
