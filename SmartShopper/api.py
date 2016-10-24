# A test amazon-api-call using python wrapper and installed/downloaded class
# By Arsalon N Amini-Hajibashi 10/21/2016

# Parameters/environment setup/wrapper import
from amazon.api import AmazonAPI
amazon = AmazonAPI('AKIAIIP7A5N6GF54YKIQ', 'L+BdIDCohFe6ZVV1PCxxVdmzjBkiK2WesZYMHtx8', 'arsalon-20')

# fn(1) userinput searches for 'style' of clothing (trousers, T-shirts)
# fn(2) user requests item detail
# fn(3) pybrain sends input from optimized reward function regarding a user preference, new intelligent search is made
# fn(4) user requests item placed into cart for checkout



def getClothingSimilarity(asin):
    products = amazon.similarity_lookup(ItemId='asin')
    print dir(products)

def getClothingSearch():
    product = amazon.search_n(1, Keywords = 'T-shirts' , SearchIndex ='All')
    for i, product in enumerate(product):
        print"{0}. '{1}'".format(i, product.title)
        print"{0}. '{1}'".format(i, product.asin)
        print"{0}. '{1}'".format(i, product.genre)
        print"{0}. '{1}'".format(i, product.features)
        print"{0}. '{1}'".format(i, product.images)
        asin = product.asin
        b=getClothingSimilarity(asin)
        

a=getClothingSearch()
  # print dir(product)






# def getDetail(id):
#     detail = amazon.lookup(ItemId='id')
#     print(detail)


# getSearch()
# getDetail(id)


