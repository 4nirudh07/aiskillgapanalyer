import React, { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import { AuthContext } from '../context/AuthContext';
import { Link } from 'react-router-dom';
import { Target, CheckCircle, AlertCircle, ArrowRight } from 'lucide-react';
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

const Dashboard = () => {
    const { user } = useContext(AuthContext);
    const [stats, setStats] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchDashboard = async () => {
            try {
                const profileRes = await axios.get('http://127.0.0.1:8000/api/profile', {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
                });
                const skillsRes = await axios.get('http://127.0.0.1:8000/api/skills', {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
                });
                const analysisRes = await axios.get('http://127.0.0.1:8000/api/skill-gap/latest', {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
                });
                const recsRes = await axios.post('http://127.0.0.1:8000/api/jobs/recommended', {}, {
                    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
                });

                setStats({
                    profile: profileRes.data,
                    skills: skillsRes.data,
                    analysis: analysisRes.data,
                    recs: recsRes.data.recommendations.slice(0, 3)
                });
            } catch (err) {
                console.error(err);
            } finally {
                setLoading(false);
            }
        };
        fetchDashboard();
    }, []);

    if (loading) return <div className="empty-state" style={{ height: '50vh', border: 'none' }}>Loading dashboard...</div>;

    const hasSkills = stats?.skills?.length > 0;
    const hasAnalysis = !!stats?.analysis;

    const chartData = stats?.analysis?.result?.partially_matched_skills?.map(s => ({
        name: s.skill,
        Current: s.current === 'Beginner' ? 25 : s.current === 'Intermediate' ? 50 : s.current === 'Advanced' ? 75 : 100,
        Required: s.required === 'Beginner' ? 25 : s.required === 'Intermediate' ? 50 : s.required === 'Advanced' ? 75 : 100,
    })) || [];

    return (
        <div>
            <div className="flex justify-between items-center mb-6">
                <div>
                    <h1>Good morning, {user?.name}</h1>
                    <p className="text-muted">Target role: {stats?.profile?.target_role || 'Not set'}</p>
                </div>
            </div>

            {!hasSkills ? (
                <div className="empty-state">
                    <Target size={48} className="empty-icon" />
                    <h3>No skills added yet</h3>
                    <p className="mb-4">Add your skills to calculate your career readiness.</p>
                    <Link to="/skills" className="btn btn-primary">Add skills</Link>
                </div>
            ) : (
                <div className="grid grid-cols-3 mb-6">
                    <div className="card">
                        <h3 className="text-muted text-sm" style={{ fontWeight: '500' }}>Readiness Score</h3>
                        <div style={{ fontSize: '36px', fontWeight: '700', marginTop: '8px', color: 'var(--text-primary)' }}>
                            {hasAnalysis ? `${stats.analysis.result.readiness_score}%` : 'N/A'}
                        </div>
                        <p className="text-muted text-sm mt-2">{hasAnalysis ? `For ${stats.analysis.target_role}` : 'Run analysis first'}</p>
                        {!hasAnalysis && <Link to="/analysis" className="btn btn-secondary mt-4 w-full">Run Analysis</Link>}
                    </div>

                    <div className="card">
                        <div className="flex justify-between items-center mb-2">
                            <h3 className="text-muted text-sm" style={{ fontWeight: '500' }}>Matched Skills</h3>
                            <CheckCircle size={20} style={{ color: 'var(--success)' }} />
                        </div>
                        <div style={{ fontSize: '36px', fontWeight: '700', color: 'var(--text-primary)' }}>
                            {hasAnalysis ? stats.analysis.result.matched_skills.length : 0}
                        </div>
                    </div>

                    <div className="card">
                        <div className="flex justify-between items-center mb-2">
                            <h3 className="text-muted text-sm" style={{ fontWeight: '500' }}>Missing Skills</h3>
                            <AlertCircle size={20} style={{ color: 'var(--warning)' }} />
                        </div>
                        <div style={{ fontSize: '36px', fontWeight: '700', color: 'var(--text-primary)' }}>
                            {hasAnalysis ? stats.analysis.result.missing_skills.length : 0}
                        </div>
                    </div>
                </div>
            )}

            {hasAnalysis && (
                <div className="grid grid-cols-2">
                    {chartData.length > 0 && (
                        <div className="card">
                            <h3 className="mb-4">Skill Proficiency Gap</h3>
                            <div style={{ width: '100%', height: 250 }}>
                                <ResponsiveContainer>
                                    <BarChart data={chartData} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
                                        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--border-color)" />
                                        <XAxis dataKey="name" tick={{ fontSize: 12, fill: 'var(--text-secondary)' }} />
                                        <YAxis tick={{ fontSize: 12, fill: 'var(--text-secondary)' }} />
                                        <Tooltip contentStyle={{ borderRadius: '8px', border: '1px solid var(--border-color)' }} />
                                        <Bar dataKey="Current" fill="var(--accent-primary)" radius={[4, 4, 0, 0]} />
                                        <Bar dataKey="Required" fill="var(--border-color)" radius={[4, 4, 0, 0]} />
                                    </BarChart>
                                </ResponsiveContainer>
                            </div>
                        </div>
                    )}

                    <div className="card">
                        <div className="flex justify-between items-center mb-4">
                            <h3>Top Recommended Jobs</h3>
                            <Link to="/jobs" className="flex items-center gap-2 text-sm" style={{ color: 'var(--accent-primary)' }}>
                                View all <ArrowRight size={16} />
                            </Link>
                        </div>
                        <div className="flex flex-col gap-4">
                            {stats?.recs?.map(job => (
                                <div key={job.job_id} className="flex justify-between items-center" style={{ paddingBottom: '16px', borderBottom: '1px solid var(--border-color)' }}>
                                    <div>
                                        <h4 style={{ fontWeight: '600', fontSize: '15px' }}>{job.title}</h4>
                                        <span className="text-muted text-sm">{job.company} • {job.location}</span>
                                    </div>
                                    <div className="tag tag-success" style={{ fontWeight: '600' }}>{job.match_percentage}% Match</div>
                                </div>
                            ))}
                            {stats?.recs?.length === 0 && <p className="text-muted text-sm">No recommendations found. Try adding more skills.</p>}
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Dashboard;
