using System;   
using Android.App;
using Android.Content;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;
using Core;
using System.Collections.Generic;

namespace Android
{
    [Activity(Label = "MPlayer Recruitment", MainLauncher = true, Icon = "@drawable/icon")]
    public class MainActivity : Activity
    {
        int count = 1;

        protected override void OnCreate(Bundle bundle)
        {
            base.OnCreate(bundle);

            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.Main);

            EditText name = FindViewById<EditText>(Resource.Id.editTextName);
            EditText mail = FindViewById<EditText>(Resource.Id.editTextMail);

            EditText html = FindViewById<EditText>(Resource.Id.editTextHTML);
            EditText css = FindViewById<EditText>(Resource.Id.editTextCSS);
            EditText javascript = FindViewById<EditText>(Resource.Id.editTextJavascript);
            EditText python = FindViewById<EditText>(Resource.Id.editTextPython);
            EditText django = FindViewById<EditText>(Resource.Id.editTextDjango);
            EditText android = FindViewById<EditText>(Resource.Id.editTextAndroid);
            EditText ios = FindViewById<EditText>(Resource.Id.editTextIOS);

            // Get our button from the layout resource,
            // and attach an event to it
            Button button = FindViewById<Button>(Resource.Id.buttonSend);
			
            button.Click += delegate
            {
                    if (name.Text == null || name.Text.Length <= 0) {
                        name.RequestFocus();
                        Toast.MakeText(this, "Informe nome", ToastLength.Long).Show();
                    } else if (mail.Text == null || mail.Text.Length <= 0) {
                        name.RequestFocus();
                        Toast.MakeText(this, "Informe e-mail", ToastLength.Long).Show();
                    } else {
                
                        Recruitment recruitment = new Recruitment
                            {
                                name = name.Text,
                                mail = mail.Text,
                                skills = new List<Skills> {
                                    (new Skills(SkillsTypes.HTML, html.Text)),
                                    (new Skills(SkillsTypes.CSS,  css.Text)),
                                    (new Skills(SkillsTypes.JAVASCRIPT, javascript.Text)),
                                    (new Skills(SkillsTypes.PYTHON, python.Text)),
                                    (new Skills(SkillsTypes.DJANGO, django.Text)),
                                    (new Skills(SkillsTypes.ANDROID, android.Text)),
                                    (new Skills(SkillsTypes.IOS, ios.Text)),
                                }
                            };
                                               
                        new RecruitmentWebService().post(recruitment);

                        StartActivity(typeof(ThanksActivity));

                    }
            };
        }
    }
}


