#author: Cody Rountree
#an implementation of chord



import Node
import random


class Chord:
    def __init__(self, number_of_nodes, m):
        self.number_of_nodes = number_of_nodes
        self.m = m
        self.current_node = 0
        self.key_id = 0
        self.node_list = []
        self.finger_tables = []
        self.current_path = []
        self.solved = 0

    def generate_nodes(self):
        random_nums = random.sample(range(1, 2**self.m), self.number_of_nodes)
        random_nums.sort()
        print(random_nums)
        for num in random_nums:
            newNode = Node.Node(num)
            self.node_list.append(newNode)


    def generate_finger_tables(self):
        for node in self.node_list:
            node.create_finger_table(self.m, self.node_list)

    def pick_start_node(self):
        rand_node_index = random.randint(0, len(self.node_list) - 1)
        start_node = self.node_list[rand_node_index]
        self.current_node = start_node
        self.current_path = [self.current_node]

    def pick_key_id(self):
        rand_key_id = random.randint(1, 2**self.m)
        self.key_id = rand_key_id

    def search_node_finger_table(self):
        current_val = self.current_node.finger_table[0][0]
        next_node_number = self.current_node.node_number
        if(current_val == self.key_id):
            next_node_number = self.current_node.node_number
        if(current_val > self.key_id):
            adjusted_key_id = self.key_id + (2**self.m)
            for i in range(self.m):
                if(self.current_node.finger_table[i][0] <= adjusted_key_id and self.current_node.finger_table[i][0] > current_val):
                    current_val = self.current_node.finger_table[i][0]
                    next_node_number = self.current_node.finger_table[i][2]
        if(current_val < self.key_id):
            for i in range(len(self.node_list)):
                if(self.current_node == self.node_list[0]):
                    self.solved = 1
                    break
            for i in range(self.m):
                if(self.current_node.finger_table[i][0] <= self.key_id and self.current_node.finger_table[i][0] > current_val):
                    current_val = self.current_node.finger_table[i][0]
                    next_node_number = self.current_node.finger_table[i][2]
        return next_node_number

    def find_next_node(self, a_node_number):
        for node in self.node_list:
            if(node.node_number == a_node_number):
                self.current_node = node
                self.current_path.append(node)

    def solve(self):
        count = 0
        self.current_path = [self.current_node]
        while(not self.solved):
            self.find_next_node(self.search_node_finger_table())
            self.current_node.finger_table_to_string()
            previous_node_number = 0
            for i in range(len(self.node_list)):
                if(self.node_list[i] == self.current_node):
                    if(self.node_list[i] == self.node_list[0]):
                        if((self.key_id + (2**self.m)) <= (self.node_list[i].node_number + (2**self.m)) and ((self.key_id + (2**self.m)) > self.node_list[-1].node_number)):
                            self.solved = 1
                    else:
                        previous_node_number = self.node_list[i-1].node_number
            if((self.key_id + (2**self.m)) <= (self.current_node.node_number + (2**self.m)) and (self.key_id + (2**self.m)) > (previous_node_number + (2**self.m))):
                self.solved = 1
            if(self.key_id == self.current_node.node_number or (self.key_id + (2**self.m)) == (self.current_node.node_number + (2**self.m))):
                self.solved = 1
            if(count == 50):
                self.solved = 1
                print("\n***************\nError: infinite loop\n***************")
            count += 1

    def show_path(self):
        path_string = "\npath: "
        for i in range(len(self.current_path)):
            if(i < (len(self.current_path) - 1)):
                path_string = path_string + "N" + str(self.current_path[i].node_number) + "--> "
            else:
                path_string = path_string + "N" + str(self.current_path[i].node_number)
        return path_string


if __name__ == '__main__':
    number_of_nodes = input("enter a number of nodes: ")
    m = input("enter a desired ID space size: ")

    theChord = Chord(int(number_of_nodes), int(m))
    theChord.generate_nodes()
    theChord.generate_finger_tables()

    theChord.pick_start_node()
    print("\nthe start node (Nstart) is: N" + str(theChord.current_node.node_number))

    theChord.pick_key_id()
    print("the key ID is: K" + str(theChord.key_id))

    print("\nN" + str(theChord.current_node.node_number) + " wants to find K" + str(theChord.key_id))

    theChord.current_node.finger_table_to_string()

    theChord.solve()

    print(theChord.show_path())







