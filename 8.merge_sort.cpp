// #include <iostream>
// using namespace std;
// class Demo{
//     public:
//         int i;
//         Demo(){
//             i=8000;
//         }
// };
// int main(){
//     Demo demo;
//     cout << demo.i << endl;
// }

#include <iostream>
using namespace std;
class Demo{
    public:
        int i;
        Demo(int val){
            i=val;
        }
};
int main(){
    Demo demo(6000);
    Demo demo2(7000);
    cout << demo.i << endl;
    cout << demo2.i << endl;
}