package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;

public class customizing_page extends AppCompatActivity {

    private int mood_value;
    private myapplication myapplication;

    public void saveData(int mood_value, boolean checkbox_pop, boolean checkbox_dance, boolean checkbox_ballad,
                          boolean checkbox_hiphop, boolean checkbox_rock, boolean checkbox_classic, String edit_voice_name, String edit_voice_phone, String edit_food){
        SharedPreferences sharedPreferences = null;
        if(myapplication != null) {
            sharedPreferences = myapplication.getMySharedPreferences();
        }
        SharedPreferences.Editor editor = sharedPreferences.edit();

        if(mood_value>0 && mood_value<=20){
            editor.putBoolean("badmood0music_pop",checkbox_pop);
            editor.putBoolean("badmood0music_dance",checkbox_dance);
            editor.putBoolean("badmood0music_ballad",checkbox_ballad);
            editor.putBoolean("badmood0music_hiphop",checkbox_hiphop);
            editor.putBoolean("badmood0music_rock",checkbox_rock);
            editor.putBoolean("badmood0music_classic",checkbox_classic);
            editor.putString("badmood0voice_name",edit_voice_name);
            editor.putString("badmood0voice_phone",edit_voice_phone);
            editor.putString("badmood0food",edit_food);
        }

        else if(mood_value>20 && mood_value<=40){
            editor.putBoolean("badmood1music_pop",checkbox_pop);
            editor.putBoolean("badmood1music_dance",checkbox_dance);
            editor.putBoolean("badmood1music_ballad",checkbox_ballad);
            editor.putBoolean("badmood1music_hiphop",checkbox_hiphop);
            editor.putBoolean("badmood1music_rock",checkbox_rock);
            editor.putBoolean("badmood1music_classic",checkbox_classic);
            editor.putString("badmood1voice_name",edit_voice_name);
            editor.putString("badmood1voice_phone",edit_voice_phone);
            editor.putString("badmood1food",edit_food);
        }
        else if(mood_value>40 && mood_value<=60){
            editor.putBoolean("badmood2music_pop",checkbox_pop);
            editor.putBoolean("badmood2music_dance",checkbox_dance);
            editor.putBoolean("badmood2music_ballad",checkbox_ballad);
            editor.putBoolean("badmood2music_hiphop",checkbox_hiphop);
            editor.putBoolean("badmood2music_rock",checkbox_rock);
            editor.putBoolean("badmood2music_classic",checkbox_classic);
            editor.putString("badmood2voice_name",edit_voice_name);
            editor.putString("badmood2voice_phone",edit_voice_phone);
            editor.putString("badmood2food",edit_food);
        }
        else if(mood_value>60 && mood_value<=80){
            editor.putBoolean("badmood3music_pop",checkbox_pop);
            editor.putBoolean("badmood3music_dance",checkbox_dance);
            editor.putBoolean("badmood3music_ballad",checkbox_ballad);
            editor.putBoolean("badmood3music_hiphop",checkbox_hiphop);
            editor.putBoolean("badmood3music_rock",checkbox_rock);
            editor.putBoolean("badmood3music_classic",checkbox_classic);
            editor.putString("badmood3voice_name",edit_voice_name);
            editor.putString("badmood3voice_phone",edit_voice_phone);
            editor.putString("badmood3food",edit_food);
        }
        else if(mood_value>80 && mood_value<=100){
            editor.putBoolean("badmood4music_pop",checkbox_pop);
            editor.putBoolean("badmood4music_dance",checkbox_dance);
            editor.putBoolean("badmood4music_ballad",checkbox_ballad);
            editor.putBoolean("badmood4music_hiphop",checkbox_hiphop);
            editor.putBoolean("badmood4music_rock",checkbox_rock);
            editor.putBoolean("badmood4music_classic",checkbox_classic);
            editor.putString("badmood4voice_name",edit_voice_name);
            editor.putString("badmood4voice_phone",edit_voice_phone);
            editor.putString("badmood4food",edit_food);
        }
        else if(mood_value>100 && mood_value<=120){
            editor.putBoolean("goodmood0music_pop",checkbox_pop);
            editor.putBoolean("goodmood0music_dance",checkbox_dance);
            editor.putBoolean("goodmood0music_ballad",checkbox_ballad);
            editor.putBoolean("goodmood0music_hiphop",checkbox_hiphop);
            editor.putBoolean("goodmood0music_rock",checkbox_rock);
            editor.putBoolean("goodmood0music_classic",checkbox_classic);
            editor.putString("goodmood0voice_name",edit_voice_name);
            editor.putString("goodmood0voice_phone",edit_voice_phone);
            editor.putString("goodmood0food",edit_food);
        }
        else if(mood_value>120 && mood_value<=140){
            editor.putBoolean("goodmood1music_pop",checkbox_pop);
            editor.putBoolean("goodmood1music_dance",checkbox_dance);
            editor.putBoolean("goodmood1music_ballad",checkbox_ballad);
            editor.putBoolean("goodmood1music_hiphop",checkbox_hiphop);
            editor.putBoolean("goodmood1music_rock",checkbox_rock);
            editor.putBoolean("goodmood1music_classic",checkbox_classic);
            editor.putString("goodmood1voice_name",edit_voice_name);
            editor.putString("goodmood1voice_phone",edit_voice_phone);
            editor.putString("goodmood1food",edit_food);
        }
        else if(mood_value>140 && mood_value<=160){
            editor.putBoolean("goodmood2music_pop",checkbox_pop);
            editor.putBoolean("goodmood2music_dance",checkbox_dance);
            editor.putBoolean("goodmood2music_ballad",checkbox_ballad);
            editor.putBoolean("goodmood2music_hiphop",checkbox_hiphop);
            editor.putBoolean("goodmood2music_rock",checkbox_rock);
            editor.putBoolean("goodmood2music_classic",checkbox_classic);
            editor.putString("goodmood2voice_name",edit_voice_name);
            editor.putString("goodmood2voice_phone",edit_voice_phone);
            editor.putString("goodmood2food",edit_food);
        }
        else if(mood_value>160 && mood_value<=180){
            editor.putBoolean("goodmood3music_pop",checkbox_pop);
            editor.putBoolean("goodmood3music_dance",checkbox_dance);
            editor.putBoolean("goodmood3music_ballad",checkbox_ballad);
            editor.putBoolean("goodmood3music_hiphop",checkbox_hiphop);
            editor.putBoolean("goodmood3music_rock",checkbox_rock);
            editor.putBoolean("goodmood3music_classic",checkbox_classic);
            editor.putString("goodmood3voice_name",edit_voice_name);
            editor.putString("goodmood3voice_phone",edit_voice_phone);
            editor.putString("goodmood3food",edit_food);
        }
        else if(mood_value>180 && mood_value<=200){
            editor.putBoolean("goodmood4music_pop",checkbox_pop);
            editor.putBoolean("goodmood4music_dance",checkbox_dance);
            editor.putBoolean("goodmood4music_ballad",checkbox_ballad);
            editor.putBoolean("goodmood4music_hiphop",checkbox_hiphop);
            editor.putBoolean("goodmood4music_rock",checkbox_rock);
            editor.putBoolean("goodmood4music_classic",checkbox_classic);
            editor.putString("goodmood4voice_name",edit_voice_name);
            editor.putString("goodmood4voice_phone",edit_voice_phone);
            editor.putString("goodmood4food",edit_food);
        }
        editor.commit();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_customizing_page);

