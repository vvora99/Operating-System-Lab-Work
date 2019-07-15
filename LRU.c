#include <stdio.h>

int findPOS(int arr[], int n){
    int i, minimum = arr[0], pos = 0;
 
    for(i = 1; i < n; ++i){
        if(arr[i] < minimum){
            minimum = arr[i];
            pos = i;
        }
    }
    return pos;
}


int main()
{
    int frames, pages;
    int i, j, flag1, flag2, count, faults=0, pos;
    int arr_frames[10],arr_pages[20],arr[30];
    
    printf("Enter number of frames: ");
    scanf("%d", &frames);
    
    printf("Enter number of pages: ");
    scanf("%d", &pages);
    
    printf("Enter reference string (Page numbers separated by spaces): ");
    
    for(i = 0; i < pages; ++i){
        scanf("%d", &arr_pages[i]);
    }
    
    for(i = 0; i < frames; ++i){
        arr_frames[i] = -1;
    }
    
    for(i = 0; i < pages; ++i){
        flag1 = 0;
        flag2 = 0;
        
        for(j = 0; j < frames; ++j){
            if(arr_frames[j] == arr_pages[i]){
                count++;
                arr[j] = count;
                flag1 = 1;
                flag2 = 1;
                break;
               }
        }
        
        if(flag1 == 0){
            for(j = 0; j < frames; ++j){
                if(arr_frames[j] == -1){
                    count++;
                    faults++;
                    arr_frames[j] = arr_pages[i];
                    arr[j] = count;
                    flag2 = 1;
                    break;
                }
            }    
        }
        
        if(flag2 == 0){
            pos = findPOS(arr, frames);
            count++;
            faults++;
            arr_frames[pos] = arr_pages[i];
            arr[pos] = count;
        }
        
        printf("\n");
        
        for(j = 0; j < frames; ++j){
            printf("%d\t", arr_frames[j]);
        }
    }
        
    printf("\n\nTotal Page Faults = %d", faults);
    
    return 0;
}
