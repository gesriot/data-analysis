def generate_values(a, b):
    if not (0.1 <= a <= 0.9) or not (1 <= b <= 9):
        raise ValueError("a должно быть в [0.1; 0.9], b - в диапазоне [1; 9]")
    ls = list(range(10))
    a_ = int(a*10) - 1
    for i in range(11 - b):
        ls.remove((a_ + i) % 10)
    ls.append(a_)
    return ls

def process_file(path, offset, discard_values):
    """
    (10 - discard_values) значений начиная с offset
    """
    with open(path, 'r') as f:
        result = []
        for line in f:
            line = line.strip()
            data = line.split(',')
            value = data[-1]
            encoder, fraction = value.split('.')
            encoder = int(encoder)
            fraction = int(fraction)

            discard_range = generate_values(offset, discard_values)

            if fraction not in discard_range:
                value_ = float(value) - offset
                
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
    process_file("new-57.csv", 0.8, 3)

if __name__ == "__main__":
    main()
