        System.assert(order1.grandtotal__c == 109.25,

                 'Order grand total was not $86.4375 but was '

                 + order1.grandtotal__c);

        System.assert(order1.shippingdiscount__c == -19.50,

                 'Order shipping discount was not -$19.50 but was '

                 + order1.shippingdiscount__c);

      }

      // Negative testing for inserting bad input

      public static testmethod void testNegativeTests(){

        // Create the shipping invoice. It's a best practice to either use defaults

        // or to explicitly set all values to zero so as to avoid having

        // extraneous data in your test.

        Shipping_Invoice__C order1 = new Shipping_Invoice__C(subtotal__c = 0,

                   totalweight__c = 0, grandtotal__c = 0,

                   ShippingDiscount__c = 0, Shipping__c = 0, tax__c = 0);

        // Insert the order and populate with items.

```


### Apex Developer Guide Reserved Keywords

```
        insert Order1;

        Item__c item1 = new Item__C(Price__c = -10, weight__c = 1, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item2 = new Item__C(Price__c = 25, weight__c = -2, quantity__c = 1,

                         Shipping_Invoice__C = order1.id);

        Item__c item3 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = -1,

                         Shipping_Invoice__C = order1.id);

        Item__c item4 = new Item__C(Price__c = 40, weight__c = 3, quantity__c = 0,

                         Shipping_Invoice__C = order1.id);

        try{

           insert item1;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Price must be non-negative'),

                  'Price was negative but was not caught');

        }

        try{

           insert item2;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Weight must be non-negative'),

                  'Weight was negative but was not caught');

        }

        try{

           insert item3;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Quantity must be positive'),

                  'Quantity was negative but was not caught');

        }

        try{

           insert item4;

        }

        catch(Exception e)

        {

           system.assert(e.getMessage().contains('Quantity must be positive'),

                  'Quantity was zero but was not caught');

        }

      }

   }

### Reserved Keywords

```

These words can be used only as keywords.


Apex Developer Guide Reserved Keywords

**Table 12: Reserved Keywords**

abstract false package

activate final parallel

and finally pragma

any float private

array for protected

as from public

asc global retrieve

autonomous goto return

begin group rollback

bigdecimal having select

blob hint set

boolean if short

break implements sObject

bulk import sort

by in static

byte inner string

case insert super

cast instanceof switch

catch int synchronized

char integer system

class interface testmethod

collect into then

commit join this

const like throw

continue limit time

currency list transaction

date long trigger

datetime loop true

decimal map try

default merge undelete

delete new update

desc not upsert

do null using

double nulls virtual

else number void


### Apex Developer Guide Documentation Typographical Conventions

end object webservice

enum of when

exception on where

exit or while

export outer

extends override

These words are special types of keywords that aren't reserved words and can be used as identifiers.

**•** after

**•** before

**•** count

**•** excludes

**•** first

**•** includes

**•** last

**•** order

**•** sharing

**•** with

### Documentation Typographical Conventions

Apex and Visualforce documentation uses these typographical conventions.

**Convention** **Description**

```
Courier font

Italics

```

In descriptions of syntax, a monospace font indicates items that you should type as shown,
except for brackets. For example:

```
Public class HelloWorld

```

In descriptions of syntax, italics represent variables. You supply the actual value. In the following
example, three values must be supplied: _`datatype variable_name`_ [ = _`value`_ ];

If the syntax is bold and italic, the text represents a code element that needs a value supplied
by you, such as a class name or variable value:

```
 public static class YourClassHere { ... }

```

**`Bold Courier font`** In code samples and syntax descriptions, a bold courier font emphasizes a portion of the code
or syntax.

< >

In descriptions of syntax, less-than and greater-than symbols (< >) are typed exactly as shown.


Apex Developer Guide Documentation Typographical Conventions

**Convention** **Description**

```
                     <apex:column value="{!contact.Name}"/>

                     <apex:column value="{!contact.MailingCity}"/>

                     <apex:column value="{!contact.Phone}"/>

                    </apex:pageBlockTable>

```

{ }

[ ]

|

In descriptions of syntax, braces ({ }) are typed exactly as shown.

```
<apex:page>

   Hello {!$User.FirstName}!

</apex:page>

```

In descriptions of syntax, anything included in brackets is optional. In the following example,
specifying _**`value`**_ is optional:

```
 data_type variable_name [ = value ];

```

In descriptions of syntax, the pipe sign means “or”. You can do one of the following (not all).
In the following example, you can create a new unpopulated set in one of two ways, or you
can populate the set:

```
Set< data_type > set_name

  [= new Set< data_type >();] |

  [= new Set< data_type { value [, value2 . . .] };] |

  ;

```

