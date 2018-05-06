class StartConv extends SqRootScript
{
    conv_start = 0;
    conv_stop = 8;
    conv_step = 0;
    conv_times = [
        12.914,
        17.849,
        11.900,
        19.325,
        15.313,
        15.820,
        8.440,
        2.629
        ];
    conv_cameras = ["cam1", "cam2", "cam1", "cam2", "cam1", "cam2", "cam1", "cam2"];
/*
    conv_actors = ["vernon", "willy", "vernon", "willy", "vernon", "willy", "vernon", "willy"];
    conv_samples = ["sg11101A", "sg51101B", "sg11101C", "sg51101D", "sg11101E", "sg51101F", "sg11101G", "sg51101H"];

    function OnSim()
    {
        if (message().starting) {
            foreach (sample in conv_samples) {
                print("debug: " + Data.GetString("facepos", sample));
            }
            foreach (sample in conv_samples) {
                local result = Sound.PreLoad(sample);
                print("Preloaded " + sample + ": " + (result ? "OK" : "fail"));
            }
        }
    }
*/
    function OnFrobWorldEnd()
    {
        conv_step = conv_start;
        Camera();
    }

    function Camera() {
        print("Step " + conv_step + ":");
        if (conv_step < conv_stop) {
            local cam = Object.Named(conv_cameras[conv_step]);
            local wait = 0.25;
            print("  Attaching camera to " + cam + " and waiting for " + wait);
            Debug.Command("cam_attach " + cam);
            SetOneShotTimer(self, "camera", wait);
        } else {
            print("  Restoring camera to player.");
            Debug.Command("cam_attach " + Object.Named("cam3"));
        }
    }

    function OnTimer() {
        if (message().name == "camera") {
            local wait = conv_times[conv_step] + 0.15;
            local conv = Object.Named("ConvArcher0" + conv_step);
            print("  Starting conversation " + conv + " and waiting for " + wait);
            SendMessage(conv, "TurnOn");
            SetOneShotTimer(self, "action", wait);
        } else if (message().name == "action") {
            conv_step = conv_step + 1;
            print("  Finished conversation, moving to step " + conv_step);
            Camera();
        } else {
            print("  Unexpected timer name: " + message().name);
        }
    }
}
