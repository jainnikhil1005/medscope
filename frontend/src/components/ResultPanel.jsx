import React from 'react';

export default function ResultPanel({ result }) {
  return (
    <div style={{ marginTop: '1rem' }}>
      <h2>Status: {result.status}</h2>
      {result.details && <p>{result.details}</p>}
    </div>
  );
}