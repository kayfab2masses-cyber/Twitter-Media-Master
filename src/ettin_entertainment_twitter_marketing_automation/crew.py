import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool
)





@CrewBase
class EttinEntertainmentTwitterMarketingAutomationCrew:
    """EttinEntertainmentTwitterMarketingAutomation crew"""

    
    @agent
    def twitter_scout(self) -> Agent:
        
        return Agent(
            config=self.agents_config["twitter_scout"],
            
            
            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def brand_voice_writer(self) -> Agent:
        
        return Agent(
            config=self.agents_config["brand_voice_writer"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def daggerheart_rules_expert(self) -> Agent:
        
        return Agent(
            config=self.agents_config["daggerheart_rules_expert"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def social_media_publisher(self) -> Agent:
        
        return Agent(
            config=self.agents_config["social_media_publisher"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def monitor_ttrpg_community_trends(self) -> Task:
        return Task(
            config=self.tasks_config["monitor_ttrpg_community_trends"],
            markdown=False,
            
            
        )
    
    @task
    def draft_engaging_twitter_content(self) -> Task:
        return Task(
            config=self.tasks_config["draft_engaging_twitter_content"],
            markdown=False,
            
            
        )
    
    @task
    def validate_daggerheart_accuracy(self) -> Task:
        return Task(
            config=self.tasks_config["validate_daggerheart_accuracy"],
            markdown=False,
            
            
        )
    
    @task
    def optimize_and_schedule_posts(self) -> Task:
        return Task(
            config=self.tasks_config["optimize_and_schedule_posts"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the EttinEntertainmentTwitterMarketingAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
