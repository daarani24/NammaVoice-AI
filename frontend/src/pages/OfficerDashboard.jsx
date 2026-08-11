import { useState, useEffect } from "react";
import api from "../api/api";

export default function OfficerDashboard() {
  const [pool, setPool] = useState([]);

  const loadPool = async () => {
    const res = await api.get("/officer/pool");
    setPool(res.data);
  };

  // eslint-disable-next-line react-hooks/set-state-in-effect
  useEffect(() => { loadPool(); }, []);

  const accept = async (id) => {
    await api.post(`/officer/${id}/accept`);
    loadPool();
  };

  const markCompleted = async (id) => {
    await api.patch(`/officer/${id}/status`, { status: "completed" });
    loadPool();
  };

  return (
    <div>
      <h2>Department Complaint Pool</h2>
      <ul>
        {pool.map((c) => (
          <li key={c.id}>
            {c.title} — {c.status}
            <button onClick={() => accept(c.id)}>Accept</button>
            <button onClick={() => markCompleted(c.id)}>Mark Completed</button>
          </li>
        ))}
      </ul>
    </div>
  );
}