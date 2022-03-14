import csv
import random
import sys

# Numero de simulações
N = 1000

def main():

  if len(sys.argv) != 2:
    sys.exit("Digite: python tournament.py FILENAME.csv")

  teams = []
  with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    next(file)
    for row in reader:
      teams.append({"name": row[0], "rating": int(row[1])})

  counts = {}
  for i in range(1000):
    winner = simulate_tournament(teams)
    counts[winner] = counts[winner] + 1 if winner in counts else 1

  for team in sorted(counts, key=lambda team: counts[team], reverse=True):
    print(f"{team}: {counts[team] * 100 / N:.1f}% chance de ganhar")


def simulate_game(team1, team2):
  """Simulate a game. Return True if team1 wins, False otherwise."""
  rating1 = team1["rating"]
  rating2 = team2["rating"]
  probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
  return random.random() < probability

def simulate_round(teams):
  """Simulate a round. Return a list of winning teams."""
  winners = []

  for i in range(0, len(teams), 2):
    if simulate_game(teams[i], teams[i + 1]):
      winners.append(teams[i])
    else:
      winners.append(teams[i + 1])

  return winners

def simulate_tournament(teams):
  """Simulate a tournament. Return name of winning team."""
  
  winners = teams
  while (True):
    winners = simulate_round(winners)
    if len(winners) == 1:
      return winners[0]["name"]

if __name__ == "__main__":
  main()
