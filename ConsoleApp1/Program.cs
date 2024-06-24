using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            Console.CursorVisible = false;
            char[,] map =
            {
                {'#','#','#','#','#','#','#','#','#','#','#','#'},
                {'#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ','#'},
                {'#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ','#'},
                {'#',' ','#',' ','X',' ',' ',' ',' ',' ',' ','#'},
                {'#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'},
                {'#',' ','#',' ',' ',' ',' ','#','#','#','X','#'},
                {'#',' ','#',' ',' ',' ',' ','#','X','#',' ','#'},
                {'#',' ','#',' ',' ',' ',' ','#',' ','#',' ','#'},
                {'#',' ','#',' ',' ',' ',' ','#',' ','#',' ','#'},
                {'#',' ','#',' ',' ',' ',' ',' ',' ',' ',' ','#'},
                {'#',' ','#','#','#','#',' ',' ',' ',' ',' ','#'},
                {'#',' ',' ',' ',' ','#',' ',' ',' ',' ',' ','#'},
                {'#',' ','X',' ',' ','#',' ',' ',' ',' ','X','#'},
                {'#','#','#','#','#','#','#','#','#','#','#','#'}
            };

            // Console.SetCursorPosition(0,0);

            int userX = 6, userY = 6;
            char[] bag = new char[1];

            while (true)
            {
                // Console.SetCursorPosition(0, 50);
                System.Console.Write("Сумка: ");
                for(int i = 0; i < bag.Length; i++)
                {
                    System.Console.Write(bag[i] + " ");
                }
                System.Console.WriteLine();


                for (int i = 0; i < map.GetLength(0); i++)
                {
                    for (int j = 0; j < map.GetLength(1); j++)
                    {
                        System.Console.Write(map[i, j]);
                    }
                    System.Console.WriteLine();
                }

                Console.SetCursorPosition(userY, userX);
                Console.Write('@');

                ConsoleKeyInfo charKey = Console.ReadKey();
                switch (charKey.Key)
                {
                    case ConsoleKey.UpArrow:
                        if (map[userX - 1, userY] != '#')
                        {
                            userX--;
                        }
                        break;
                    case ConsoleKey.DownArrow:
                        if (map[userX + 1, userY] != '#')
                        {
                            userX++;
                        }
                        break;
                    case ConsoleKey.LeftArrow:
                        if (map[userX, userY - 1] != '#')
                        {
                            userY--;
                        }
                        break;
                    case ConsoleKey.RightArrow:
                        if (map[userX, userY + 1] != '#')
                        {
                            userY++;
                        }
                        break;
                }

                if (map[userX, userY] == 'X')
                {
                    map[userX, userY] = 'o';
                    char[] tempBag = new char[bag.Length + 1];
                    for(int i = 0; i < bag.Length; i++)
                    {
                        tempBag[i] = bag[i];
                    }
                    tempBag[tempBag.Length - 1] = 'X';
                    bag = tempBag;
                }
                Console.Clear();
            }
        }
    }
}