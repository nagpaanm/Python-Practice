'''
Created on Jan. 21, 2023

@author: Anmol Nagpal
'''

# O(n) runtime
def nextVersion(version):
    """
    This function will take a version <string> as a parameter, and will return a
    string containing the next version number.
    
    ***Rule: No number but the first may be greater than 9: if any are, 
    you must set them to 0 and increment the next number in sequence.
    
    @type version: string
    @return: string
    """
    # retrieve very last period in the version (if it exists)
    last_period = version.rfind(".")
    
    # no periods in version
    if last_period == -1:
        return str(int(version) + 1)
    else:
        # create a list out of all of the numbers separated by a '.'
        new_version_list = version.split(".")
        last_num = new_version_list[len(new_version_list) - 1]
        if last_num == "9":
            iterator = len(new_version_list) - 1
            # iterate over the version list, starting from the end
            while last_num == "9":
                if iterator == 0:
                    # at the beginning of the list
                    new_version_list[iterator] = str(int(new_version_list[iterator]) + 1)
                    return ".".join(new_version_list)
                else:
                    new_version_list[iterator] = str(0)
                    last_num = new_version_list[iterator - 1]
                iterator -= 1
            # once the loop ends, add 1 to the version list at index iterator
            new_version_list[iterator] = str(int(new_version_list[iterator]) + 1)
            return ".".join(new_version_list)
        else:
            # add 1 to the very last number in the version
            return version[0:last_period + 1] + str(int(version[last_period + 1]) + 1)
        
def nextVersionTests():
    """ 
    NOTE - typically tests should be written in a separate file. For sake
    of demonstration (and to save time), I've added them here.
    """
    assert nextVersion("1.2.3") == "1.2.4", "Incorrect"
    assert nextVersion("0.9.9") == "1.0.0", "Incorrect"
    assert nextVersion("1") == "2", "Incorrect"
    assert nextVersion("1.2.3.4.5.6.7.8") == "1.2.3.4.5.6.7.9", "Incorrect"
    assert nextVersion("9.9") == "10.0", "Incorrect"
    assert nextVersion("0") == "1", "Incorrect"
    assert nextVersion("30") == "31", "Incorrect"
    assert nextVersion("454.9.9.9") == "455.0.0.0", "Incorrect"
    assert nextVersion("454.9.9.0") == "454.9.9.1", "Incorrect"
    assert nextVersion("59.0") == "59.1", "Incorrect"
    assert nextVersion("1.2.3.4.5.6.7.8.9") == "1.2.3.4.5.6.7.9.0", "Incorrect"
    assert nextVersion("1.2.3.4.5.6.7.9.0") == "1.2.3.4.5.6.7.9.1", "Incorrect"
    assert nextVersion("10.9") == "11.0", "Incorrect"
    assert nextVersion("10.7.5.3") == "10.7.5.4", "Incorrect"
    assert nextVersion("99.9.9.9.9.9.9.9.9.9.9.9.9.9.9.9") == "100.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0", "Incorrect"
    assert nextVersion("100.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0") == "100.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1", "Incorrect"
    
    
if __name__ == "__main__":
    nextVersionTests()

"""
{Security - discussion} What changes if the above assumption is removed? What are
some potential threats/risk scenarios if a function like this breaks?

Assumption: You can assume all test inputs to be valid.

If the assumption above is removed than each input supplied to the nextVersion()
function will need to be validated to ensure it is correct. It will need to be
validated in a way such that to ensure the format of the version supplied is 
correct (i.e. not starting or ending with a '.' and following the function rule 
of only the first number being able to be greater than 9), the length 
(number of characters) in the version is between a certain bound, and that only 
applicable characters are in the version string ('.' and an integer).

Threats/risks if a function like this breaks
- incorrectly labeling of version to corresponding software
    - may lead to customers installing an older version that contains vulnerabilities - erodes customer trust
    - may make it difficult for customers to determine what the most recent version is
    - may override previous versions in the repo if the name of the version has been repeated
    - may break pipelines and other dependencies that need to reference the version number
"""