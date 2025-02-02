import pandas as pd
import json
import xml.etree.ElementTree as ET
import mysql.connector

def convert_csv_to_horus(input_file, output_file):
    df = pd.read_csv(input_file)
    df.to_csv(output_file, sep='|', index=False)
    print(f"Converted {input_file} to HORUS format and saved as {output_file}")

def convert_json_to_horus(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df.to_csv(output_file, sep='|', index=False)
    print(f"Converted {input_file} to HORUS format and saved as {output_file}")

def convert_xml_to_horus(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    data = [{child.tag: child.text for child in elem} for elem in root]
    df = pd.DataFrame(data)
    df.to_csv(output_file, sep='|', index=False)
    print(f"Converted {input_file} to HORUS format and saved as {output_file}")

def convert_mysql_to_horus(host, user, password, database, table_name, output_file):
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    df.to_csv(output_file, sep='|', index=False)
    conn.close()
    print(f"Converted MySQL table {table_name} to HORUS format and saved as {output_file}")

if __name__ == "__main__":
    convert_csv_to_horus("input.csv", "output_horus.csv")
    convert_json_to_horus("input.json", "output_horus.json")
    convert_xml_to_horus("input.xml", "output_horus.xml")
    convert_mysql_to_horus("localhost", "root", "password", "mydb", "users", "output_horus_mysql.csv")




from PIL import Image
import numpy as np
import wave
import struct

def convert_image_to_horus(image_file, output_file):
    img = Image.open(image_file).convert('L')  # Convert to grayscale
    img_array = np.array(img)
    np.savetxt(output_file, img_array, delimiter='|', fmt='%d')
    print(f"Converted {image_file} to HORUS format and saved as {output_file}")

def convert_audio_to_horus(audio_file, output_file):
    with wave.open(audio_file, 'r') as wav_file:
        frames = wav_file.readframes(wav_file.getnframes())
        audio_data = struct.unpack(f"{wav_file.getnframes()}h", frames)
    np.savetxt(output_file, audio_data, delimiter='|', fmt='%d')
    print(f"Converted {audio_file} to HORUS format and saved as {output_file}")

if __name__ == "__main__":
    convert_image_to_horus("input.jpg", "output_horus_image.txt")
    convert_audio_to_horus("input.wav", "output_horus_audio.txt")
