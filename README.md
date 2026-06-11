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
Install dependencies:

Bash
pip install crewai
Download and start Ollama in the background:

Bash
ollama run llama3.2:1b
Execute the simulation:

Bash
python agent.py

---

## 3. The "Next Step" Upgrade (To make it look even better)
If you want to take this repository from a "good learning project" to a "wow, this person can build production agent systems" project, add a **User Interface**.

Instead of running it strictly inside your terminal via `if __name__ == "__main__":`, you can install `streamlit` (`pip install streamlit`) and build a quick frontend chat screen in under 30 lines of code. 

Showing an agent operating behind a clean UI where a user can type a problem and watch the terminal logs output onto a beautiful web app dashboard is the ultimate portfolio builder.

Do you want to add a quick Streamlit web interface to this project before you upload it to GitHub?
