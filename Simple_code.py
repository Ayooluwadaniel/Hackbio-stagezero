# Team Information Script

team = [
    {
        "name": "Ayooluwa Daniel Onajoko",
        "slack_username": "Ayooluwa Daniel",
        "country": "Nigeria",
        "hobby": "Playing Chess",
        "affiliations": "Nigerian Institute of Medical Research (NIMR)",
        "DNA sequence": "ATGGGTCACAGCGGCAGATAAAAGCAGGTGCGTCCTTGTTCGAGAGTCTGCGTCCTC"
    },
    {
        "name": "Aworetan Olamide",
        "slack_username": "Olamide_etan",
        "country": "Nigeria",
        "hobby": "Swimming",
        "affiliations": "Kazlat Public Analyst Laboratory",
        "DNA sequence": "ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTAT"
    },
    {
        "name": "Faith Omondi",
        "slack_username": "Faith",
        "country": "Kenya",
        "hobby": "Drawing",
        "affiliations": "University of Nairobi",
        "DNA sequence": "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAG"
    },
    {
        "name": "Shreya Venugopalan Omesh Chendilkumar",
        "slack_username": "Shreya",
        "country": "India",
        "hobby": "Listening to music",
        "affiliations": "Anna University",
        "DNA sequence": "AGTGCAGACGCGGCTCCTAGCGGATGGGTGCTATTGTGAGGCGGTTGTAGAAGGTATGAGGAGGCTGT"
    },
    {
        "name": "Taiwo Bankole",
        "slack_username": "Taiwo Bankole",
        "country": "Nigeria",
        "hobby": "Reading",
        "affiliations": "University of Maryland",
        "DNA sequence": "ACAGCCCACAAAATTCCACCTGCTCACAGGTTGGCTGGCTCGACCCAGGTGGTGTCCCCTGCTCTGAGCC"
    },
    {
        "name": "Adeyeye Daniel",
        "slack_username": "Adeyeye Daniel",
        "country": "Nigeria",
        "hobby": "Writing",
        "affiliations": "Mohammed VI Polytechnic University",
        "DNA sequence": "ATGCGTACGTTAGCCTGACCGGATCGTTAAGGCTGATCGGCAATGCCGTTGATCCTGAGCTTGGACGATGCT"
    },
    {
        "name": "Ofosaren Favour Oghenevwerhie",
        "slack_username": "Ofosaren Favour",
        "country": "Nigeria",
        "hobby": "Dancing",
        "affiliations": "Delta State University",
        "DNA sequence": "ATGCGTACCTGAACTGCTTAGGCTTACGGAATCGTAA"
    },
    {
        "name": "Oyiyechukwu Elizabeth Chikelu",
        "slack_username": "Elizabeth Chikelu",
        "country": "Nigeria",
        "hobby": "Writing",
        "affiliations": "Enugu State University of Science and Technology, Nigeria",
        "DNA sequence": "AGCTCCCGGCCAAGCCAGCACCATGGCCAGATACCGATGCTGCCGCAGCAAAAGCAGGAGCAGATGCCGC"
    },
    {
        "name": "Jana Zaki",
        "slack_username": "Jana Zaki",
        "country": "UK",
        "hobby": "Drawing",
        "affiliations": "UCL",
        "DNA sequence": "ATGCGTACCTGAACTGCTTAGGCTTACGGAATCGTAA"
    }
]

# Print each member's details
for member in team:
    print("==")
    print(f"Name: {member['name']}")
    print(f"Slack Username: {member['slack_username']}")
    print(f"Country: {member['country']}")
    print(f"Hobby: {member['hobby']}")
    print(f"Affiliations: {member['affiliations']}")
    print(f"Favorite Gene Sequence: {member['DNA sequence']}")
    print("==\n")
