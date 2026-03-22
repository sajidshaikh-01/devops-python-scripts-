import subprocess

pods = subprocess.check_output(["kubectl", "get", "pods"]).decode()

for line in pods.split("\n"):
    if "CrashLoopBackOff" in line:
        pod_name = line.split()[0]
        subprocess.run(["kubectl", "delete", "pod", pod_name])
        print("Restarted pod:", pod_name)
