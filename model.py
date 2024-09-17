# model.py

import random
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import os
from agents import EmployeeAgent, GenerativeAI
from networks import (
    create_hierarchical_network,
    create_onion_network,
    create_small_world_network,
    create_scale_free_network,
    add_random_edges,
    remove_random_edges
)

class OrganizationModel:
    """
    The main model representing the organization.
    """
    def __init__(self, 
                 num_employees=100, 
                 num_levels=5,  # Adjusted to 5 to include all agents
                 span_of_control=3,  # Adjusted to 3
                 org_network_type='hierarchical', 
                 social_network_type='small_world',
                 social_k=4, 
                 social_p=0.1, 
                 social_m=2,
                 ai_contribution=2.0,
                 knowledge_decay_rate=0.05,
                 ai_evolution_threshold=15,
                 ai_evolution_decrement_threshold=3,
                 ai_evolution_increment=0.5,
                 attitude_positive_threshold=0.5,
                 attitude_negative_threshold=-0.5,
                 dynamic_network=True,
                 network_change_frequency=10,
                 num_edges_change=5):
        """
        Initialize the organization model.

        Parameters:
            num_employees: Number of human agents
            num_levels: Number of hierarchical levels (for organizational networks)
            span_of_control: Number of direct reports per manager
            org_network_type: 'hierarchical' or 'onion'
            social_network_type: 'small_world' or 'scale_free'
            social_k: Parameter for social network (e.g., neighbors in small-world)
            social_p: Rewiring probability for small-world
            social_m: Parameter for scale-free network (number of edges to attach)
            ai_contribution: AI's initial knowledge contribution per interaction
            knowledge_decay_rate: Rate at which agents' knowledge decays each step
            ai_evolution_threshold: Usage count threshold to evolve AI
            ai_evolution_decrement_threshold: Usage count threshold to diminish AI
            ai_evolution_increment: Amount by which AI's contribution changes
            attitude_positive_threshold: Knowledge increase threshold to become more positive
            attitude_negative_threshold: Knowledge decrease threshold to become more negative
            dynamic_network: Boolean indicating if social network should change over time
            network_change_frequency: Steps between network changes
            num_edges_change: Number of edges to add/remove during each network change
        """
        self.num_employees = num_employees
        self.knowledge_decay_rate = knowledge_decay_rate
        self.ai_evolution_threshold = ai_evolution_threshold
        self.ai_evolution_decrement_threshold = ai_evolution_decrement_threshold
        self.ai_evolution_increment = ai_evolution_increment
        self.attitude_positive_threshold = attitude_positive_threshold
        self.attitude_negative_threshold = attitude_negative_threshold

        self.dynamic_network = dynamic_network
        self.network_change_frequency = network_change_frequency
        self.num_edges_change = num_edges_change
        self.current_step = 0

        # Create Organizational Network
        if org_network_type == 'hierarchical':
            self.org_network = create_hierarchical_network(num_levels, span_of_control)
        elif org_network_type == 'onion':
            self.org_network = create_onion_network(num_levels, span_of_control)
        else:
            raise ValueError("Unsupported organizational network type.")

        # Create Social Interaction Network
        total_agents = num_employees + 1  # +1 for AI agent
        if social_network_type == 'small_world':
            self.social_network = create_small_world_network(total_agents, social_k, social_p)
        elif social_network_type == 'scale_free':
            self.social_network = create_scale_free_network(total_agents, social_m)
        else:
            raise ValueError("Unsupported social network type.")

        # Initialize Generative AI Agent
        ai_unique_id = num_employees  # Assign last ID to AI
        self.ai_agent = GenerativeAI(ai_unique_id, ai_contribution)

        # Initialize Agents
        self.agents = []
        roles = ['Manager', 'Specialist', 'Staff']
        role_probabilities = [0.2, 0.3, 0.5]  # Adjust as needed

        for i in range(num_employees):
            role = self.assign_role(i, num_levels, span_of_control, roles, role_probabilities)
            expertise = random.uniform(1, 10)
            ai_attitude = self.assign_ai_attitude()
            agent = EmployeeAgent(i, role, expertise, ai_attitude)
            self.agents.append(agent)

        # Place AI agent
        self.agents.append(self.ai_agent)  # Index num_employees

        # Data Storage
        self.data = {
            "Step": [],
            "Average Knowledge": [],
            "Positive Attitudes": [],
            "Neutral Attitudes": [],
            "Negative Attitudes": [],
            "AI Knowledge Contribution": [],
            "Network Centrality": []
        }

        # Ensure data directory exists
        if not os.path.exists('data'):
            os.makedirs('data')

    def assign_role(self, agent_id, num_levels, span_of_control, roles, role_probs):
        """
        Assigns a role to an agent based on hierarchical level and predefined probabilities.
        """
        # Determine hierarchical level
        level = self.get_agent_level(agent_id)
        if level == 0:
            return 'CEO'
        else:
            role = random.choices(roles, weights=role_probs, k=1)[0]
            return role

    def get_agent_level(self, agent_id):
        """
        Determines the hierarchical level of an agent in the organizational network.
        """
        level = 0
        current_id = agent_id
        while True:
            predecessors = list(self.org_network.predecessors(current_id))
            if not predecessors:
                break
            current_id = predecessors[0]
            level += 1
        return level

    def assign_ai_attitude(self):
        """
        Assigns an initial attitude towards AI based on predefined probabilities.
        """
        r = random.random()
        if r < 0.5:
            return 'positive'
        elif r < 0.8:
            return 'neutral'
        else:
            return 'negative'

    def compute_average_knowledge(self):
        """
        Computes the average knowledge of all employees.
        """
        total_knowledge = sum(agent.knowledge for agent in self.agents 
                              if isinstance(agent, EmployeeAgent))
        return total_knowledge / self.num_employees

    def ai_utilization(self):
        """
        Calculates AI utilization based on agent attitudes.
        """
        positive = sum(1 for agent in self.agents 
                      if isinstance(agent, EmployeeAgent) and agent.ai_attitude == 'positive')
        neutral = sum(1 for agent in self.agents 
                     if isinstance(agent, EmployeeAgent) and agent.ai_attitude == 'neutral')
        negative = sum(1 for agent in self.agents 
                      if isinstance(agent, EmployeeAgent) and agent.ai_attitude == 'negative')
        return {
            "Positive": positive,
            "Neutral": neutral,
            "Negative": negative
        }

    def get_ai_contribution(self):
        """
        Retrieves the current knowledge contribution of the AI.
        """
        return self.ai_agent.knowledge_contribution

    def compute_network_centrality(self):
        """
        Computes centrality measures for the social network.
        """
        centrality = nx.degree_centrality(self.social_network)
        avg_centrality = sum(centrality.values()) / len(centrality)
        return avg_centrality

    def step(self):
        """
        Advances the model by one step.
        """
        self.current_step += 1

        # Agents interact with their networks
        for agent in self.agents:
            if isinstance(agent, EmployeeAgent):
                # Knowledge decay
                agent.knowledge = max(0, agent.knowledge - self.knowledge_decay_rate)

                # Interact with social network
                social_neighbors = list(self.social_network.neighbors(agent.unique_id))
                if social_neighbors:
                    partner_id = random.choice(social_neighbors)
                    partner = self.agents[partner_id]
                    agent.interact_with_agent(partner)

                # Interact with organizational network
                if agent.unique_id in self.org_network:
                    org_neighbors = list(self.org_network.neighbors(agent.unique_id))
                    if org_neighbors:
                        org_partner_id = random.choice(org_neighbors)
                        if org_partner_id < len(self.agents):  # Ensure within bounds
                            org_partner = self.agents[org_partner_id]
                            agent.interact_with_agent(org_partner)

                # Interact with Generative AI
                agent.interact_with_ai(self.ai_agent)

                # Update AI Attitude
                agent.update_ai_attitude(self)

        # AI evolves based on usage
        self.ai_agent.step(self)

        # Handle dynamic network changes
        if self.dynamic_network and self.current_step % self.network_change_frequency == 0:
            self.modify_social_network()

        # Collect Data
        self.collect_data()

    def modify_social_network(self):
        """
        Dynamically modifies the social network by adding/removing edges.
        """
        print(f"Modifying social network at step {self.current_step}...")
        # Decide randomly to add or remove edges
        action = random.choice(['add', 'remove'])
        if action == 'add':
            add_random_edges(self.social_network, self.num_edges_change)
            print(f"Added {self.num_edges_change} random edges.")
        elif action == 'remove':
            remove_random_edges(self.social_network, self.num_edges_change)
            print(f"Removed {self.num_edges_change} random edges.")

    def collect_data(self):
        """
        Collects data at the current step.
        """
        avg_knowledge = self.compute_average_knowledge()
        ai_util = self.ai_utilization()
        ai_contribution = self.get_ai_contribution()
        network_centrality = self.compute_network_centrality()

        self.data["Step"].append(self.current_step)
        self.data["Average Knowledge"].append(avg_knowledge)
        self.data["Positive Attitudes"].append(ai_util["Positive"])
        self.data["Neutral Attitudes"].append(ai_util["Neutral"])
        self.data["Negative Attitudes"].append(ai_util["Negative"])
        self.data["AI Knowledge Contribution"].append(ai_contribution)
        self.data["Network Centrality"].append(network_centrality)

    def run_model(self, n_steps=100):
        """
        Runs the model for a specified number of steps and saves the results.
        """
        for i in range(n_steps):
            self.step()
            if (i+1) % 10 == 0:
                print(f"Step {i+1} completed.")

        # Save data to CSV
        df = pd.DataFrame(self.data)
        df.to_csv('data/results.csv', index=False)
        print("Simulation completed. Results saved to 'data/results.csv'.")

    def visualize_networks(self):
        """
        Visualizes the organizational and social interaction networks.
        """
        # Organizational Network
        plt.figure(figsize=(12, 8))
        pos_org = nx.spring_layout(self.org_network.to_undirected(), seed=42)
        nx.draw(self.org_network.to_undirected(), pos=pos_org, with_labels=True, node_size=300, 
                node_color='lightblue', edge_color='gray', arrows=True)
        plt.title("Organizational Network")
        plt.show()

        # Social Interaction Network
        plt.figure(figsize=(12, 8))
        pos_social = nx.spring_layout(self.social_network, seed=42)
        nx.draw(self.social_network, pos=pos_social, with_labels=False, node_size=50, 
                node_color='lightgreen', edge_color='gray')
        plt.title("Social Interaction Network")
        plt.show()
