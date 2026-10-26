import React, { useState, useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';
import { AuthContext } from '../context/AuthContext';
import { Triangle } from 'lucide-react';

const Auth = () => {
    const [isLogin, setIsLogin] = useState(true);
    const [formData, setFormData] = useState({ name: '', email: '', password: '' });
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            if (isLogin) {
                const params = new URLSearchParams();
                params.append('username', formData.email);
                params.append('password', formData.password);
                
                const res = await axios.post('http://127.0.0.1:8000/api/auth/login', params);
                login(res.data.access_token);
                navigate('/dashboard');
            } else {
                await axios.post('http://127.0.0.1:8000/api/auth/register', {
                    name: formData.name,
                    email: formData.email,
                    password: formData.password
                });
                
                const params = new URLSearchParams();
                params.append('username', formData.email);
                params.append('password', formData.password);
                
                const res = await axios.post('http://127.0.0.1:8000/api/auth/login', params);
                login(res.data.access_token);
                navigate('/profile');
            }
        } catch (err) {
            setError(err.response?.data?.detail || 'An error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="auth-container" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Link to="/" style={{ color: 'var(--text-primary)', marginBottom: '32px' }}>
                <Triangle size={32} fill="currentColor" />
            </Link>
            <div className="card" style={{ width: '100%' }}>
                <div style={{ textAlign: 'center', marginBottom: '24px' }}>
                    <h2 style={{ fontSize: '24px', fontWeight: '600' }}>{isLogin ? 'Welcome back' : 'Create an account'}</h2>
                    <p className="text-muted mt-2">{isLogin ? 'Enter your details to access your dashboard.' : 'Start analyzing your skill gaps today.'}</p>
                </div>
                
                <form onSubmit={handleSubmit}>
                    {error && <div style={{ padding: '12px', backgroundColor: 'var(--error-bg)', color: 'var(--error)', borderRadius: '6px', marginBottom: '16px', fontSize: '14px' }}>{error}</div>}
                    
                    {!isLogin && (
                        <div className="form-group">
                            <label className="form-label">Full Name</label>
                            <input 
                                className="form-input"
                                type="text" 
                                value={formData.name} 
                                onChange={(e) => setFormData({...formData, name: e.target.value})}
                                required={!isLogin}
                                placeholder="John Doe"
                            />
                        </div>
                    )}
                    
                    <div className="form-group">
                        <label className="form-label">Email Address</label>
                        <input 
                            className="form-input"
                            type="email" 
                            value={formData.email} 
                            onChange={(e) => setFormData({...formData, email: e.target.value})}
                            required
                            placeholder="you@example.com"
                        />
                    </div>
                    
                    <div className="form-group">
                        <label className="form-label">Password</label>
                        <input 
                            className="form-input"
                            type="password" 
                            value={formData.password} 
                            onChange={(e) => setFormData({...formData, password: e.target.value})}
                            required
                            placeholder="••••••••"
                        />
                    </div>
                    
                    <button type="submit" className="btn btn-primary w-full mt-4" disabled={loading} style={{ padding: '10px' }}>
                        {loading ? 'Please wait...' : (isLogin ? 'Log in' : 'Create account')}
                    </button>
                </form>
                
                <div style={{ marginTop: '24px', textAlign: 'center', fontSize: '14px' }}>
                    <p className="text-muted">
                        {isLogin ? "Don't have an account? " : "Already have an account? "}
                        <button 
                            type="button" 
                            onClick={() => setIsLogin(!isLogin)}
                            style={{ background: 'none', border: 'none', color: 'var(--accent-primary)', fontWeight: '500', cursor: 'pointer' }}
                        >
                            {isLogin ? 'Sign up' : 'Log in'}
                        </button>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Auth;
