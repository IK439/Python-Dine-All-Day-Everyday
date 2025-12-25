# Python-Dine-All-Day-Everyday

This project is a Python object-oriented program that models a restaurant business with multiple franchise locations and time-based menus. It demonstrates how menus, franchises, and businesses can be structured and interact with each other.

## Overview

The system consists of three main classes:

- **Business** – Represents a restaurant brand that owns one or more franchises.
- **Franchise** – Represents a physical restaurant location with an address and a set of menus.
- **Menu** – Represents a menu with food and drink items, prices, and availability times.

The program also includes example data for different menus (Early Bird, Brunch, Dinner, Kids) and a separate panini-only restaurant.

## Features

- Define multiple menus with:
  - Item names and prices
  - Start and end availability times (24-hour format)
- Determine which menus are available at a given time
- Calculate a customer’s bill from selected menu items
- Display human-readable menu availability times
- Support multiple franchise locations under one business
- Demonstrate a standalone panini restaurant as a separate business

## Time Format

Menu availability times use **24-hour format**, for example:

- `700` → 7am  
- `1100` → 11am  
- `1700` → 5pm  

Times are automatically formatted into readable `am/pm` strings when displayed.

## Example Usage

The script demonstrates:
- Printing a franchise address
- Checking available menus at different times of day
- Calculating example bills for Early Bird and Brunch menus
- Displaying menu descriptions
- Creating and displaying a panini-only restaurant menu

All results are printed directly to the console.

## Requirements

- Python 3.x
- No external libraries required

## How to Run

Run the script using:

```bash
python your_script_name.py
