import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import api from "../api/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const formData = new URLSearchParams();

      formData.append("username", email);
      formData.append("password", password);

      const res = await api.post("/auth/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      localStorage.setItem("token", res.data.access_token);

      const me = await api.get("/me");

      localStorage.setItem("role", me.data.role);

      if (me.data.role === "officer") navigate("/officer");
      else if (me.data.role === "collector") navigate("/collector");
      else navigate("/citizen");

    } catch (err) {
      console.error("Login failed:", err.response?.data || err);
      setError(
        err.response?.data?.detail || "Invalid email or password"
      );
    }
  };

  return (
    <div className="page">
      <div className="card">
        <h2>Log in to NammaVoice AI</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit">
            Log In
          </button>
          {error && (
            <p className="error-text">
              {error}
            </p>
          )}
        </form>
        <p className="switch-text">
          New here?{" "}
          <Link to="/signup">
            Create an account
          </Link>
        </p>
      </div>
    </div>
  );
}