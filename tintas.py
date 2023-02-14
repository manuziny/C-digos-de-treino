metros = float(input('Digite o tamanho em metros que deseja pintar:'))
metrosLitro = 3
litrosLata = 18

# 1L -----3
#  x ----- 30 = 10 Litros
# 3x = 30
# x = 10 L

# 1 lata ------18L e R$ 80.00
# x ------ 10L
# 18x = 10
# x = 10/18

if metros > metrosLitro:
    qntsLitros = metros / 3
    qntsLatas = qntsLitros / 18
    while qntsLatas > 1:
        contador = qntsLatas
        qntaPagar = 80 * qntsLatas
        print('Precisará de: {} latas'.format(contador))
        print('Pagará: R$ {}'.format(qntaPagar))
        break
    else:
        print('Precisará: de 1 lata e 80 reais')
else:
    print('Precisará de: 1 lata e 80 reias')
