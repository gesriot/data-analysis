import csv

def adjust_values(input_file, output_file):
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.reader(csv_in)
        writer = csv.writer(csv_out)

        for row in reader:
            holder = int(float(row[-1]) * 10) - 570
            if holder < 0:
                holder += 3680
            row[-1] = str(holder / 10.0)
            writer.writerow(row)

adjust_values('2023.11.29__10_55_58.csv', 'new_empty.csv')