import sys, subprocess

print(r'<openbox_pipe_menu>')

if len(sys.argv) < 2:
	print(r'<item label="Error (no arg)">')

match sys.argv[1]:
	case "layout":
		current_layout = subprocess.check_output(["xkb-switch"]).upper().decode()
		next_layout = subprocess.check_output(["xkb-switch"]).upper().decode()
		print(rf'<item label="{current_layout} -&gt; {next_layout}">')
		print(rf'</item>')
	case _:
		print(r'<item label="Error (bad arg)">')

print('r</openbox_pipe_menu>')
