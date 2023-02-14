# máx 50kg --------- R$ 4.00 por quilo > máx
pesoPeixes = float(input('Digite o peso dos peixes que pescou em kg: '))

if pesoPeixes > 50:
    excesso = pesoPeixes - 50
    multa = excesso * 4
    print('Seu excesso foi de: {}kg'.format(excesso))
    print('A multa a ser paga é de: R$ {}'.format(multa))
else: 
    print('Você não pagará excesso!')