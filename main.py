import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        
        heapq.heappush(cables, cost)
        
        total_cost += cost
    
    return total_cost

cable_lengths = [4, 3, 2, 6]
min_cost = min_connection_cost(cable_lengths)
print(f"Мінімальні витрати на об'єднання кабелів: {min_cost}")
