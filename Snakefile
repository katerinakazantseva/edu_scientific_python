rule all:
    input: "input/input"
    output: "output/output"
    shell: "cat {input} | wc -w > {output}"                                              
