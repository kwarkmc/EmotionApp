package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.github.mikephil.charting.animation.Easing;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.components.Description;
import com.github.mikephil.charting.components.XAxis;
import com.github.mikephil.charting.components.YAxis;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;

import java.util.ArrayList;
import java.util.List;

public class solution extends AppCompatActivity {
    private int mood_value;
    private String v_n;
    private String f_n;
    private myapplication myapplication;
    private void loadData(int mood_value){
        SharedPreferences sharedPreferences = myapplication.getMySharedPreferences();

        if (mood_value<=20){
            String e_v_n = sharedPreferences.getString("badmood0voice_name", "");
            String e_f = sharedPreferences.getString("badmood0food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>20 && mood_value<=40){
            String e_v_n = sharedPreferences.getString("badmood1voice_name", "");
            String e_f = sharedPreferences.getString("badmood1food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>40 && mood_value<=60){
            String e_v_n = sharedPreferences.getString("badmood2voice_name", "");
            String e_f = sharedPreferences.getString("badmood2food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>60 && mood_value<=80){
            String e_v_n = sharedPreferences.getString("badmood3voice_name", "");
            String e_f = sharedPreferences.getString("badmood3food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>80 && mood_value<=100){
            String e_v_n = sharedPreferences.getString("badmood4voice_name", "");
            String e_f = sharedPreferences.getString("badmood4food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>100 && mood_value<=120){
            String e_v_n = sharedPreferences.getString("goodmood0voice_name", "");
            String e_f = sharedPreferences.getString("goodmood0food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>120 && mood_value<=140){
            String e_v_n = sharedPreferences.getString("goodmood1voice_name", "");
            String e_f = sharedPreferences.getString("goodmood1food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>140 && mood_value<=160){
            String e_v_n = sharedPreferences.getString("goodmood2voice_name", "");
            String e_f = sharedPreferences.getString("goodmood2food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>160 && mood_value<=180){
            String e_v_n = sharedPreferences.getString("goodmood3voice_name", "");
            String e_f = sharedPreferences.getString("goodmood3food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
        else if (mood_value>180 && mood_value<=200){
            String e_v_n = sharedPreferences.getString("goodmood4voice_name", "");
            String e_f = sharedPreferences.getString("goodmood4food", "");
            v_n = e_v_n;
            f_n = e_f;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_solution);

        myapplication = (myapplication) getApplication();

        Intent intent = getIntent();
        if (intent != null) {
            mood_value = intent.getIntExtra("mood_key", 0);
        }

        loadData(mood_value);

        TextView voice_name = findViewById(R.id.voice_name);
        voice_name.setText(v_n);
        TextView food_name = findViewById(R.id.food_name);
        food_name.setText(f_n);

        TextView solution_ment = findViewById(R.id.solution_ment);
        if (mood_value<100) {
            solution_ment.setText("오늘 정말 힘든 하루였군요.\n 위로가 될진 모르겠지만 힘냅시다.");
        }
        else{
            solution_ment.setText("오늘은 정말 행복한 하루.\n 내일도 화이팅!");
        }



        Button button_re = findViewById(R.id.back_button);
        button_re.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent();
                intent.putExtra("ho", "gu");
                setResult(RESULT_OK, intent);
                finish();
            }
        });
    }
}