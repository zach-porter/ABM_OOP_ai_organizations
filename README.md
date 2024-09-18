
# Organization ABM with Generative AI
This project simulates the impact of generative AI on social dynamics and knowledge exchange within an organization using an Agent-Based Model (ABM). <br />
The model incorporates hierarchical and social networks, diverse agent behaviors, AI evolution, and dynamic network changes to provide insights into how AI influences workforce dynamics and organizational performance.

## Table of Contents
Project Overview <br />
Features<br />
Project Structure<br />
Dependencies<br />
Installation Instructions<br />
Running the Simulation<br />
Visualizing the Results<br />
Key Parameters<br />
Advanced Features<br />
Future Enhancements<br />
Contributing<br />
License<br />

## Project Overview
This ABM models how agents (employees) within an organization interact with each other and with a Generative AI system. The organizational structure is represented by a hierarchical network, while social interactions are captured via a small-world or scale-free network. Agents dynamically adjust their attitudes toward AI based on their experiences, and the generative AI evolves its knowledge contribution based on its usage.<br />
The model also allows for dynamic network changes to simulate real-world organizational shifts, such as new social ties being formed or dissolved over time within the organization. In addition, various behavioral dynamics and advanced data analysis features are implemented to explore correlations between AI utilization and knowledge growth.

## Features
-Agents with Diverse Roles: Employees are assigned roles such as Managers, Specialists, and Staff, each influencing their interactions and behaviors.<br />
-Generative AI Evolution: The AI system evolves its knowledge contribution based on agent usage patterns.<br />
-Dynamic Networks: Social networks can change dynamically, simulating real-world organizational evolution.<br />
-Knowledge Decay: Agents lose knowledge over time unless it's reinforced by interactions with other agents or AI.<br />
-Behavioral Dynamics: Agents change their attitudes towards AI based on their knowledge gains or losses.<br />
-Advanced Data Analysis: Includes metrics like network centrality, AI utilization, and correlations between AI contribution and knowledge growth.<br />

## Dependencies
This project uses the following Python packages:<br />
-NetworkX: For network creation and analysis<br />
-Matplotlib: For plotting and visualizations<br />
-Pandas: For data manipulation and analysis<br />
Ensure you have Python 3.7 or higher installed.<br />

## Running the Simulation
To run the simulation, execute the main.py file. This will initialize the model, visualize the organizational and social networks, and run the simulation for a specified number of steps (default is 100).<br />
### Simulation Output
-Network Visualizations: Visualizes the organizational and social interaction networks at the start.<br />
-Simulation Progress: Prints progress updates every 10 steps.<br />
-Data Saving: Simulation results are saved in the data/results.csv file.<br />

## Visualizing the Results
After running the simulation, use the visualize_results.py script to generate plots and analyze the collected data.<br />
### Generated Plots
-Average Knowledge Over Time: Shows how knowledge evolves within the organization.<br />
-AI Utilization Over Time: Displays the distribution of attitudes towards AI (Positive, Neutral, Negative).<br />
-AI Knowledge Contribution Over Time: Illustrates how AI's contribution changes based on agent usage.<br />
-Network Centrality Over Time: Tracks the average degree centrality of the social network over time.<br />
-Correlation Between AI Contribution and Knowledge: Scatter plot showing the relationship between AI knowledge contribution and average knowledge.<br />
Plots are saved in the data/ directory as PNG files.<br />

## Key Parameters
You can adjust various parameters in the model by modifying the main.py file. Key parameters include:<br />
-num_employees: Total number of employees (agents) in the organization.<br />
-num_levels: Number of levels in the hierarchical organizational structure.<br />
-span_of_control: Number of direct reports per manager.<br />
-ai_contribution: Initial knowledge contribution of the AI.<br />
-knowledge_decay_rate: Rate at which agents lose knowledge over time.<br />
-dynamic_network: Enable or disable dynamic changes in the social network.<br />
-network_change_frequency: Frequency of dynamic changes in the network.<br />
-num_edges_change: Number of edges added or removed during network changes.<br />
