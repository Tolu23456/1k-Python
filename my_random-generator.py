import math
import time

class UniverseEngine:
    def __init__(self, e_constant=0.5829348123049123):
        self.e = e_constant
        self._flux = 0

    def _get_base_physics(self, mode="non-linear"):
        """Internal math core for the Universe logic."""
        self._flux += 1
        
        if mode == "linear":
            # Original version: standard time, slower movement
            n = time.time()
            delta_n = n - int(n)
        elif mode == "high-res":
            # Nanosecond version: much faster jitter
            n = time.perf_counter_ns()
            delta_n = (n * 10**7) % 1
        else:
            # Non-linear (Chaos): Using the Sine Oscillator
            n = time.perf_counter_ns()
            oscillator = math.sin(n * self.e + self._flux)
            delta_n = (oscillator + 1) / 2
        
        # Stability adjustment to prevent zero-results
        delta_n = (delta_n * 0.8) + 0.1
        
        term1 = math.sqrt(n)
        term2 = delta_n - (delta_n ** self.e)
        return abs(term1 * term2 * self.e)

    def generate(self, mode="non-linear", length=10, output_type="int", allow_negative=False):
        """
        The main generator method.
        output_type: 'int', 'float'
        """
        raw = self._get_base_physics(mode)
        
        # Handle Negatives randomly if requested
        multiplier = 1
        if allow_negative:
            # We use the raw math to decide the sign (pseudo-random)
            multiplier = -1 if (int(raw * 10**6) % 2 == 0) else 1

        if output_type == "float":
            # Return as a fraction/decimal
            return (raw % 1) * multiplier
        
        else:
            # Return as an integer with a specific length
            # We use modulo to "clamp" the number to the desired digit length
            limit = 10**length
            id_out = int(raw * 10**15) % limit
            
            # Ensure the length is exact (padding if necessary)
            if len(str(id_out)) < length:
                id_out += (10**(length-1))
                
            return id_out * multiplier

# --- Implementation Example ---
universe = UniverseEngine()

print("--- Integer Modes (Length 12) ---")
print(f"Linear:     {universe.generate(mode='linear', length=12)}")
print(f"High-Res:   {universe.generate(mode='high-res', length=12)}")
print(f"Non-Linear: {universe.generate(mode='non-linear', length=12)}")

print("\n--- Advanced Formatting ---")
print(f"Negative Int: {universe.generate(length=8, allow_negative=True)}")
print(f"Fraction:     {universe.generate(output_type='float'):.10f}")
print(f"Both (+/-):   {universe.generate(output_type='float', allow_negative=True):.10f}")