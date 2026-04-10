import React, { useState, useEffect } from 'react';
import AnalyticsService from '../services/AnalyticsService';
import SummaryCard from './SummaryCard';
import EventChart from './EventChart';

const Dashboard = () => {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const data = await AnalyticsService.getSummary();
        setSummary(data);
      } catch (error) {
        console.error('Error fetching summary:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchSummary();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="dashboard">
      <div className="summary-cards">
        <SummaryCard title="Total Events" value={summary?.total_events || 0} />
        <SummaryCard title="Unique Users" value={summary?.unique_users || 0} />
      </div>
      <div className="charts">
        <EventChart data={summary?.event_types || {}} />
      </div>
    </div>
  );
};

export default Dashboard;