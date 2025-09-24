import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

NUM_ROWS = 1000

# === Generate Affiliates Data ===
affiliates_data = []
for i in range(1, NUM_ROWS + 1):
    created_at = fake.date_time_between(start_date='-2y', end_date='now', tzinfo=None)
    affiliates_data.append({
        'id': i,
        'code': fake.unique.pystr(min_chars=6, max_chars=8).upper(),
        'origin': random.choice(['YouTube', 'Discord', 'X', 'Twitch', None]),
        'redeemed_at': created_at + timedelta(minutes=random.randint(1, 60))
    })
affiliates_df = pd.DataFrame(affiliates_data)

# === Generate Players Data ===
players_data = []
for i in range(1, NUM_ROWS + 1):
    created_at = fake.date_time_between(start_date='-2y', end_date='now', tzinfo=None)
    is_kyc = random.choice([True, True, True, False]) # 75% chance of being KYC approved
    
    affiliate_id = random.choice([None] + list(affiliates_df['id'].sample(frac=0.5)))

    players_data.append({
        'id': i,
        'country_code': fake.country_code(),
        'affiliate_id': affiliate_id,
        'is_kyc_approved': is_kyc,
        'created_at': created_at,
        'updated_at': created_at + timedelta(days=random.randint(1, 30))
    })
players_df = pd.DataFrame(players_data)

kyc_approved_players = players_df[players_df['is_kyc_approved'] == True]

# --- Generate Transactions Data ---
transactions_data = []
for i in range(1, NUM_ROWS + 1):
    player_row = kyc_approved_players.sample(1).iloc[0]
    player_id = player_row['id']
    player_updated_at = player_row['updated_at']

    transactions_data.append({
        'id': i,
        'timestamp': fake.date_time_between(start_date=player_updated_at, end_date='now', tzinfo=None),
        'player_id': player_id,
        'type': random.choice(['Deposit', 'Withdraw']),
        'amount': round(random.uniform(10.0, 1000.0), 2)
    })
transactions_df = pd.DataFrame(transactions_data)


# === Save to CSV ===
affiliates_df.to_csv('affiliates.csv', index=False)
players_df.to_csv('players.csv', index=False)
transactions_df.to_csv('transactions.csv', index=False)

print(f"Generated {NUM_ROWS} rows for each table.")
print("\nAffiliates Head:")
print(affiliates_df.head())
print("\nPlayers Head:")
print(players_df.head())
print("\nTransactions Head:")
print(transactions_df.head())