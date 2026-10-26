import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Target, AlertTriangle, CheckCircle, Bot } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

const Analysis = () => {
    const [roles, setRoles] = useState([]);
    const [selectedRole, setSelectedRole] = useState('');
    const [analysis, setAnalysis] = useState(null);
    const [loading, setLoading] = useState(false);
    const [rolesLoading, setRolesLoading] = useState(true);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/roles')
            .then(res => {
                setRoles(res.data.roles);
                if (res.data.roles.length > 0) setSelectedRole(res.data.roles[0].role_id);
                setRolesLoading(false);
            })
            .catch(console.error);
            
        axios.get('http://127.0.0.1:8000/api/skill-gap/latest', {
            headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
        })
            .then(res => {
                if(res.data) setAnalysis(res.data.result);
            }).catch(()=>{});
    }, []);

    const handleAnalyze = async () => {
        if (!selectedRole) return;
        setLoading(true);
        try {
            const res = await axios.post('http://127.0.0.1:8000/api/skill-gap/analyze', { target_role: selectedRole }, {
                headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
            });
            setAnalysis(res.data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <header className="mb-6">
                <h1>Skill Gap Analysis</h1>
                <p className="text-muted">Compare your skills against industry standards for your target role.</p>
            </header>

            <div className="card mb-6 flex flex-wrap items-center justify-between gap-4">
                <div className="flex items-center gap-4 flex-1 min-w-[300px]">
                    <label className="form-label" style={{ marginBottom: 0, whiteSpace: 'nowrap', fontWeight: '600' }}>Target Role:</label>
                    {rolesLoading ? (
                        <select className="form-select" disabled><option>Loading roles...</option></select>
                    ) : (
                        <select className="form-select" value={selectedRole} onChange={e => setSelectedRole(e.target.value)}>
                            {roles.map(r => <option key={r.role_id} value={r.role_id}>{r.title}</option>)}
                        </select>
                    )}
                </div>
                <button className="btn btn-primary flex items-center gap-2" onClick={handleAnalyze} disabled={loading || rolesLoading}>
                    <Target size={18} />
                    {loading ? 'Analyzing...' : 'Run Analysis'}
                </button>
            </div>

            {analysis && (
                <div>
                    <div className="grid grid-cols-3 mb-8">
                        <div className="card flex flex-col items-center justify-center text-center">
                            <div className="text-muted mb-2 text-sm" style={{ fontWeight: '500' }}>Overall Readiness</div>
                            <div style={{ fontSize: '48px', fontWeight: '700', color: 'var(--accent-primary)', marginBottom: '8px' }}>
                                {typeof analysis.readiness_score === 'number' ? analysis.readiness_score.toFixed(1) : parseFloat(analysis.readiness_score).toFixed(1)}%
                            </div>
                            <p className="text-xs text-muted">Based on importance and proficiency of required skills.</p>
                        </div>
                        
                        <div className="card" style={{ gridColumn: 'span 2' }}>
                            <h3 className="mb-4">Skill Match Overview</h3>
                            <div className="grid grid-cols-2 gap-8">
                                <div>
                                    <div className="flex items-center mb-4" style={{ color: 'var(--success)', fontWeight: '600' }}>
                                        <CheckCircle size={18} className="mr-2" style={{ marginRight: '8px' }}/> Matched ({analysis.matched_skills.length})
                                    </div>
                                    <div className="flex flex-wrap gap-2">
                                        {analysis.matched_skills.map(s => <span key={s} className="tag tag-success">{s}</span>)}
                                        {analysis.matched_skills.length === 0 && <span className="text-muted text-sm">None</span>}
                                    </div>
                                </div>
                                <div>
                                    <div className="flex items-center mb-4" style={{ color: 'var(--error)', fontWeight: '600' }}>
                                        <AlertTriangle size={18} className="mr-2" style={{ marginRight: '8px' }}/> Missing ({analysis.missing_skills.length})
                                    </div>
                                    <div className="flex flex-wrap gap-2">
                                        {analysis.missing_skills.map(s => <span key={s} className="tag tag-error">{s}</span>)}
                                        {analysis.missing_skills.length === 0 && <span className="text-muted text-sm">None</span>}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="flex items-center gap-2 mb-4">
                        <div style={{ backgroundColor: 'var(--accent-light)', color: 'var(--accent-primary)', padding: '8px', borderRadius: '8px' }}>
                            <Bot size={24} />
                        </div>
                        <h2 style={{ marginBottom: 0 }}>AI Skill Tester Final Report</h2>
                    </div>
                    
                    {analysis.markdown_report ? (
                        <div className="card markdown-body" style={{ padding: '30px', backgroundColor: 'var(--bg-secondary)', border: '1px solid var(--border-color)', borderRadius: '12px', lineHeight: '1.6', fontSize: '15px', color: 'var(--text-primary)', boxShadow: 'var(--shadow-sm)' }}>
                            <ReactMarkdown>{analysis.markdown_report}</ReactMarkdown>
                        </div>
                    ) : (
                        <div className="empty-state">
                            <CheckCircle size={48} style={{ color: 'var(--success)' }} className="empty-icon" />
                            <h3>Report Not Available</h3>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Analysis;
