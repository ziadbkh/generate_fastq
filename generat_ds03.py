from generate_fastq import *
import os

#replace paths
output_dir = "/mnt/d/DS03"

sample_sheet = """
sample_id	i7	i5	template	i7_rc	i5_rc	read_cnt
SAM-00397	CGCTACAT	AACCTACG	i58:um8:i78	1	1	14553251
SAM-00398	AATCCAGC	GCATCCTA	i58:um8:i78	1	1	14906296
SAM-00399	CGTCTAAC	CAACGAGT	i58:um8:i78	1	1	18801164
SAM-00400	AACTCGGA	TGCAAGAC	i58:um8:i78	1	1	16930706
SAM-00401	GTCGAGAA	CTTACAGC	i58:um8:i78	1	1	22784247
SAM-00402	ACAACAGC	ACCGACAA	i58:um8:i78	1	1	15013062
SAM-00403	ATGACAGG	ACATGCCA	i58:um8:i78	1	1	33225009
SAM-00404	GCACACAA	GAGCAATC	i58:um8:i78	1	1	15575894
SAM-00405	CTCCTAGT	CCTCATCT	i58:um8:i78	1	1	16418066
SAM-00406	TCTTCGAC	TACTGCTC	i58:um8:i78	1	1	16159159
SAM-00407	GACTACGA	TTACCGAC	i58:um8:i78	1	1	17452971
SAM-00408	ACTCCTAC	CCGTAACT	i58:um8:i78	1	1	15663510
SAM-00409	CTTCCTTC	TTCCAGGT	i58:um8:i78	1	1	18864116
SAM-00410	ACCATCCT	CCATGAAC	i58:um8:i78	1	1	12419827
SAM-00411	CGTCCATT	TTCCTCCT	i58:um8:i78	1	1	16389088
SAM-00412	AACTTGCC	CCAACTTC	i58:um8:i78	1	1	16631593
SAM-00413	GTACACCT	GAGACCAA	i58:um8:i78	1	1	18303418
SAM-00414	ACGAGAAC	ACAGTTCG	i58:um8:i78	1	1	13542276
SAM-00415	CGACCTAA	CTAACCTG	i58:um8:i78	1	1	18472636
SAM-00416	TACATCGG	TCCGATCA	i58:um8:i78	1	1	17334140
SAM-00417	ATCGTCTC	AGAAGGAC	i58:um8:i78	1	1	15480370
SAM-00418	CCAACACT	GACGAACT	i58:um8:i78	1	1	16627949
SAM-00419	TCTAGGAG	TTGCAACG	i58:um8:i78	1	1	28429338
SAM-00420	CTCGAACA	CCAACGAA	i58:um8:i78	1	1	27282329
SAM-00421	ACGGACTT	ATCGGAGA	i58:um8:i78	1	1	14882704
SAM-00422	CTAAGACC	CCTAACAG	i58:um8:i78	1	1	15156777
SAM-00423	AACCGAAC	CATACTCG	i58:um8:i78	1	1	26298216
SAM-00424	CCTTAGGT	TGCCTCAA	i58:um8:i78	1	1	6988
Undetermined	NNNNNNNN	NNNNNNNN	i58:um8:i78	1	1	12995495

"""
my_files = []
for line in sample_sheet.split("\n"):
    if len(line) < 5 or line.startswith("sample_id"):
        continue
    #print(line.split())
    vals = line.split()
    #vals[6] = 5
    print(f"generating fastq files for sample {vals[0]}...")
    generate_fastq(f"{output_dir}-{vals[0]}", vals[6], 100, vals[1], vals[2], 8, allowed_mismatches=1)
    my_files.append(f"{output_dir}-{vals[0]}")

print("Merging all files ...")
all_files_str = ' '.join([f"{x}_R2.fastq.gz" for x in my_files])
os.system(f"cat {all_files_str} > {output_dir}_R2.fastq.gz")

all_files_str = ' '.join([f"{x}_R1.fastq.gz" for x in my_files])
os.system(f"cat {all_files_str} > {output_dir}_R1.fastq.gz")

print("deleting sample files..")
for f in my_files:
    print(f"deleting {f}_R1/2.fastq.gz...")
    os.system(f"rm {f}_R1.fastq.gz")
    os.system(f"rm {f}_R2.fastq.gz")
