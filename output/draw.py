import matplotlib.pyplot as plt

import pdb

bleu2f = open('./bleu_layers_2.txt', 'r')
bleu4f = open('./bleu_layers_4.txt', 'r')
bleu6f = open('./bleu_layers_6.txt', 'r')
bleu8f = open('./bleu_layers_8.txt', 'r')

loss2f = open('./loss_layers_2.txt', 'r')
loss4f = open('./loss_layers_4.txt', 'r')
loss6f = open('./loss_layers_6.txt', 'r')
loss8f = open('./loss_layers_8.txt', 'r')

bleu2 = [eval(item) for item in bleu2f.readlines()]
bleu4 = [eval(item) for item in bleu4f.readlines()]
bleu6 = [eval(item) for item in bleu6f.readlines()]
bleu8 = [eval(item) for item in bleu8f.readlines()]

loss2 = [eval(item) for item in loss2f.readlines()]
loss4 = [eval(item) for item in loss4f.readlines()]
loss6 = [eval(item) for item in loss6f.readlines()]
loss8 = [eval(item) for item in loss8f.readlines()]

x = [i for i in range(100)]


plt.plot(x, bleu2, label='layers 2')
plt.plot(x, bleu4, label='layers 4')
plt.plot(x, bleu6, label='layers 6')
plt.plot(x, bleu8, label='layers 8')
plt.legend()
plt.savefig('./bleu.png')
plt.clf()

plt.plot(x, loss2, label='layers 2')
plt.plot(x, loss4, label='layers 4')
plt.plot(x, loss6, label='layers 6')
plt.plot(x, loss8, label='layers 8')
plt.legend()
plt.savefig('./loss.png')
plt.clf()

plt.plot(x, loss2, label='layers 2')
plt.plot(x, loss4, label='layers 4')
plt.plot(x, loss6, label='layers 6')
plt.plot(x, loss8, label='layers 8')
plt.xlim(40, 99)
plt.ylim(0, 150)
plt.legend()
plt.savefig('./loss2.png')