import time

reminders = []

def set_deadline_reminder(task, remind_time):
    # Example: Just stores reminders in a list for demonstration
    reminders.append((task, remind_time))
    print(f'Reminder set for task: {task} at {remind_time}')

    # Dummy implementation to demonstrate waiting for reminder
    time_to_wait = remind_time - time.time()
    if time_to_wait > 0:
        time.sleep(time_to_wait)
    print(f'Reminder: Time to complete task - {task}')
