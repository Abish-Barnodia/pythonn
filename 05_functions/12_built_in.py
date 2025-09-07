def chai_flavour(flavour = "masala"):
    """Return the flavour of chai."""
    chai="ginger"
    return flavour

print(chai_flavour.__doc__)
print(chai_flavour.__name__)


# help(len)

def generate_bill(chai=0, somasa=0):
    """
    calculate the total bill for chai and somasa

    : param chai:number of chai cups (10 rupees each)
    :param somasa: number of somasa(15 rupees each)
    :return : (total amount, thank you message as string)
    
    """
    total = chai*10+somasa*15
    return total, "Thank you for visiting abc.com"