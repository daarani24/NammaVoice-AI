import { useState, useEffect } from "react";
import api from "../api/api";

export default function CollectorDashboard() {
  const [data, setData] = useState({ stats: {}, complaints: [] });
  const [error, setError] = useState("");

  const loadDashboard = async () => {
    try {
      const res = await api.get("/collector/dashboard");
      setData(res.data);
    // eslint-disable-next-line no-unused-vars
    } catch (err) {
      setError("Failed to load dashboard");
    }
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadDashboard();
  }, []);

  const { stats, complaints } = data;

  return (
    <div className="dashboard">
      <h2>District Dashboard</h2>
      {error && <p className="error-text">{error}</p>}

      <div className="stats-row">
        <div className="stat-box">
          <span className="stat-number">{stats.total ?? "-"}</span>
          <span className="stat-label">Total</span>
        </div>
        <div className="stat-box">
          <span className="stat-number">{stats.pending ?? "-"}</span>
          <span className="stat-label">Pending</span>
        </div>
        <div className="stat-box">
          <span className="stat-number">{stats.completed ?? "-"}</span>
          <span className="stat-label">Completed</span>
        </div>
      </div>

      <h2>All Complaints in District</h2>
      {complaints.length === 0 && <p>No complaints yet.</p>}
      {complaints.map((c) => (
        <div className="complaint-item" key={c.id}>
          <span>{c.title}</span>
          <span className="status-badge">{c.status}</span>
        </div>
      ))}
    </div>
  );
}