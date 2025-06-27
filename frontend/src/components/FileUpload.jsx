import React, { useState } from 'react';
import useUpload from '../hooks/useUpload';

export default function FileUpload({ setLoading, setResult }) {
    const [files, setFiles] = useState([]);
    const { commit } = useUpload();
    