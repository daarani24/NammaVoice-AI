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
- GitHub Actions CI pipeline (runs tests on every push and pull request)
- Backend deployed to Render
- Frontend deployed to Vercel
- Database on Neon (PostgreSQL, cloud-hosted)
- `/health` monitoring endpoint
- CORS locked to production frontend URL

## Review III — Day 60
- AI enhancement: automatic complaint category prediction and priority prediction (High, Medium, Low)
- Synthetic dataset generator (`ML/generate_data.py`) with a configurable dataset size
- Model training script (`ML/train.py`) using TF-IDF and Logistic Regression
- ML prediction service (`ml_service.py`) called automatically when a complaint is submitted
- Three new columns on the Complaint table: `predicted_category`, `priority`, `confidence_score` (Alembic migration)
- Officer dashboard shows complaints in priority order
- Unit tests for the ML service and for complaint submission with the model mocked
- `Enhancement_Proposal.md` explaining the problem, approach, and tech choices
- Architecture diagram updated with the ML service
- README v3 with the ML section, setup steps, and comparison details

### Changed
- CI pipeline now generates the dataset and trains the models before running tests
- Render build command now trains the models during every deploy
- Photo upload moved into the complaint submission form, so one complaint has one photo

### Fixed
- Folder name casing (`ML`) now matches between the local disk, GitHub, CI, and Render