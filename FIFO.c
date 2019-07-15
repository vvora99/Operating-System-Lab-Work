#include<stdio.h>
 
int main()
{
      int pages_array[15], page_faults = 0, m, n, s, pages, frames;
      
      printf("\nEnter Total Number of Pages:\t");
      scanf("%d", &pages);
      
      printf("\nEnter value of Pages:\n");
      for(m = 0; m < pages; m++)
      {
            printf("Page No. [%d]:\t", m + 1);
            scanf("%d", &pages_array[m]);
      }
      
      printf("\nEnter Total Number of Frames:\t");
      {
            scanf("%d", &frames);
      }
      
      int temp[frames];
      for(m = 0; m < frames; m++)
      {
            temp[m] = -1;
      }
      
      for(m = 0; m < pages; m++)
      {
            s = 0;
            for(n = 0; n < frames; n++)
            {
                  if(pages_array[m] == temp[n])
                  {
                        s++;
                        page_faults--;
                  }
            }     
            page_faults++;
            if((page_faults <= frames) && (s == 0))
            {
                  temp[m] = pages_array[m];
            }   
            else if(s == 0)
            {
                  temp[(page_faults - 1) % frames] = pages_array[m];
            }
            printf("\n");
            for(n = 0; n < frames; n++)
            {     
                  printf("%d\t", temp[n]);
            }
      } 
      printf("\nTotal Page Faults:\t%d\n", page_faults);
      return 0;
}