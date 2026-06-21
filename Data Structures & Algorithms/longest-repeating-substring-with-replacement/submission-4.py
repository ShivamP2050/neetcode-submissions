class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s is None or len(s) == 0:
            return 0

        count = {}
        l = 0
        r = 0
        res = 0
        curr = s[0]

        while r < len(s):
            ch = s[r]
            if ch in count:
                count[ch] = count[ch] + 1
            else:
                count[ch] = 1

            # recompute current most frequent char in the window
            for key in count:
                if count[key] > count[curr]:
                    curr = key

            while (r - l + 1) - count[curr] > k:
                left_char = s[l]
                count[left_char] = count[left_char] - 1
                l = l + 1

                # after shrinking, recompute curr again to avoid over-shrinking
                # (keeps algorithm correct even when previous curr dropped)
                if len(count) > 0:
                    # ensure curr is a valid key; if its count hit zero, pick any key first
                    if count.get(curr, 0) == 0:
                        for any_key in count:
                            curr = any_key
                            break
                    for key in count:
                        if count[key] > count[curr]:
                            curr = key

            window_len = r - l + 1
            if window_len > res:
                res = window_len

            r = r + 1

        return res
        