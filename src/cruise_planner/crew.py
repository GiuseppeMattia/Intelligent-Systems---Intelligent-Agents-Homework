from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CruisePlanner():
    """CruisePlanner crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    
    @agent
    def places_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['places_expert'], 
            verbose=True,
        )

    @agent
    def food_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['food_expert'], 
            verbose=True,
        )

    @agent
    def activities_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['activities_expert'], 
            verbose=True,
        )

    @agent
    def cruise_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['cruise_manager'], 
            verbose=True,
            max_iter=2
        )
    
    @agent
    def tourist_simulator(self) -> Agent:
        return Agent(
            config=self.agents_config['tourist_simulator'], 
            verbose=True
        )
    
    @agent
    def improvement_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['improvement_analyst'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def places_task(self) -> Task:
        return Task(
            config=self.tasks_config['places_task']
        )

    @task
    def food_task(self) -> Task:
        return Task(
            config=self.tasks_config['food_task']
        )

    @task
    def activities_task(self) -> Task:
        return Task(
            config=self.tasks_config['activities_task']
        )

    @task
    def plan_cruise_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_cruise_task'],
            output_file='reports/cruise_plan.md'
        )
    
    @task
    def simulate_feedback_task(self) -> Task:
        return Task(
            config=self.tasks_config['simulate_feedback_task'],
            output_file='reports/tourist_feedback.md'
        )
    
    @task
    def improvement_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['improvement_report_task'],
            output_file='reports/improvement_plan.md'
        )
    
    @task
    def refine_cruise_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['refine_cruise_plan_task'],
            output_file='reports/refined_cruise_plan.md'
        )

    # @crew
    # def crew(self) -> Crew:
    #     """Creates the CruisePlanner crew"""
    #     # To learn how to add knowledge sources to your crew, check out the documentation:
    #     # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            max_rpm=1,
        )
