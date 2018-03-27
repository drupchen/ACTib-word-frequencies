import os
import re
from collections import defaultdict

os.makedirs('./output/', exist_ok=True)
in_dir = 'ACTib'
out_dir = 'output'
# for collection in os.listdir(in_dir):
#     for f in os.listdir('{}/{}'.format(in_dir, collection)):
#         current_freqs = defaultdict(int)
#
#         with open('{}/{}/{}'.format(in_dir, collection, f)) as g:
#             content = g.readlines()
#             for line in content:
#                 # very approximate attempt to turn affixed particle segmentation into words
#                 # to fit in pybo's syllabled approach
#                 line = re.sub(r'([^་]) ((འེ|ས|ར|འམ|འང|འོ|འིའོ)[་།])', r'\1\2', line)
#                 for word in line.split():
#                     current_freqs[word] += 1
#
#         entries = ((key, freq) for key, freq in current_freqs.items())
#         entries = sorted(entries, key=lambda x: x[1], reverse=True)
#         os.makedirs('{}/{}'.format(out_dir, collection), exist_ok=True)
#         with open('{}/{}/{}_freqs.txt'.format(out_dir, collection, f), 'w') as h:
#             for entry in entries:
#                 word, freq = entry
#                 h.write('{}\t{}\n'.format(word, freq))
#
# for collection in os.listdir(out_dir):
#     if not os.path.isfile('{}/{}'.format(out_dir, collection)):
#         collection_freqs = defaultdict(int)
#         for f in os.listdir('{}/{}'.format(out_dir, collection)):
#             with open('{}/{}/{}'.format(out_dir, collection, f)) as g:
#                 content = g.readlines()
#                 for line in content:
#                     word, freq = line.split()
#                     collection_freqs[word] += int(freq)
#
#         entries = ((key, freq) for key, freq in collection_freqs.items())
#         entries = sorted(entries, key=lambda x: x[1], reverse=True)
#         with open('{}/{}_freqs.txt'.format(out_dir, collection), 'w') as h:
#             for entry in entries:
#                 word, freq = entry
#                 h.write('{}\t{}\n'.format(word, freq))

actib_freqs = defaultdict(int)
for freq in os.listdir(out_dir):
    if os.path.isfile('{}/{}'.format(out_dir, freq)):
        with open('{}/{}'.format(out_dir, freq)) as g:
            content = g.readlines()
            for line in content:
                word, freq = line.split()
                actib_freqs[word] += int(freq)

entries = ((key, freq) for key, freq in actib_freqs.items())
entries = sorted(entries, key=lambda x: x[1], reverse=True)
with open(out_dir+'/total_freqs.txt', 'w') as h:
    for entry in entries:
        word, freq = entry
        h.write('{}\t{}\n'.format(word, freq))
