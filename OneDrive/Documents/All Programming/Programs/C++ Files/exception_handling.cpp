#include<iostream>
#include<string>
using namespace std;

class Palindrome{
    public:
    Palindrome(){
        cout<<endl<<"#############  PALINDROME  ###############\n" <<endl;;
        string num;
        cout<<"Enter any number: ";
        cin>>num;
        try{
            for (int i=0;i<num.length();i++){
                if (isdigit(num[i])==false){
                    throw "E";
                }
            }
        }
        catch(char const* x){
            cout<<"Please enter an integer\n";
            return;
        }
        string rev="";
        for (int i = num.length()-1;i>=0;i--){
            rev+=num[i];
        }
        
        if (num!=rev){
            cout<<"Not Palindrome!!\n";
        }
        else{
            cout<<"Palindrome!!\n";
        }
    }
};
int main(){
    Palindrome p1;
    return 0;
}