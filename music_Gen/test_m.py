import os
os.system("melody_rnn_generate \
--config=attention_rnn \
 --bundle_file=attention_rnn.mag \
--output_dir=/Users/singhyogendra/randomgen/AllInOne-Generator/tempmusic \
num_output=20 \
num_steps=200 \
primer_melody='[120]'")
