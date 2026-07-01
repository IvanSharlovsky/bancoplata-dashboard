import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Настройки
np.random.seed(42)
n_issues = 500
teams = ['PAYMENTS', 'MOBILE', 'BACKEND', 'DATA']
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 6, 30)

# Генерация данных
data = []
for i in range(n_issues):
    created = start_date + timedelta(days=np.random.randint(0, 540))
    cycle_time = np.random.exponential(7)  # среднее ~7 дней
    resolved = created + timedelta(days=int(cycle_time))
    
    # У 5% задач — аномально долгий цикл (>30 дней)
    if np.random.random() < 0.05:
        resolved = created + timedelta(days=np.random.randint(30, 90))
    
    data.append({
        'issue_id': f'ISS-{i+1:04d}',
        'team': random.choice(teams),
        'created': created.strftime('%Y-%m-%d'),
        'resolved': resolved.strftime('%Y-%m-%d'),
        'cycle_time_days': (resolved - created).days,
        'priority': random.choice(['High', 'Medium', 'Low'])
    })

# Сохранение
df = pd.DataFrame(data)
df.to_csv('engineering_delivery_data.csv', index=False)
print("✅ Датасет сохранён как 'engineering_delivery_data.csv'")