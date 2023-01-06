# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = list(map(lambda x: int(x), input().split()))

# 1ST METHOD

# # upper half
# for i in range(1, int(N/2)+1):
#     print((".|." * (2 * i - 1)).center(M, "-"))

# # middle
# print("WELCOME".center(M, "-"))

# # lower half
# for i in range(1, int(N/2)+1):
#     print((".|." * (N - (2 * i))).center(M, "-"))
# -----------------------------------------
# 2ND METHOD

# for i in range(1, N+1):
#     print(
#             (
#                 (".|." * (2 * i - 1)).center(M, "-") * (i < (int(N/2) + 1)) +\
#                 "WELCOME".center(M, "-") * (i == int(N/2) + 1) + \
#                 (".|." * ((N - i) * 2 + 1)).center(M, "-") * (i > (int(N/2) + 1))
#             )
#     )

# -----------------------------------------
# 3RD METHOD
# CRAZY ONE LINER
_ = [
    print((".|." * (2 * i - 1)).center(M, "-") * (i < (int(N / 2) + 1)) + "WELCOME".center(M, "-") * (
                i == int(N / 2) + 1) + (".|." * ((N - i) * 2 + 1)).center(M, "-") * (i > (int(N / 2) + 1))) for i in
    range(1, N + 1)
]
