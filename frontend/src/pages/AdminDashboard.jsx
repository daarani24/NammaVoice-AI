import { useState, useEffect } from "react";
import api from "../api/api";

export default function AdminDashboard() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    api.get("/admin/users")
      .then((res) => setUsers(res.data))
      .catch(() => setError("Failed to load users"));
  }, []);

  return (
    <div className="dashboard">
      <h2>All Users</h2>
      {error && <p className="error-text">{error}</p>}
      {users.map((u) => (
        <div className="complaint-item" key={u.id}>
          <span>{u.name} ({u.email})</span>
          <span className="status-badge">{u.role}</span>
        </div>
      ))}
    </div>
  );
}