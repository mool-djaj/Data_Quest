import sys

def main() -> None:
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}

    print("=== Inventory System Analysis ===")
    for arg in args:
        parts: list[str] = arg.split(":")
        if len(parts) != 2:
            print(f"Error invalid parameter '{arg}'")
            continue
            
        item: str = parts[0]
        qty_str: str = parts[1]

        if item in inventory.keys():
            print(f"Redundant item '{item}' discarding")
            continue

        try:
            qty: int = int(qty_str)
            inventory[item] = qty
        except ValueError:
            print(f"Quantity error for '{item}': invalid literal for int() with base 10: '{qty_str}'")

    print(f"Got inventory: {inventory}")
    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    if total_qty > 0:
        most_abundant: str = item_list[0]
        least_abundant: str = item_list[0]
        
        for item in item_list:
            qty = inventory[item]
            pct: float = round((qty / total_qty) * 100, 1)
            print(f"Item {item} represents {pct}%")
            
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item
            if inventory[item] < inventory[least_abundant]:
                least_abundant = item

        print(f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}")
        print(f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()