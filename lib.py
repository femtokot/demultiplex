def filter_and_output(frecord, rrecord, brecord):
    if brecord['sequence'] != "CGATGTAT":
        return 0
    
    start_find=rrecord["sequence"].find("A"*9) 
    if start_find != -1:
        trimed = rrecord["sequence"][24:start_find]
        if len(trimed) >=8:
            print(trimed)
            

def generate_records_from_fastq(file_descriptor_object):
    next_line = lambda: next(file_descriptor_object)
    end_of_file_flag = False
    while not end_of_file_flag:
        try:
            yield {
                "identifier_string": str.strip(next_line()),
                "sequence": str.strip(next_line()),
                "quality_marker": str.strip(next_line()),
                "quality_string": str.strip(next_line()),
            }
        except StopIteration:
            end_of_file_flag = True


def wrapper(forward, reverse, barcode):
    forward_records = generate_records_from_fastq(forward) 
    reverse_records = generate_records_from_fastq(reverse) 
    barcode_records = generate_records_from_fastq(barcode)

    frecord = next(forward_records, None)
    rrecord = next(reverse_records, None)
    brecord = next(barcode_records, None)

    while frecord and brecord and rrecord:    
        filter_and_output(frecord, rrecord, brecord)

        frecord = next(forward_records)
        rrecord = next(reverse_records)
        brecord = next(barcode_records)
