def sniffer():
    import serial
    listener = serial.Serial(port='COM3', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                             bytesize=serial.EIGHTBITS, timeout=None)
    querry_start_list = ['01', '02', '03', '04']
    querry_start_list_two = ['0103', '0203', '0303', '0403']
    querry_start_list_three = ['0103012c', '0203012c', '0303012c', '0403012c']
    querry_start_list_four = ['0103008c', '0203008c', '0303008c', '0403008c']
    response = ''
    query = ''
    query_start = ''
    generator_parameters = {'Engine rpm' : None}
    query_start = listener.read().hex()
    if query_start in querry_start_list:
        query_start += listener.read().hex()
        if query_start in querry_start_list_two:
            query_start += listener.read(2).hex()
            if query_start in querry_start_list_four:
                query = query_start + listener.read(4).hex()
                response = listener.read(245).hex()
#               print(response, sep='\n')
                generator_parameters['Generator number'] = response[:2]
#               generator_parameters['Function'] = response[2:4]
#               generator_parameters['Byte count'] = response[4:6]
#               generator_parameters['Generator Total Reactive Power'] = (int(response[6:14], 16) - 2000000000)/1000  # 0x008C 2 registers
#               generator_parameters['Generator Total Percent Reactive Power'] = int(response[14:18], 16) * 0.0078125 - 251 # 1 register
#               generator_parameters['Generator Total Real Energy Exported'] = int(response[18:26], 16) # 2 registers
#               generator_parameters['Generator Total Reactive Energy Exported'] = int(response[26:34], 16) # 2 registers
                generator_parameters['Generator Average Line-Neutral AC RMS Voltage'] = int(response[34:38], 16)  # 1 register
                generator_parameters['Generator Front Bearing Temperature'] = int(response[38:42], 16) * 0.03125 - 273 # 1 register
                generator_parameters['Generator Rear Bearing Temperature'] = int(response[42:46], 16) * 0.03125 - 273 # 1 register
                generator_parameters['Generator Phase A Winding Temperature'] = int(response[46:50], 16) * 0.03125 - 273 # 1 register
                generator_parameters['Generator Phase B Winding Temperature'] = int(response[50:54], 16) * 0.03125 - 273 # 1 register
                generator_parameters['Generator Phase C Winding Temperature'] = int(response[54:58], 16) * 0.03125 - 273 #  1 register
                generator_parameters['Engine Oil Temperature'] = int(response[238:242], 16) * 0.03125 - 273 # 1 register
                generator_parameters['Engine Oil Pressure'] = int(response[242:246], 16) * 0.125 # 1 register
                generator_parameters['Engine Coolant Temperature'] = int(response[246:250], 16) * 0.03125 - 273 # 1 register
                generator_parameters['Battery Voltage'] = int(response[250:254], 16) * 0.05 # 1 register
                generator_parameters['Engine rpm'] = int(response[254:258], 16) * 0.125 # 1 register
                generator_parameters['Engine Operating Hours'] = int(int(response[258:266], 16) * 0.05) # 2 registers                    generator_parameters['Automatic Start/Stop State'] = int(response[266:270], 16) # 1 register
#                print(generator_parameters)
    return print(generator_parameters['Engine rpm'])
