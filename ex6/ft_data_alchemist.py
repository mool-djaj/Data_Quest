import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma'
        'Gregory', 'john', 'kevin', 'Liam'
        ]
    print(f"Initial list of players: {players}")

    capitalized_all: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_all}")

    capitalized_only: list[str] = [
        name for name in players if name[0].isupper()
        ]
    print(f"New list of capitalized names only: {capitalized_only}")

    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in capitalized_all
        }
    print(f"Score dict: {score_dict}")

    total: int = sum(score_dict.values())
    count: int = len(score_dict)
    avg: float = round(total / count, 2)
    print(f"Score average is {avg}")

    high_scores: dict[str, int] = {
        name: score_dict[name] for name in score_dict if score_dict[name] > avg
        }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
