import math


def alpha_beta(depth, nodeIndex, maximizing_player,
               values, alpha, beta, height):

    if depth == height:
        return values[nodeIndex]

    if maximizing_player:
        best = -math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta,
                height
            )

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta,
                height
            )

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = list(map(
    int,
    input("Enter 8 leaf node values: ").split()
))

height = int(math.log2(len(values)))

if len(values) != 2 ** height:
    print("The number of leaf values must be a power of 2.")
else:
    optimal_value = alpha_beta(
        0, 0, True, values,
        -math.inf, math.inf, height
    )

    print("Optimal value:", optimal_value)