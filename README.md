How to Run Locally
1. Clone the Repository
Bash
git clone https://github.com/KhulileN/local-it-ops-agent.git
cd local-it-ops-agent
2. Configure Environment Variables
Duplicate the provided template and create your own configuration file:

Bash
cp .env.example .env
3. Install Dependencies
Ensure you have Python installed, then run:

Bash
pip install crewai python-dotenv
4. Initialize the Local LLM
Make sure Ollama is running on your machine, then pull and run the lightweight runtime engine in a separate terminal:

Bash
ollama run llama3.2:1b
5. Execute the Simulation
Run the core pipeline engine to witness the autonomous reasoning process stream directly to your terminal:

Bash
python agent.py
