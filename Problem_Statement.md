# Problem Statement — NammaVoice AI

## 1. Title
NammaVoice AI – AI Powered Civic Governance Platform

## 2. Domain
Civic Tech / Governance / Public Infrastructure Management

## 3. User Types
1. Citizen
2. Ward/Department Officer
3. District Collector
4. Admin

## 4. Problem
Citizens report civic issues (potholes, garbage, water leaks, broken
streetlights) through scattered, disconnected channels — WhatsApp,
calls, social media, government offices. There is no single source of
truth, no way to track a complaint's status, and no visibility for
higher authorities until a manual inspection or report surfaces the
issue.

## 5. Solution
A single platform where a citizen reports an issue with a photo, GPS
location, and description. The complaint moves through a defined
lifecycle (Submitted → Verified → Under Action → Completed → Citizen
Verified → Closed), stays visible at every stage, and gives Collectors
a real-time dashboard instead of relying on manual reports.

## 6. Entities 
1. User
2. Complaint
3. Category
4. Department
5. District / Ward
6. ComplaintStatusHistory
7. ComplaintEvidence

## 7. User Roles 
- Citizen: submits complaints, uploads evidence, verifies resolution
- Officer: receives assigned complaints, updates status, uploads completion proof
- Collector: views district-wide dashboard, monitors pending/completed complaints
- Admin: manages users, officers, and districts

## 8. Success Criteria
- A citizen can submit a complaint end-to-end and see its live status
- An officer can pick up, act on, and close a complaint with evidence
- A Collector dashboard reflects real complaint counts (total/pending/completed)
- The complaint lifecycle is fully auditable via status history

## 9. Out of Scope (for MVP — Day 1–41)
- All AI features (image classification, duplicate detection, priority
  prediction, etc.) — deferred to Specialization phase, Day 42–59
- RBAC granularity beyond 4 basic roles, audit logs, notifications,
  caching, CI/CD, monitoring — deferred to post-capstone roadmap
- Admin module UI — backend model only for now if time is short

## 10. Track
Python (FastAPI + PostgreSQL + SQLAlchemy)