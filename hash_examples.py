import hashlib
from tabulate import tabulate

# Convert the string to bytes because the library does not support hashing strings

string_to_hash = b'Aperture Cyber example'
salt = b'mysalt'
hashlib_algos = ['md5', 'sha1', 'sha224', 'sha3_224', 'sha256', 'sha3_256', 'sha384', 'sha512', 'sha3_512',]
# hashlib_algos = ['shake_128']

hash_results_list = []

print('Algorithms Guaranteed in hashlib: {}'.format(hashlib.algorithms_guaranteed))
print('Algorithms available in hashlib: {}'.format(hashlib.algorithms_available))
print('String to hash: {}'.format(string_to_hash))
print()

# enumerate through the algorithms available within the hashlib
for hash_algo in hashlib.algorithms_available:
    # print(hash_algo)
    if 'shake' in hash_algo:
        continue
    else:
        # print('{} {} {}'.format(hash_algo, '\t', hashlib.new(hash_algo, string_to_hash).hexdigest()))
        hash_digest = hashlib.new(hash_algo, string_to_hash).hexdigest()
        hash_digest_length = len(hash_digest)
        hash_results_list.append([hash_algo, hash_digest_length, 'N', hash_digest])

# calculate the salted digest using the pbkdf2_hmac algorithm
dk = hashlib.pbkdf2_hmac('sha256', string_to_hash, salt, 100000)
hash_digest = dk.hex()
hash_digest_length = len(hash_digest)
hash_results_list.append(['sha256 (pbkdf2)', hash_digest_length, 'Y', hash_digest])

hash_results_list.sort()

print(tabulate(hash_results_list, headers=['Hash Algorithm', 'Length', 'Salted', 'Hash Digest'], tablefmt='orgtbl'))
