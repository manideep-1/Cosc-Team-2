package com.example.myapplication;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Layout;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.Space;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.util.HashMap;
import java.util.Map;

import static com.example.myapplication.loginpage.access_tkn;

public class MainActivity extends AppCompatActivity {
    //LinearLayout LabsLinearLayout;
    //FloatingActionButton AddFAB;

    BottomNavigationView bnv;
    EditText et2;
    EditText et3;
    EditText et4;
    RequestQueue queuea;
    JsonObjectRequest DetailsRequest;
    Button buttonn;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        queuea = Volley.newRequestQueue(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        et2 = (EditText) findViewById(R.id.et2);
        et3 = (EditText) findViewById(R.id.et3);
        et4 = (EditText) findViewById(R.id.et4);
        buttonn = (Button) findViewById(R.id.buttonn);


        //LabsLinearLayout=(LinearLayout)findViewById(R.id.LabsLinearLayout);
        // AddFAB=(FloatingActionButton)findViewById(R.id.AddFAB);

        // firstrow();
        bnv = (BottomNavigationView) findViewById(R.id.bnv);
        bnv.setSelectedItemId(R.id.LabsNav);

        bnv.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.LabsNav:
                        return true;
                    case R.id.SemNav:
                        startActivity(new Intent(getApplicationContext(), seminar_hall2.class));
                        overridePendingTransition(0, 0);
                        return true;
                    case R.id.FacultyNav:
                        startActivity(new Intent(getApplicationContext(), Faculty.class));
                        overridePendingTransition(0, 0);
                        return true;

                }
                return false;
            }
        });
        buttonn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String URL2 = "https://internship-team-2.herokuapp.com/lab";
                final String user_idlab = et2.getText().toString();
                final String room_idlab=et3.getText().toString();
                final String purposelab=et4.getText().toString();

                // final String club_name=et1.getText().toString();

                JSONObject labdetails = new JSONObject();
                try {
                    // labdetails.put("club_name",club_name);
                    labdetails.put("user_id", user_idlab);
                    labdetails.put("room_id",room_idlab);
                    labdetails.put("purpose",purposelab);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                DetailsRequest = new JsonObjectRequest(Request.Method.POST,
                        URL2,
                        labdetails,
                        new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                Toast toast = Toast.makeText(getApplicationContext(), "Request Sent!", Toast.LENGTH_LONG);
                                toast.show();


                            }

                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                Toast toast = Toast.makeText(getApplicationContext(), error.toString(), Toast.LENGTH_LONG);
                                toast.show();


                            }
                        }) {
                    @Override
                    public Map<String, String> getHeaders() throws AuthFailureError {
                        Map<String, String> params = new HashMap<String, String>();
                        params.put("Authorization", "Bearer " + access_tkn);
                        return params;
                    }
                    @Override
                    public Map<String, String> getParams() {
                        Map<String, String> params = new HashMap<>();
                        //  params.put("club_name",club_name);
                        params.put("user_id", user_idlab);
                        params.put("room_id",room_idlab);
                        params.put("purpose",purposelab);
                        return params;
                    }

                };
                queuea.add(DetailsRequest);



            }
        });
    }
}







        /*AddFAB.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                add("Lab_name","NA","NA","BOOK","BOOK","BOOK");
                //LinearLayout eachlab=new LinearLayout(this);
                //eachlab.setOrientation(LinearLayout.VERTICAL);




            }
        });*/



  /*  public void firstrow(){
        LinearLayout first_row=new LinearLayout(this);
        TextView col1=new TextView(this);
        TextView col2=new TextView(this);
        TextView col3=new TextView(this);
        TextView col4=new TextView(this);
        TextView col5=new TextView(this);
        TextView col6=new TextView(this);
        col1.setText("LAB");
        col2.setText("I");
        col3.setText("II");
        col4.setText("III");
        col5.setText("IV");
        col6.setText("V");
        col1.setPadding(50,5,50,5);
        col2.setPadding(50,5,50,5);
        col3.setPadding(50,5,50,5);
        col4.setPadding(50,5,50,5);
        col5.setPadding(50,5,50,5);
        col6.setPadding(50,5,50,5);
        first_row.addView(col1);
        first_row.addView(col2);
        first_row.addView(col3);
        first_row.addView(col4);
        first_row.addView(col5);
        first_row.addView(col6);
        LabsLinearLayout.addView(first_row);




    }




    public void add(String labname,String st1,String st2,String st3,String st4,String st5){
        Space space2= new Space(this);
        Space space3=new Space(this);
        Space space4=new Space(this);
        Space space5=new Space(this);
        Space space6=new Space(this);
        Space space7=new Space(this);
        LinearLayout eachlab= new LinearLayout(this);
        //eachlab.setBackgroundColor(Color.GRAY);
        LinearLayout.LayoutParams layoutParams=new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT,LinearLayout.LayoutParams.WRAP_CONTENT);
        layoutParams.setMargins(0,0,0,37);
        TextView Labs=new TextView(this);
        Labs.setTextSize(15);
        Labs.setPadding(10,0,10,0);
        TextView hr1=new TextView(this);
        hr1.setBackground(getResources().getDrawable(R.drawable.redbtn));
        TextView hr2=new TextView(this);
        hr2.setBackground(getResources().getDrawable(R.drawable.redbtn));
        TextView hr3=new TextView(this);
        hr3.setBackground(getResources().getDrawable(R.drawable.greenbtn));
        TextView hr4=new TextView(this);
        hr4.setBackground(getResources().getDrawable(R.drawable.greenbtn));
        TextView hr5=new TextView(this);
        hr5.setBackground(getResources().getDrawable(R.drawable.greenbtn));
        Labs.setText(labname);
        hr1.setText(st1);
        hr2.setText(st2);
        hr3.setText(st3);
        hr4.setText(st4);
        hr5.setText(st5);
        Labs.setPadding(10,5,10,8);
        hr1.setPadding(25,5,25,8);
        hr2.setPadding(25,5,25,8);
        hr3.setPadding(25,5,25,8);
        hr4.setPadding(25,5,25,8);
        hr5.setPadding(25,5,25,8);

        eachlab.addView(Labs);
        eachlab.addView(space2,11,2);
        eachlab.addView(hr1);
        eachlab.addView(space3,11,2);
        eachlab.addView(hr2);
        eachlab.addView(space4,11,2);
        eachlab.addView(hr3);
        eachlab.addView(space5,11,2);
        eachlab.addView(hr4);
        eachlab.addView(space6,11,2);
        eachlab.addView(hr5);

        LabsLinearLayout.addView(eachlab,layoutParams);
        //LabsLinearLayout.addView(space7,10,50);





    }*/
