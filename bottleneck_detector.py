# Bottleneck Detection Module
def find_bottlenecks(tasks):
    bottlenecks = []
    for task in tasks:
        if task['review_delay_days'] > 3:
            bottlenecks.append({
                "task": task['name'],
                "reason": "Review delay",
                "delay_days": task['review_delay_days']
            })
        if task['handoff_delay_days'] > 2:
            bottlenecks.append({
                "task": task['name'],
                "reason": "Handoff delay",
                "delay_days": task['handoff_delay_days']
            })
    return bottlenecks
