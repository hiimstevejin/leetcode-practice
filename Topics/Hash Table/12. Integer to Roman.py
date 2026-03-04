class Solution:
    # clean solution
    def intToRoman(self, num: int) -> str:
            roman_symbols = [
                (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
            ]

            res = []
            for value, symbol in roman_symbols:
                if num == 0:
                    break

                # 1. How many of this symbol can we fit?
                count = num // value

                # 2. Add them to the list
                if count > 0:
                    res.append(symbol * count)

                # 3. Keep the remainder for the next loop
                num = num % value

            return "".join(res)

    # Shitty solution but works in O(1) because constraint was 3999
    def intToRoman(self, num: int) -> str:
        roman_int = {
            1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM",1000:"M",
        }

        res = []
        while num > 0:
            for number, symbol in reversed(roman_int.items()):
                occurance = num // number
                for _ in range(occurance):
                    res.append(symbol)
                num = num - number * occurance

        return "".join(res)
