
   #include<iostream.h>
   #include<conio.h>

   void main()
   {
      int x[30], size, i, max, min;

       clrscr();

   cout<<"\n\n Enter size : ";
      cin>>size;

   cout<<"\n\n Enter nums : \n";
     for(i=0 ; i<size ; i++)
     {
	 cin>>x[i];
     }

	min = max = x[0];

     for(i=1 ; i<size ; i++)
     {
	 if(max < x[i])
	 {
	     max = x[i];
	 }

	 if(min > x[i])
	 {
	    min = x[i];
	 }
     }

     cout<<"\n\n min = "<<min;
     cout<<"\n\n max = "<<max;

       getch();
   }












