import random

def create_keyfile(start=34, stop=127, filename=None):
    '''(int, int, str) -> None
    
       Create a secret key. If filename is specified, write the key to the
       named file.
       
       This is provided in case you want to generate new keys.
    '''
    from_list = list(range(start, stop))
    random.shuffle(from_list)
    group_length = random.randint(2,30)
    result = str(group_length) + '\n'
    for coding_char, cipher_char in zip(range(start, stop), from_list):
        result = result + (chr(coding_char) + chr(cipher_char)) + '\n'
    if filename != None:
        file = open(filename, 'w')
        file.write(result)
        file.close()
    else:
        print(result)


def encipher(plaintext, group_length, coding_char_to_ciphered_char):
    '''(str, int, dict of str to str) -> str
    
    '''
    group_length = abs(int(group_length))
    ### STAGE 1: Add the string STOP to the end of the plaintext
    new_text = plaintext + 'STOP'
    ### STAGE 2: Pad the result of stage 1 with spaces so that it is a multiple of n
    if group_length != 0:
        result_remainder = len(new_text) % abs(group_length)   #Find the remaining number result_remainder which equals to len(new_text)mod(group_length)
        if result_remainder != 0:
            new_text = new_text + (abs(group_length) - result_remainder) * ' '   #Pad the result of stage 1 with spaces so that new_text is a multiple of n, where n = group_length
        ### STAGE 3: Group the plaintext in to groups of n and reverse each group
        mothership_list = []
        babyship_list = []
        for letter in new_text:
            babyship_list.append(letter)
            if len(babyship_list) == group_length:   #Check if the length of the babyship_list equals to the group length
                mothership_list.append(babyship_list)
                babyship_list = []   #Redeclare babyship_list as an empty list so we can run the for loop again until we run out of letter from new_text to iterate over
        reversed_new_text = reverse_groups(mothership_list)   #Apply the reverse_groups function on the mothership_list
    else:
        reversed_new_text = new_text   #Do not run STAGE 2 and STAGE 3 operations on new_text
    ###STAGE 4: For each character in the reversed groups, replace each coding character with its corresponding ciphered character from the mapping pairs
    enciphered_text = ''
    for letter in reversed_new_text:
        if letter in coding_char_to_ciphered_char.keys():
            enciphered_text += coding_char_to_ciphered_char[letter]   #If letter is in the list of keys, then concatanate the values of coding_char_to_ciphered_char to the enciphered_text
        else:   
            enciphered_text += letter
    return enciphered_text


def decipher(ciphertext, group_length, coding_char_to_ciphered_char):
    '''(str, int, dict of str to str) -> str
    
    '''
    ### STEP 1: Replace each ciphered character with the original coding character
    deciphered_dict = {}
    for key in coding_char_to_ciphered_char.keys():
        deciphered_dict[coding_char_to_ciphered_char[key]] = key   
    deciphered_text = ''    
    for letter in ciphertext:
        if letter in deciphered_dict.keys():   
            deciphered_text += deciphered_dict[letter]   #Concatanate the values of deciphered_dict to the deciphered_text
        else:   
            deciphered_text += letter
    ### STEP 2: Group the characters into groups of n and reverse each group
    if group_length != 0:
        mothership_list = []   
        babyship_list = []
        for letter in deciphered_text:
            babyship_list.append(letter)
            if len(babyship_list) == group_length:   #Check if the length of the babyship_list equals to group_length
                mothership_list.append(babyship_list)   #If the above boolean is true, append babyship_list to the mothership_list
                babyship_list = []   #Redeclare babyship_list as an empty list so we can run the for loop until we loop over all of the elements in deciphered_text
        reversed_deciphered_text = reverse_groups(mothership_list)   #Use the reverse_groups function to reverse the mothership_list
    else:
        reversed_deciphered_text = deciphered_text
    ### STEP 3/4: Strip off empty spaces from the end of the string/Remove the word "STOP" from the end of the string
    return reversed_deciphered_text.strip()[:-4]   #Return the reversed_deciphered_text the 'STOP' deleted    
    
    
def reverse_groups(list_of_groups):
    '''(list of [list of str]) -> str
    
       Returns a string that contains the reversed groups of some text.
       The original lists must remain unmodified.
       
       >>> reverse_groups([['A', 'B', 'C'], ['D', 'E', 'F']])
       'CBAFED'
       
    '''
    output_string = ''
    for sub_list in list_of_groups:
        sub_list.reverse()   #Reverse elements in sub_list list
        for letter in sub_list: 
            output_string += letter   #Concatanate each item letter from the list sub_list to the string output_string          
    return output_string
    
    
def get_key(file):
    '''(file open for reading) -> tuple of objects
    
       Return a tuple containing an int of the group length and a dictionary of
       mapping pairs.
    '''
    pair_dict = {}
    group_length = int(file.readline().strip())   #Read every single line of the file, delete empty space before and after the text in a read line, and get an int of the group length contained in a read line
    letter_pair_list = file.readlines()   #Read the lines in a in a file to receive a list containing pairs of letters
    for pair in letter_pair_list:   
        plain_pair = pair.strip('\n')   #For pair in letter_pair_list, strip pair of breaks
        pair_dict[plain_pair[0]] = plain_pair[1]
    return (group_length, pair_dict)
    

def get_key_file():
    '''() -> file open for reading
    
       Return the key file.
    '''
    return open(input("Enter the name of the key file: "), 'r')


def get_text_filename():
    '''() -> str
    
       Return the name of the file containing the plaintext or cipher text.
    '''
    
    return input("Enter the file to read: ")


def process(filename, group_length, coding_char_to_ciphered_char):
    '''
    
       If the filename provided ends in '.txt', encipher its contents and
       store the results in a new file with the same name, except with
       '.txt' replaced with '.enc'. If the filename does not end in '.txt',
       decipher the file's contents and print it to the screen.
    '''
    if filename.endswith('.txt'):
        file_old_txt = open(filename, 'r')   
        plaintext = file_old_txt.read()
        enciphered_txt = encipher(plaintext, group_length, coding_char_to_ciphered_char)
        new_filename = filename[:-4] + '.enc'   #Create a new file with .enc parameter by modifying the filename.txt file
        new_enc_file = open(new_filename, 'w')   #Open and write to new_filename
        new_enc_file.write(enciphered_txt)   #Write enciphered text to new_enc_file
        new_enc_file.close()   
        file_old_txt.close()   
    else:
        file_old_enc = open(filename, 'r')
        ciphertext = file_old_enc.read()   
        print(decipher(ciphertext, group_length, coding_char_to_ciphered_char))

if __name__ == '__main__':
    # Read a keyfile
    (group_length, coding_char_to_ciphered_char) = get_key(get_key_file())
    # Encipher/decipher a file using the key data obtained from the keyfile.
    process(get_text_filename(), group_length, coding_char_to_ciphered_char)
