#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, string, sys, os
import itertools, hashlib
os.system('clear')
print ('''
    |==================================|
    |                              |    
    | [+] Author: marcos Alexandre     |
    | [+] NickName: Krypton Zero       |
    | [+] Data: 18/03/2017             |
    | [+] Email:systemmendax@gmail.com |
    |==================================|
''')
nome        = 'Python Krypton-md5'
versao     = 'Ainda Em construção'
AUTHOR      = 'Marcos Alexandre'
Descricao = nome + ''' tenta quebrar -> md5, -> sha1 -> sha224 -> sha256 -> sha384 ->  sha512 com método Brute Force'''

CHRS = string.printable.replace(' \t\n\r\x0b\x0c', '')
dicionario_tipos_modulos = {
    'md5'     : 32,
    'sha1'    : 40,
    'sha224'  : 56,
    'sha256'  : 64,
    'sha384'  : 96,
    'sha512'  : 128
}

def ajuda():
    print '\n'+nome
    print 'Author  : {}'.format(AUTHOR)
    print 'versao : {}\n'.format(versao)
    print Descricao
    print '''\nparâmetro:
    -m \t Para tentar com módulo específico escolha.
    -todos \t Para tentar com todos os módulos.
    -c \t Para tentar com caracteres específicos.
    -todos-c \t Para tentar com todos os caracteres.\n\nUsar:
    Especifico Modulos
     Krypton-md5 -m <tipo_de_modulo> <hashed> -c <Caracteres> <min_comprimento> <max_comprimento>
     Krypton-md5 -m md5 d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     Krypton-md5 -m <tipo_de_modulo> <hashed> -todos-c <min_comprimento> <max_comprimento>
     Krypton-md5 -m md5 d73d1e93a306b8230410cbe496ec84bf -ac 1 2

    TODOS OS MÓDULOS
     Krypton-md5 -todos <hashed> -c <Caracteres> <min_comprimento> <max_comprimento>
     Krypton-md5 -todos d73d1e93a306b8230410cbe496ec84bf -c ABC 1 2

     Krypton-md5 -todos <hashed> -ac <min_comprimento> <max_comprimento>
     Krypton-md5 -todos d73d1e93a306b8230410cbe496ec84bf -todos-c 1 2
    .
    '''

def Decifrador(escolha, tipo_de_modulo, hashed, chrs, min_comprimento, max_comprimento):
    if tipo_de_modulo in dicionario_tipos_modulos.keys():
        Improvisar_modulo = getattr(hashlib, '{}'.format(tipo_de_modulo))
    else:
        print '\n O `{}` não existe no módulo de lista! \n Por favor tente isto: {}\n'.format(tipo_de_modulo, dicionario_tipos_modulos.keys())
        sys.exit()
    if min_comprimento > max_comprimento:
        print '\n Min-comprimento deve ser maior que Max-comprimento ou como o mesmo que com Max-comprimento.\n'
        sys.exit()
    if len(hashed) not in dicionario_tipos_modulos.values():
        print "\n O hash fornecido não corresponde a nenhum bitmap de hashes conhecido."
        print " Comprimento correto para o tipo hases:"
        for k, i in sorted(dicionario_tipos_modulos.iteritems()):
            print ' -', k,':',i
        print ''
        sys.exit()
    if escolha == '-m' and len(hashed) != dicionario_tipos_modulos[tipo_de_modulo]:
        print "\n O hash `{}` não existe em `{}`. \n Por favor, tente outro tipo!\n".format(hashed, tipo_de_modulo)
        sys.exit()

    Chip_de_resultado_final = ''

    try:
        for n in range(min_comprimento, max_comprimento+1):
            for xs in itertools.product(chrs, repeat=n):
                result_chip = ''.join(xs)
                hash_chip = Improvisar_modulo(result_chip).hexdigest()
                if hashed == hash_chip:
                    Chip_de_resultado_final += result_chip

                    print 'Decrypt encontrado : {}'.format(Chip_de_resultado_final)
                    print 'Tipo Decrypt : {}'.format(tipo_de_modulo)
                    print 'Fim do tempo  : {}\n'.format(time.strftime('%H:%M:%S'))
                    sys.exit()
                else:
                    print '  Esta é parte mais demorada então espere'
                    print '\t{} {}\n'.format(nome, versao)
                    print 'CTRL+C Para Sair!'
                    print 'caracteres para tentar : {}'.format(chrs)
                    print 'Min-Comprimento        : {}'.format(min_comprimento)
                    print 'Max-Comprimento        : {}'.format(max_comprimento)
                    if escolha == '-todos':
                        print 'Tipo Decrypt encontrado : {}'.format(tipo_de_modulo)
                    else:
                        print 'Tipo de Criptografia : {}'.format(tipo_de_modulo)
                    print 'Tentando Com: {} - {}'.format(result_chip, hash_chip)
                    time.sleep(0.01)
                    print("\033c")
    except KeyboardInterrupt:
        print 'Acabou!!!\n'
        sys.exit()

    if Chip_de_resultado_final == '':
        print 'Não Encontrado!'
        print 'Fim de Tempo: {}\n'.format(time.strftime('%H:%M:%S'))
        sys.exit()
    else: pass

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 8: ajuda()
    elif sys.argv[1] == '-m':
        try:
            if sys.argv[4] == '-todos':
                Decifrador(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5], int(sys.argv[6]), int(sys.argv[7]))
            elif sys.argv[4] == '-todos-c':
                Decifrador(sys.argv[1], sys.argv[2], sys.argv[3], CHRS, int(sys.argv[5]), int(sys.argv[6]))
            else: ajuda()
        except IndexError: ajuda()
    elif sys.argv[1] == '-todos':
        try:
            len_hases = len(sys.argv[2])
            try:
                tipo_de_modulo = dicionario_tipos_modulos.keys()[dicionario_tipos_modulos.values().index(len_hases)]
            except ValueError:
                print "\n O hash fornecido não corresponde a qualquer um dos hashes conhecidos bitmap"
                print " Comprimento correto para o tipo hases:"
                for k, i in sorted(dicionario_tipos_modulos.iteritems()):
                    print ' -', k,':',i
                print ''
                sys.exit()
            if sys.argv[3] == '-c':
                Decifrador(sys.argv[1], tipo_de_modulo, sys.argv[2], sys.argv[4], int(sys.argv[5]), int(sys.argv[6]))
            elif sys.argv[3] == '-todos-c':
                Decifrador(sys.argv[1], tipo_de_modulo, sys.argv[2], CHRS, int(sys.argv[4]), int(sys.argv[5]))
            else: ajuda()
        except IndexError: ajuda()
    else: ajuda()