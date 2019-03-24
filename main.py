import vobject as v

with open('Contacts.vcf', 'r') as contacts:
    contacts_string = contacts.read()

contacts = list(v.readComponents(contacts_string))

new_contacts = ""


def vcard(family, given, tel):
    """Creates a vCard object with the provided elements

    """
    c = v.vCard()
    c.add('n')
    # switch family and given to have GIVEN FAMILY in that order,
    # since Nokia S30+ ignores FN and takes N (which is in FAMILY
    # GIVEN order)
    c.n.value = v.vcard.Name(family=given,
                             given=family)
    c.add('fn')
    c.fn.value = given + " " + family

    c.add('tel')
    c.tel.value = tel

    return c


for elem in contacts:
    # Check if contact has more phone numbers
    try:
        fam = elem.n.value.family
        giv = elem.n.value.given
        tel = elem.tel.value
        new_contact = vcard(fam, giv, tel)
        new_contacts += new_contact.serialize() + "\n"

        extra_tel_numbers = elem.contents['tel']
        if len(extra_tel_numbers) > 1:
            cnt = 2
            for extra_tel in range(1, len(extra_tel_numbers)):
                extra_contact = vcard(fam + " " + str(cnt), giv,
                                      elem.contents['tel'][extra_tel].value)
                cnt += 1

                new_contacts += extra_contact.serialize() + "\n"

    except (KeyError, AttributeError):
        pass

print(new_contacts)
