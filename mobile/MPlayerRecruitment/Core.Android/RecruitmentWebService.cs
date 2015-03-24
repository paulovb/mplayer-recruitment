using System;
using RestSharp;

namespace Core
{
    public class RecruitmentWebService
    {
        RestClient client;

        public RecruitmentWebService()
        {
            client = new RestClient(Properties.URL_BASE);
        }

        public void post(Recruitment recruitment) {

            var request = new RestRequest("recruitment/", Method.POST);

            request.AddHeader("Content-type", "application/json");
            request.AddJsonBody(recruitment.ToJson());
                      
            IRestResponse response = client.Execute(request);

            Console.Write(response.Content);
        }
    }
}

