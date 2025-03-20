import matplotlib.pyplot as plt

def visualize_time_usage(data):
    # Example: Simple bar chart representing time spent on tasks
    tasks = list(data.keys())
    time_spent = list(data.values())

    plt.bar(tasks, time_spent)
    plt.xlabel('Tasks')
    plt.ylabel('Time Spent (hours)')
    plt.title('Time Usage Visualization')
    plt.show()
