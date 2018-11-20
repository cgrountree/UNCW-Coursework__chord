import Chord


#author: Cody Rountree

class Node:
    def __init__(self, node_number):
        self.node_number = node_number
        self.finger_table = []

    def create_finger_table(self, m, node_list):
        for i in range(m):
            entry_value_node = 0
            table_entry_value = self.node_number + 2**i
            math_string = "N" + str(self.node_number) + "+" + str(2**i)
            if (table_entry_value <= node_list[-1].node_number):
                for k in node_list:
                    if (table_entry_value <= k.node_number):
                        entry_value_node = k.node_number
                        break
            if (table_entry_value >= node_list[-1].node_number):
                adjusted_entry_value = table_entry_value - (2**m)
                if (adjusted_entry_value <= node_list[-1].node_number):
                    for k in node_list:
                        if (adjusted_entry_value <= k.node_number):
                            entry_value_node = k.node_number
                            break

            self.finger_table.append([self.node_number + 2**i, math_string, entry_value_node])

    def finger_table_to_string(self):
        print("\n" + "N" + str(self.node_number) + " finger table")
        for i in self.finger_table:
            print("K" + str(i[0]) + "\t" + i[1] + '\t' + "N" + str(i[2]))