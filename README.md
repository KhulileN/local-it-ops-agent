# Local Enterprise IT Support AI Agent

An autonomous, local AI agent built using **CrewAI** and **Ollama (Llama 3.2)** designed to triage IT support issues, query live mock database architectures, and autonomously escalate infrastructure outages to engineering teams.

## 🚀 How It Works
Unlike traditional linear automation, this project utilizes an agentic reasoning loop. The agent evaluates an incoming user complaint and dynamically decides which tools to call based on live diagnostic data.

[User Message]
│
▼
[AI Agent Core] ──► 1. Queries Active Directory DB (Verifies account status)
│
├──► 2. Queries Infrastructure API (Checks for system outages)
│
└──► 3. Logic Branch: Resolves issue OR executes Jira/Zendesk Ticket Escalation


## 🛠️ Tech Stack & Architecture
* **Framework:** CrewAI
* **LLM Engine:** Ollama (Running `llama3.2:1b` locally)
* **Language:** Python 3.13+

## 🔧 Features Demonstrated
1. **Autonomous Tool Routing:** The agent determines whether an issue is isolated to a single user or is part of a broader system outage by combining multiple tool inputs.
2. **Local Embedding-Free Architecture:** Custom lightweight Python decorators (`@tool`) to interface with local services without requiring external cloud API dependencies.
3. **Strict Enterprise Persona Guardrails:** The agent limits its operational scope strictly to technical diagnostic data parsing.

## 🏃‍♂️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/KhulileN/local-it-ops-agent.git](https://github.com/KhulileN/local-it-ops-agent.git)
   cd your-repo-name

2. Configure Environment Variables
Duplicate the provided .env.example template and create your own configuration file:

Bash
cp .env.example .env
(Alternatively, manually create a .env file in the root directory ensuring OLLAMA_BASE_URL and OLLAMA_MODEL point to your local service instance).

3. Install Dependencies
Ensure you have Python installed, then run:

pip install crewai python-dotenv

4. Initialize the Local LLM
Make sure Ollama is running on your machine, then pull and run the lightweight runtime engine in a separate terminal:

ollama run llama3.2:1b

5. Execute the Simulation
Run the core pipeline engine to witness the autonomous reasoning process stream directly to your terminal:

python agent.py

📊 Sample Execution Logic Flow
When a user passes an ambiguous complaint like "I can't connect to the corporate VPN from home," the local runner will orchestrate the following:

Step 1: Invokes Query User Database to verify if the individual profile is active or locked in Active Directory.

Step 2: Invokes Check System Status API to dynamically query live cloud gateway routing metrics.

Step 3: Detects network telemetry faults (e.g., 95% packet loss on US-West gateway) and automatically runs Log Production Ticket to inject a high-priority ticket tracking index into the DevOps dashboard backlog.

