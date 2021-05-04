import usaddress
addr='123 Main St. Suite 100 Chicago, IL'

# The parse method will split your address string into components, and label each component.
# expected output: [(u'123', 'AddressNumber'), (u'Main', 'StreetName'), (u'St.', 'StreetNamePostType'), (u'Suite', 'OccupancyType'), (u'100', 'OccupancyIdentifier'), (u'Chicago,', 'PlaceName'), (u'IL', 'StateName')]
usaddress.parse(addr)

# The tag method will try to be a little smarter
# it will merge consecutive components, strip commas, & return an address type
# expected output: (OrderedDict([('AddressNumber', u'123'), ('StreetName', u'Main'), ('StreetNamePostType', u'St.'), ('OccupancyType', u'Suite'), ('OccupancyIdentifier', u'100'), ('PlaceName', u'Chicago'), ('StateName', u'IL')]), 'Street Address')
usaddress.tag(addr)