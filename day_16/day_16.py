'''
AoC - Day 16 - WIP

## Part 1

# Input
Each line describes a valve
Example format 'Valve AA has flow rate=0; tunnels lead to valves DD, II, BB'
The first part is the name and flow rate per minute for the valve
The second part is the other valves it's connected to
Can travel to the connected valves in 1 minute
Can open a valve in 1 minute

# Caclulation
There are 30 minutes. Need to decided on an action for each minute
- Do nothing
- Open a valve at current location
- Travel to a connected valve
For each minute, calculate the total pressure released each minute, which is the
sum of flow rates for all open valves

One option. At current node, find shortest path to every other node. Then
calculate how much pressure would be released if we travelled directly there,
then opened it, and it remained open until the end of 30 minutes. Does that give
us the optimal solution?

# Output
What is the most pressure that can be released in 30min
'''

import networkx

FILE_PATH = 'day_16/input.txt'
FILE_PATH = 'day_16/test.txt'
ACTIONS_PATH = 'day_16/actions_test.txt'
NUM_MIN = 30

def calc_total_pressure(flow_rates, actions, valve_status):
    '''
    Calculate total pressure released over 30 minutes
    '''

    cumulative_pressure = 0

    for i in range(0, NUM_MIN):

        print('== Minute', i + 1, '==')
        # Print open valves
        print('Open valves:', [valve for valve, status in valve_status.items()\
                               if status])

        # Calc pressure released
        pressure = sum([flow_rates[valve] for valve, status in\
                        valve_status.items() if status])
        cumulative_pressure += pressure
        print('Pressure released:', pressure)

        if actions[i][0] == 'open':
            valve_status[actions[i][1]] = True
            print('Open valve', actions[i][1])
        elif actions[i][0] == 'move':
            print('Move to', actions[i][1])

    print('Total pressure released:', cumulative_pressure)

def main():
    '''
    Main function
    '''
    with open(FILE_PATH, 'r', encoding='utf-8') as input_file:
        data = input_file.read().splitlines()

        # Create a dictionary of valves and flow rate
        valve_name = [line[6:8] for line in data]
        valve_flow = [line.split('=')[1] for line in data]
        valve_flow = [int(line.split(';')[0]) for line in valve_flow]
        flow_rates = dict(zip(valve_name, valve_flow))
        valve_status = dict(zip(valve_name, [False] * len(valve_name)))

        # Create a dictionary of valves each valve is connected to
        conn_valves_data = [line.split(';')[1] for line in data]
        conn_valves = [[] for _ in range(len(data))]

        for i, line in enumerate(conn_valves_data):
            for name in valve_name:
                if name in line:
                    conn_valves[i].append(name)

        conn_valves = dict(zip(valve_name, conn_valves))

    # Create a network of valves
    # The dictionary conn_valves gives the valves each valve is connected to
    # Graph is directed, and no weights
    graph = networkx.Graph()
    for valve, conn in conn_valves.items():
        for conn_valve in conn:
            graph.add_edge(valve, conn_valve)

    # TO DO
    # Section that determines the actions to take at each minute

    # Read actions
    with open(ACTIONS_PATH, 'r', encoding='utf-8') as actions_file:
        actions = actions_file.read().splitlines()
        actions = [line.split(' ') for line in actions]

    calc_total_pressure(flow_rates, actions, valve_status)

if __name__ == "__main__":
    main()