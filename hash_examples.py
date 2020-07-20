import hashlib

# Convert the string to bytes because the library does not support hashing strings

string_to_hash = b'Aperture Cyber examples'
hashlib_algos = ['md5', 'sha1', 'sha224', 'sha3_224', 'sha256', 'sha3_256', 'sha384', 'sha512', 'sha3_512',]
#hashlib_algos = ['shake_128']


print(hashlib.algorithms_guaranteed)

for hash_algo in hashlib_algos:
    print('{} {} {}'.format(hash_algo, '\t', hashlib.new(hash_algo, string_to_hash).hexdigest()))

print('Algorithms available in hashlib: {}'.format(hashlib.algorithms_available))
for hash_algo in hashlib.algorithms_available:
    print('{} {} {}'.format(hash_algo, '\t', hashlib.new(hash_algo, string_to_hash).hexdigest()))
