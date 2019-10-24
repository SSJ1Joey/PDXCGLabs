data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks = []

def peak():
    if data[0] > data[1]:
        peaks.append(data[0])
    elif data[1] > data[0] and data[1] > data[2]:
        peaks.append(data[1])
    elif data[2] > data[1] and data[2] > data[3]:
        peaks.append(data[2])
    elif data[3] > data[2] and data[3] > data[4]:
        peaks.append(data[3])
    elif data[4] > data[3] and data[4] > data[5]:
        peaks.append(data[4])
    elif data[5] > data[4] and data[5] > data[6]:
        peaks.append(data[5])
    elif data[6] > data[5] and data[6] > data[7]:
        peaks.append(data[6])
    elif data[7] > data[6] and data[7] > data[8]:
        peaks.append(data[7])
    elif data[8] > data[7] and data[8] > data[9]:
        peaks.append(data[8])
    elif data[9] > data[8] and data[9] > data[10]:
        peaks.append(data[9])
    elif data[10] > data[9] and data[10] > data[11]:
        peaks.append(data[10])
    elif data[11] > data[10] and data[11] > data[12]:
        peaks.append(data[11])
    elif data[12] > data[11] and data[12] > data[13]:
        peaks.append(data[12])
    elif data[13] > data[12] and data[13] > data[14]:
        peaks.append(data[13])
    elif data[14] > data[13] and data[14] > data[15]:
        peaks.append(data[14])
    elif data[15] > data[14] and data[15] > data[16]:
        peaks.append(data[15])
    elif data[16] > data[15] and data[16] > data[17]:
        peaks.append(data[16])
    elif data[17] > data[16] and data[17] > data[18]:
        peaks.append(data[17])
    elif data[18] > data[17] and data[18] > data[19]:
        peaks.append(data[18])
    elif data[19] > data[18] and data[19] > data[20]:
        peaks.append(data[19])
     

peak()
print(peaks)
    
    
     

    



