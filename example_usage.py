from client import LinearSprintVelocityCycleForecasterClient

def main():
    client = LinearSprintVelocityCycleForecasterClient()
    res = client.forecast_sprint_velocity()
    print('Sprint Velocity Forecaster: ' + res['forecast_id'] + ' (' + res['cycle_name'] + ')')
    print('Avg Velocity: ' + str(res['average_historical_velocity']) + ' | Prob: ' + str(res['completion_probability_pct']) + '%')
    print('Chart URL: ' + res['burndown_chart_url'])

if __name__ == '__main__':
    main()
