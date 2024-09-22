#include <iostream>
#include <limits> 
#include <stdio.h>

int addition(){
    bool cont = true;
    int num1 = 0;
    int num2;
    char userInput;
    while(cont){
        std::cout << "Enter a number: " << std::endl;
        std::cin >> num2;
        if (std::cin.fail()) {
            std::cout << "Invalid input. Please enter a number." << std::endl;
            std::cin.clear(); // Clear the error state
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignore the rest of the invalid input
            continue; // Start the loop again
        } else {
            num1 = num1+num2;
            printf("Answer is %d\n", num1);
            std::cout << "Continue? (Y/N)" << std::endl;
            std::cin >> userInput;
            if (std::cin.fail()) {
                std::cout << "Invalid input. Please enter a number." << std::endl;
                std::cin.clear(); // Clear the error state
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignore the rest of the invalid input
                continue; // Start the loop again
            } else {
                if(toupper(userInput) == 'Y'){
                    continue;
                } else if(toupper(userInput) == 'N') {
                    std::cout << "Thanks for using the program!" << std::endl;
                    cont = false;
                    break;
                } else {
                    std::cout << "Invalid input" << std::endl;
                    std::cout << "Force shutting down program!" << std::endl;
                    cont = false;
                    break;
                }
            }
        }
    }
}

int main(){
    int choice;
    bool selection = true;
    
    while (selection){
        std::cout << "Select a choice:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n";
        std::cout << "Please enter a number from 1 to 4: " << std::endl;
        std::cin >> choice;

        if (std::cin.fail()) {
            std::cout << "Invalid input. Please enter a number." << std::endl;
            std::cin.clear(); // Clear the error state
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Ignore the rest of the invalid input
            continue; // Start the loop again
        }

        switch (choice){
            case 1:
                std::cout << "You chose Addition!" << std::endl;
                selection = false;
                addition();
                break;
            case 2:
                std::cout << "You chose Subtraction!" << std::endl;
                selection = false;
                break;
            case 3:
                std::cout << "You chose Multiplication!" << std::endl;
                selection = false;
                break;
            case 4:
                std::cout << "You chose Division!" << std::endl;
                selection = false;
                break;
            default:
                std::cout << "Please only enter a number from 1 to 4" << std::endl;
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                break;
            }
    }


    return 0;
}