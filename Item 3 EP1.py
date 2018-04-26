#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:51:16 2018

@author: gabrielzezze
"""

import json
with open ('teste.txt', 'r') as arquivo:
    Estoque = json.loads(arquivo.read())
    
Estoque = {}
while True:
    print("Controle de Estoque: ")
    print("0 - Sair")
    print("1 - Adicionar Item")
    print("2 - Remover Item")
    print("3 - Alterar Item")
    print("4 - Imprimir Estoque")
    x = int(input("Faca sua escolha? "))
    if x == 0:
        print("Ate mais!")
        break
    elif x == 1:
        produto = (input("Nome do Produto: "))
        quantidade1 = int(input("Quantidade inicial: "))
        precouni = float(input("Preco unitario: "))
        if produto not in Estoque:
            while quantidade1 < 0:
                print("Quantidade inicial nao pode ser negativa! ")
                quantidade1 = int(input("Quantidade Inicial: "))
                if quantidade1 > 0:    
                    break
            while precouni < 0:
                print("Preco nao pode ser negativo! ")
                precouni = float(input("Preco unitario: "))
                if precouni > 0:
                    break
            Estoque[produto] = quantidade1
            Estoque["Preco unitario {}".format(produto)] = precouni
            
        else:
            print("Produto ja cadastrado! ")
    elif x == 2:
        produto = input("Nome do Produto: ")
        if produto in Estoque:
            del Estoque[produto]
            del Estoque["Preco unitario {}".format(produto)]
        else:
            print("Elemento nao encontrado! ")
    elif x == 3:
        produto2 = input("Nome do Produto a ser alterado: ")
        if produto2 in Estoque:
            w = input("Deseja alterar a quantidade?(S/N) ")
            if w == "S":
                quantidade2 = int(input("Nova Quantidade: "))                                    
                Estoque[produto2] += quantidade2
            y = input("Deseja alterar preco(S/N): ")
            if y == "S":
                precouni2 = float(input("Novo Preco: "))
                Estoque["Preco unitario {}".format(produto2)] = precouni2
                                                                        
        elif produto2 not in Estoque:
            print("Produto nao Cadastrado! ")                
    elif x == 4:
        print(Estoque)