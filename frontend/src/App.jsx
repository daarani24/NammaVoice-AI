import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import CitizenDashboard from "./pages/CitizenDashboard";
import OfficerDashboard from "./pages/OfficerDashboard";
import CollectorDashboard from "./pages/CollectorDashboard";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/citizen" element={<CitizenDashboard />} />
        <Route path="/officer" element={<OfficerDashboard />} />
        <Route path="/collector" element={<CollectorDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}