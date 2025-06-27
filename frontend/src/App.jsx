import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import ResultPanel from './components/ResultPanel';
import Loader from './components/Loader';

export default function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  return (
    <div style={{ maxWidth: 600, margin: 'auto', padding: '1rem' }}>
      <h1>MedScope</h1>
      <FileUpload setLoading={setLoading} setResult={setResult} />
      {loading && <Loader />}
      {result && <ResultPanel result={result} />}
    </div>
  );
}