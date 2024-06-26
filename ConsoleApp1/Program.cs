using System;
using System.IO;
using System.Formats.Asn1;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            char[,] map = ReadMap("map.txt");
            DrawMap(map);
        }


        private static char[,] ReadMap(string path)
        {
            string[] file = File.ReadAllLines("map.txt");
         
            char[,] map = new char[GetMaxLengthOfLine(file), file.Length];

            for(int x = 0; x < map.GetLength(0); x++)
            {
                for(int y=0; y < map.GetLength(1); y++)
                    map[x,y] = file[y][x];
            }
            
            return map;
        }

        private static void DrawMap(char[,] map)
        {
            for(int y=0; y < map.GetLength(1); y++)
                {
                    for(int x = 0; x < map.GetLength(0); x++)
                    {
                        System.Console.Write(map[x, y]);
                    }
                }
                System.Console.WriteLine();
        }


        private static int GetMaxLengthOfLine(string[] lines)
        {
            int maxLength = lines[0].Length;

            foreach (var line in lines)
                if(line.Length > maxLength)
                    maxLength = line.Length;

            return maxLength;
        }

    }
}