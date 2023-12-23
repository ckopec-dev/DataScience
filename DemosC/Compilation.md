
# Pre-process to stdout
`$ gcc -E Compilation.c`

# Pre-process to file
`$ gcc -E -o Compilation_pp.c Compilation.c`

# Compile to assembly
`$ gcc -S Compilation.c`

# Compile to object file
`$ gcc -c Compilation.s`

# Compile to executable
`$ gcc -o Compilation Compilation.o`

# Run executable
`$ ./Compilation`