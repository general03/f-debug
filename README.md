# Debugging

## VSCode

You can use the "Run" command and configure the right file

Like this `launch.json`

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python : Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "0"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            
        }
    ]
}
```

## PDB

### Help

```
(Pdb) help
```

### General

Launch the command `python -m pdb file.py`
Use `next` to step up the debugger, from line 1 to line x

### Specific place

Put `pdb.set_trace()` to put breakpoint
Launch the command `python file.py`

### Call function

Inside pdb shell put `pdb.runcall(add, 2)`

### Result

```shell
> /home/david/debug/file.py(7)<module>()
-> comment = 'PDB end file'
(Pdb) print(comment)
PDB breakpoint
```