import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Briefcase, MapPin, DollarSign, Building } from 'lucide-react';

const Jobs = () => {
    const [jobs, setJobs] = useState([]);
    const [loading, setLoading] = useState(true);
    const [viewMode, setViewMode] = useState('recommended');

    const fetchJobs = async (mode) => {
        setLoading(true);
        try {
            if (mode === 'recommended') {
                const res = await axios.post('http://127.0.0.1:8000/api/jobs/recommended', {}, {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
                });
                setJobs(res.data.recommendations);
            } else {
                const res = await axios.get('http://127.0.0.1:8000/api/jobs');
                let allJobs = res.data.jobs;
                if (mode === 'trending') {
                    // Simulate trending jobs by taking top 4 most in-demand roles
                    allJobs = allJobs.slice(0, 4).map(j => ({ ...j, why_recommended: '🔥 High demand in the market right now!' }));
                }
                setJobs(allJobs);
            }
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchJobs(viewMode);
    }, [viewMode]);

    return (
        <div>
            <header className="flex justify-between items-center mb-6">
                <div>
                    <h1>Job Recommendations</h1>
                    <p className="text-muted">Jobs matched to your current skill profile.</p>
                </div>
                <div style={{ display: 'flex', gap: '8px', background: 'var(--bg-secondary)', padding: '4px', borderRadius: 'var(--border-radius-md)', border: '1px solid var(--border-color)' }}>
                    <button 
                        className="btn" 
                        style={{ background: viewMode === 'recommended' ? 'var(--bg-tertiary)' : 'transparent', border: 'none', color: viewMode === 'recommended' ? 'var(--text-primary)' : 'var(--text-secondary)' }}
                        onClick={() => setViewMode('recommended')}
                    >
                        For You
                    </button>
                    <button 
                        className="btn" 
                        style={{ background: viewMode === 'trending' ? 'var(--bg-tertiary)' : 'transparent', border: 'none', color: viewMode === 'trending' ? 'var(--text-primary)' : 'var(--text-secondary)' }}
                        onClick={() => setViewMode('trending')}
                    >
                        🔥 Trending Jobs
                    </button>
                    <button 
                        className="btn" 
                        style={{ background: viewMode === 'all' ? 'var(--bg-tertiary)' : 'transparent', border: 'none', color: viewMode === 'all' ? 'var(--text-primary)' : 'var(--text-secondary)' }}
                        onClick={() => setViewMode('all')}
                    >
                        All Jobs
                    </button>
                </div>
            </header>

            {loading ? (
                <div className="empty-state" style={{ border: 'none', height: '40vh' }}>Finding perfect matches...</div>
            ) : (
                <div className="grid grid-cols-2">
                    {jobs.map(job => (
                        <div key={job.job_id} className="card" style={{ display: 'flex', flexDirection: 'column' }}>
                            <div className="flex justify-between items-center mb-2">
                                <h3 style={{ fontSize: '18px', fontWeight: '600' }}>{job.title}</h3>
                                {job.match_percentage !== undefined && (
                                    <div className="tag tag-success" style={{ fontWeight: '600', fontSize: '14px' }}>
                                        {job.match_percentage}% match
                                    </div>
                                )}
                            </div>
                            
                            <div className="flex items-center text-muted text-sm mb-4">
                                <Building size={16} style={{ marginRight: '6px' }}/> {job.company}
                            </div>
                            
                            <div className="flex flex-wrap gap-4 mb-4 text-sm text-muted">
                                <div className="flex items-center"><MapPin size={14} style={{ marginRight: '6px' }}/> {job.location} ({job.work_mode})</div>
                                <div className="flex items-center"><Briefcase size={14} style={{ marginRight: '6px' }}/> {job.experience}</div>
                                {job.salary && <div className="flex items-center"><DollarSign size={14} style={{ marginRight: '6px' }}/> {job.salary}</div>}
                            </div>

                            {(viewMode === 'recommended' || viewMode === 'trending') && job.why_recommended && (
                                <div style={{ background: 'var(--bg-tertiary)', padding: '12px', borderRadius: 'var(--border-radius-md)', marginBottom: '16px', fontSize: '14px' }}>
                                    {job.why_recommended}
                                </div>
                            )}

                            <div className="mt-auto pt-4">
                                <h4 className="text-sm" style={{ fontWeight: '600', marginBottom: '8px' }}>Required Skills:</h4>
                                <div className="flex flex-wrap gap-2">
                                    {job.required_skills?.map(s => {
                                        let isMatched = false;
                                        if (viewMode === 'recommended' || viewMode === 'trending') {
                                            isMatched = job.matched_skills?.includes(s.toLowerCase?.() || s);
                                        }
                                        return (
                                            <span key={s} className={`tag ${(viewMode === 'recommended' || viewMode === 'trending') ? (isMatched ? 'tag-success' : 'tag-error') : ''}`}>
                                                {s}
                                            </span>
                                        );
                                    })}
                                </div>
                            </div>
                            
                            <button className="btn btn-secondary w-full mt-6">View Job Details</button>
                        </div>
                    ))}
                    
                    {jobs.length === 0 && (
                        <div className="empty-state" style={{ gridColumn: '1 / -1' }}>
                            <Briefcase size={48} className="empty-icon" />
                            <h3>No jobs found</h3>
                            <p className="text-muted">Try adding more skills to your profile.</p>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Jobs;
