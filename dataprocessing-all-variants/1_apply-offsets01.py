def process_file(path, offset, scale_id):
    with open(path, 'r') as f:
        result = []
        for line in f:
            line = line.strip()
            data = line.split(',')
            value = data[-1]
            encoder, fraction = value.split('.')
            encoder = int(encoder)
            fraction = int(fraction)

            # Применяем изменения только для конкретной scale_id
            if int(data[1]) == scale_id:
                value_ = float(value) - offset
                
                if value_ < 0:
                    value_ = value_ + 368
                value = f'{value_:.1f}'
                data[-1] = value
            line = ','.join(data)
            result.append(line)
    with open('result01.csv', 'w') as f:
        for line in result:
            f.write(line + '\n')

process_file("2023.11.29__16_56_16_empty_all_scales.csv", 0.1, 4)
