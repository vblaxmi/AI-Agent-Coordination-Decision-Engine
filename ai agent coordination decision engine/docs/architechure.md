md
# Architecture

## Components

1. Coordinator Agent
   - Controls workflow execution

2. HR Agent
   - Workforce analysis

3. Finance Agent
   - Cost analysis

4. Operations Agent
   - Operational impact analysis

5. Decision Engine
   - Consolidates recommendations

## Flow

User Request
      ↓
Coordinator Agent
      ↓
 ┌──────────────┐
 │ HR Agent     │
 │ Finance Agent│
 │ Operations   │
 └──────────────┘
      ↓
Decision Engine
      ↓
Final Recommendation