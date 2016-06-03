from tkinter import Button
from front.module import Module
from front.dialogs import TextDialog


class ActionBarManager():
    def __init__(self, frame, schema_module, window):
        self.frame = frame
        self.schema_module = schema_module
        self.create_buttons()
        self.window = window

    def create_buttons(self):
        new_module_but = Button(self.frame, text="New Module ...",
                                command=self.new_module_action)
        new_module_but.pack(pady=2)
        save_button = Button(self.frame, text="Save",
                             command=self.save_action)
        save_button.pack(pady=2)
        compile_button = Button(self.frame, text="Compile",
                                command=self.compile_action)
        compile_button.pack(pady=2)

    def new_module_action(self):
        new_module_dialog = TextDialog(self.window,
                                       "Choose new module name", "Module name")

        self.window.wait_window(new_module_dialog.dialog)

        if new_module_dialog.field_value is not None:
            new_module = Module(new_module_dialog.field_value, self.window.workspace)
            self.schema_module.add_module(new_module)
            self.schema_module.refresh()
            self.create_python_module(new_module)

    def save_action(self):
        # TODO
        print("TODO")

    def compile_action(self):
        # TODO
        print("TODO")

    def create_python_module(self, module):
        open(module.py_file, 'a').close()
