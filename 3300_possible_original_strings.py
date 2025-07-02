class Solution:
    def possibleStringCount(self, word: str) -> int:

        def get_runs(word):
            runs = []
            i = 0
            while i < len(word):
                ch = word[i]
                count = 1
                while i + 1 < len(word) and word[i + 1] == ch:
                    i += 1
                    count += 1
                runs.append((ch, count))
                i += 1
            return runs

        def generate_variants(runs):
            variants = set()
            base = ''.join(ch * count for ch, count in runs)
            variants.add(base)
            for i, (ch, count) in enumerate(runs):
                if count <= 1:
                    continue
                for reduced_len in range(1, count):
                    new_runs = runs.copy()
                    new_runs[i] = (ch, reduced_len)
                    s = ''.join(c * n for c, n in new_runs)
                    variants.add(s)
            return variants

        runs = get_runs(word)
        variants = generate_variants(runs)
        return len(variants)

if __name__ == "__main__":
    sol = Solution()
    test_word = "abbcccc"
    print(sol.possibleStringCount(test_word))  # Expected output: 5
