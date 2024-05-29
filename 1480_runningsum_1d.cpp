#include<iostream>
using namespace std;
int main(){
    int n,x;
    cout<<"\nRunning Sum of 1-D array\n";
    cout<<"\nEnter the number of entries you want in the array:";
    cin>>n;
    int base_array[n];
    //input base array
    for(int i=0; i<n; i++){
        cout<<"\nEnter #"<<i+1<<" element of array: ";
        cin>>base_array[i];
    }
    //output entered array
    cout<<"\nEntered Array:[";
    for(x = 0; x<n; x++) {
        if (x == n - 1) {
            cout << base_array[x]<< "]";
        } else {
            cout << base_array[x] << ", ";
        }
    }
    cout<<"\nThe running sum is: ";

    int running_sum[n];
    //calculate running sum
    running_sum[0] = base_array[0];
    for(int i = 1; i<n; ++i){
        running_sum[i] = running_sum[i-1] + base_array[i];
    }
    //print running sum
    cout<<"\n\nRunning sum is: [";
    for(int i = 0; i<n; i++) {
        if (i == n - 1) {
            cout << running_sum[i] << "]";
        } else {
            cout << running_sum[i] << ", ";
        }
    }
    return 0;
}
