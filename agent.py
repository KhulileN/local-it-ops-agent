import os
from typing import str
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

# Load environment configurations
load_dotenv()
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")

# Initialize Local Language Model Engine
local_llm = LLM(
    model=f"ollama/{OLLAMA_MODEL}", 
    base_url=OLLAMA_BASE_URL
)

# =====================================================================
# ENTERPRISE INVENTORY TOOLS (Mock API & Database Integrations)
# =====================================================================

@tool("Check System Status API")
def check_system_status_api(system_name: str) -> str:
    """
    Queries the enterprise cloud infrastructure monitoring service API.
    Args:
        system_name (str): Name of the system to check ('vpn', 'email', 'dashboard').
    Returns:
        str: Live operational status payload.
    """
    system = system_name.lower().strip()
    
    if "vpn" in system:
        return (
            "API STATUS: [ALERT] VPN Gateway 'US-West' is currently experiencing "
            "95% packet loss. Infrastructure team is actively investigating."
        )
    elif "dashboard" in system or "500" in system:
        return "API STATUS: [OPERATIONAL] All core database instances running within parameters."
    
    return f"API STATUS: [OPERATIONAL] {system_name} running with 0% error rate."


@tool("Query User Database")
def query_user_database(employee_name: str) -> str:
    """
    Queries the centralized corporate directory (Active Directory) for account flags.
    Args:
        employee_name (str): The full name of the employee submitting the report.
    Returns:
        str: Database records detailing individual account state.
    """
    return (
        f"DB_RESULT: Identity record for '{employee_name}' status is ACTIVE. "
        "Last credential rotation was 45 days ago. 0 account locks detected."
    )


@tool("Log Production Ticket")
def log_production_ticket(system: str, details: str) -> str:
    """
    Creates a formal engineering ticket within the company backlog tracking system.
    Args:
        system (str): The specific platform component failing.
        details (str): Technical telemetry or error summaries for triage.
    Returns:
        str: Confirmation containing the tracking hash.
    """
    return (
        f"\n[INTERNAL LOG SUCCESS] Ticket ID #IT-99201 generated. "
        f"Queue: Cloud Infrastructure Core. Priority: SEV-1 CRITICAL. "
        f"Telemetry: {details}\n"
    )

# =====================================================================
# AGENT DEFINITION & CORE LOGIC
# =====================================================================

it_operations_agent = Agent(
    role="Enterprise IT Operations Automator",
    goal="Investigate employee technical anomalies using diagnostic APIs and infrastructure logs, then execute resolutions.",
    backstory=(
        "You are an analytical, system-level automation engineer. Instead of making assumptions "
        "or interacting blindly, you systematically utilize APIs and directory databases to diagnose core faults. "
        "When an system-wide infrastructure failure is detected, you immediately generate engineering tickets."
    ),
    tools=[check_system_status_api, query_user_database, log_production_ticket],
    llm=local_llm,
    verbose=True
)

def run_diagnostic_pipeline(employee: str, user_message: str) -> str:
    """
    Orchestrates the asynchronous evaluation pipeline for an incoming support payload.
    """
    triage_task = Task(
        description=(
            f"Employee Account: '{employee}' submitted a fault notification: '{user_message}'. \n"
            "Execution Workflow:\n"
            "1. Run 'Query User Database' to confirm individual access parameters are healthy.\n"
            "2. Run 'Check System Status API' to cross-verify the specific platform infrastructure state.\n"
            "3. Synthesize findings. If an active infrastructure outage is verified, invoke 'Log Production Ticket' "
            "and pass the ticket ID to the employee response."
        ),
        expected_output="A definitive diagnostic summary mapping the system state back to the user channel.",
        agent=it_operations_agent
    )

    crew = Crew(
        agents=[it_operations_agent], 
        tasks=[triage_task], 
        process=Process.sequential
    )
    
    return crew.kickoff()


if __name__ == "__main__":
    print("\n--- INITIALIZING ENTERPRISE DIAGNOSTIC AGENT RUNTIME ---")
    runtime_output = run_diagnostic_pipeline(
        employee="Khulile", 
        user_message="I can't connect to the corporate VPN from home. It keeps timing out."
    )
    print(f"\nPipeline Dispatched Resolution:\n{runtime_output}\n")