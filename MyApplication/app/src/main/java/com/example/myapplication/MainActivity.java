package com.example.myapplication;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import android.widget.Button;
import android.os.AsyncTask;
import android.os.Environment;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {


    private static final String SERVER_URL = "http://192.168.0.133:5000/upload";
    private static final MediaType MEDIA_TYPE_M4A = MediaType.parse("audio/m4a");
    public static final int REQUEST_CODE_MENU = 101;
    SQLiteDatabase database;
    String table_name = "Mood";

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == REQUEST_CODE_MENU){
            Toast.makeText(getApplicationContext(),
                    "다시 시작하려면 MOOD CLICK!", Toast.LENGTH_LONG).show();

        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button button = findViewById(R.id.main_button);
        button.setOnClickListener(new View.OnClickListener(){
           @Override
            public void onClick(View v){
               new UploadTask().execute();
               Intent intent = new Intent(getApplicationContext(),first_page.class);
               startActivityForResult(intent,REQUEST_CODE_MENU);

            }
        });
    }
    public void onButtonClick(View v) {
        new UploadTask().execute();
    }


    private class UploadTask extends AsyncTask<Void, Void, Void> {

        private OkHttpClient client = new OkHttpClient();
        private String responseStr;
        @Override
        protected void onPreExecute() {
            super.onPreExecute();
            Toast.makeText(MainActivity.this, "파일 업로드중..", Toast.LENGTH_SHORT).show();
        }

        @Override
        protected Void doInBackground(Void... voids) {
            List<File> files = getM4AFiles();
            for (File file : files) {
                try {
                    responseStr = uploadFile(file);

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return null;
        }

        private List<File> getM4AFiles() {
            List<File> fileList = new ArrayList<>();
            String downloadPath = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS).getAbsolutePath();
            File dir = new File(downloadPath);
            File[] files = dir.listFiles();
            if (files != null) {
                for (File file : files) {
                    if (file.getName().endsWith(".m4a")) {
                        fileList.add(file);
                    }
                }
            }
            return fileList;
        }

        private String uploadFile(File file) throws IOException {
            RequestBody requestBody = new MultipartBody.Builder()
                    .setType(MultipartBody.FORM)
                    .addFormDataPart("file", file.getName(),
                            RequestBody.create(MEDIA_TYPE_M4A, file))
                    .build();

            Request request = new Request.Builder()
                    .url(SERVER_URL)
                    .post(requestBody)
                    .build();

            try (Response response = client.newCall(request).execute()) {
                if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);
                return response.body().string();

            }
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            super.onPostExecute(aVoid);
            Toast.makeText(MainActivity.this, "업로드가 완료되었습니다.", Toast.LENGTH_SHORT).show();
            try {
                int responseInt = Integer.parseInt(responseStr);
                Toast.makeText(MainActivity.this, "반환값 : " + responseInt, Toast.LENGTH_SHORT).show();
            } catch (NumberFormatException e) {
                e.printStackTrace();
            }
        }
}}