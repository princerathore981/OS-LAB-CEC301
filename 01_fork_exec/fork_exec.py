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
