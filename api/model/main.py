import subprocess
from metaflow import Flow
from subprocess import call

def test(un:int,deux:int):
    return un+deux
def essai(un:int,deux:int):
    return un*deux
def launchMyFlow():
    print("jsp")
    subprocess.call(['python','model/flows/hello.py','run'])
    run = Flow('HelloFlow').latest_successful_run
    return
