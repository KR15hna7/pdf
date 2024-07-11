import subprocess, base64, sys, os

cwd = os.getcwd()

doc = "\M246"
original_folder_path = cwd + '\Pages' + doc + '\Original'
generated_folder_path = cwd + '\Pages' + doc + '\Incorrect'

original_files = os.listdir(original_folder_path)
generated_files = os.listdir(generated_folder_path)

if original_files == generated_files:
    print("Original and Generated File Names Match")
else:
    print("Original and Generated File Names Do Not Match")
    original_set = set(os.listdir(original_folder_path))
    generated_set = set(os.listdir(generated_folder_path))
    missing_in_generated = original_set - generated_set
    missing_in_original = generated_set - original_set
    print("Missing in Generated files: ", missing_in_generated)
    print("Missing in Original files: ", missing_in_original)
    sys.exit(1)
print("print only on match")

for item in original_files:
    command = f''' 
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

    $original_dir = "$(pwd)\Pages{doc}\Original\{item}"
    $generated_dir = "$(pwd)\Pages{doc}\Incorrect\{item}"
    $report_dir = "$(pwd)\Pages\Reports{doc}\{item}"

    echo $original_dir
    echo $generated_dir
    echo $report_dir
    
    E:\Software\comparepdfcmd\comparepdfcmd -C E:\Software\comparepdfcmd\example.ini -r $report_dir $original_dir $generated_dir
    '''

    commandBase64 = base64.b64encode(command.encode("utf-16-le")).decode()
    proc = subprocess.run( f"powershell.exe -EncodedCommand {commandBase64}", capture_output=True, encoding="utf-8", shell=True)
    print(proc.stdout)
    # print(proc.stderr)
    # print(proc.stdout.strip().split("/"))