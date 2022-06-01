import qrcode
import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("Insira o texto do QR-Code:")],     # Part 2 - The Layout
            [sg.Input(key='texto')],
            [sg.Text('Nome do Arquivo:')],
            [sg.Input(key='nomeArquivo')],
            [sg.Button('Gerar QR'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Gerador de QR-Code', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break
	qr = qrcode.QRCode(
		version = 1,
		box_size = 32,
		border = 2
	)
	qr.add_data(values['texto'])
	qr.make(fit=True)
	img = qr.make_image(fill='black', back_color = 'white')
	img.save(values['nomeArquivo']+".png")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window