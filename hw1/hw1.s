##########################################
# Name: Jonathan Chiu
# Email: chiu.j@husky.neu.edu
# Section: WVG 102 TF 9:50am - 11:30am 
# Homework: 1 - Final Revision
# Due: 9/18/2013
##########################################

.data
prompt: 
	.asciiz "Positive integer: "
endPromptA:
	.asciiz "The value of factorial "
endPromptB:
	.asciiz " is:\n"
	.text

main:
	# +--------------------------------------------+
	# | Initiate beginning prompt for user input
	# +--------------------------------------------+
	
	############### prompt
	
	li $v0, 4 # Load the system call for print_str
	la $a0, prompt # Load address of the string to print (the prompt)
	syscall # Print the loaded string
	
	############### Read user input
	
	li $v0, 5 # Load the read_int system call
	syscall # Save user input to $v0
	move $s0, $v0 # Move the user's input (x) from $v0 to $s0 (y) to prepare for factorial function below
		      # y = x
	
	move $s2, $v0 # Save the user's input to $s2 (this is for final answer prep)
	jal factorial # Jump and link to the factorial function || $ra = factorial
	
	# +--------------------------------------------+
	# | Ending prompts to print final answer
	# +--------------------------------------------+
	
	############### endPromptA - "The value of factorial..."
	
	move $s4, $v0 # Save the final result of factorial into $s4
	li $v0, 4 # Load the system call for print_str
	la $a0, endPromptA # Load the address of endPromptA into register $a0
	syscall # Print the string
	
	############### User's original input - "The value of factorial x..."
	
	li $v0, 1 # Load the system call for print_int (in this case, the user's original input)
	move $a0, $s2 # Set $a0 content to be the user's input
	syscall # Print the user's input
	
	############### endPromptB - "The value of factorial x is..."
	
	li $v0, 4 # Load the system call for print_str
	la $a0, endPromptB # Load the address of endPromptB to $a0
	syscall # Print the string
	
	############### Print final answer - "The value of factorial x is factorial(x)"
	
	move $s3, $s4 # Move the final factorial result into $s3
	li $v0, 1 # Load system call for print_int
	move $a0, $s3 # Move contents of $s3 to $a0
	syscall # Print the final answer
	li $v0, 10 # Load the exit system call to prevent an infinite print loop
	syscall # Exit
	
# +--------------------------------------------+
# | Factorial calculations
# +--------------------------------------------+
factorial:
	slti $s1, $s0, 2 # Check to see if user input at $s0 < 2
			 # y < 2
	beq $s1, 1, process # If $s0 < 2, then jump to process
			    # if (y < 2) { process(y); }
	j returnFull # Else, jump to returnFull
		     # else { returnFull(y); }

	jr $ra # After factorial is done, jump back to return address
	       # to prepare for final answer print out
	
############### If $s0 < 2, this process method will process $s0 
############### accordingly with either returnOne or multByOne

process:
	beq $s0, 0, returnOne # If $s0 = 0, jump to returnOne
			      # if (y == 0) { returnOne(y); }
	j multByOne # Jump to multBhOne
		    # else { multByOne(y); }

############### This will only be jumped to if $s0 = 0

returnOne:	
	addi $v0, $zero, 1 # Set return register $v0 to int 1
			   # x = 1
	jr $ra # Jump back to return address of main to print the answer

############### This will only be jumped to if $s0 = 1

multByOne:
	mul $v0, $v0, 1 # Set $v0 to $v0 times 1
			# x = x * 1
	jr $ra # Jump back to return address of main to print the answer

############### If $s0 >= 2, then begin standard factorial calculations and perform recursion

returnFull:
	move $s1, $s0 # Move $s0 (y) to $s1 (z)
		      # z = y
	add $s0, $s1, -1 # Set $s0 to ($s1 - 1)
		      	 # y = z - 1
	mul $v0, $v0, $s0 # Set $v0 to the old $v0 * $s0
			  # x = x * y
	j factorial # Jump back to factorial (recursion)
		    # factorial(y - 1)
