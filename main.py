class GF16:
    # Wielomian pierwotny w GF(2) dla GF(2^4): x^4 + x + 1
    # To odpowiada wartości binarnej 0b10011, gdzie x^4 = 1, x = 1, i 1 = 1
    primitive_polynomial = 0b10011  # Reprezentacja binarna x^4 + x + 1

    def __init__(self, value):
        """Upewnij się, że wartość mieści się w polu GF(2^4)."""
        self.value = value & 0b1111  # Utrzymujemy tylko 4 bity (od 0 do 15)

    def __repr__(self):
        return f"GF16({self.value})"

    def __add__(self, other):
        """Dodawanie w GF(2^4) jest realizowane za pomocą XOR."""
        return GF16(self.value ^ other.value)

    def __mul__(self, other):
        """Mnożenie w GF(2^4) z redukcją przez wielomian pierwotny."""
        result = 0
        a = self.value
        b = other.value

        while b > 0:
            # Jeśli najmłodszy bit b jest 1, dodaj a do wyniku
            if b & 1:
                result ^= a

            # Przesuń a w lewo (mnożenie przez x w GF(2))
            a <<= 1

            # Sprawdź, czy a przekracza 4 bity, co wymaga redukcji
            if a & 0b10000:  # jeśli a >= 2^4, to przekracza zakres GF(2^4)
                a ^= GF16.primitive_polynomial

            # Przesuń b w prawo, aby przetworzyć kolejny bit
            b >>= 1

        return GF16(result)

    def __eq__(self, other):
        """Porównanie wartości w GF(2^4)."""
        return self.value == other.value


# Testowanie operacji
a = GF16(0b0101)  # reprezentacja dla pierwszego wielomianu
b = GF16(0b0010)  # reprezentacja dla drugiego wielomianu

# Dodawanie w GF(2^4)
print(f"{a} + {b} = {a + b}")

# Mnożenie w GF(2^4)
print(f"{a} * {b} = {a * b}")
