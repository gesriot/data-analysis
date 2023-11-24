def process_file(path):
    with open(path, 'r') as f:
        result = []
        for line in f:
            line = line.strip()
            data = line.split(',')
            value = data[-1]
            encoder, fraction = value.split('.')
            encoder = int(encoder)
            fraction = int(fraction)

            if fraction not in (5, 6, 7):
                value_ = float(value) - 0.8
                if value_ < 0:
                    value_ = value_ + 368
                value = f'{value_:.1f}'
                data[-1] = value
                line = ','.join(data)
                result.append(line)
    with open('result.csv', 'w') as f:
        for line in result:
            f.write(line + '\n')

def main():
    process_file("file_cut.csv")

if __name__ == "__main__":
    main()
