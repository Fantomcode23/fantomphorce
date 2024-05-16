import React, { useState } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
//import './App.css';

function HomePage() {
  return (
    <div className="App">
      <header className="App-header">
        <Link to="/login"><button>Login</button></Link>
        <Link to="/signup"><button>Sign Up</button></Link>
      </header>
    </div>
  );
}

function LoginPage() {
  const [message, setMessage] = useState('');
  const handleLogin = async () => {
    try {
      const response = await fetch('/login');
      const data = await response.text();
      setMessage(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <button onClick={handleLogin}>Login</button>
      <p>{message}</p>
    </div>
  );
}

function SignupPage() {
  const [message, setMessage] = useState('');
  const handleSignup = async () => {
    try {
      const response = await fetch('/signup');
      const data = await response.text();
      setMessage(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <button onClick={handleSignup}>Sign Up</button>
      <p>{message}</p>
    </div>
  );
}

function EmissionsCalculator() {
  const [country, setCountry] = useState('India');
  const [distance, setDistance] = useState(0);
  const [electricity, setElectricity] = useState(0);
  const [meals, setMeals] = useState(0);
  const [waste, setWaste] = useState(0);
  const [emissions, setEmissions] = useState({});

  const calculateEmissions = () => {
    axios.post('/calculate', {
      country,
      distance,
      electricity,
      meals,
      waste
    }).then(res => {
      setEmissions(res.data);
    });
  };

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <input type="text" value={country} onChange={e => setCountry(e.target.value)} />
          <input type="number" value={distance} onChange={e => setDistance(e.target.value)} />
          <input type="number" value={electricity} onChange={e => setElectricity(e.target.value)} />
          <input type="number" value={meals} onChange={e => setMeals(e.target.value)} />
          <input type="number" value={waste} onChange={e => setWaste(e.target.value)} />
          <button onClick={calculateEmissions}>Calculate Emissions</button>
        <div>
          {emissions && Object.entries(emissions).map(([key, value]) => (
            <p key={key}>{key}: {value}</p>
          ))}
        </div>
        </div>
      </header>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        <Route path="/calculate" element={<EmissionsCalculator />} />
        <Route path="/" element={<HomePage />} />
      </Routes>
    </Router>
  );
}

export default App;