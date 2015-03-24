// WARNING
//
// This file has been generated automatically by Xamarin Studio to store outlets and
// actions made in the UI designer. If it is removed, they will be lost.
// Manual changes to this file may not be handled correctly.
//
using Foundation;
using System.CodeDom.Compiler;

namespace IOS
{
	[Register ("MasterViewController")]
	partial class MasterViewController
	{
		[Outlet]
		UIKit.UIButton btnSend { get; set; }

		[Outlet]
		UIKit.UIScrollView svBackground { get; set; }

		[Outlet]
		UIKit.UITextField txtAndroid { get; set; }

		[Outlet]
		UIKit.UITextField txtCSS { get; set; }

		[Outlet]
		UIKit.UITextField txtDjango { get; set; }

		[Outlet]
		UIKit.UITextField txtEmail { get; set; }

		[Outlet]
		UIKit.UITextField txtHTML { get; set; }

		[Outlet]
		UIKit.UITextField txtIOS { get; set; }

		[Outlet]
		UIKit.UITextField txtJavascript { get; set; }

		[Outlet]
		UIKit.UITextField txtName { get; set; }

		[Outlet]
		UIKit.UITextField txtPython { get; set; }
		
		void ReleaseDesignerOutlets ()
		{
			if (svBackground != null) {
				svBackground.Dispose ();
				svBackground = null;
			}

			if (btnSend != null) {
				btnSend.Dispose ();
				btnSend = null;
			}

			if (txtAndroid != null) {
				txtAndroid.Dispose ();
				txtAndroid = null;
			}

			if (txtCSS != null) {
				txtCSS.Dispose ();
				txtCSS = null;
			}

			if (txtDjango != null) {
				txtDjango.Dispose ();
				txtDjango = null;
			}

			if (txtEmail != null) {
				txtEmail.Dispose ();
				txtEmail = null;
			}

			if (txtHTML != null) {
				txtHTML.Dispose ();
				txtHTML = null;
			}

			if (txtIOS != null) {
				txtIOS.Dispose ();
				txtIOS = null;
			}

			if (txtJavascript != null) {
				txtJavascript.Dispose ();
				txtJavascript = null;
			}

			if (txtName != null) {
				txtName.Dispose ();
				txtName = null;
			}

			if (txtPython != null) {
				txtPython.Dispose ();
				txtPython = null;
			}
		}
	}
}
