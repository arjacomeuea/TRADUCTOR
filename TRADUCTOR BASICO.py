using System;
using System.Collections.Generic;

public class TraductorBasico
{
    public static void Main(string[] args)
    {
        Dictionary<string, string> diccionario = new Dictionary<string, string>()
        {
            {"time", "tiempo"},
            {"person", "persona"},
            {"year", "año"},
            {"way", "camino/forma"},
            {"day", "día"},
            {"thing", "cosa"},
            {"man", "hombre"},
            {"world", "mundo"},
            {"life", "vida"},
            {"hand", "mano"},
            {"part", "parte"},
            {"child", "niño/a"},
            {"eye", "ojo"},
            {"woman", "mujer"},
            {"place", "lugar"},
            {"work", "trabajo"},
            {"week", "semana"},
            {"case", "caso"},
            {"point", "punto/tema"},
            {"government", "gobierno"},
            {"company", "empresa/compañía"}
        };

        while (true)
        {
            Console.WriteLine("\nMENU");
            Console.WriteLine("=======================================================");
            Console.WriteLine("1. Traducir una frase");
            Console.WriteLine("2. Ingresar más palabras al diccionario");
            Console.WriteLine("0. Salir");

            Console.Write("Seleccione una opción: ");
            string opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1":
                    Console.Write("Ingrese la frase: ");
                    string frase = Console.ReadLine().ToLower();
                    string fraseTraducida = TraducirFrase(frase, diccionario);
                    Console.WriteLine("Su frase traducida es: " + fraseTraducida);
                    break;
                case "2":
                    AgregarPalabra(diccionario);
                    break;
                case "0":
                    Console.WriteLine("¡Hasta luego!");
                    return;
                default:
                    Console.WriteLine("Opción no válida. Intente de nuevo.");
                    break;
            }
        }
    }

    public static string TraducirFrase(string frase, Dictionary<string, string> diccionario)
    {
        string[] palabras = frase.Split(' ');
        List<string> fraseTraducida = new List<string>();

        foreach (string palabra in palabras)
        {
            if (diccionario.ContainsKey(palabra))
            {
                fraseTraducida.Add(diccionario[palabra]);
            }
            else
            {
                fraseTraducida.Add(palabra);
            }
        }

        return string.Join(" ", fraseTraducida);
    }

    public static void AgregarPalabra(Dictionary<string, string> diccionario)
    {
        Console.Write("Ingrese la palabra en inglés: ");
        string palabraIngles = Console.ReadLine().ToLower();

        Console.Write("Ingrese la traducción en español: ");
        string palabraEspanol = Console.ReadLine().ToLower();

        diccionario[palabraIngles] = palabraEspanol;
        Console.WriteLine($"Palabra '{palabraIngles}' agregada al diccionario.");
    }
}