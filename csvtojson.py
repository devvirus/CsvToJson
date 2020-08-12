import csv
import json

def make_json_tree(csv_file_path):

    children = []
    treeArr = []

    #create a list of lists from CSV

    reader = csv.reader(open(csv_file_path, 'rt')) # in python3

    #print('\n-------reader--------\n')

    #print(reader)

    next(reader) # in python3 # csv header(first row)

    for row in reader:

        children.append(row)

        if row[1] != '':

            #create tree root

            tree = {'label': row[1],'id': row[2],'link': row[3], 'children': []}

        else:

            tree = {'label': 0,'id': 0,'link': '', 'children': []}



        if row[4] != '':

            #create a generic subtree

            subtree = {'label': row[4],'id': row[5],'link': row[6], 'children': []}

        else:

            subtree = {'label': 0,'id': 0,'link': '', 'children': []}



        if row[7] != '':

            #create a generic subtree

            ssubtree = {'label': row[7],'id': row[8],'link': row[9], 'children': []}

        else:

            ssubtree = {'label': 0,'id': 0,'link': '', 'children': []}



    for i in children:

        if i[1] != '':

            #so we append the current group

            tree = {'label': row[1],'id': row[2],'link': row[3], 'children': []}

            subtree['label'] = i[1]

            #start a new group

            if i[4] != '':

                if i[7] != '':

                    subtree['children'] = [{'label': i[7],'id': i[8],'link': i[9], 'children': subtree['children']}]

                else:

                    subtree['children'] = []

                tree['children'].append({'label': i[4],'id': i[5],'link': i[6], 'children': subtree['children']})

                subtree['children'] = []

            else:

                subtree['children'] = []

            #and rename the subtree

                subtree['label'] = i[1]

        else:

            tree = None



        if tree is not None:

            treeArr.append(tree)

        #break



        #remove the generic starting name

    tree['children'] = tree['children'][1:]

    return treeArr
















