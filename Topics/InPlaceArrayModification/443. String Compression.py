class Solution:
    # Two pointer 1st one is stylistically better
    # Time O(n)
    # Space O(1)
    def compress(self, chars: List[str]) -> int:
        write = 0
        left = 0

        for read in range(len(chars)):
            if read == len(chars) - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[left]
                write += 1

                count = read - left + 1
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1

                left = read + 1

        return write

    # still optimal but verbose
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        write = 0
        count = 0
        curr_char = chars[write]

        for read in range(len(chars)):
            if chars[read] == curr_char:
                count += 1
            else:
                if count == 1:
                    chars[write] = curr_char
                    write += 1
                else:
                    chars[write] = curr_char
                    str_count = str(count)
                    for i in range(len(str_count)):
                        write += 1
                        chars[write] = str_count[i]
                    write += 1
                curr_char = chars[read]
                count = 1
        chars[write] = curr_char
        str_count = str(count)
        if count != 1:
            for i in range(len(str_count)):
                write += 1
                chars[write] = str_count[i]

        return write + 1
