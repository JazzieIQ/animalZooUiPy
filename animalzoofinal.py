# Final Project
#
# Python file name: animalzoofinal.py
#
# Date: 12-02-2023

# Programmer's name: Matthew Gutierrez

import pygame
from pygame.locals import *
from tkinter import Tk, filedialog
import sys
import datetime

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Zoo Habitat Management")

font = pygame.font.Font(None, 36)
dialogue_font = pygame.font.Font(None, 24)

start_button = pygame.Rect(50, 50, 150, 50)
cancel_button = pygame.Rect(250, 50, 150, 50)
submit_button = pygame.Rect(500, 50, 150, 50)

checkboxes = []

input_rect = pygame.Rect(50, 120, 700, 36)
input_text = ""
input_active = False

arriving_animals = []
animal_names = []

# Dialogue box class
class DialogueBox:
    def __init__(self, x, y, width, height, font, initial_max_lines=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.max_lines = initial_max_lines
        self.lines = []
        self.scroll_pos = 0

    def add_line(self, text):
        words = text.split()
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if self.font.size(test_line)[0] <= self.rect.width - 20:
                current_line = test_line
            else:
                self.lines.append(current_line)
                current_line = word + ' '
        self.lines.append(current_line)

        # Increase max_lines if needed
        self.max_lines = max(len(self.lines), self.max_lines + 1)

        while len(self.lines) > self.max_lines:
            self.lines.pop(0)

    def render(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)

        y_offset = 10
        for line in self.lines:
            text_surface = self.font.render(line, True, BLACK)
            surface.blit(text_surface, (self.rect.x + 10, self.rect.y + y_offset))
            y_offset += self.font.get_linesize()

        # Draw scroll bar
        scroll_bar_rect = pygame.Rect(self.rect.x + self.rect.width - 15, self.rect.y, 15, self.rect.height)
        pygame.draw.rect(surface, BLACK, scroll_bar_rect)

    def scroll(self, direction):
        if direction == "up" and self.scroll_pos > 0:
            self.scroll_pos -= 1
        elif direction == "down" and self.scroll_pos + self.max_lines < len(self.lines):
            self.scroll_pos += 1

# Create a dialogue box
dialogue_box = DialogueBox(50, 200, 1300, 1200, dialogue_font, initial_max_lines=5)

def open_file_dialog():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    root.destroy()

    return file_path

running = True
def clear_lines(self):
    self.lines = []
    dialogue_box.add_line("Welcome to Mac Mac's Interface for Creating Habitats. You will need two documents to begin.")
    dialogue_box.add_line("(1st doc is for Animal details. 2nd doc is animal names. Press start to begin.)")
    dialogue_box.add_line("*Be sure docs follow Zoo Habitat Dox Protocol found in instruction manual before submitting and reviewing Final Habitat Creation Document.")
clear_lines(dialogue_box)

## Initializations snd functions

def gen_birth_day(year_old, birth_season):
    year = 2023 - year_old
    month_day = {
        "spring": "03-19",
        "summer": "05-21",
        "fall": "08-19",
        "winter": "12-19"
    }.get(birth_season, "01-01")
    new_date = f"{year}-{month_day}"
    return new_date


def gen_unique_id(species_name, num_of_species):
    if species_name == "hyena":
        return f"Hy0{num_of_species}"
    elif species_name == "lion":
        return f"Li0{num_of_species}"
    elif species_name == "tiger":
        return f"Ti0{num_of_species}"
    elif species_name == "bear":
        return f"Be0{num_of_species}"
    else:
        return "error"

#
hyena_habitat = []
lion_habitat = []
tiger_habitat = []
bear_habitat = []

habs = [None] * 4
hyenas = [None] * 13
lions = [None] * 13
tigers = [None] * 13
bears = [None] * 13

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):

                arriving_animals_file = open_file_dialog()

                if arriving_animals_file == "":
                    dialogue_box.add_line("No file #1 selected")
                    break
                dialogue_box.add_line("\nLet's begin!\n")
                with open(arriving_animals_file, 'r') as file:
                    #arriving_animals = file.readlines()
                    animals = file.readlines()
                    dialogue_box.add_line("New Animals to the Following Habitats.\n")
                    for animal in animals[:16]:
                        dialogue_box.add_line(animal.strip())
                    #dialogue_box.add_line("Arriving Animals: {}".format(animals))

                animal_names_file = open_file_dialog()
                if animal_names_file == "":
                    dialogue_box.add_line("No file #2 selected")
                    break
                dialogue_box.add_line("\n\n Parsing Habitat Names... \n\n")
                with open(animal_names_file, 'r') as file:
                    #animal_names = file.readlines()
                    names = file.read()
                    names = names.replace("Names:\n", "Habitat: ").replace("Ryker\n", "Ryker")
                    #dialogue_box.add_line("Animal Names: {}".format(names))
