import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
    FileReadTool
)

# We no longer import PostToTwitterTool because we are not auto-posting.

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
            
            
            tools=[FileReadTool()],
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
    
    # We have removed the social_media_publisher agent
    

    
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
    
    # This is the new, final task from our tasks.yaml
    @task
    def validate_and_finalize_content(self) -> Task:
        return Task(
            config=self.tasks_config["validate_and_finalize_content"],
            markdown=False,
            
            
        )
    
    # We have removed the publishing task
    

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