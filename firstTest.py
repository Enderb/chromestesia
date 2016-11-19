import pygame.midi
from bootstrap import *
from random import randint

def number_to_note(number):
	notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']
	return notes[number%12]

def number_to_pixel(number):
	pixels = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
	return pixels[11 - number%12]

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
			event = input_device.read(1)[0]
			data = event[0]
			timestamp = event[1]
			note_number = data[1]
			velocity = data[2]
			
			#Notes go from 21 (A1) to 108 (C7)
			#Sustain pedal is 64, same as E3
			if note_number != 0:
				print(note_number, number_to_note(note_number), velocity)
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
