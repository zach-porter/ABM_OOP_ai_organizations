# visualize_results.py

import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_metrics(data_path='data/results.csv'):
    """
    Plots various metrics from the simulation data.
    """
    if not os.path.exists(data_path):
        print(f"Data file '{data_path}' not found.")
        return

    data = pd.read_csv(data_path)

    # Plot Average Knowledge Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(data["Step"], data["Average Knowledge"], label="Average Knowledge", color='blue')
    plt.xlabel("Time Steps")
    plt.ylabel("Average Knowledge")
    plt.title("Average Knowledge Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/average_knowledge_over_time.png')
    plt.show()

    # Plot AI Utilization Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(data["Step"], data["Positive Attitudes"], label="Positive Attitudes", color='green')
    plt.plot(data["Step"], data["Neutral Attitudes"], label="Neutral Attitudes", color='orange')
    plt.plot(data["Step"], data["Negative Attitudes"], label="Negative Attitudes", color='red')
    plt.xlabel("Time Steps")
    plt.ylabel("Number of Agents")
    plt.title("AI Utilization Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/ai_utilization_over_time.png')
    plt.show()

    # Plot AI Knowledge Contribution Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(data["Step"], data["AI Knowledge Contribution"], label="AI Knowledge Contribution", color='purple')
    plt.xlabel("Time Steps")
    plt.ylabel("AI Knowledge Contribution")
    plt.title("AI Knowledge Contribution Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/ai_contribution_over_time.png')
    plt.show()

    # Plot Network Centrality Over Time
    plt.figure(figsize=(12, 6))
    plt.plot(data["Step"], data["Network Centrality"], label="Average Network Centrality", color='brown')
    plt.xlabel("Time Steps")
    plt.ylabel("Average Degree Centrality")
    plt.title("Average Network Centrality Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/network_centrality_over_time.png')
    plt.show()

    # Advanced Analysis: Correlation between AI Knowledge Contribution and Average Knowledge
    plt.figure(figsize=(12, 6))
    plt.scatter(data["AI Knowledge Contribution"], data["Average Knowledge"], color='teal')
    plt.xlabel("AI Knowledge Contribution")
    plt.ylabel("Average Knowledge")
    plt.title("Correlation between AI Contribution and Average Knowledge")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/correlation_ai_knowledge_average_knowledge.png')
    plt.show()

    correlation = data["AI Knowledge Contribution"].corr(data["Average Knowledge"])
    print(f"Correlation between AI Knowledge Contribution and Average Knowledge: {correlation:.2f}")

    # Additional Plots can be added as needed

def main():
    plot_metrics()

if __name__ == "__main__":
    main()
