
def schedule_tasks(tasks):
    # Sort tasks based on priority (assuming task is a tuple (priority, task_name))
    # Higher number indicates higher priority
    tasks.sort(reverse=True, key=lambda x: x[0])
    print('Scheduled tasks:')
    for priority, task in tasks:
        print(f'{task} (Priority: {priority})')
    return [task for priority, task in tasks]
