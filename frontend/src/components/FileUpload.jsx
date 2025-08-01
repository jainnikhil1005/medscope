import React, { useState } from 'react';
import useUpload from '../hooks/useUpload';

export default function FileUpload({ setLoading, setResult }) {
    const [files, setFiles] = useState([]);
    const { commit } = useUpload();
    
    const onChange = e => setFiles(e.target.files);
    const onSubmit = () => {
    setLoading(true);
    commit(files[0], files[1], res => {
      setResult(res);
      setLoading(false);
    });
  };

  return (
    <div>
      <input type="file" onChange={onChange} multiple />
      <button onClick={onSubmit} disabled={files.length < 2}>
        Check Interaction
      </button>
    </div>
  );
}