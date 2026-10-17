inventory = {
    'F001': {'name': 'Food Packages', 'stock': 250},
    'B001': {'name': 'Blankets', 'stock': 120},
    'W001': {'name': 'Water Containers', 'stock': 300},
    'M001': {'name': 'Medical Kits', 'stock': 80}
}
transactions = []
 
def display_inventory():
    print('\nCURRENT INVENTORY')
    for code, info in inventory.items():
        print(f"{code}: {info['name']} – {info['stock']} units")
 
def distribute(item_code, qty):
    if item_code not in inventory:
        return False, 'Unknown item code'
    try:
        qty = int(qty)
    except (TypeError, ValueError):
        return False, 'Quantity must be an integer'
    if qty <= 0:
        return False, 'Quantity must be positive'
    if qty > inventory[item_code]['stock']:
        return False, 'Insufficient stock'
    # only update after all checks have passed
    inventory[item_code]['stock'] -= qty
    transactions.append({
        'code': item_code,
        'qty': qty,
        'remaining': inventory[item_code]['stock']
    })
    return True, 'Distribution successful'
