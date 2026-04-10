import React from 'react';
import './App.css';
import Dashboard from './components/Dashboard';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Real-Time Analytics Dashboard</h1>
      </header>
      <main>
        <Dashboard />
      </main>
    </div>
  );
}

export default App;