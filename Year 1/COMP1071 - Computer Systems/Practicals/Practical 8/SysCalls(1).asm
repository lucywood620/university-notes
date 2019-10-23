.data
string1: .space 10
string2: .asciiz "Oh:"
var1: .word 1234
.text
.globl main
main:
ori $v0, $0, 5
syscall
lw	$s0, var1
add $a0, $v0, $s0
ori $v0, $0, 1
syscall
ori $v0, $0, 8
la $a0, string1
ori $a1, $0, 10
syscall
la $a0, string2
ori $v0, $0, 4
syscall

ori $v0, $0, 10
syscall
