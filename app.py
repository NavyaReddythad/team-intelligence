# Team Intelligence App
def get_productivity_score(tasks_completed, tasks_total):
    return (tasks_completed / tasks_total) * 100

def get_burnout_risk(after_hours_commits, avg_commits):
    if after_hours_commits > avg_commits * 0.5:
        return "HIGH"
    return "LOW"
