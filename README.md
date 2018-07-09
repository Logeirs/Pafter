# Pafter - Password Filterer

Pafter is a python script that filters a password dictionary using a custom password policy.
This idea came from the question of using a dictionary (i.e. rockyou) when you know that half of the passwords aren't matching the policy.


## Details
The way this tool works is by splitting the input dictionary into chunks, which are then processed in parallel using multiprocessing.
The chunk size is what you may want to change according to your needs (size of the dictionary, hardware, etc.). 


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
- Minimum length: 8
- Lowercase only

```$ ./pafter.py rockyou.txt new_dictionary.txt -minl 8 -low```


- Minimum length: 6
- Maximum length 10
- Lowercase included
- Uppercase included
- Numbers included

```$ ./pafter.py rockyou.txt new_dictionary.txt -minl 6 -maxl 10 -low -up -num```


- Fixed length: 8
- Everything included: lowercase, uppecase, numbers, special characters

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

