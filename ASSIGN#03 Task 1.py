import hashlib
import time
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        # Combines block content into a single string for hashing
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    def create_genesis_block(self):
        # The first block in a chain (index 0)
        return Block(0, "Genesis Block", "0")
    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)
    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print(f"Prev Hash: {block.previous_hash}")
            print("-" * 30)
# --- Implementation & Demonstration ---
my_blockchain = Blockchain()
my_blockchain.add_block("Transaction: Alice pays Bob 10 BTC")
my_blockchain.add_block("Transaction: Bob pays Charlie 5 BTC")
my_blockchain.add_block("Transaction: Charlie pays David 2 BTC")
my_blockchain.add_block("Transaction: David pays Eve 1 BTC")
print("--- Original Blockchain ---")
my_blockchain.display_chain()
# Demonstrating Immortality/Integrity
print("\n[!] Attempting to modify Block 1...")
my_blockchain.chain[1].data = "HACKED: Alice pays Hacker 100 BTC"
# Recalculating the hash of the modified block
new_hash = my_blockchain.chain[1].calculate_hash()
print(f"Modified Block 1 Hash: {new_hash}")
print(f"Block 2's stored Previous Hash: {my_blockchain.chain[2].previous_hash}")
if new_hash != my_blockchain.chain[2].previous_hash:
    print("\nRESULT: The chain is BROKEN. The hash mismatch invalidates all subsequent blocks.")