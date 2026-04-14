Product Definition

A Consistency-First Learning System that converts any course into a low-stress, habit-driven daily plan

🧱 1. Core Data Model (Product-Level, Not Technical)

Think in terms of entities and meaning, not tables.

🔹 Course

Represents a learning commitment.

Fields:

course_name
total_duration (e.g., 9 hours)
total_sessions (derived: 1 hr/session)
start_date
status → (active / completed / paused)
🔹 Session (Most Important Entity)

Represents a single day’s learning unit.

Fields:

session_number (1, 2, 3…)
scheduled_date
status:
PLANNED
COMPLETED
MISSED
duration (fixed: ≤ 1 hour)

👉 This is your habit unit

🔹 Daily Reflection

Represents thinking time (not consumption)

Fields:

date
duration (target: 30 mins)
status (done / skipped)
🔹 User Preferences

Defines lifestyle constraints

Fields:

preferred_study_hours (e.g., 7–10 PM)
weekend_availability (yes / limited / full)
max_sessions_per_day (default: 1 weekday, 2 weekend)
🧠 2. Core Policies (Your Product Brain)

These are non-negotiable rules that shape behavior.

🔥 Policy 1: Session Limit

No session should exceed 1 hour

Purpose:

Prevent fatigue
Make learning approachable
🔥 Policy 2: Daily Consistency

Default = 1 session per day

Purpose:

Build habit
Reduce decision fatigue
🔥 Policy 3: Gap Enforcement

Minimum 3-hour gap between sessions

Purpose:

Avoid binge learning
Improve retention

(MVP: mostly relevant when multiple sessions/day introduced later)

🔥 Policy 4: Reflection Rule

At least 30 mins/day for reflection

Purpose:

Convert input → understanding
Encourage active learning
🔥 Policy 5: Adaptive Rescheduling

If a session is missed → shift future sessions forward

Purpose:

Remove guilt
Preserve consistency
🔥 Policy 6: No Catch-Up Overload

Never assign multiple sessions to compensate for missed ones

Purpose:

Protect habit stability
Avoid burnout
⚙️ 3. Planning Engine (Behavior Logic)

This is your core system intelligence.

🔹 Step 1: Course → Sessions
Break course into 1-hour sessions
Example:
9-hour course → 9 sessions
🔹 Step 2: Session Distribution

Weekdays:

1 session/day

Weekends:

1–2 sessions (optional boost, not mandatory)
🔹 Step 3: Plan Output

System generates:

“You will complete this course in X days with a consistent pace”

🔹 Step 4: User Confirmation

User sees plan:

Accept ✅
Adjust 🔄

👉 Important: user feels in control

🧠 4. Behavior Design (This is your real strength)
🔹 Daily Experience

User opens app → sees:

1 session
1 reflection task

👉 No overload
👉 No decisions needed

🔹 After Session

System response:

Encourages stopping
Reinforces habit
🔹 If Missed

System response:

No punishment
Quiet reschedule
🔹 Messaging Tone
Supportive
Non-judgmental
Consistency-focused
⚠️ 5. Anti-Patterns (Strictly Avoid)

These will kill your product:

❌ Showing full course list daily
❌ Allowing binge completion
❌ Punishing missed days
❌ Over-complicated scheduling logic
❌ Too many notifications
📊 6. Success Metrics (Product Validation)

Track:

Daily consistency rate (% days user completes session)
Drop-off after 3 days
Completion rate of courses
Reflection completion rate (very important)
🔥 Final Product Identity

You are NOT building:

a course tracker

You ARE building:

a habit enforcement system for learning