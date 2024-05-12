


#Leer un archivo dicom
dcm_data = pydicom.dcmread(r'Datos\000000.dcm')
dcm_data

# Extraer el nombre del paciente ussando su etiqueta DICOM única (0010, 0010)
dcm_data[0x0010 , 0x0010]
dcm_data[0x0010 , 0x0010].value

# Extraiga los atributos relacionados con la etiqueta 0x0028, estos están relacionados con ImagePixel
dcm_data.group_dataset (0x0028)

# Píxeles de la imagen
dcm_data.pixel_array

# Representación de la imagen
im = dcm_data.pixel_array
plt.imshow(im, cmap= 'gray' )
plt.axis( 'off' )
plt.title( 'Corte axial de una TC de tórax' )
plt.colorbar()
plt.show()

#Accedemos a las etiquetas que queremos anonimizar
data_elements = ['PatientID','PatientBirthDate']
for i in data_elements:
    print(dcm_data.data_element(i))
    dcm_data[i].value = 'Anonimo'
    print(dcm_data.data_element(i))

#Para guardar la imagen modificada
dcm_data.save_as('nueva_imagen.dcm')

dcm_data['PatientID'].value='anonimo'







