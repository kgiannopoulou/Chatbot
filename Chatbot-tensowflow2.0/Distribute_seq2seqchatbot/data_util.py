# coding=utf-8
import json
import os
import re
import jieba
from zhon.hanzi import punctuation
from config import getConfig
import io
import tensorflow as tf


gConfig = {}
gConfig = getConfig.get_config()
conv_path = gConfig['resource_data']
vocab_inp_path = gConfig['vocab_inp_path']
vocab_tar_path = gConfig['vocab_tar_path']
vocab_inp_size = gConfig['vocab_inp_size']
vocab_tar_size = gConfig['vocab_tar_size']
seq_train = gConfig['seq_data']
def predata_util():
 
    if not os.path.exists(conv_path):
        print("找不到需要处理的文件，请确认在train_data文件中是否存在该文件")
  
        for line in f:
            line = line.strip('\n')
            line = re.sub(r"[%s]+" % punctuation, "", line)  # 去除标点符号
            if line == '':
                continue
            if line[0] == gConfig['e']:
                if one_conv:
                    seq_train.write(one_conv[:-1] + '\n')
                    i = i + 1
                    if i % 1000 == 0:
                        print('处理进度：', i)
                one_conv = ""
            elif line[0] == gConfig['m']:
                one_conv = one_conv + str(" ".join(jieba.cut(line.split(' ')[1]))) + '\t'  # 存储一次问或答
    seq_train.close()

def create_vocab(lang, vocab_path, vocab_size):
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=vocab_size, oov_token=3)
    tokenizer.fit_on_texts(lang)
    vocab = json.loads(tokenizer.to_json(ensure_ascii=False))
    vocab['index_word'] = tokenizer.index_word
    vocab['word_index'] = tokenizer.word_index
    vocab['document_count']=tokenizer.document_count
    vocab = json.dumps(vocab, ensure_ascii=False)
    with open(vocab_path, 'w', encoding='utf-8') as f:
        f.write(vocab)
    f.close()
    print("字典保存在:{}".format(vocab_path))

def preprocess_sentence(w):
    w = 'start ' + w + ' end'
    return w
lines = io.open(seq_train, encoding='UTF-8').readlines()
word_pairs = [[preprocess_sentence(w) for w in l.split('\t')] for l in lines]
input_lang, target_lang = zip(*word_pairs)
predata_util()
create_vocab(input_lang,vocab_inp_path,vocab_inp_size)
create_vocab(target_lang,vocab_tar_path,vocab_tar_size)
