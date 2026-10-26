import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, AuthContext } from './context/AuthContext';
import Navbar from './components/Navbar';
import Landing from './pages/Landing';
import Auth from './pages/Auth';
import Dashboard from './pages/Dashboard';
import Skills from './pages/Skills';
import Analysis from './pages/Analysis';
import Jobs from './pages/Jobs';
import Profile from './pages/Profile';
import './style.css';

const ProtectedRoute = ({ children }) => {
    return <div className="app-layout"><Navbar /><main className="main-content">{children}</main></div>;
};

function App() {
    return (
        <AuthProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Landing />} />
                    <Route path="/auth" element={<Auth />} />
                    <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
                    <Route path="/skills" element={<ProtectedRoute><Skills /></ProtectedRoute>} />
                    <Route path="/analysis" element={<ProtectedRoute><Analysis /></ProtectedRoute>} />
                    <Route path="/jobs" element={<ProtectedRoute><Jobs /></ProtectedRoute>} />
                    <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
                </Routes>
            </BrowserRouter>
        </AuthProvider>
    );
}

export default App;
