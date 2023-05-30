import sys
import itertools

def TSP(distances):
    n = len(distances)    
    saved_result = {}
    
    def visit_cities(curr_city, remaining_cities):
        # all visited then return 
        if not remaining_cities:
            return distances[curr_city][0], [0]

        # check if already save result
        if (curr_city, remaining_cities) in saved_result:
            return saved_result[(curr_city, remaining_cities)]

        # initialize maxsize as a min distance and min path to None
        min_distance = sys.maxsize
        min_path = None

        # visit all the cities
        for next_city in remaining_cities:            
            new_remaining_cities = tuple(city for city in remaining_cities if city != next_city)
            distance = distances[curr_city][next_city]            
            subproblem_distance, subproblem_path = visit_cities(next_city, new_remaining_cities)            
            if distance + subproblem_distance < min_distance:
                min_distance = distance + subproblem_distance
                min_path = [curr_city] + subproblem_path    
        saved_result[(curr_city, remaining_cities)] = (min_distance, min_path)
        return min_distance, min_path
    
    minimum_distance, best_route = visit_cities(0, tuple(range(1, n)))
    return minimum_distance, best_route

distances = [
    [0, 29, 20, 21, 16, 31, 100, 12, 4, 31],
    [29, 0, 15, 29, 28, 40, 72, 21, 29, 41],
    [20, 15, 0, 15, 14, 25, 81, 9, 23, 27],
    [21, 29, 15, 0, 4, 12, 92, 12, 25, 13],
    [16, 28, 14, 4, 0, 16, 94, 9, 20, 16],
    [31, 40, 25, 12, 16, 0, 95, 24, 36, 3],
    [100, 72, 81, 92, 94, 95, 0, 90, 101, 99],
    [12, 21, 9, 12, 9, 24, 90, 0, 15, 25],
    [4, 29, 23, 25, 20, 36, 101, 15, 0, 35],
    [31, 41, 27, 13, 16, 3, 99, 25, 35, 0]
]

city_bank_branches = {
    0: "Uttara Branch",
    1: "City Bank Airport",
    2: "City Bank Nikunja",
    3: "City Bank Beside Uttara Diagnostic",
    4: "City Bank Mirpur 12",
    5: "City Bank Le Meridien",
    6: "City Bank Shaheed Sarani",
    7: "City Bank Narayanganj",
    8: "City Bank Pallabi",
    9: "City Bank JFP"
}

minimum_distance, best_route = TSP(distances)
shortest_path = "best route: " + " -> ".join(city_bank_branches[route] for route in best_route)
shortest_path += "\n since this is the optimal route: It will take minimum amount of fuel"
    
# Save to file
with open("output_file.txt", "w") as file:    
    file.write(shortest_path)
print("Output to output_file.txt.")
