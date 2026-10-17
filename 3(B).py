def save_all(inv_file='inventory.txt', txn_file='distributions.txt'):
    with open(inv_file, 'w') as f:
        for code, info in inventory.items():
            f.write(f"{code},{info['name']},{info['stock']}\n")
    with open(txn_file, 'w') as f:
        for t in transactions:
            f.write(f"{t['code']},{t['qty']},{t['remaining']}\n")
 
def load_inventory(inv_file='inventory.txt'):
    global inventory
    inventory = {}
    try:
        with open(inv_file) as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    continue
                try:
                    stock = int(parts[2])
                    if stock < 0:
                        continue
                    inventory[parts[0]] = {'name': parts[1], 'stock': stock}
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