#
                #dialogue_box.add_line(str(animals))
                #dialogue_box.add_line(str(names))
                #dialogue_box.add_line("Parsing Data...")

                with open("zooHabitats.txt", "w") as output_file:
                    output_file.write("Created Habitat Enclosures\n")
                    output_file.write("New Animals to the Following Habitats.\n")

                    current_date = datetime.date.today()
                    in_taking_date = current_date - datetime.timedelta(days=7)
                    pre_quart_date = current_date - datetime.timedelta(days=4 * 30 + 12)

                    years_old = 0
                    num_of_hyenas = 0
                    num_of_lions = 0
                    num_of_tigers = 0
                    num_of_bears = 0
                    j = 0
                    index_key = 0
                    end_key = 0
                    #### Habitat and Name list array
                    data_names = names.replace(": \n", ", ").replace("\n\n", ", ").split(",", 52)
                    dialogue_box.add_line(str(data_names))
                    dialogue_box.add_line("\n")
                    ##### Data for Animals too refactor later.
                    data_animals = str(animals).replace("Tunisia\n", "Tunisia").replace("Tanzania\n",
                                                                                        "Tanzania").replace(
                        "Bangladesh\n", "Bangladesh").replace("Nepal\n", "Nepal").replace("Alaska \n", "Alaska")
                    #dialogue_box.add_line(data_animals)
                    dialogue_box.add_line("\n")
                    #### Split and Append + Format for Habitat and Names
                    for j in range(12):
                        if j < len(data_names):
                            if data_names[j].strip() == "Hyena Habitat":
                                habs[0] = data_names[j].strip()
                            else:
                                hyenas[j] = data_names[j]

                    dialogue_box.add_line(f"These names are for {habs[0]}:")
                    for j in range(5):
                        if hyenas[j] is not None:
                            dialogue_box.add_line(hyenas[j])
                    for j in range(12, 25):
                        if j < len(data_names):
                            if data_names[j].strip() == "Lion Habitat":
                                habs[1] = data_names[j].strip()
                            else:
                                lions[j - 13] = data_names[j]

                    dialogue_box.add_line(f"These names are for {habs[1]}:")
                    for j in range(13, 17):
                        if lions[j - 13] is not None:
                            dialogue_box.add_line(lions[j - 13])

                    for j in range(25, 36):
                        if j < len(data_names):
                            if data_names[j].strip() == "Bear Habitat":
                                habs[2] = data_names[j].strip()
                            else:
                                bears[j - 26] = data_names[j]

                    dialogue_box.add_line(f"These names are for {habs[2]}:")
                    for j in range(26, 30):
                        if bears[j - 26] is not None:
                            dialogue_box.add_line(bears[j - 26])

                    for j in range(36, 47):
                        if j < len(data_names):
                            if data_names[j].strip() == "Tiger Habitat":
                                habs[3] = data_names[j].strip()
                            else:
                                tigers[j - 39] = data_names[j]

                    dialogue_box.add_line(f"These names are for {habs[3]}:")
                    for j in range(39, 43):
                        if tigers[j - 39] is not None:
                            dialogue_box.add_line(tigers[j - 39])
                    #### Split Animals Doc to Initialized and declared variables for doc write-in
                    for i in range(16):
                        split_animals = animals[i].split()
                        split_str_comma = animals[i].split(",")
                        ##### Split Data Variables
                        dialogue_box.add_line("\n")
                        years_old = int(split_animals[0])
                        season = split_animals[7]
                        species = split_str_comma[0].split()[4]
                        birthdate = gen_birth_day(years_old, season)
                        sex = split_animals[3]
                        color = split_str_comma[2]
                        weight = split_str_comma[3]
                        origin = split_str_comma[4] + "," + split_str_comma[5]
                        ##### List for individual animal.
                        if species == "hyena":
                            num_of_hyenas += 1
                            unique_id = gen_unique_id(species, num_of_hyenas)
                            animal = {
                                "id": unique_id,
                                "name": hyenas[num_of_hyenas],
                                "birthday": birthdate,
                                "color": color.replace(" ", ""),
                                "sex": sex.replace(" ", ""),
                                "weight": weight.replace("  ", " "),
                                "arrival": current_date,
                                "age": years_old
                            }
                            dialogue_box.add_line(
                                f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                            hyena_habitat.append(animal)
                        elif species == "lion":
                            num_of_lions += 1
                            unique_id = gen_unique_id(species, num_of_lions)
                            animal = {
                                "id": unique_id,
                                "name": lions[num_of_lions - 1],
                                "birthday": birthdate,
                                "color": color.replace(" ", ""),
                                "sex": sex.replace(" ", ""),
                                "weight": weight.replace("  ", " "),
                                "arrival": current_date,
                                "age": years_old
                            }
                            dialogue_box.add_line(
                                f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                            lion_habitat.append(animal)
                        elif species == "tiger":
                            num_of_tigers += 1
                            unique_id = gen_unique_id(species, num_of_tigers)
                            animal = {
                                "id": unique_id,
                                "name": tigers[num_of_tigers - 1],
                                "birthday": birthdate,
                                "color": color.replace(" ", ""),
                                "sex": sex.replace(" ", ""),
                                "weight": weight.replace("  ", " "),
                                "arrival": current_date,
                                "age": years_old
                            }
                            dialogue_box.add_line(
                                f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                            tiger_habitat.append(animal)
                        elif species == "bear":
                            num_of_bears += 1
                            unique_id = gen_unique_id(species, num_of_bears)
                            animal = {
                                "id": unique_id,
                                "name": bears[num_of_bears - 1],
                                "birthday": birthdate,
                                "color": color.replace(" ", ""),
                                "sex": sex.replace(" ", ""),
                                "weight": weight.replace("  ", " "),
                                "arrival": current_date,
                                "age": years_old
                            }
                            dialogue_box.add_line(
                                f"{animal['id']}: {animal['name']}\n{animal['age']} years old {animal['sex']}.\nBirthday: {animal['birthday']}\n{animal['color']} {animal['weight']}\nArrival {animal['arrival']}")
                            bear_habitat.append(animal)
                        dialogue_box.add_line("\n")

                    dialogue_box.add_line(f"numOfHyenas = {num_of_hyenas}")
                    dialogue_box.add_line(f"numOfLions = {num_of_lions}")
                    dialogue_box.add_line(f"numOfTigers = {num_of_tigers}")
                    dialogue_box.add_line(f"numOfBears = {num_of_bears}")

                    # dialogue_box.add_lineing linked lists
                    output_file.write(f'\n"{habs[0]}"\n')
                    for animal in hyena_habitat:
                        output_file.write(
                            f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

                    output_file.write(f'\n"{habs[1]}"\n')
                    for animal in lion_habitat:
                        output_file.write(
                            f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

                    output_file.write(f'\n"{habs[2]}"\n')
                    for animal in bear_habitat:
                        output_file.write(
                            f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

                    output_file.write(f'\n"{habs[3]}"\n')
                    for animal in tiger_habitat:
                        output_file.write(
                            f"{animal['id']} {animal['name']} {animal['age']} years old, birthday is {animal['birthday']}, {animal['color']}, sex is {animal['sex']}, weight is {animal['weight']}\n")

            elif cancel_button.collidepoint(event.pos):
                clear_lines(dialogue_box)
            elif submit_button.collidepoint(event.pos):
                zoo_habitats = open_file_dialog()
        # Check for mouse wheel events to scroll the dialogue box
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            dialogue_box.scroll("up")
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            dialogue_box.scroll("down")

    pygame.draw.rect(screen, (0, 128, 255), start_button)
    pygame.draw.rect(screen, (255, 0, 0), cancel_button)
    pygame.draw.rect(screen, (0, 255, 0), submit_button)

    start_text = font.render("Start", True, WHITE)
    cancel_text = font.render("Cancel", True, WHITE)
    submit_text = font.render("Submit", True, WHITE)
    screen.blit(start_text, (start_button.x + 50, start_button.y + 10))
    screen.blit(cancel_text, (cancel_button.x + 40, cancel_button.y + 10))
    screen.blit(submit_text, (submit_button.x + 40, submit_button.y + 10))

    pygame.draw.rect(screen, BLACK, input_rect, 2)
    text_surface = font.render(input_text, True, BLACK)
    width = max(200, text_surface.get_width()+10)
    input_rect.w = width
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    dialogue_box.render(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
