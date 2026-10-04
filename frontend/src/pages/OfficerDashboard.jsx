import { useState, useEffect } from "react";
import api from "../api/api";

export default function OfficerDashboard() {
  const [pool, setPool] = useState([]);

  const loadPool = async () => {
    const res = await api.get("/officer/pool");
    setPool(res.data);
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadPool();
  }, []);

  const accept = async (id) => {
    await api.post(`/officer/${id}/accept`);
    loadPool();
  };

  const markCompleted = async (id) => {
    await api.patch(`/officer/${id}/status`, { status: "completed" });
    loadPool();
  };

  const priorityOrder = {
    high: 0,
    medium: 1,
    low: 2,
  };

  const sortedPool = [...pool].sort(
    (a, b) =>
      (priorityOrder[a.priority] ?? 3) -
      (priorityOrder[b.priority] ?? 3)
  );

  return (
    <div>
      <h2>Department Complaint Pool</h2>

      <ul>
        {sortedPool.map((c) => (
          <li key={c.id}>
            <strong>{c.title}</strong> — {c.status}

            <br />
            Priority: {c.priority || "Not assigned"}
            <br />

            {c.predicted_category && (
              <>
                AI Category: {c.predicted_category}
                <br />
              </>
            )}

            {c.confidence_score !== null &&
              c.confidence_score !== undefined && (
                <>
                  AI Confidence:{" "}
                  {(c.confidence_score * 100).toFixed(0)}%
                  <br />
                </>
              )}

            <button onClick={() => accept(c.id)}>
              Accept
            </button>

            <button onClick={() => markCompleted(c.id)}>
              Mark Completed
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}