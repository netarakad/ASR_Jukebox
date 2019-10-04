trial_songs [["Queen", "Nervous", "InMyBlood", "Why"],
			["Thriller", "BeatIt", "PYT", "BillieJean"],
			["S&M", "Cheers", "OnlyGirl", "WhatsMyName"],
			["PianoMan", "Vienna", "RockAndRollToMe", "DidntStartFire"]]

pin_count = 4
buttons_pressed = dequeue()
current_states = [True]*pin_count

display_width = 1024
dispay_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
black = (0,0,0)
white = (255, 255, 255)

def button_index_to_GPIO_pin(i):
	pins = [20, 21, 22, 23]
	return pins[i]

def play_song(str):
	pygame.mixer.music.load("/home/pi/Music" + str + ".mp3")
	pygame.mixer.music.play()
	time.sleep(.2)

def display_image(str, x, y):
	print("here")
	game_display.blit(pygame.image.load("/home/pi/Pictures/" + str))
x = (0)
y = (0)

while True:
	for i in range(pin_count):
		if (current_states[i] == True) and (GPIO.input(button_index_to_GPIO_pin(i)) == False):
			print("button pressed...")
			current_states[i] == False
			buttons_pressed.append(i)
		elif (current_states[i] == False) and (GPIO.input(button_index_to_GPIO_pin(i)) == True):
			current_states[i] = True

	if len(buttons_pressed) == 2:
		buttons = (buttons_pressed.pop(), buttons_pressed.pop())
		play_song(trial_songs[buttons[1]][buttons[0]])
		display_image(trial_songs[buttons[1]][buttons[0]], x, y)
		pygame.display.update()

while pygame.mixer.music.getBusy() == True:
	continue
