# Created by Gheethvijay at 8/1/23
Feature: Test to see the amazon cart empty

  Scenario: Verify if the Amazon cart is empty when the user clicks on the cart icon
      Given Open Amazon page
      When  Click on the cart icon
      Then  Verify Your Amazon Cart is empty message shows

