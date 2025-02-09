from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

@CrewBase
class CodeExecutionCrew():
	"""CodeExecution crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def coding_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['coding_agent'],
			tools=[CodeInterpreterTool(unsafe_mode=True)],
			# allow_code_execution=True,
			verbose=True
		)

	@task
	def data_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_analysis_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CodeExecution crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
