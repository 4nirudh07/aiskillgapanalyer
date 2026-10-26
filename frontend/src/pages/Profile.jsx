import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { AuthContext } from '../context/AuthContext';
import { Save } from 'lucide-react';

const Profile = () => {
    const { user } = useContext(AuthContext);
    const [profile, setProfile] = useState({
        name: user?.name || '',
        email: user?.email || '',
        phone: '', location: '', education: '', degree: '',
        college: '', grad_year: '', experience_level: 'Entry Level',
        current_role: '', target_role: '', github: '', linkedin: '', portfolio: ''
    });
    const [roles, setRoles] = useState([]);
    const [saving, setSaving] = useState(false);
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/profile', {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        }).then(res => {
            if (Object.keys(res.data).length > 0) setProfile(prev => ({...prev, ...res.data}));
        });
        axios.get('http://127.0.0.1:8000/api/roles').then(res => setRoles(res.data.roles));
    }, []);

    const handleSave = async (e) => {
        e.preventDefault();
        setSaving(true);
        setMessage('');
        try {
            await axios.put('http://127.0.0.1:8000/api/profile', profile, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setMessage('Profile updated successfully!');
            setTimeout(() => setMessage(''), 3000);
        } catch (err) {
            console.error(err);
            setMessage('Failed to update profile.');
        } finally {
            setSaving(false);
        }
    };

    const handleChange = (e) => {
        setProfile({ ...profile, [e.target.name]: e.target.value });
    };

    return (
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
            <header className="mb-6">
                <h1>Professional Profile</h1>
                <p className="text-muted">Manage your personal and career details.</p>
            </header>

            <form onSubmit={handleSave} className="card">
                {message && (
                    <div style={{ padding: '12px', backgroundColor: message.includes('success') ? 'var(--success-bg)' : 'var(--error-bg)', color: message.includes('success') ? 'var(--success)' : 'var(--error)', borderRadius: '6px', marginBottom: '24px', fontSize: '14px' }}>
                        {message}
                    </div>
                )}
                
                <h3 className="mb-4" style={{ fontSize: '16px', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px' }}>Basic Info</h3>
                <div className="flex gap-4">
                    <div className="form-group flex-1">
                        <label className="form-label">Full Name</label>
                        <input className="form-input" type="text" name="name" value={profile.name} onChange={handleChange} required />
                    </div>
                    <div className="form-group flex-1">
                        <label className="form-label">Email</label>
                        <input className="form-input" type="email" name="email" value={profile.email} disabled style={{ backgroundColor: 'var(--bg-tertiary)' }} />
                        <span className="text-xs text-muted mt-1 inline-block">Email cannot be changed</span>
                    </div>
                </div>

                <div className="flex gap-4">
                    <div className="form-group flex-1">
                        <label className="form-label">Phone Number</label>
                        <input className="form-input" type="tel" name="phone" value={profile.phone} onChange={handleChange} />
                    </div>
                    <div className="form-group flex-1">
                        <label className="form-label">Location</label>
                        <input className="form-input" type="text" name="location" value={profile.location} onChange={handleChange} placeholder="City, Country" />
                    </div>
                </div>

                <h3 className="mb-4 mt-6" style={{ fontSize: '16px', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px' }}>Education & Experience</h3>
                <div className="flex gap-4">
                    <div className="form-group flex-1">
                        <label className="form-label">Degree</label>
                        <input className="form-input" type="text" name="degree" value={profile.degree} onChange={handleChange} placeholder="e.g. B.Tech" />
                    </div>
                    <div className="form-group flex-1">
                        <label className="form-label">College/University</label>
                        <input className="form-input" type="text" name="college" value={profile.college} onChange={handleChange} />
                    </div>
                    <div className="form-group" style={{width: '120px'}}>
                        <label className="form-label">Grad Year</label>
                        <input className="form-input" type="text" name="grad_year" value={profile.grad_year} onChange={handleChange} />
                    </div>
                </div>

                <div className="flex gap-4">
                    <div className="form-group flex-1">
                        <label className="form-label">Experience Level</label>
                        <select className="form-select" name="experience_level" value={profile.experience_level} onChange={handleChange}>
                            <option value="Student">Student</option>
                            <option value="Entry Level">Entry Level (0-2 years)</option>
                            <option value="Mid Level">Mid Level (3-5 years)</option>
                            <option value="Senior">Senior (5+ years)</option>
                        </select>
                    </div>
                    <div className="form-group flex-1">
                        <label className="form-label">Current Role</label>
                        <input className="form-input" type="text" name="current_role" value={profile.current_role} onChange={handleChange} />
                    </div>
                    <div className="form-group flex-1">
                        <label className="form-label">Target Role</label>
                        <select className="form-select" name="target_role" value={profile.target_role} onChange={handleChange}>
                            <option value="">Select Target Role</option>
                            {roles.map(r => <option key={r.role_id} value={r.title}>{r.title}</option>)}
                        </select>
                    </div>
                </div>

                <h3 className="mb-4 mt-6" style={{ fontSize: '16px', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px' }}>Links</h3>
                <div className="flex gap-4">
                    <div className="form-group flex-1">
                        <label className="form-label">GitHub Profile</label>
                        <input className="form-input" type="url" name="github" value={profile.github} onChange={handleChange} placeholder="https://github.com/username" />
                    </div>
                    <div className="form-group flex-1">
                        <label className="form-label">LinkedIn Profile</label>
                        <input className="form-input" type="url" name="linkedin" value={profile.linkedin} onChange={handleChange} placeholder="https://linkedin.com/in/username" />
                    </div>
                </div>
                
                <div className="mt-8 flex justify-end">
                    <button type="submit" className="btn btn-primary flex items-center gap-2" disabled={saving}>
                        <Save size={18} />
                        {saving ? 'Saving...' : 'Save Profile'}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default Profile;
