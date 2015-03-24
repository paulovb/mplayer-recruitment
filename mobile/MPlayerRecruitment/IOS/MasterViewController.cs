using System;
using System.Drawing;
using System.Collections.Generic;

using CoreGraphics;
using Foundation;
using UIKit;
using Core;

namespace IOS
{
    public partial class MasterViewController : UIViewController
    {
       
        public MasterViewController(IntPtr handle)
            : base(handle)
        {
            Title = NSBundle.MainBundle.LocalizedString("Master", "Rastreador de MPlayers");
			
            if (UIDevice.CurrentDevice.UserInterfaceIdiom == UIUserInterfaceIdiom.Pad)
            {
                PreferredContentSize = new CGSize(320f, 600f);
            }
        }

        public override void DidReceiveMemoryWarning()
        {
            // Releases the view if it doesn't have a superview.
            base.DidReceiveMemoryWarning();
			
            // Release any cached data, images, etc that aren't in use.
        }

        public override void ViewDidLoad()
        {
            base.ViewDidLoad();

            btnSend.TouchUpInside += delegate {

                if (txtName.Text == null || txtName.Text.Length <= 0) {
                    new UIAlertView("Informe nome", "", null, "OK", null).Show();
                } else if (txtEmail.Text == null || txtEmail.Text.Length <= 0) {
                    new UIAlertView("Informe e-mail", "", null, "OK", null).Show();
                } else {

                    Recruitment recruitment = new Recruitment
                        {
                            name = txtName.Text,
                            mail = txtEmail.Text,
                            skills = new List<Skills> {
                                (new Skills(SkillsTypes.HTML, txtHTML.Text)),
                                (new Skills(SkillsTypes.CSS,  txtCSS.Text)),
                                (new Skills(SkillsTypes.JAVASCRIPT, txtJavascript.Text)),
                                (new Skills(SkillsTypes.PYTHON, txtPython.Text)),
                                (new Skills(SkillsTypes.DJANGO, txtDjango.Text)),
                                (new Skills(SkillsTypes.ANDROID, txtAndroid.Text)),
                                (new Skills(SkillsTypes.IOS, txtIOS.Text)),
                            }
                        };

                    new RecruitmentWebService().post(recruitment);

                    new UIAlertView("Sucesso!", "Obrigado, entraremos em contato assim que pudermos!", null, "OK", null).Show();

                }

            };
        }


   
    }
}

