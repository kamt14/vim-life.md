import os
from datetime import datetime

# Definimos los nombres de los archivos
current_calendar_file = '/home/kleber/wiki/Calendar.md'
archive_calendar_file = '/home/kleber/wiki/archive/calendar.txt'
archive_recurring_file = '/home/kleber/wiki/archive/recurring.txt'

# Nos aseguramos de que la carpeta de archivo exista
os.makedirs(os.path.dirname(archive_calendar_file), exist_ok=True)

# Obtenemos la fecha actual
today = datetime.now().strftime("%d-%m-%Y %A")

def read_calendar_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    blocks = []
    current_block = []

    for line in lines:
        if line.strip() == '':
            if current_block:
                blocks.append(''.join(current_block).strip())
                current_block = []
        else:
            current_block.append(line)

    # Añadimos el último bloque si no está vacío
    if current_block:
        blocks.append(''.join(current_block).strip())

    return blocks

def add_current_date_to_calendar():
    if not os.path.exists(current_calendar_file):
        with open(current_calendar_file, 'w') as file:
            file.write(f"{today}\n+helo \n\n")
    else:
        # Leemos recurring.txt y obtenemos bloques
        blocks = read_calendar_file(archive_recurring_file)
        list_add = "" # append events
        day = today.split(' ')[1]
        datetime = today.split(' ')[0].split('-')
        nb = read_calendar_file(current_calendar_file)
        nb_date = nb[0].split('\n')[0]  # Obtenemos solo la fecha

        for block in blocks:
            lines = block.split('\n')
            if lines[0] == '@anual':
                for line in lines[1:]:
                    date_selected = line.split('#')[0]
                    date_selected = date_selected.split('-')
                    s_day = date_selected[0]
                    s_month = date_selected[1].strip()
                    if s_day == datetime[0] and s_month == datetime[1]:
                        list_add = list_add + '+ ' + line.split('#')[1] +'\n'
            if lines[0] == '@mensual':
                for line in lines[1:]:
                    date_selected = line.split('#')[0].strip()
                    if date_selected == datetime[0]:
                        list_add = list_add + '+ ' +line.split('#')[1] +'\n'

            if lines[0] == '@semanal':
                for line in lines[1:]:
                    date_selected = line.split('#')[0].strip()
                    if date_selected == day:
                        list_add = list_add + '+ ' + line.split('#')[1] + '\n'

        if today.split()[0] != nb_date.split(' ')[0]:
            with open(current_calendar_file, 'w') as file:
                file.write(f"{today}\n{list_add}+ \n\n")

def archive_past_dates():
    # Leemos el archivo y obtenemos los bloques
    blocks = read_calendar_file(current_calendar_file)

    # Extraemos el bloque con la fecha actual y los que no
    c_block, p_block = process_blocks(blocks, today)

    # Exportamos el archivo
    with open(archive_calendar_file, 'r') as file:
        content = file.read()
    with open(archive_calendar_file, 'w') as file:
        for block in p_block:
            file.write(block + '\n\n')
        file.write(content)

def process_blocks(blocks, today):
    current_blocks = []
    past_blocks = []

    for block in blocks:
        lines = block.split('\n')
        if lines[0] == today:
            current_blocks.append(block)
        else:
            past_blocks.append(block)

    return current_blocks, past_blocks

if __name__ == "__main__":
    archive_past_dates()
    add_current_date_to_calendar()

