# Changelog

## Review I — Day 11
- Problem statement finalized
- Architecture, ER, and Class diagrams (v1)
- Auth module: signup, login, JWT
- Citizen module: submit complaint, view own complaints
- Officer module: department pool, accept complaint, update status

## Review II — Day 41
- Collector module: district dashboard with complaint stats
- Admin module: user listing with role-based access guard
- Evidence upload via Cloudinary (citizen initial photo)
- Citizen verification and closure step
- Unit tests for auth, complaint, collector, and admin services
- GitHub Actions CI pipeline (runs tests on every push/PR)
- Backend deployed to Render
- Frontend deployed to Vercel
- Database on Neon (PostgreSQL, cloud-hosted)
- `/health` monitoring endpoint
- CORS locked to production frontend URL