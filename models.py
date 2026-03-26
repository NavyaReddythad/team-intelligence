# Data Models
class TeamMember:
    def __init__(self, name, role, team):
        self.name = name
        self.role = role
        self.team = team

class Task:
    def __init__(self, title, assignee, story_points, status):
        self.title = title
        self.assignee = assignee
        self.story_points = story_points
        self.status = status
