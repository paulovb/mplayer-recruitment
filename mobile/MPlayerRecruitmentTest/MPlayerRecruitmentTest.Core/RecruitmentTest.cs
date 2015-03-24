using Core.Android;
using NUnit.Framework;
using System;
using System.Json;

namespace MPlayerRecruitmentTest.Core
{
    [TestFixture()]
    public class Test
    {
        [Test()]
        public void RecruitmentParseTest()
        {
            Recruitment recruitment = new Recruitment();

            recruitment.name = "Paulo Vítor Bischof";
            recruitment.mail = "paulo.bischof@gmail.com";           

            String json = recruitment.ToJson();

            String expected = "{\"name\":\"Paulo Vítor Bischof\",\"mail\":\"paulo.bischof@gmail.com\",\"skills\":null}";

            Assert.AreEqual(json, expected);
        }
    }
}

