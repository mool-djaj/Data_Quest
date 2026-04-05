import random
from typing import Generator

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release", "use"]

def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))

def consume_event(event_list: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        idx: int = random.randint(0, len(event_list) - 1)
        item: tuple[str, str] = event_list.pop(idx)
        yield item

def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream: Generator[tuple[str, str], None, None] = gen_event()

    for i in range(1000):
        event: tuple[str, str] = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_events: list[tuple[str, str]] = []
    for i in range(10):
        list_events.append(next(stream))

    print(f"\nBuilt list of 10 events: {list_events}")

    for consumed in consume_event(list_events):
        print(f"Got event from list: {consumed}")
        print(f"Remains in list: {list_events}")

if __name__ == "__main__":
    main()