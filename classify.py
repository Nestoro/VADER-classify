from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import argparse

args_parser = argparse.ArgumentParser(description='Run VADER classification Task on file')

args_parser.add_argument('--input', type=str, help='input file', required=True)
args_parser.add_argument('--output', type=str, help='output file', required=True)


args = args_parser.parse_args()

output_path = args.output
input_path = args.input

inputFile = open(input_path, 'r')
OutputFile = open(output_path, 'w')

OutputFile.flush()

Lines = inputFile.readlines()

analyzer = SentimentIntensityAnalyzer()
for line in Lines:
    vs = analyzer.polarity_scores(line)
    OutputFile.write(str(vs) + '\n')
    
inputFile.close()
OutputFile.close()