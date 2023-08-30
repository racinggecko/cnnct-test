class Compiler:
    def __init__(self):
        self.generated_code = []
        self.variables = {}
        self.functions = {}

    def compile(self, source_code):
        lines = source_code.split('\n')
        for line in lines:
            if line.strip():
                self.process_line(line)

    def process_line(self, line):
        if line.startswith("print"):
            content = line.split('{')[1].split('}')[0]
            content = self.replace_variables(content)
            self.generate_print(content)
        elif line.startswith("new var_"):
            var_name, value = line.split(':')[0][8:], line.split(':')[1]
            self.generate_variable(var_name, value)
        elif line.startswith("new fx"):
            fx_name = line.split(' ')[2]
            self.generate_function(fx_name)
        elif line.startswith("call fx"):
            fx_name = line.split(' ')[2]
            self.generate_function_call(fx_name)

    def generate_print(self, content):
        self.generated_code.append(f'print({content})')

    def generate_variable(self, var_name, value):
        self.variables[var_name] = value
        self.generated_code.append(f'{var_name} = {value}')

    def generate_function(self, fx_name):
        self.functions[fx_name] = []
        self.generated_code.append(f'def {fx_name}():')
        
    def generate_function_call(self, fx_name):
        self.generated_code.append(f'{fx_name}()')

    def replace_variables(self, content):
        for var_name, value in self.variables.items():
            content = content.replace(f'{{{var_name}}}', str(value))
        for fx_name in self.functions:
            content = content.replace(f'{{call fx {fx_name}}}', f'{fx_name}()')
        return content


    def execute_generated_code(self):
        generated_code = '\n'.join(self.generated_code)
        exec(generated_code, self.variables, self.functions)

if __name__ == "__main__":
    print("Enter your Cnnct code. Type 'cnnct.break' on a new line to finish.")
    source_code = ""
    while True:
        line = input()
        if line.strip() == 'cnnct.break':
            break
        source_code += line + '\n'

    my_compiler = Compiler()
    my_compiler.compile(source_code)
    my_compiler.execute_generated_code()
