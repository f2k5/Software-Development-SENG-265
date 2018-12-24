/*
 * UVic SENG 265, Fall 2018, A#1
 *
 * This will contain a solution to sengfmt. In order to complete the
 * task of formatting a file, it must open and read the file (hint: 
 * using fopen() and fgets() method) and format the text content base on the 
 * commands in the file. The program should output the formated content 
 * to the command line screen by default (hint: using printf() method).
 *
 * Supported commands include:
 * ?width width :  Each line following the command will be formatted such 
 *                 that there is never more than width characters in each line 
 * ?mrgn left   :  Each line following the command will be indented left spaces 
 *                 from the left-hand margin.
 * ?fmt on/off  :  This is used to turn formatting on and off. 
 */

/*
 * Author: Fardin Khan
 * Student ID: V00876483
 */

//Code:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Assumptions for max input line 
//char and max no. of lines in 
//and input file:
#define MAX_LINE_LEN 133
#define MAX_LINES 300

int main(int argc, char *argv[]) 
{
	/* #ifdef DEBUG: leave it comments else code won't run */ 

	//File content will be stored line by line here:
	char keep[MAX_LINE_LEN];
    
    //A char array containing a new line char
    //Will be used to compare with an empty line:
	char empty_line[2] = "\n";
    //char null_line[1] = "\0";

  /* width_num and margin_num are variables that will hold 
     the address of a char. They are technically the digits 
     of the width and margin BUT in char form!
     To use they must be converted to an integer! */
    char *width_num;
    char *margin_num;
    //char *fmt_off;

    //int variables to store width and margin:
    int w = 0;
    int m = 0;

    int cmd_off_ignore_all = 0;
    int cmd_on_edit_all = 1;
    int ignore_empty_lines = 0;

    int do_once = 0;

    //Initializing line to be used later:
    int line_l = 0;
    int word_l = 0;

//    int input_line_len = 0;

	//made for comparison with original text:
	char w_c[7] = "?width";
	char m_c[6] = "?mrgn";
    char f_off[9] = "?fmt off"; //format off
    char f_on[8] = "?fmt on"; //format on

	//fp is a variable that holds the address to a FILE (type):
	FILE *fp;

	//Opening the file and reading it:
	fp = fopen(argv[1], "r");

	//If any error occurs or end of file reached:
	if (fp == NULL)
	{
		fprintf(stderr, "Not able to open file %s\n", argv[1]);
		exit(1);
	}

	//prints the input file line by line:
	while (fgets (keep, MAX_LINE_LEN, fp))
	{

        //removing the new line char 
        //at the end of each sentence:
        //sentence_l = strlen(keep);
        //keep[sentence_l] = ' ';

        //get the length of each line (keep)
//        input_line_len = strlen(keep);
		
		
        // -------------- Now search for the text commands: ---------------
        /*if at all present the commands will be present at the beginning of 
          each input file. They will be the first words of the first sentence: */

        //searching for the fmt command: ?fmt off
        if ((keep[0] == f_off[0]) && (keep[1] == f_off[1]) && (keep[2] == f_off[2]) && (keep[3] == f_off[3]) && (keep[4] == f_off[4]) && (keep[5] == f_off[5]) && (keep[6] == f_off[6]) && (keep[7] == f_off[7]))
        {
            cmd_off_ignore_all++;
            cmd_on_edit_all = 2;
            ignore_empty_lines++;
            //cmd_on_edit_all = 1;
            //if 0 work on width and margin
            //since the above is not 0 anymore 
            //we ignore all text commands: width and margin
        }
        //searching for the fmt command: ?fmt on
        else if ((keep[0] == f_on[0]) && (keep[1] == f_on[1]) && (keep[2] == f_on[2]) && (keep[3] == f_on[3]) && (keep[4] == f_on[4]) && (keep[5] == f_on[5]) && (keep[6] == f_on[6]))
        {
            cmd_on_edit_all = 1;
            cmd_off_ignore_all = 0;
            ignore_empty_lines = 0;
            //if NOT 0, work on width and margin
        }
        //searching for the command: ?width
		else if ((keep[0] == w_c[0]) && (keep[1] == w_c[1]) && (keep[2] == w_c[2]) && (keep[3] == w_c[3]) && (keep[4] == w_c[4]) && (keep[5] == w_c[5]))
		{
			//Use strtok to find the width num.
            width_num = strtok (keep, " ");
            width_num = strtok (NULL, " ");
            w = atoi (width_num);
		}
		//searching for the command: ?mrgn
		else if ((keep[0] == m_c[0]) && (keep[1] == m_c[1]) && (keep[2] == m_c[2]) && (keep[3] == m_c[3]) && (keep[4] == m_c[4]))
		{
			margin_num = strtok (keep, " ");
			margin_num = strtok (NULL, " ");
			m = atoi (margin_num);
		}
        //if line is empty, print an empty line:
        else if ((strcmp(keep, empty_line) == 0) && (ignore_empty_lines == 0))
        {
            //printf("\n");
            //printf("\n");
            printf("\n");
            printf("\n");
            //word_l = 0;
            line_l = 0;
            do_once = 0; 
        }
        //else if (keep[input_line_len] == "\n")
        //{
        //    keep[input_line_len] = " ";
        //}
    	// -------------------- SEARCH FOR COMMANDS OVER ---------------------

		//Now that we have the commands (if present at all!) we use the 
		//commands and edit the text from the input file
		else 
        { 
            if ((w != 0 || m != 0) && (cmd_off_ignore_all == 0) && (cmd_on_edit_all == 1))
            {
            	//printf("%s", keep);

            	//Use strtok to get the words. 
            	//print word-by-word
            	//if word.len+space != w, add space
            	//if adding a new word makes sentence.len>w print "\n"- to get to next line
            	//also we need to check for empty line 

                

                char *each_word = strtok(keep, " \n");
            	//line_l = 0;
            	while (each_word != NULL)
                {
                    word_l = 0;
            		word_l = strlen(each_word);
            		line_l = line_l + word_l;

            		
                    if (line_l < w)
            		{
            			//line_l++; //
                        //line_l = line_l + word_l;
                        if (m != 0 && do_once == 0)
                        {   
                            int i = 0;
                            while (i < m)
                            {
                                printf(" ");
                                line_l++;
                                i++;
                            }
                            do_once++;
                        }
                        line_l++;
            			printf("%s ", each_word); //print words with a space
            		}
            		else if (line_l == w)
                    {
            			//if line_l becomes == to w, u don't 
            			//need space after your print the word
                        printf("%s", each_word);
                        printf("\n");
                        
                        if (m != 0)
                        {   
                            int j = 0;
                            while (j < m)
                            {
                                printf(" ");
                                line_l++;
                                j++;
                            }
                            //do_once++;
                        } 
                        //printf("%s", each_word);
            			//printf("%s ", each_word);
            			line_l = 0;
                        line_l += m;
                        //line_l = line_l + word_l;
                        //line_l++;
            		}
            		else if (line_l > w)
            		{
            			printf("\n");
                        if (m != 0)
                        {   
                            //New line:
                            //give spaces (margin)
                            //add words
                            int k = 0;
                            while (k < m)
                            {
                                printf(" ");
                                line_l++;
                                k++;
                            }
                            //do_once++;
                        }
            			printf("%s ", each_word);
            			line_l = 0;
                        //line_l++;
                        line_l = line_l + word_l;
                        line_l++;
                        line_l += m;
                        //line_l++;
            		}

            		//word_l = 0;
            		each_word = strtok(NULL, " \n");
            	}



            	


            }
            else
            {
            	printf("%s", keep);
            }
            //printf("\n");

		}

		//make an if-else that looks for an empty line
		
    }
    
	//checking if the code correctly got the commands:
	/*
	printf("\n===========\n");
	printf("Width: %d\n", w);
    printf("Margin: %d\n", m);
    printf("===========\n");
    */
    

    // -- Only for test, remove later --
        //printf("\n");
	



	

	
//#endif
	exit(0);
}
