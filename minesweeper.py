def annotate(grid):
    """
    Takes a 2D list of strings where '#' is a mine and '-' is empty,
    and returns a new 2D list where each '-' is replaced by an integer
    count of adjacent mines.
    """
    rows = len(grid)
    if rows == 0:
        return []

    cols = len(grid[0])
    # Prepare an output grid of the same size
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            if grid[r][c] == "#":
                # Keep mines as-is
                new_row.append("#")
            else:
                # Count all adjacent mines
                count = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == "#"
                        ):
                            count += 1
                new_row.append(count)
        result.append(new_row)

    return result


if __name__ == "__main__":
    # Example usage
    sample = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

    annotated = annotate(sample)
    for row in annotated:
        print(row)
