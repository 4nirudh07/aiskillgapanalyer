import React from 'react';
import { Link } from 'react-router-dom';
import { Triangle, Target, Briefcase, Activity, ArrowRight } from 'lucide-react';

const Landing = () => {
    return (
        <div className="app-layout">
            <nav className="navbar">
                <div className="nav-brand">
                    <Triangle size={20} fill="currentColor" />
                    <span>SkillGap</span>
                </div>
                <div className="nav-links">
                    <Link to="/dashboard" className="btn btn-primary">Enter App</Link>
                </div>
            </nav>

            <main className="main-content" style={{ maxWidth: '1000px', textAlign: 'center', paddingTop: '100px' }}>
                <div style={{ marginBottom: '64px' }}>
                    <h1 style={{ fontSize: '48px', fontWeight: '800', letterSpacing: '-0.04em', lineHeight: '1.1', marginBottom: '24px' }}>
                        Know what you know.<br />
                        <span style={{ color: 'var(--text-tertiary)' }}>Know what you're missing.</span><br />
                        Build the skills that get you hired.
                    </h1>
                    
                    <p style={{ fontSize: '18px', color: 'var(--text-secondary)', maxWidth: '600px', margin: '0 auto 40px', lineHeight: '1.6' }}>
                        Analyze your current skills against industry requirements, calculate your skill gap, 
                        and get actionable recommendations to land your target role.
                    </p>
                    
                    <Link to="/dashboard" className="btn btn-primary flex items-center gap-2 mx-auto" style={{ padding: '12px 24px', fontSize: '16px', display: 'inline-flex' }}>
                        Start Your Analysis <ArrowRight size={18} />
                    </Link>
                </div>

                <div className="grid grid-cols-3" style={{ textAlign: 'left', marginTop: '100px' }}>
                    <div className="card">
                        <div style={{ marginBottom: '16px', color: 'var(--accent-primary)' }}><Activity size={24} /></div>
                        <h3>Smart Analysis</h3>
                        <p className="text-sm">Compare your skills against real-world job requirements with exact matching.</p>
                    </div>
                    <div className="card">
                        <div style={{ marginBottom: '16px', color: 'var(--accent-primary)' }}><Target size={24} /></div>
                        <h3>Targeted Roadmaps</h3>
                        <p className="text-sm">Get priority-based learning paths for the exact skills you are missing.</p>
                    </div>
                    <div className="card">
                        <div style={{ marginBottom: '16px', color: 'var(--accent-primary)' }}><Briefcase size={24} /></div>
                        <h3>Intelligent Matches</h3>
                        <p className="text-sm">Find jobs that actually match your profile, with clear explanations of why.</p>
                    </div>
                </div>
            </main>

            <footer style={{ padding: '40px', textAlign: 'center', color: 'var(--text-tertiary)', fontSize: '14px', borderTop: '1px solid var(--border-color)' }}>
                <p>&copy; {new Date().getFullYear()} SkillGap. AI Skill Gap & Job Recommendation System.</p>
            </footer>
        </div>
    );
};

export default Landing;
