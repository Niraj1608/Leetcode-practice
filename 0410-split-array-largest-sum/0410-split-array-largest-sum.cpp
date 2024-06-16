class Solution {
public:

    bool isPossible(vector<int> &arr,int k, int n , int mid)
    {
        int studentcount=1;
        int pagesum=0;
        for(int i=0;i<n;i++){
            if(pagesum +arr[i]<=mid){
                pagesum+=arr[i];
            }
            else{
                studentcount++;
                if(studentcount>k||arr[i]>mid){
                    return false;
                }
                pagesum=arr[i];
            }
            if(studentcount > k) {
                    return false;
            }
        }
            
        return true;
        
    }
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        int s = 0;
        int sum=0;
        for(int i=0;i<n;i++){
            sum +=nums[i];
        }
        int e = sum;
        int ans = -1;
        int mid = s + (e-s)/2;
    
    while(s<=e)
    {
        if(isPossible(nums,k,n,mid)) {
            //cout<<" Mid returned TRUE" << endl;
            ans = mid;
            e = mid - 1;
        }
        else
        {
            s = mid + 1;
        }
        mid = s + (e-s)/2;
    }
    return ans;
    }
};