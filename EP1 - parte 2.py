#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:58:07 2018

@author: lucasmellis
"""
import json
with open ('Banco-de-Dados.json', 'r') as arquivo:
    dicionario = json.loads(arquivo.read())
    
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
        if produto not in Estoque:
            while quantidade1 < 0:
                print("Quantidade inicial nao pode ser negativa! ")
                quantidade1 = int(input("Quantidade Inicial: "))
                if quantidade1 > 0:    
                    break
            Estoque[produto] = quantidade1
            
        else:
            print("Produto ja cadastrado! ")
    elif x == 2:
        produto = input("Nome do Produto: ")
        if produto in Estoque:
            del Estoque[produto]
        else:
            print("Elemento nao encontrado! ")
    elif x == 3:
        produto2 = input("Nome do Produto a ser alterado: ")
        if produto2 in Estoque:
            quantidade2 = int(input("Nova Quantidade: "))                        
            soma = (quantidade1 + quantidade2)
            Estoque[produto2] = soma                                
        elif produto2 not in Estoque:
            print("Produto nao Cadastrado! ")                
    elif x == 4:
        print(Estoque)

           
            
            
        
    
        
    
    