using System;
using System.Threading;
using System.IO;
using System.Formats.Asn1;
using System.Data;
using System.IO.Compression;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main()
        {
            Renderer renderer = new Renderer();
            Player player = new Player(10, 10);

            renderer.Draw(player.X, player.Y);
        }
    }

    class Renderer
    {
        public void Draw(int x, int y, char character = '@')
        {
            Console.CursorVisible = false;
            Console.SetCursorPosition(x, y);
            System.Console.Write(character);
            System.Console.ReadKey(true);
        }
    }

    class Player
    {
        public int X;
        public int Y;

        public Player(int x, int y)
        {
            X = x;
            Y = y;
        }


    }
}

