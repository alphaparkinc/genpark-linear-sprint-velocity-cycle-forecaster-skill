class LinearSprintVelocityCycleForecasterClient:
    def forecast_sprint_velocity(self, cycle_name='Cycle 42', planned_story_points=85, completed_points_past_3_cycles=[78, 82, 80]):
        avg_velocity = round(sum(completed_points_past_3_cycles) / len(completed_points_past_3_cycles), 1)
        confidence = round(min(1.0, avg_velocity / planned_story_points), 2)
        return {
            'forecast_id': 'spr_vlc_4412',
            'cycle_name': cycle_name,
            'planned_points': planned_story_points,
            'average_historical_velocity': avg_velocity,
            'completion_probability_pct': round(confidence * 100, 1),
            'scope_creep_alert': planned_story_points > (avg_velocity * 1.1),
            'recommended_point_trim': max(0, planned_story_points - int(avg_velocity)),
            'burndown_chart_url': 'https://productivity.developer.genpark.ai/linear/cycles/cycle42.svg'
        }
