import PySimpleGUI as sg
import filterIIR as filter
import imageProcessing as ip
import correlation as co

sg.theme('GreenTan')
menu_def = [['Help', 'About']]

tab1_layout = [[sg.Text('IIR Filter\nGenerating signal from 10Hz to 50Hz\nFrequency filter to filter the wanted frequency')],
              [sg.Text('Filter Type'),sg.Combo(['Lowpass','Highpass'],default_value='Lowpass',key='Sig_type')],
              [sg.Text('Cutoff Frequency'), sg.Input(key='low_cut_freq'),sg.Text('Filter Order'), sg.Input(key='filter_order')],
              [sg.Text('Frequency Filter [Hz]'), sg.Input(key='freq_filter')],
              [sg.Button('Generate Graph', key='graph_btn')]]


tab2_layout = [[sg.Text('Using lowpass and highpass we can take an existing image to find the sharp and smooth edges \nAlso allows us to make an image more blury')],
               [sg.Text('Blur Level \n  0 - 10 (Safe)\n 10 - 20 (Moderate)\n 20 and up makes the image very bury and hard to see')],
               [sg.HSep()],
               [sg.Text('Sharpnes Level \n  0 - 5 (Safe)\n 5 - 10 (Moderate)\n 10 and up very sharp')],
               [sg.Text('Blur Level'),sg.Input(key='blur_level'),sg.Text('Sharpnes Level'),sg.Input(key='sharp_level')],
               [sg.Radio('Blur',1,default=True),sg.Radio('Sharp',1)],
               [sg.Button('Generate Image', key='gen_image')]]

tab3_layout = [[sg.Text('Generating signal with 10 pulses, combining the generated signal with noise to make it hard to read.\n Using cross-correlation to recieve the original signal')],
               [sg.Radio('Predefined Pulse',1,default=True)],
               [sg.HSep()],
               [sg.Text('Number of pulses [max 10]'),sg.Input(key='nr_pulses'),sg.Button('Set', key='set_pulse'),sg.Button('Clear', key='clear_pulse')],
               [sg.Radio('Custom Pulses',1),sg.Input(key='pl1',size=(2, 2)),sg.Input(key='pl2',size=(2, 2)),sg.Input(key='pl3',size=(2, 2)),
                sg.Input(key='pl4',size=(2, 2)),sg.Input(key='pl5',size=(2, 2)),sg.Input(key='pl6',size=(2, 2)),sg.Input(key='pl7',size=(2, 2)),
                sg.Input(key='pl8',size=(2, 2)),sg.Input(key='pl9',size=(2, 2)),sg.Input(key='pl10',size=(2, 2))],
               [sg.Button('Generate Graphs', key='gen_correlation')],
               [sg.Text('Number of pulses is too high', key='pulse_warning', visible=False)]]

layout = [[sg.Menu(menu_def)],
          [[sg.TabGroup([[sg.Tab('IIR Filter', tab1_layout), sg.Tab('Image Processing', tab2_layout),
          sg.Tab('Correlation', tab3_layout)]])]]]

window = sg.Window('Signal Processing', layout, default_element_size=(12,1), finalize=True)

while True:
    event, values = window.read()    
    if event == sg.WIN_CLOSED:          
        break
    
    elif event == 'About':
        sg.popup('Signal Processing','A demo program for signal processing \n Created by Jani Godari \n Copyright 2022 \n UPB')
    
    elif event == 'graph_btn':
        filter.low_high_pass(values['Sig_type'],values['filter_order'],values['low_cut_freq'],values['freq_filter'])
    
    elif event == 'gen_image':
        print(event,values)
        if values[2] == True:
            ip.blur_img(values['blur_level'])
        else:
            ip.edge_finder(values['sharp_level'])  

    elif event == 'set_pulse':
        if(int(values['nr_pulses']) > 10):
            window['pulse_warning'].Update(visible=True)
        else:
            nr_pulse = int(values['nr_pulses'])
            for i in range(nr_pulse, 10):
                window['pl'+str(i+1)].Update(disabled=True)
            window['pulse_warning'].Update(visible=False)

    elif event == 'clear_pulse':
        for i in range(0, 10):
            window['pl'+str(i+1)].Update(disabled=False)
            window['pl'+str(i+1)].Update(disabled=False)

        
    elif event == 'gen_correlation':
        val_puls = [0 for _ in range(10)]
        empty_arr = []
        
        if(values[4] == True):
               co.correlation(empty_arr)
        else:
            if(int(values['nr_pulses']) > 11):
                window['pulse_warning'].Update(visible=True)
            else:
                nr_pulse = int(values['nr_pulses'])
                
                for i in range(0,nr_pulse):
                    val_puls[i] = int(values['pl'+str(i+1)])
                co.correlation(val_puls)        

window.close()
