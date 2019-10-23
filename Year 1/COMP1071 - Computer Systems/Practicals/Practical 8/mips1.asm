.data
ourinput: .space 160

.text

.globl main
main:
li $v0, 8
la $a0, ourinput
li $a1, 64
syscall
la $t1, ourinput
la $t2, ourinput
start_of_this_loop:
lb $t3,($t2)
beqz $t3, branch_dest
addu $t2,$t2,1
b start_of_this_loop
subu $t2,$t2,2
sb $0 ($t2)
subu $t2,$t2,1
lb $t4, ($t1)
lb $t5,($t2)
branch_dest:
