from csv import reader

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        for i in range(len(list_of_rows)):
            for j in range(len(list_of_rows[i])):
                if list_of_rows[i][j].isdigit():
                    list_of_rows[i][j]=int(list_of_rows[i][j])
        return list_of_rows
