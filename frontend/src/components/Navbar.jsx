import React, { useContext } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';
import { Triangle, LogOut } from 'lucide-react';

const Navbar = () => {
    const { logout } = useContext(AuthContext);
    const location = useLocation();

    const isActive = (path) => location.pathname === path ? 'active' : '';

    return (
        <nav className="navbar">
            <Link to="/dashboard" className="nav-brand">
                <Triangle size={20} fill="currentColor" />
                <span>SkillGap</span>
            </Link>
            
            <div className="nav-links">
                <Link to="/dashboard" className={`nav-link ${isActive('/dashboard')}`}>Dashboard</Link>
                <Link to="/skills" className={`nav-link ${isActive('/skills')}`}>My Skills</Link>
                <Link to="/analysis" className={`nav-link ${isActive('/analysis')}`}>Skill Gap</Link>
                <Link to="/jobs" className={`nav-link ${isActive('/jobs')}`}>Jobs</Link>
                <Link to="/profile" className={`nav-link ${isActive('/profile')}`}>Profile</Link>
                <button 
                    onClick={logout} 
                    className="nav-link flex items-center gap-2" 
                    style={{ background: 'none', border: 'none', cursor: 'pointer' }}
                >
                    <LogOut size={16} /> Logout
                </button>
            </div>
        </nav>
    );
};

export default Navbar;
