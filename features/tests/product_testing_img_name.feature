# Created by Gheethvijay at 8/16/23
Feature:Test to verify that every product on amazon search result page has
  a product name and product image


  Scenario:Verifying that every product on amazon search result page has a product name and product image

     Given Open Amazon page
     When  Testing for webcam
     Then  Verify search result is "webcam"
     Then  Verify every product has a product name and an image


    Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by alias <dept_name>
    When Inputting a <product_name>
    Then Verify <search_dept> department is selected
    Examples:
    |dept_name    | product_name    |search_dept|
    |Handmade     |Handmade Jewelry  |Handmade  |
    |Books        | Medical books     |Books    |