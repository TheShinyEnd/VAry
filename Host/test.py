import av
import wave
import sys
import traceback
import os
import multiprocessing
from datetime import datetime
import uuid

"""
It took over 3 days to figure out the multiprocessing issue.
I was trying to convert an MP4 video file to a WAV audio file using the PyAV library in a separate process
(When running in the main process, of dvrfy(the intendend script for this conversion)
..it was incredbily slow, the main process had a lot of threads running, thus
..resulting in it being slow, so slow, that i, firstly, thought
..the script has froze/errored).
The conversion process was working fine in the main process, but it was failing in the child process.
After a lot of debugging and research, I found out that a simple 2 liner was causing the issue..
if __name__ == '__main__': multiprocessing.freeze_support().. fml.

This was a script to test my theory and solution, eventually i came to try multiprocessing.freeze_support(), and it worked.
This is why there are so many prints and try-excepts in the code.
"""




def fprint(*args, **kwargs):
    """Prints to console with a timestamp and flushes."""
    print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]", *args, **kwargs)
    sys.stdout.flush()

def mp4_to_wav_converter(input_filepath, output_filepath):
    """
    Converts an MP4 video file to a WAV audio file using pyav with detailed logging.
    """
    success = False
    try:
        fprint(f"Child Process: Converting '{input_filepath}' to '{output_filepath}'")
        fprint(f"Child Process: Opening input file: {input_filepath}")
        input_container = av.open(input_filepath)
        fprint("Child Process: Input file opened successfully.")

        # Get the first audio stream
        audio_stream = next((s for s in input_container.streams if s.type == 'audio'), None)
        fprint("Child Process: Audio stream obtained")
        if audio_stream is None:
            raise ValueError("No audio stream found in the input MP4 file.")

        fprint(f"Child Process: Opening output file: {output_filepath}")
        output_container = av.open(output_filepath, mode='w')
        fprint("Child Process: Output file opened successfully.")

        output_stream = output_container.add_stream("pcm_s16le", rate=audio_stream.rate)
        fprint("Child Process: Output stream added")
        fprint("Child Process: Starting frame decoding and encoding...")

        for frame in input_container.decode(audio_stream):
            try:
                output_container.mux(output_stream.encode(frame))
            except Exception as frame_encode_error:
                fprint(f"Child Process: Error encoding frame: {frame_encode_error}")
                fprint(traceback.format_exc())
                continue

        fprint("Child Process: Flushing output stream...")
        output_container.mux(output_stream.encode())
        fprint("Child Process: Closing output container...")
        output_container.close()
        input_container.close()
        fprint(f"Child Process: Conversion completed successfully for: '{input_filepath}' to '{output_filepath}'")
        print(f"Child Process: Successfully converted '{input_filepath}' to '{output_filepath}'")
        success = True
        return True

    except Exception as main_error:
        fprint(f"Child Process: An error occurred during conversion process: {main_error}")
        fprint(traceback.format_exc())
        print(f"Child Process: An error occurred: {main_error}")
        return False

    finally:
        fprint(f"Child Process: Conversion process finished. Success: {success}")


def convert_mp4_to_wav_pyav_multiprocess(src_path, dst_path):
    """
    Runs the MP4 to WAV conversion in a separate process.
    """
    try:
        process = multiprocessing.Process(
            target=mp4_to_wav_converter,
            args=(src_path, dst_path)
        )
        process.start()
        print(f"Main Process: Conversion process started in multiprocessing for '{src_path}' to '{dst_path}'")
        process.join(timeout=120)  # 2-minute timeout

        if process.is_alive():
            process.terminate()
            process.join()
            print(f"Main Process: Conversion process timed out for '{src_path}' to '{dst_path}'")
            return False, "Conversion timed out"

        if process.exitcode == 0:
            print(f"Main Process: Conversion process exited gracefully for '{src_path}' to '{dst_path}'")
            return True, "Conversion successful"
        else:
            print(f"Main Process: Conversion process failed with exit code {process.exitcode} for '{src_path}' to '{dst_path}'")
            return False, "Conversion failed"

    except Exception as e:
        print(f"Main Process: Error starting conversion process: {str(e)} for '{src_path}' to '{dst_path}'")
        return False, f"Error starting conversion process: {str(e)}"


if __name__ == '__main__':
    # Ensures Windows doesn’t re-run main logic in child processes.
    multiprocessing.freeze_support()

    input_mp4_file = r"C:\Users\Test\Desktop\test.mp4"
    output_wav_file_single = r"C:\Users\Test\Desktop\test_single.wav"
    output_wav_file_multi = r"C:\Users\Test\Desktop\test_multi.wav"

    if not os.path.exists(input_mp4_file):
        print(f"Error: Input MP4 file not found at: {input_mp4_file}")
        sys.exit(1)

    print("\n--- Testing in Single Process ---")
    single_process_success = mp4_to_wav_converter(input_mp4_file, output_wav_file_single)
    if single_process_success:
        print(f"Main Process: Single process conversion successful. WAV file saved at: {output_wav_file_single}")
    else:
        print("Main Process: Single process conversion failed. Check console output for errors.")

    print("\n--- Testing in Multiprocessing ---")
    multi_process_success, multi_process_message = convert_mp4_to_wav_pyav_multiprocess(
        input_mp4_file, output_wav_file_multi
    )
    if multi_process_success:
        print(f"Main Process: Multiprocess conversion successful. WAV file saved at: {output_wav_file_multi}")
    else:
        print(f"Main Process: Multiprocess conversion failed: {multi_process_message}")

    print("\n--- Testing Completed ---")
