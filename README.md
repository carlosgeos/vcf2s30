# VCF 2 S30+

Nokia phones using the [S30+
OS](https://en.wikipedia.org/wiki/Series_30%2B) do not allow multiple
phone numbers per contact.

When importing contacts from a `.vcf` file, only the first phone
number of a contact is kept. This script add extra vCard entries to
the file with the same name + [2|3|4...] so the phone takes it into
account.

## Usage

Add a `Contacts.vcf` to the working dir and:

```sh
$ pipenv install
$ pipenv shell
$ python3 main.py > new_contacts.vcf
$ python3 main.py > backup.dat         # for Nokia 130
```
