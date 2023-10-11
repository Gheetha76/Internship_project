# Created by Gheethvijay at 8/1/23
Feature:  Check if the cart has the added items

   @smoke
   Scenario Outline: Verify if the added product is in the cart
      Given Open Amazon page
      When Inputting a <product>
      Then select a particular product
      Then Add product to the cart
      Then Verify <item> is in the cart
      Examples:
         | product     | item               |
         | cell phone| Subtotal (1 item): |




