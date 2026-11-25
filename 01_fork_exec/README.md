# Program 1
### Introduction to Linux System Calls, Process Creation using fork(), exec() and wait()
## Aim
To study basic Linux/UNIX system calls related to process management and to write
Python programs using fork(), exec() family and wait() system calls to create and
manage child processes.
## Theory
- A process is a program in execution. Every process in UNIX/Linux is identified by a
unique Process ID (PID). The operating system provides system calls to create,
control and terminate processes.
- fork() creates a new process (child) which is an almost exact copy of the calling
(parent) process. It returns 0 in the child, the child's PID in the parent, and -1 on
failure.
- The exec() family of functions (execl, execv, execlp, execvp, execve) replaces the
current process image with a new program. The PID does not change; only the code,
data and stack are replaced.
- wait()/waitpid() suspends execution of the calling process until one of its children
terminates, and allows the parent to collect the child's exit status, preventing
zombie processes.
- getpid() returns the process ID of the calling process; getppid() returns the parent's
process ID.
## Program (Python)
```
import os
import sys
def main():
    print(f"Parent process: PID = {os.getpid()}")
    sys.stdout.flush()
    try:
        pid = os.fork()
    except OSError:
        # fork failed
        print("fork failed")
        return 1
    if pid == 0:
        # Child process
        print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
        print("Child is about to exec 'ls -l'")
        sys.stdout.flush()
        try:
            os.execvp("ls", ["ls", "-l"])
        except OSError as e:
            # exec only returns on error
            print(f"exec failed: {e}")
            os._exit(1)
    else:
        # Parent process
        print(f"Parent waiting for child (PID = {pid}) to finish...")
        sys.stdout.flush()
         _, status = os.wait()
        if os.WIFEXITED(status):
            print(f"Child exited with status {os.WEXITSTATUS(status)}")
        print("Parent process resumes and exits.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
```
## Compilation & Execution
```python3 fork_exec.py```
## Sample Output
```Parent process: PID = 4521
Parent waiting for child (PID = 4522) to finish...
Child process: PID = 4522, Parent PID = 4521
Child is about to exec 'ls -l'
total 24-rwxr-xr-x 1 user user 16824 Sep 3 09:10 fork_exec-rw-r--r-- 1 user user 612 Sep 3 09:09 fork_exec.c
Child exited with status 0
Parent process resumes and exits.```
