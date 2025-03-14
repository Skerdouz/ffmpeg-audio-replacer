import subprocess
import argparse
from pathlib import Path

def main():
	parser = argparse.ArgumentParser(description="FFMPEG audio replacer")
	parser.add_argument("video_in", type=Path, help="Video input file")
	parser.add_argument("audio_in", type=Path, help="Audio input file")
	parser.add_argument("ts", type=str, help="Audio start timestamp (hh:mm:ss)")
	parser.add_argument("video_out", type=Path, help="Output file name (with file format)")
	args = parser.parse_args()

	command = f"ffmpeg -i \"{args.video_in}\" -ss {args.ts} -i \"{args.audio_in}\" -c:v copy -map 0:v -map 1:a -shortest \"{args.video_out}\""
	subprocess.run(command, shell=True)

if __name__ == "__main__":
	main()