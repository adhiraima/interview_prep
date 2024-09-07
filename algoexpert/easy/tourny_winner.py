def tournamentWinner(competitions, results):
    # Write your code here.
    home_away_map = {1:0, 0:1}
    # print(competitions)
    # print(results)
    result_map = {}
    for i in range(0, len(competitions)):
        # print(f"Winner {competitions[i][home_away_map[results[i]]]}")
        if competitions[i][home_away_map[results[i]]] in result_map.keys():
            result_map[competitions[i][home_away_map[results[i]]]] += 1
        else:
            result_map[competitions[i][home_away_map[results[i]]]] = 1
    # print(result_map)
    winner = ""
    max = 0
    for key in result_map.keys():
        if result_map[key] > max:
            # print(f"setting key: {key}")
            max = result_map[key]
            winner = key
    return winner
