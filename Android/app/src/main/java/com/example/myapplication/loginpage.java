package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class loginpage extends AppCompatActivity {
    static String access_tkn;
    String user_n;
    String user_pass;
    private RequestQueue queue;
    JsonObjectRequest loginRequest;
    Button loginbtn;
    EditText usernameET;
    EditText pswrdET;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        queue= Volley.newRequestQueue(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loginpage);
        loginbtn=(Button)findViewById(R.id.loginbtn);
        usernameET=(EditText)findViewById(R.id.usernameET);
        pswrdET=(EditText)findViewById(R.id.passwordET);



        loginbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String URL="https://team2api.herokuapp.com/ulogin";
                user_n=usernameET.getText().toString();
                user_pass=pswrdET.getText().toString();
                JSONObject data= new JSONObject();
                try {
                    data.put("username",user_n);
                    data.put("password",user_pass);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                loginRequest=new JsonObjectRequest(Request.Method.POST,
                        URL,
                        data,
                        new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                try {
                                    access_tkn=response.getString("access_token");
                                    OpenMainActivity();

                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }



                            }

                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                Toast toast = Toast.makeText(getApplicationContext(),"Enter Valid Credentials",Toast.LENGTH_LONG);
                                toast.show();



                            }
                        });
                queue.add(loginRequest);



            }
        });

        /*loginbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent login=new Intent(loginpage.this,MainActivity.class);
                startActivity(login);
            }
        });*/
    }

    private void OpenMainActivity() {
        Intent logintent=new Intent(loginpage.this,MainActivity.class);
        startActivity(logintent);
    }
}