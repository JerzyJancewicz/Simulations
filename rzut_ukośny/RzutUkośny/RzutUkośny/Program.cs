using System;

namespace RzutUkośny
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            string[,] graph = new string[17, 140];
            // 16 60
            Physics physics = new Physics();
            Console.WriteLine("\t\t\t Improved Euler \t\t\t\t\t\t\t   Euler");
            physics.DrawGraph(graph);
        }
    }
}