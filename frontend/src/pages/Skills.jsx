import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Plus, X, Upload } from 'lucide-react';

const Skills = () => {
    const [skills, setSkills] = useState([]);
    const [loading, setLoading] = useState(true);
    const [uploading, setUploading] = useState(false);
    const [newSkill, setNewSkill] = useState({ name: '', category: 'Programming', proficiency: 'Intermediate', years: 1 });
    const [error, setError] = useState('');

    const categories = ['Programming', 'Frontend', 'Backend', 'Database', 'Cloud', 'DevOps', 'Data Science', 'AI/ML', 'Soft Skills', 'Tools', 'Other'];
    const proficiencies = ['Beginner', 'Intermediate', 'Advanced', 'Expert'];

    const fetchSkills = async () => {
        try {
            const res = await axios.get('http://127.0.0.1:8000/api/skills', {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setSkills(res.data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => { fetchSkills(); }, []);

    const handleAdd = async (e) => {
        e.preventDefault();
        setError('');
        try {
            await axios.post('http://127.0.0.1:8000/api/skills', newSkill, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setNewSkill({ ...newSkill, name: '' });
            fetchSkills();
        } catch (err) {
            setError(err.response?.data?.detail || 'Failed to add skill');
        }
    };

    const handleDelete = async (name) => {
        try {
            await axios.delete(`http://127.0.0.1:8000/api/skills/${name}`, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            fetchSkills();
        } catch (err) {
            console.error(err);
        }
    };

    const handleFileUpload = async (e) => {
        const file = e.target.files[0];
        if (!file) return;
        setUploading(true);
        const formData = new FormData();
        formData.append('file', file);
        try {
            const res = await axios.post('http://127.0.0.1:8000/api/resume/skills', formData, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            const extracted = res.data.extracted_skills;
            if (extracted && extracted.length > 0) {
                for (const s of extracted) {
                    try {
                        await axios.post('http://127.0.0.1:8000/api/skills', { name: s, category: 'Other', proficiency: 'Beginner', years: 0 }, {
                            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
                        });
                    } catch (e) { }
                }
                fetchSkills();
            } else {
                setError('No recognized skills were found in this resume.');
            }
        } catch (err) {
            setError('Failed to process resume');
        } finally {
            setUploading(false);
            e.target.value = '';
        }
    };

    if (loading) return <div className="empty-state" style={{ height: '40vh', border: 'none' }}>Loading skills...</div>;

    return (
        <div>
            <header className="mb-6">
                <h1>My Skills</h1>
                <p className="text-muted">Manage your skills and proficiencies.</p>
            </header>

            <div className="grid grid-cols-3">
                <div className="card" style={{ gridColumn: 'span 1', height: 'fit-content' }}>
                    <h3 className="mb-4">Add New Skill</h3>
                    <form onSubmit={handleAdd}>
                        {error && <div style={{ padding: '12px', backgroundColor: 'var(--error-bg)', color: 'var(--error)', borderRadius: '6px', marginBottom: '16px', fontSize: '14px' }}>{error}</div>}
                        <div className="form-group">
                            <label className="form-label">Skill Name</label>
                            <input className="form-input" type="text" value={newSkill.name} onChange={e => setNewSkill({...newSkill, name: e.target.value})} required placeholder="e.g. React" />
                        </div>
                        <div className="form-group">
                            <label className="form-label">Category</label>
                            <select className="form-select" value={newSkill.category} onChange={e => setNewSkill({...newSkill, category: e.target.value})}>
                                {categories.map(c => <option key={c} value={c}>{c}</option>)}
                            </select>
                        </div>
                        <div className="form-group">
                            <label className="form-label">Proficiency</label>
                            <select className="form-select" value={newSkill.proficiency} onChange={e => setNewSkill({...newSkill, proficiency: e.target.value})}>
                                {proficiencies.map(p => <option key={p} value={p}>{p}</option>)}
                            </select>
                        </div>
                        <button type="submit" className="btn btn-primary w-full flex items-center justify-center gap-2"><Plus size={18} /> Add Skill</button>
                    </form>
                    
                    <div style={{ textAlign: 'center', margin: '24px 0', position: 'relative' }}>
                        <div style={{ position: 'absolute', top: '50%', left: 0, right: 0, borderTop: '1px solid var(--border-color)', zIndex: 1 }}></div>
                        <span style={{ position: 'relative', zIndex: 2, background: 'var(--bg-secondary)', padding: '0 12px', color: 'var(--text-tertiary)', fontSize: '12px', fontWeight: '500' }}>OR</span>
                    </div>
                    
                    <div>
                        <input type="file" id="resume" accept=".pdf,.docx,.txt" onChange={handleFileUpload} disabled={uploading} style={{ display: 'none' }} />
                        <label htmlFor="resume" className="btn btn-secondary w-full flex items-center justify-center gap-2" style={{ cursor: 'pointer' }}>
                            <Upload size={18} />
                            {uploading ? 'Extracting...' : 'Extract from Resume'}
                        </label>
                        <p className="text-muted text-xs mt-2 text-center">Upload PDF, DOCX or TXT</p>
                    </div>
                </div>

                <div className="card" style={{ gridColumn: 'span 2' }}>
                    <h3 className="mb-4">Your Skill Inventory ({skills.length})</h3>
                    {skills.length === 0 ? (
                        <div className="empty-state mt-4">
                            No skills added yet.
                        </div>
                    ) : (
                        <div className="grid grid-cols-2">
                            {skills.map(s => (
                                <div key={s.name} className="flex justify-between items-center" style={{ padding: '16px', border: '1px solid var(--border-color)', borderRadius: 'var(--border-radius-md)' }}>
                                    <div>
                                        <div style={{ fontWeight: '600', marginBottom: '4px' }}>{s.name}</div>
                                        <div className="text-xs text-muted">{s.category} • {s.proficiency}</div>
                                    </div>
                                    <button 
                                        className="btn" 
                                        onClick={() => handleDelete(s.name)}
                                        style={{ background: 'none', border: 'none', color: 'var(--text-tertiary)', cursor: 'pointer', padding: '4px' }}
                                    >
                                        <X size={18} />
                                    </button>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Skills;
