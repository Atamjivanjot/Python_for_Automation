import subprocess

print("===== SYSTEM HEALTH CHECK =====")

print("\nDISK SPACE:")
subprocess.run(
    'powershell "Get-PSDrive -PSProvider FileSystem"',
    shell=True
)

print("\nMEMORY:")
subprocess.run(
    'powershell "Get-CimInstance Win32_OperatingSystem | Select TotalVisibleMemorySize,FreePhysicalMemory"',
    shell=True
)

print("\nUPTIME:")
subprocess.run(
    'powershell "(Get-Date) - (gcim Win32_OperatingSystem).LastBootUpTime"',
    shell=True
)