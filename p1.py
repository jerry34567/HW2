import numpy as np
from util import mod_inv


def decode(cipher, key):
    #TODO
    '''
    Decode cipher with public key.

    Arguments:
        cipher: str, cipher text
        key: str, public key

    Return:
        plain: str, plain text
    '''
    plain = ''
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'
    public_key = np.reshape(key, (-1, 3)).T
    private_key = mod_inv(public_key)
    cipher_text = np.reshape(cipher, (-1, 3)).T
    temp = np.mod(private_key @ cipher_text, 31)
    for i in range (0, temp.shape[1]):
        for j in range (0, temp.shape[0]):
            plain.append(letters[temp[j][i]])
    
    return plain
