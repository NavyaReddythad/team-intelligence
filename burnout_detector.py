# Burnout Detection Module
def detect_burnout(after_hours_activity, backlog_size, productivity_trend):
    risk_score = 0
    if after_hours_activity > 10:
        risk_score += 3
    if backlog_size > 20:
        risk_score += 2
    if productivity_trend == "declining":
        risk_score += 3
    if risk_score >= 6:
        return "HIGH RISK"
    elif risk_score >= 3:
        return "MEDIUM RISK"
    return "LOW RISK"
