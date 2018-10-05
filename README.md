# Pafter - Password Filterer

Pafter is a python script that filters a password dictionary using a custom password policy.
This idea came from the question of using a dictionary (i.e. rockyou) when you know that half of the passwords isn't matching the policy.


## Details
The way this tool works is by splitting the input dictionary into chunks, which are then processed in parallel using multiprocessing.
The chunk size is what you may want to change according to your needs (size of the dictionary, hardware, etc.). 


#### Update
Pafter has been updated! The main change is about how the filter was performed.

The initial version allowed you to filter what you wanted and what you did not. As an example, `-low -num` would match **only** passwords with lowercase and numbers, but not those with uppercase or special characters (i.e. "Password1" would not match). This is precise but not practical, because in the real life web applications are unlikely to prevent you from using a range of characters (and if they do, you should run away).

Pafter v2.0 will now consider valid any password matching the password policy, even if they contain characters not explicitly specified. For instance, "password1", "Password1" or "Password1!" would be valid with `-low -num`.


## Download via Git
Run this command to clone from Git:
```git clone https://github.com/Logeirs/Pafter.git```


## Usage
To get a list of options:
```
$ ./pafter.py -h

usage: pafter.py [-h] [-minl MINL] [-maxl MAXL] [-low] [-up] [-num] [-spec]
                 file_input file_output

Password Filterer: Filter a password dictionary by applying a specific password policy.

positional arguments:
  file_input   input file
  file_output  output file

optional arguments:
  -h, --help   show this help message and exit
  -minl MINL   minimum password length
  -maxl MAXL   maximum password length
  -low         include lowercase characters
  -up          include uppercase characters
  -num         include numbers
  -spec        include special characters
```


## Examples
1. Example 1
   - Minimum length: 8
   - [x] Lowercase
   - [ ] Uppercase
   - [ ] Numbers
   - [ ] Special characters

```$ ./pafter.py rockyou.txt new_dictionary.txt -minl 8 -low```

2. Example 2
   - Minimum length: 6
   - Maximum length: 10
   - [x] Lowercase
   - [x] Uppercase
   - [x] Numbers
   - [ ] Special characters

```$ ./pafter.py rockyou.txt new_dictionary.txt -minl 6 -maxl 10 -low -up -num```

3. Example 3
   - Fixed length: 8
   - [x] Lowercase
   - [x] Uppercase
   - [x] Numbers
   - [x] Special characters

```$ ./pafter.py rockyou.txt new_dictionary.txt -minl 8 -maxl 8 -low -up -num -spec```


## Performance tests
The performance tests below were run using rockyou.txt (136Mb) on a Windows 7 VM with 4 CPU cores and 8Go of RAM.
A chunk size of 16Mb or 32Mb gives the fastest results but is quite CPU intensive, compared to 64Mb where it's less intensive but takes nearly twice as much time.

* SIZE_16_MBYTES
```
$ ./pafter.py rockyou.txt new.txt -minl 6 -maxl 10 -low -up -num
[+] Filtering...
[+] Done! Writing results (309112), please be patient...

Executed in 321s


$ ./pafter.py rockyou.txt new.txt -minl 6 -low -up -num -spec
[+] Filtering...
[+] Done! Writing results (52360), please be patient...

Executed in 277s


$ ./pafter.py rockyou.txt new.txt -minl 6 -maxl 8 -low
[+] Filtering...
[+] Done! Writing results (1885369), please be patient...

Executed in 533s
```


* SIZE_32_MBYTES
```
$ ./pafter.py rockyou.txt new.txt -minl 6 -maxl 10 -low -up -num
[+] Filtering...
[+] Done! Writing results (309112), please be patient...

Executed in 323s


$ ./pafter.py rockyou.txt new.txt -minl 6 -low -up -num -spec
[+] Filtering...
[+] Done! Writing results (52360), please be patient...

Executed in 276s


$ ./pafter.py rockyou.txt new.txt -minl 6 -maxl 8 -low
[+] Filtering...
[+] Done! Writing results (1885369), please be patient...

Executed in 532s
```


* SIZE_64_MBYTES
```
$ ./pafter.py rockyou.txt new.txt -minl 6 -maxl 10 -low -up -num
[+] Filtering...
[+] Done! Writing results (309112), please be patient...

Executed in 499s


$ ./pafter.py rockyou.txt new.txt -minl 6 -low -up -num -spec
[+] Filtering...
[+] Done! Writing results (52360), please be patient...

Executed in 425s


$ ./pafter.py rockyou.txt new.txt -minl 6 -maxl 8 -low
[+] Filtering...
[+] Done! Writing results (1885369), please be patient...

Executed in 747s
```

## Contributions
Thanks to Matt for helping me with the tool name :)