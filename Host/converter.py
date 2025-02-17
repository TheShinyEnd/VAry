import av
import wave
import sys
import traceback
from datetime import datetime

def fprint(*args, **kwargs):
    """Prints to console with a timestamp and flushes."""
    print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]", *args, **kwargs)
    sys.stdout.flush()

def mp4_to_wav_converter(input_filepath, output_filepath):
    """Converts an MP4 video file to a WAV audio file using pyav with detailed logging."""
    try:
        fprint(f"Converting '{input_filepath}' to '{output_filepath}'")
        
        fprint(f"Opening input file: {input_filepath}")
        input_container = av.open(input_filepath)
        fprint(f"Input file opened successfully.")

        
        audio_stream = None
        for stream in input_container.streams:
            if stream.type == 'audio':
                audio_stream = stream
                break
        fprint(f"Audio stream obtained")
        if audio_stream is None:
            raise ValueError("No audio stream found in the input MP4 file.")

        
        fprint(f"Opening output file: {output_filepath}")
        output_container = av.open(output_filepath, mode='w')
        fprint(f"Output file opened successfully.")

        
        output_stream = output_container.add_stream("pcm_s16le", rate=audio_stream.rate)  
        fprint(f"Output stream added")

        fprint(f"Starting frame decoding and encoding...")
        
        for frame in input_container.decode(audio_stream):
            try: 
                output_container.mux(output_stream.encode(frame))
            except Exception as frame_encode_error:
                fprint(f"Error encoding frame: {frame_encode_error}") 
                fprint(traceback.format_exc()) 
                
                continue 

        
        fprint(f"Flushing output stream...")
        output_container.mux(output_stream.encode())
        fprint(f"Closing output container...")
        output_container.close()
        input_container.close()
        fprint(f"Conversion completed successfully for: '{input_filepath}' to '{output_filepath}'")
        print(f"Successfully converted '{input_filepath}' to '{output_filepath}'") 
        return True

    except Exception as main_error: 
        fprint(f"An error occurred during conversion process: {main_error}")
        fprint(traceback.format_exc()) 
        print(f"An error occurred: {main_error}") 
        return False
