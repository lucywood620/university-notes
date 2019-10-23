
.data
str:
.asciiz "The sum is = "

.text

.globl main
main:
lui $t1,0xFECD
ori $t1,$t1,0x4563

li $v0, 5
syscall
add $s1, $zero, $v0
li $v0, 5
syscall
addu $s1, $s1, $v0
la $a0, str
li $v0, 4
syscall
move $a0 $s1
li $v0, 1
syscall
j main
li $v0, 10
syscall