# Rabin-Karp Algorithm in Python (with visual marking)

def search(pat, txt, q=(2**31 - 1)):  # Using large prime like INT_MAX
    d = 256  # Number of characters in the input alphabet
    M = len(pat)
    N = len(txt)
    p = 0  # Hash value for pattern
    t = 0  # Hash value for text
    h = 1
    matches = []  # Store match positions

    print("Original Pattern:", pat)
   # print("Text:", txt)

    # The value of h would be "pow(d, M-1) % q"
    for i in range(M - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # If hash values match, then check characters one by one
        if p == t:
            match = True
            for j in range(M):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                print("Pattern found at index", i)
                matches.append(i)

        # Calculate hash value for next window of text
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t += q

    # Print visual representation
    if matches:
        marker = [" "] * N
        for i in matches:
            for j in range(M):
                marker[i + j] = "*"
        print("\n Match:")
        print(txt)
        print("".join(marker))
    else:
        print("No pattern found.")


# Driver code
if __name__ == "__main__":
    txt = "AABAACAADAABAABA"
    pat = "AABA"
   # q = 2**31 - 1
    search(pat, txt)