        myapplication = (myapplication) getApplication();

        Intent intent = getIntent();
        if (intent != null) {
            mood_value = intent.getIntExtra("mood_key", 0);
        }

        CheckBox checkBox_pop = findViewById(R.id.checkBox_pop);
        boolean checkbox_pop = checkBox_pop.isChecked();

        CheckBox checkBox_dance = findViewById(R.id.checkBox_dance);
        boolean checkbox_dance = checkBox_dance.isChecked();

        CheckBox checkBox_ballad = findViewById(R.id.checkBox_ballad);
        boolean checkbox_ballad = checkBox_ballad.isChecked();

        CheckBox checkBox_hiphop = findViewById(R.id.checkBox_hiphop);
        boolean checkbox_hiphop = checkBox_hiphop.isChecked();

        CheckBox checkBox_rock = findViewById(R.id.checkBox_rock);
        boolean checkbox_rock = checkBox_rock.isChecked();

        CheckBox checkBox_classic = findViewById(R.id.checkBox_classic);
        boolean checkbox_classic = checkBox_classic.isChecked();

        EditText edit_v_n = findViewById(R.id.edit_voice_name);
        String edit_voice_name = edit_v_n.getText().toString();

        EditText edit_v_p = findViewById(R.id.edit_voice_phone);
        String edit_voice_phone = edit_v_p.getText().toString();

        EditText edit_f = findViewById(R.id.edit_food);
        String edit_voice_food = edit_f.getText().toString();

        Button button_re = findViewById(R.id.back_button);
        button_re.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Intent intent = new Intent();
                intent.putExtra("na","ho");
                setResult(RESULT_OK, intent);
                finish();
            }
        });

        Button button_save = findViewById(R.id.save_button);
        button_save.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                saveData(mood_value, checkbox_pop, checkbox_dance, checkbox_ballad, checkbox_hiphop, checkbox_rock, checkbox_classic, edit_voice_name, edit_voice_phone, edit_voice_food);
            }
        });


    }


}
