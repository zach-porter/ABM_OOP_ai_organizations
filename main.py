# main.py

from model import OrganizationModel

def main():
    # Initialize the model with desired parameters
    model = OrganizationModel(
        num_employees=100,         # Total number of employees
        num_levels=5,              # Increased to 5 to include all agents
        span_of_control=3,         # Decreased to 3
        org_network_type='hierarchical',  # 'hierarchical' or 'onion'
        social_network_type='small_world', # 'small_world' or 'scale_free'
        social_k=4,                # For small-world: number of neighbors
        social_p=0.1,              # For small-world: rewiring probability
        social_m=2,                # For scale-free: number of edges to attach
        ai_contribution=2.0,       # AI's initial knowledge contribution per interaction
        knowledge_decay_rate=0.05, # Knowledge decay rate per step
        ai_evolution_threshold=15, # AI evolves if used more than this threshold
        ai_evolution_decrement_threshold=3, # AI diminishes if used less than this threshold
        ai_evolution_increment=0.5, # Amount AI's contribution changes upon evolution
        attitude_positive_threshold=0.5, # Threshold to become more positive
        attitude_negative_threshold=-0.5, # Threshold to become more negative
        dynamic_network=True,      # Enable dynamic network changes
        network_change_frequency=10, # Steps between network changes
        num_edges_change=5          # Number of edges to add/remove during each network change
    )

    # Optionally, visualize the networks before running the model
    model.visualize_networks()

    # Run the model for a specified number of steps
    model.run_model(n_steps=100)

if __name__ == "__main__":
    main()
