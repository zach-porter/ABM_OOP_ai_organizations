# agents.py

import random

class GenerativeAI:
    """
    Represents the Generative AI system within the organization.
    It evolves its knowledge contribution based on usage.
    """
    def __init__(self, unique_id, initial_contribution=2.0):
        self.unique_id = unique_id
        self.knowledge_contribution = initial_contribution
        self.usage_count = 0

    def step(self, model):
        """
        Evolution logic: Increase or decrease contribution based on usage.
        """
        if self.usage_count > model.ai_evolution_threshold:
            self.knowledge_contribution += model.ai_evolution_increment
            self.usage_count = 0  # Reset after evolution
            print(f"AI evolved! New knowledge contribution: {self.knowledge_contribution}")
        elif self.usage_count < model.ai_evolution_decrement_threshold:
            self.knowledge_contribution = max(0.5, self.knowledge_contribution - model.ai_evolution_increment)
            self.usage_count = 0  # Reset after diminution
            print(f"AI diminished! New knowledge contribution: {self.knowledge_contribution}")
        # Reset usage count for the next step
        self.usage_count = 0

    def provide_information(self):
        """
        Provides knowledge to an agent and increments usage count.
        """
        self.usage_count += 1
        return self.knowledge_contribution


class EmployeeAgent:
    """
    Represents an employee within the organization.
    Agents can have different roles and exhibit behavioral dynamics.
    """
    def __init__(self, unique_id, role, expertise, ai_attitude):
        self.unique_id = unique_id
        self.role = role  # e.g., Manager, Specialist, Staff
        self.expertise = expertise  # Expertise level (1-10)
        self.ai_attitude = ai_attitude  # 'positive', 'neutral', 'negative'
        self.knowledge = expertise  # Initialize knowledge base
        self.behavior_modifier = self.set_behavior_modifier()

    def set_behavior_modifier(self):
        """
        Sets a modifier based on the agent's role to influence interactions.
        """
        if self.role == 'Manager':
            return 1.2
        elif self.role == 'Specialist':
            return 1.0
        else:  # Staff
            return 0.8

    def interact_with_agent(self, partner):
        """
        Exchange information with another agent by averaging knowledge,
        adjusted by role-based behavior modifiers.
        """
        if isinstance(partner, EmployeeAgent):
            avg_knowledge = (self.knowledge + partner.knowledge) / 2
            self.knowledge = avg_knowledge * self.behavior_modifier
            partner.knowledge = avg_knowledge * partner.behavior_modifier

    def interact_with_ai(self, ai_agent):
        """
        Interact with the AI agent based on attitude.
        """
        if self.ai_attitude == 'positive':
            self.knowledge += ai_agent.provide_information()
        elif self.ai_attitude == 'neutral':
            self.knowledge += ai_agent.provide_information() * 0.5
        elif self.ai_attitude == 'negative':
            self.knowledge += ai_agent.provide_information() * 0.2

    def update_ai_attitude(self, model):
        """
        Update the agent's attitude towards AI based on recent interactions.
        """
        # Simple rule: If knowledge increases significantly, become more positive; else, become more negative
        knowledge_change = self.knowledge - self.expertise
        if knowledge_change > model.attitude_positive_threshold:
            if self.ai_attitude == 'neutral':
                self.ai_attitude = 'positive'
            elif self.ai_attitude == 'negative':
                self.ai_attitude = 'neutral'
        elif knowledge_change < model.attitude_negative_threshold:
            if self.ai_attitude == 'neutral':
                self.ai_attitude = 'negative'
            elif self.ai_attitude == 'positive':
                self.ai_attitude = 'neutral'
