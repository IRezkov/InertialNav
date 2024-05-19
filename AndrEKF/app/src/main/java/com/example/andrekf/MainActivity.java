package com.example.andrekf;

import androidx.appcompat.app.AppCompatActivity;

import 	android.os.Environment;
import android.os.Bundle;
import android.widget.TextView;
import 	java.io.File;
import java.io.IOException;

import com.example.andrekf.databinding.ActivityMainBinding;


import android.content.pm.PackageManager;
import android.content.pm.PackageInfo;

public class MainActivity extends AppCompatActivity {

    // Used to load the 'andrekf' library on application startup.
    static {
        System.loadLibrary("andrekf");
    }

    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        // Example of a call to a native method
        TextView tv = binding.sampleText;
        tv.setText(stringFromJNI());
        //String zop = getExternalFilesDir(null).getAbsolutePath();

    }

    /**
     * A native method that is implemented by the 'andrekf' native library,
     * which is packaged with this application.
     */
    public native String stringFromJNI();
}