.data
fimenos2: 	.double 2.0
fimenos1: 	.double 1.0
gimenos2: 	.double 1.0
gimenos1: 	.double 2.0
fi: 		.double 0.0
gi: 		.double 0.0
fnmenos2: 	.double 0.0
gnmenos2: 	.double 0.0
n: 			.word 0
entreN:		.asciiz "n = "
funcao1:	.asciiz "F(n-2) + G(n+200) = "
funcao2:	.asciiz " e F(n+200)- G(n-2) = "
invalida:	.asciiz "Entrada invalida!"

.text
#imprime n =
li $v0, 4
la $a0, entreN
syscall

#obtem n
li $v0, 5
syscall
sw $v0, n

#verifica n > 2
lw $t0, n
bgt $t0, 2, passo1
j done

passo1:		#calcula F(n-2) e G(n-2)
beq $t0, 3, pega_n1
beq $t0, 4, pega_n2
j calcula1

pega_n1: 	#caso n - 2 = 1
li $t1, 1
l.d $f2, fimenos2
s.d $f2, fnmenos2
l.d $f2, gimenos2
s.d $f2, gnmenos2
j passo2

pega_n2: 	#caso n - 2 = 2
li $t1, 2
l.d $f2, fimenos1
s.d $f2, fnmenos2
l.d $f2, gimenos1
s.d $f2, gnmenos2
j passo2

calcula1: 	#caso n - 2 > 2
li $t1, 3 	#for( int i = 3; ...
loop1: 		
bgt $t1, $t0, saida1	# i <= (n-2); ...

#calcula F(i)
l.d $f2, fimenos1
l.d $f4, gimenos2
add.d $f2, $f2, $f2
add.d $f2, $f2, $f4
s.d $f2, fi

#calcula G(i)
l.d $f2, gimenos1
l.d $f4, fimenos2
add.d $f2, $f2, $f4
add.d $f2, $f2, $f4
add.d $f2, $f2, $f4
s.d $f2, gi

#ajusta para proximo passo do for
l.d $f2, fimenos1
s.d $f2, fimenos2
l.d $f2, fi
s.d $f2, fimenos1
l.d $f2, gimenos1
s.d $f2, gimenos2
l.d $f2, gi
s.d $f2, gimenos1

addi $t1, $t1, 1	# i++){
j loop1
saida1:			# }
l.d $f2, fimenos1
s.d $f2, fnmenos2
l.d $f2, gimenos1
s.d $f2, gnmenos2

passo2:		#calcula F(n+200) e G(n+200)
beq $t1, 1, condicao1	#for( int i = 1,
beq $t1, 2, condicao2	#for( int i = 2,
addi $t0, $t0, 202	#for( int i de onde parou no ultimo for
j loop2

condicao1:
li $t0, 203
li $t1, 3
j loop2

condicao2:
li $t0, 204
li $t1, 3
j loop2

loop2: 		
bgt $t1, $t0, saida2	# i <= (n+200); ...

#calcula F(i)
l.d $f2, fimenos1
l.d $f4, gimenos2
add.d $f2, $f2, $f2
add.d $f2, $f2, $f4
s.d $f2, fi

#calcula G(i)
l.d $f2, gimenos1
l.d $f4, fimenos2
add.d $f2, $f2, $f4
add.d $f2, $f2, $f4
add.d $f2, $f2, $f4
s.d $f2, gi

#ajusta para proximo passo do for
l.d $f2, fimenos1
s.d $f2, fimenos2
l.d $f2, fi
s.d $f2, fimenos1
l.d $f2, gimenos1
s.d $f2, gimenos2
l.d $f2, gi
s.d $f2, gimenos1

addi $t1, $t1, 1	# i++){
j loop2
saida2:	

#calcula F(n-2) + G(n+200)
l.d $f0, fnmenos2
l.d $f2, gimenos1
add.d $f0, $f0, $f2

#(e imprime)
li $v0, 4
la $a0, funcao1
syscall
li $v0, 3
mov.d $f12, $f0
syscall

# e F(n+200) - G(n-2)
l.d $f0, fimenos1
l.d $f2, gnmenos2
sub.d $f0, $f0, $f2

#(e imprime)
li $v0, 4
la $a0, funcao2
syscall
li $v0, 3
mov.d $f12, $f0
syscall

li $v0, 10
syscall

done:	#pulo pro final do programa
li $v0, 4
la $a0, invalida
syscall

li $v0, 10
syscall