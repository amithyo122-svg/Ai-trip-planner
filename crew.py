from crewai import Crew

from tasks.budget_task import budget_task
from tasks.front_agent_task import front_agent_task
from tasks.trip_task import planner_task

from agents.budget_analyst import budget_agent
from agents.itenary_planner import planner_agent
from agents.Travel_Researcher import travel_researcher

travel_crew = Crew(
    agents=[travel_researcher, budget_agent, planner_agent],
    tasks=[front_agent_task, budget_task, planner_task],
    verbose=True
)
