nodes = [[2,7,8],[1,8,9],[8,4,9,10,11],[3,5,9],[4,11],[10,11],[1,2],[1,2,3],[4,2],[3,6],[3,5,6]]

paths = []

def IsComplete(list):
    for i in range(11):
        if not i+1 in list:
            return False
    return True

def AddBranch(node,current_path):
        for i in range(len(nodes[node-1])):
            num = nodes[node-1][i]
            if not num in current_path:
                if num == 1:
                    new_list = current_path
                    new_list.append(num)
                    if IsComplete(new_list):
                        paths.append(new_list)
                else:
                    new_list = current_path
                    new_list.append(num)
                    AddBranch(num,new_list)

AddBranch(1,[])
print(paths)
