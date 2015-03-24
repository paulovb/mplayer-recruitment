using RestSharp;
using System;
using System.Collections.Generic;
using RestSharp.Serializers;

namespace Core
{
    public static class SkillsTypes 
    { 
        public const string HTML = "HTML";
        public const string CSS = "CSS";
        public const string JAVASCRIPT = "JAVASCRIPT"; 
        public const string ANDROID = "ANDROID";
        public const string IOS = "IOS";
        public const string PYTHON = "PYTHON";
        public const string DJANGO = "DJANGO";
    }

    public class Skills
    {
        public Skills(String name, String value)
        {
            this.name = name;
            short resultado = 0;
            Int16.TryParse(value, out resultado);
            this.value = resultado;
        }

        public String name { get; set; }
        public Int16 value { get; set; }

    }

    public class Recruitment
    {
        public Recruitment()
        {

        }

        public String name { get; set; }
        public String mail { get; set; }
        public List<Skills> skills { get; set; }

        public String ToJson() {
            RestSharp.Serializers.JsonSerializer serializer = new JsonSerializer();
            var json = serializer.Serialize(this);

            return json;
        }

    }
}

