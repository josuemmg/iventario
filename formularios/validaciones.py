from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

def validate_descripcion(value):
    if " " in value or value == "":
        raise ValidationError(
        	_('No se puede crear un campo sin un nombre. porfavor ingrese uno'))
    return value

def validate_fecha(value):
	"""ToDo"""

def validar_placa(value):
	if value.isalnum() == False:
		raise ValidationError('La placa solo puede contener solo letras y numeros')
		return value
	else:
		return value

def espacios(value):
    if value.count(" ") > 0:
        raise ValidationError('NO se  puede contener espacios en blanco')
        return value
    else:
        return value


def validate_cedula(value):
	if(len(value)!=10 or not value.isdigit()):
		raise ValidationError(
            _('%(value)s no es una cédula válida'),
            code="invalid",
            params={'value': value},
        )
	else:
		impares = int(value[1]) + int(value[3]) + int(value[5]) + int(value[7])
		pares = 0
		for i in range(0,9):
			if(i%2==0):
				res = int(value[i])*2
				if(res>=10):
					res = res-9
				pares = pares+res
		total = impares+pares
		dig_validador = (((total+10)//10)*10)-total
		if(dig_validador==10):
			dig_validador = 0
		if (not(int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[-1])==dig_validador)):
			raise ValidationError(
	            _('%(value)s no es una cédula válida'),
	            code="invalid",
	            params={'value': value},
	        )