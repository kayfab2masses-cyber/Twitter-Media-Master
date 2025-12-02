#!/usr/bin/env python
import sys
from ettin_entertainment_twitter_marketing_automation.crew import EttinEntertainmentTwitterMarketingAutomationCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'target_community': 'Daggerheart, Critical Role, TTRPG, DnD, Pathfinder, Tabletop Gaming',
        'product_focus': 'The Christmas Tree\'ty One-Shot Adventure ($1.99 Holiday Sale)',
        'company_name': 'Ettin Entertainment',
        'product_knowledge_file': 'knowledge/products.json'
    }
    EttinEntertainmentTwitterMarketingAutomationCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'target_community': 'Daggerheart, Critical Role, TTRPG',
        'product_focus': 'The Christmas Tree\'ty One-Shot Adventure',
        'company_name': 'Ettin Entertainment',
        'product_knowledge_file': 'knowledge/products.json'
    }
    try:
        EttinEntertainmentTwitterMarketingAutomationCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default to run if no arguments provided, for easier usage
        run()
    else:
        command = sys.argv[1]
        if command == "run":
            run()
        elif command == "train":
            train()
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)