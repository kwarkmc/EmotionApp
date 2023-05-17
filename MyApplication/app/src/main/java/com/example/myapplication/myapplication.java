package com.example.myapplication;

import android.app.Application;
import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

public class myapplication extends Application {

    private SharedPreferences sharedPreferences;

    @Override
    public void onCreate() {
        super.onCreate();
        sharedPreferences = getSharedPreferences("moodData", MODE_PRIVATE);
    }

    public SharedPreferences getMySharedPreferences() {
        return sharedPreferences;
    }
}
