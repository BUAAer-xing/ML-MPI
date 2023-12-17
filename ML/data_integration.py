import csv

data_rows = []
with open('../data/matrix_features.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        data_rows.append([row[1], row[2], row[3], float(row[4]), float(row[5]), row[6], row[7]])

with open('../data_visualization/process_min_time.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    cnt = 0
    for row in reader:
        data_rows[cnt].append(row[1])
        cnt += 1

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['n_rows', 'n_cols', 'nnz_frac', 'min_value', 'max_value', 'avg_nz_p_row', 'std_nz_p_row',
                     'best_process'])
    for row in data_rows:
        writer.writerow(row)
