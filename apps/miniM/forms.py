from django import forms

from apps.miniM.models import miniM

class miniM(forms.ModelForm):

	class Meta:
		model = miniM

		fields = [
			'Orientacion1',
			'Orientacion2',
			'Orientacion3',
			'Orientacion4',
			'Orientacion5',
			'Espacial1',
			'Espacial2',
			'Espacial3',
			'Espacial4',
			'Espacial5',
			'fijacion',
			'calculo',
			'recuerdo',
			'lenguaje1',
			'lenguaje2',
			'lenguaje3',
			'lenguaje4',
			'lenguaje5',
			
		]
		labels = {
			'Orientacion1': '¿En qué año estamos 2022?',
			'Orientacion2': '¿En qué estación?',
			'Orientacion3': '¿En qué día (fecha)?',
			'Orientacion4': '¿En qué mes?',
			'Orientacion5': '¿En qué día de la semana?',
			'Espacial1': '¿En qué año estamos?',
			'Espacial2': '¿En qué estación?',
			'Espacial3': '¿En qué día (fecha)? ',
			'Espacial4': '¿En qué mes? ',
			'Espacial5': '¿En qué día de la semana?',
			'fijacion': 'Nombre tres palabras Peseta-Caballo-Manzana (o Balón- Bandera-Arbol) a razón de 1 por segundo. Luego se pide al paciente que las repita. Esta primera repetición otorga la puntuación. Otorgue 1 punto por cada palabra correcta, pero continúe diciéndolas hasta que el sujeto repita las 3, hasta un máximo de 6 veces',
			'calculo': '¿Si tiene 30 pesetas y me va dando de tres en tres, ¿Cuántasle van quedando?. Detenga la prueba tras 5 sustraciones. Si el sujeto no puede realizar esta prueba, pídale que deletree la palabra MUNDO al revés.? ',
			'recuerdo': 'Preguntar por las tres palabras mencionadas anteriormente',
			'lenguaje1': 'DENOMINACIÓN. \n Mostrarle un lápiz o un bolígrafo y preguntar ¿qué es esto?. Hacer lo mismo con un reloj de pulsera',
			'lenguaje2': 'REPETICIÓN. Pedirle que repita la frase: "ni sí, ni no, ni pero" (o “En un trigal había 5 perros”)',
			'lenguaje3': 'ÓRDENES. Pedirle que siga la orden: "coja un papel con la mano derecha, dóblelo por la mitad, y póngalo en el suelo"',
			'lenguaje4': 'Coje con mano d. 0-1 dobla por mitad 0-1 pone en suelo 0-1 .LECTURA. Escriba legiblemente en un papel "Cierre los ojos". Pídale que lo lea y haga lo que dice la frase ', 
			'lenguaje5': 'ESCRITURA. Que escriba una frase (con sujeto y predicado)',
			
		}
		widgets = {
			'Orientacion1': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion2': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion3': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion4': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion5': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial1': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial2': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial3': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial4': forms.TextInput(attrs={'class':'form-control'}),
			'Espacial5': forms.TextInput(attrs={'class':'form-control'}),
			'fijacion': forms.TextInput(attrs={'class':'form-control'}),
			'calculo': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje1': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje2': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje3': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje4': forms.TextInput(attrs={'class':'form-control'}),
			'lenguaje5': forms.TextInput(attrs={'class':'form-control'}),
		}