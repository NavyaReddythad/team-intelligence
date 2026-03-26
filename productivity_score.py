# Productivity Scoring Module
def calculate_team_productivity(members):
    scores = []
    for member in members:
        score = (
            member['tasks_completed'] * 10 +
            member['pr_merged'] * 5 -
            member['rework_count'] * 3
        )
        scores.append({"member": member['name'], "score": score})
    return sorted(scores, key=lambda x: x['score'], reverse=True)
