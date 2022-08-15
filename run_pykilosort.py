from pykilosort import run,add_default_handler, np1_probe, np2_probe, np2_probe_sglx
from pathlib import Path,WindowsPath
#from pykilosort.main import run
import sys

data_path = sys.argv[1]
output_path = sys.argv[2]
meta_path = sys.argv[3]




add_default_handler(level='INFO')
run(Path(data_path), dir_path=Path(output_path), probe=np2_probe_sglx(Path(meta_path)), low_memory=True)