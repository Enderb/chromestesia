import pygame.midi
from bootstrap import *
from random import randint

def number_to_note(number):
	notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
	return notes[number%12]

def number_to_pixel(number):
	pixels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
	return pixels[31 - number%32]

def number_to_color(number):
	colors = [
		Color(149,100,121),
		Color(34,143,152),
		Color(205,247,229),
		Color(223,165,61),
		Color(188,183,36),
		Color(198,202,254),
		Color(143,82,237),
		Color(228,20,114),
		Color(64,242,185),
		Color(206,39,128),
		Color(94,124,242),
		Color(17,195,228)
		]
	return colors[number%12]

def readInput(input_device):

	while True:
		if input_device.poll():
			events = input_device.read(6)

			for event in events:
				data = event[0]
				timestamp = event[1]
				#Notes will have type = 144
				#Sustain will have type = 177
				type = data[0]
				note_number = data[1]
				velocity = data[2]
			
				#Notes go from 21 (A1) to 108 (C7)
				#Sustain pedal is 64, same as E3
				if note_number != 0 and type == 144:
					print(type, note_number, number_to_note(note_number), velocity)
					pix = number_to_pixel(note_number)
					col = number_to_color(note_number)
					
					if velocity != 0:
						led.set(pix, col)
					else:
						led.setOff(pix)
					
			led.update()


if __name__ == '__main__':
	pygame.midi.init()
	print("starting")
	my_input = pygame.midi.Input(3) 
	readInput(my_input)
