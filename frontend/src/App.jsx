import { useState, useEffect } from 'react'

function App() {
  const [backendMessage, setBackendMessage] = useState('Attempting to connect...')

  useEffect(() => {
    // This fetches data from the Flask route we just created
    fetch('http://127.0.0.1:5000/api/test')
      .then((response) => response.json())
      .then((data) => setBackendMessage(data.message))
      .catch((error) => {
        console.error("Error fetching data:", error);
        setBackendMessage("Failed to connect to backend.");
      });
  }, []);

  return (
    <div style={{ padding: '40px', fontFamily: 'system-ui, sans-serif' }}>
      <h1>AI Study Planner & Tutor 🚀</h1>
      <div style={{ padding: '20px', backgroundColor: '#f0f0f0', borderRadius: '8px', marginTop: '20px' }}>
        <h3>Backend Status:</h3>
        <p style={{ color: backendMessage.includes('successful') ? 'green' : 'red', fontWeight: 'bold' }}>
          {backendMessage}
        </p>
      </div>
    </div>
  )
}

export default App