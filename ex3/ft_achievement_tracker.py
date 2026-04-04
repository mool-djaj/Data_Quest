import random

ALL_ACHIEVEMENTS: list[str] = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer', 'Hidden Path Finder'
]

def gen_player_achievements() -> set[str]:
    num_achievements: int = random.randint(6, 10)
    return set(random.sample(ALL_ACHIEVEMENTS, num_achievements))

def main() -> None:
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct: set[str] = alice.union(bob).union(charlie).union(dylan)
    print(f"\nAll distinct achievements: {all_distinct}")

    common: set[str] = alice.intersection(bob).intersection(charlie).intersection(dylan)
    print(f"Common achievements: {common}")

    print(f"Only Alice has: {alice.difference(bob.union(charlie).union(dylan))}")
    print(f"Only Bob has: {bob.difference(alice.union(charlie).union(dylan))}")
    print(f"Only Charlie has: {charlie.difference(alice.union(bob).union(dylan))}")
    print(f"Only Dylan has: {dylan.difference(alice.union(bob).union(charlie))}")

    print(f"Alice is missing: {all_distinct.difference(alice)}")
    print(f"Bob is missing: {all_distinct.difference(bob)}")
    print(f"Charlie is missing: {all_distinct.difference(charlie)}")
    print(f"Dylan is missing: {all_distinct.difference(dylan)}")

if __name__ == "__main__":
    main()