
# Organization ABM with Generative AI
This project simulates the impact of generative AI on social dynamics and knowledge exchange within an organization using an Agent-Based Model (ABM). 
The model incorporates hierarchical and social networks, diverse agent behaviors, AI evolution, and dynamic network changes to provide insights into how AI influences workforce dynamics and organizational performance.

## Table of Contents
Project Overview
Features
Project Structure
Dependencies
Installation Instructions
Running the Simulation
Visualizing the Results
Key Parameters
Advanced Features
Future Enhancements
Contributing
License

## Project Overview
This ABM models how agents (employees) within an organization interact with each other and with a Generative AI system. The organizational structure is represented by a hierarchical network, while social interactions are captured via a small-world or scale-free network. Agents dynamically adjust their attitudes toward AI based on their experiences, and the generative AI evolves its knowledge contribution based on its usage.
The model also allows for dynamic network changes to simulate real-world organizational shifts, such as new social ties being formed or dissolved over time within the organization. In addition, various behavioral dynamics and advanced data analysis features are implemented to explore correlations between AI utilization and knowledge growth.

## Features
-Agents with Diverse Roles: Employees are assigned roles such as Managers, Specialists, and Staff, each influencing their interactions and behaviors.
-Generative AI Evolution: The AI system evolves its knowledge contribution based on agent usage patterns.
-Dynamic Networks: Social networks can change dynamically, simulating real-world organizational evolution.
-Knowledge Decay: Agents lose knowledge over time unless it's reinforced by interactions with other agents or AI.
-Behavioral Dynamics: Agents change their attitudes towards AI based on their knowledge gains or losses.
-Advanced Data Analysis: Includes metrics like network centrality, AI utilization, and correlations between AI contribution and knowledge growth.

## Dependencies
This project uses the following Python packages:
-NetworkX: For network creation and analysis
-Matplotlib: For plotting and visualizations
-Pandas: For data manipulation and analysis
Ensure you have Python 3.7 or higher installed.

## Running the Simulation
To run the simulation, execute the main.py file. This will initialize the model, visualize the organizational and social networks, and run the simulation for a specified number of steps (default is 100).
### Simulation Output
-Network Visualizations: Visualizes the organizational and social interaction networks at the start.
-Simulation Progress: Prints progress updates every 10 steps.
-Data Saving: Simulation results are saved in the data/results.csv file.

## Visualizing the Results
After running the simulation, use the visualize_results.py script to generate plots and analyze the collected data.
### Generated Plots
-Average Knowledge Over Time: Shows how knowledge evolves within the organization.
-AI Utilization Over Time: Displays the distribution of attitudes towards AI (Positive, Neutral, Negative).
-AI Knowledge Contribution Over Time: Illustrates how AI's contribution changes based on agent usage.
-Network Centrality Over Time: Tracks the average degree centrality of the social network over time.
-Correlation Between AI Contribution and Knowledge: Scatter plot showing the relationship between AI knowledge contribution and average knowledge.
Plots are saved in the data/ directory as PNG files.

## Key Parameters
You can adjust various parameters in the model by modifying the main.py file. Key parameters include:
-num_employees: Total number of employees (agents) in the organization.
-num_levels: Number of levels in the hierarchical organizational structure.
-span_of_control: Number of direct reports per manager.
-ai_contribution: Initial knowledge contribution of the AI.
-knowledge_decay_rate: Rate at which agents lose knowledge over time.
-dynamic_network: Enable or disable dynamic changes in the social network.
-network_change_frequency: Frequency of dynamic changes in the network.
-num_edges_change: Number of edges added or removed during network changes.
