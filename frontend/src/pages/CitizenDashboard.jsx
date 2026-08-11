import { useState, useEffect } from "react";
import api from "../api/api";

export default function CitizenDashboard() {
  const [complaints, setComplaints] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [districts, setDistricts] = useState([]);
  const [categories, setCategories] = useState([]);

  const [form, setForm] = useState({
    title: "",
    description: "",
    category_id: "",
    district_id: "",
    department_id: "",
  });

  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  const loadComplaints = async () => {
    try {
      const res = await api.get("/complaints/my");
      setComplaints(res.data);
    } catch (err) {
      console.error("Load complaints failed:", err);
    }
  };

  const loadReferenceData = async () => {
    try {
      const [departmentRes, districtRes, categoryRes] =
        await Promise.all([
          api.get("/reference/departments"),
          api.get("/reference/districts"),
          api.get("/reference/categories"),
        ]);

      setDepartments(departmentRes.data);
      setDistricts(districtRes.data);
      setCategories(categoryRes.data);

      setError("");
    } catch (err) {
      console.error("Failed to load reference data:", err);
      setError("Failed to load complaint options");
    }
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadComplaints();
    loadReferenceData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSubmitting(true);

    try {
      await api.post("/complaints/", {
        title: form.title,
        description: form.description,
        category_id: Number(form.category_id),
        district_id: Number(form.district_id),
        department_id: Number(form.department_id),
      });

      setForm({
        title: "",
        description: "",
        category_id: "",
        district_id: "",
        department_id: "",
      });

      await loadComplaints();
    } catch (err) {
      console.error(
        "Submit failed:",
        err.response?.data || err
      );

      setError(
        err.response?.data?.detail ||
        "Failed to submit complaint"
      );
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="citizen-page">

      {/* Header */}
      <header className="citizen-header">
        <div>
          <h1>NammaVoice AI</h1>
          <p>Citizen Portal</p>
        </div>

        <div className="citizen-user">
          <span>👤 Citizen</span>
        </div>
      </header>

      {/* Main Content */}
      <main className="citizen-container">

        {/* Welcome */}
        <section className="welcome-section">
          <h2>Report a Civic Issue</h2>
          <p>
            Help improve your community by reporting public issues.
          </p>
        </section>

        {/* Complaint Form */}
        <section className="complaint-card">

          <div className="card-heading">
            <h2>Submit a Complaint</h2>
            <p>Provide the details of the issue you want to report.</p>
          </div>

          <form onSubmit={handleSubmit}>

            {/* Title */}
            <div className="form-group">
              <label>Complaint Title</label>

              <input
                type="text"
                placeholder="Example: Pothole on Main Road"
                value={form.title}
                onChange={(e) =>
                  setForm({
                    ...form,
                    title: e.target.value,
                  })
                }
                required
              />
            </div>

            {/* Description */}
            <div className="form-group">
              <label>Description</label>

              <textarea
                placeholder="Describe the issue in detail..."
                value={form.description}
                onChange={(e) =>
                  setForm({
                    ...form,
                    description: e.target.value,
                  })
                }
                required
              />
            </div>

            {/* Dropdowns */}
            <div className="form-row">

              <div className="form-group">
                <label>Category</label>

                <select
                  value={form.category_id}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      category_id: e.target.value,
                    })
                  }
                  required
                >
                  <option value="">
                    Select Category
                  </option>

                  {categories.map((category) => (
                    <option
                      key={category.id}
                      value={category.id}
                    >
                      {category.name}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label>District</label>

                <select
                  value={form.district_id}
                  onChange={(e) =>
                    setForm({
                      ...form,
                      district_id: e.target.value,
                    })
                  }
                  required
                >
                  <option value="">
                    Select District
                  </option>

                  {districts.map((district) => (
                    <option
                      key={district.id}
                      value={district.id}
                    >
                      {district.name}
                    </option>
                  ))}
                </select>
              </div>

            </div>

            {/* Department */}
            <div className="form-group">
              <label>Department</label>

              <select
                value={form.department_id}
                onChange={(e) =>
                  setForm({
                    ...form,
                    department_id: e.target.value,
                  })
                }
                required
              >
                <option value="">
                  Select Department
                </option>

                {departments.map((department) => (
                  <option
                    key={department.id}
                    value={department.id}
                  >
                    {department.name}
                  </option>
                ))}
              </select>
            </div>

            {/* Error */}
            {error && (
              <div className="error-message">
                {error}
              </div>
            )}

            {/* Submit */}
            <button
              className="submit-button"
              type="submit"
              disabled={submitting}
            >
              {submitting
                ? "Submitting..."
                : "Submit Complaint"}
            </button>

          </form>
        </section>

        {/* Complaints */}
        <section className="my-complaints">

          <div className="section-heading">
            <div>
              <h2>My Complaints</h2>
              <p>Track the complaints you have submitted.</p>
            </div>

            <span className="complaint-count">
              {complaints.length}
            </span>
          </div>

          {complaints.length === 0 ? (
            <div className="empty-state">
              <div className="empty-icon">📋</div>
              <h3>No complaints yet</h3>
              <p>
                Your submitted complaints will appear here.
              </p>
            </div>
          ) : (
            <div className="complaint-list">

              {complaints.map((c) => (
                <div
                  className="complaint-item"
                  key={c.id}
                >
                  <div className="complaint-info">

                    <h3>{c.title}</h3>

                    <p>
                      Complaint #{c.id}
                    </p>

                  </div>

                  <span className="status-badge">
                    {c.status}
                  </span>
                </div>
              ))}

            </div>
          )}

        </section>

      </main>

    </div>
  );
}