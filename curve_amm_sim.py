import math

def calculate_invariant(x, y, A):
    # Simplified invariant for demonstration, similar to Curve's concept
    # For a 2-asset pool, it's often x + y = constant or a more complex form.
    # Here, we use a simplified constant product like AMM but with a scaling factor.
    return x * y

def get_amount_out(x_in, x_total, y_total, A):
    """
    Calculates the amount of y that can be received for x_in amount of x.
    This is a simplified representation of Curve's AMM logic.
    """
    # In a real Curve pool, this involves a complex invariant function and Newton's method.
    # For this demo, we'll use a simplified proportional swap.
    # The core idea is that the invariant must be maintained (or adjusted by A).
    
    # Simplified: if we add x_in, the new x_total is x_total + x_in.
    # We need to find the new y_total such that the invariant holds.
    # new_x_total * new_y_total = invariant
    # (x_total + x_in) * new_y_total = x_total * y_total
    # new_y_total = (x_total * y_total) / (x_total + x_in)
    # y_out = y_total - new_y_total
    
    # This is a very basic approximation. Real Curve uses a more sophisticated invariant.
    # The 'A' parameter in Curve helps to keep the invariant constant for stablecoins.
    # For this simulation, we'll ignore 'A' for simplicity and focus on the swap mechanics.
    
    if x_in <= 0:
        return 0
    
    # Calculate the new total amount of x after the deposit
    new_x_total = x_total + x_in
    
    # Calculate the new total amount of y that would maintain the invariant
    # Using the simplified constant product invariant: x * y = invariant
    # invariant = x_total * y_total
    # new_y_total = invariant / new_x_total
    # y_out = y_total - new_y_total
    
    # A more direct calculation for y_out:
    # x_total * y_total = (x_total + x_in) * (y_total - y_out)
    # y_total = (x_total + x_in) * y_total / y_total - (x_total + x_in) * y_out / y_total
    # y_total * y_total = (x_total + x_in) * y_total - (x_total + x_in) * y_out
    # (x_total + x_in) * y_out = (x_total + x_in) * y_total - y_total * y_total
    # y_out = y_total - (y_total * y_total) / (x_total + x_in)
    
    # A common formula derived from invariant: y_out = y_total - (x_total * y_total) / (x_total + x_in)
    # This is still a simplification of Curve's actual invariant.
    
    # Let's use a more accurate representation of the swap for a constant product AMM
    # x1 * y1 = x2 * y2
    # x_total_after_in = x_total + x_in
    # y_total_after_out = y_total - y_out
    # x_total * y_total = (x_total + x_in) * (y_total - y_out)
    # y_out = y_total - (x_total * y_total) / (x_total + x_in)
    
    # The core idea is that the product of reserves remains constant (or adjusted by A).
    # For a simple AMM, x1*y1 = x2*y2
    # Let x1, y1 be current reserves. x2, y2 be reserves after swap.
    # x2 = x1 + x_in
    # y2 = y1 - y_out
    # x1 * y1 = (x1 + x_in) * (y1 - y_out)
    # y1 - y_out = (x1 * y1) / (x1 + x_in)
    # y_out = y1 - (x1 * y1) / (x1 + x_in)
    
    # This is the fundamental slippage calculation for a constant product AMM.
    # Curve's invariant is more complex, especially with the 'A' parameter for stablecoins.
    # The 'A' parameter amplifies the invariant, making it more resistant to price changes.
    
    # For this example, we'll simulate a simple constant product AMM swap to show slippage.
    # The concept of 'slippage' is the difference between the expected price and the actual execution price.
    # In AMMs, this is due to the curve of the liquidity pool.
    
    # Calculate the invariant before the swap
    invariant = x_total * y_total
    
    # Calculate the new total amount of x after adding x_in
    new_x_total = x_total + x_in
    
    # Calculate the new total amount of y that must exist to maintain the invariant
    # new_y_total = invariant / new_x_total
    # This is the amount of y *remaining* in the pool.
    
    # The amount of y_out is the difference between the initial y_total and the new_y_total
    y_out = y_total - (invariant / new_x_total)
    
    return y_out

def simulate_swap(initial_x, initial_y, x_to_swap, A=1000):
    """
    Simulates a swap of x for y and calculates slippage.
    A is the amplification coefficient, crucial for Curve's stablecoin pools.
    For simplicity, we'll use a basic constant product AMM logic here.
    """
    print(f"Initial state: x={initial_x}, y={initial_y}")
    print(f"Attempting to swap {x_to_swap} of x for y.")

    # Calculate expected amount out based on current price (y/x)
    expected_price = initial_y / initial_x
    expected_y_out = x_to_swap * expected_price
    print(f"Expected y out (at current price): {expected_y_out:.6f}")

    # Calculate actual amount out using the AMM formula
    actual_y_out = get_amount_out(x_to_swap, initial_x, initial_y, A)
    print(f"Actual y out (after AMM calculation): {actual_y_out:.6f}")

    # Calculate slippage
    slippage_amount = expected_y_out - actual_y_out
    slippage_percentage = (slippage_amount / expected_y_out) * 100 if expected_y_out > 0 else 0

    print(f"Slippage amount: {slippage_amount:.6f}")
    print(f"Slippage percentage: {slippage_percentage:.2f}%")

    # New state after swap
    new_x_total = initial_x + x_to_swap
    new_y_total = initial_y - actual_y_out
    print(f"Final state: x={new_x_total}, y={new_y_total}")

    # Verify invariant (approximately, due to floating point)
    final_invariant = new_x_total * new_y_total
    initial_invariant = initial_x * initial_y
    print(f"Initial invariant: {initial_invariant:.2f}")
    print(f"Final invariant: {final_invariant:.2f}")
    # In a real Curve pool, the invariant is more complex and influenced by 'A'.
    # The goal of 'A' is to keep the invariant closer to a constant for stablecoins.

# --- Simulation --- 
# Example: Swapping USDC for DAI in a Curve pool
# Assume a pool with 1,000,000 USDC and 1,000,000 DAI
# We want to swap 10,000 USDC for DAI

initial_usdc = 1_000_000
initial_dai = 1_000_000
usdc_to_swap = 10_000

simulate_swap(initial_usdc, initial_dai, usdc_to_swap)

print("\n--- Larger Swap Simulation ---")
# Simulating a larger swap to observe more significant slippage
large_usdc_to_swap = 100_000
simulate_swap(initial_usdc, initial_dai, large_usdc_to_swap)

print("\n--- Simulation with High A (Conceptual) ---")
# High 'A' parameter (like in Curve's stable pools) aims to reduce slippage.
# This simulation is still using the simplified invariant, so 'A' doesn't directly
# alter the calculation in get_amount_out as it would in a true Curve implementation.
# However, conceptually, a higher A would mean the pool is more resistant to price changes.
# For a true Curve simulation, the invariant function itself would change based on A.

# The core takeaway is that AMMs, by their nature, introduce slippage.
# Curve's advanced invariant and amplification coefficient (A) are designed to minimize this for stable assets.

simulate_swap(initial_usdc, initial_dai, usdc_to_swap, A=10000) # Higher A conceptually
