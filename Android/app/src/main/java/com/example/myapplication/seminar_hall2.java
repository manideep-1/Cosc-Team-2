package com.example.myapplication;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.material.bottomnavigation.BottomNavigationView;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.example.myapplication.loginpage.access_tkn;

public class seminar_hall2 extends AppCompatActivity {

    private Spinner spinner;
    private EditText seminar;
    EditText purpose;
    EditText Useridsem;
    EditText Roomidsem;
    Button buttonConfirm;
    BottomNavigationView bnv;
    RequestQueue queueb;
    JsonObjectRequest SembookingRequest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        queueb= Volley.newRequestQueue(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_seminar_hall2);

        seminar = (EditText) findViewById(R.id.Semname);
        purpose = (EditText) findViewById(R.id.purpose);
        buttonConfirm = (Button) findViewById(R.id.submit);
        Useridsem=(EditText)findViewById(R.id.useridsem);
        Roomidsem=(EditText)findViewById(R.id.roomidsem);
        purpose=(EditText)findViewById(R.id.purpose);

        seminar.addTextChangedListener(loginTextWatcher);
        purpose.addTextChangedListener(loginTextWatcher);

        spinner =findViewById(R.id.spinner);
        bnv=(BottomNavigationView)findViewById(R.id.bnv);
        bnv.setSelectedItemId(R.id.SemNav);

        bnv=(BottomNavigationView)findViewById(R.id.bnv);
        bnv.setSelectedItemId(R.id.LabsNav);

        bnv=(BottomNavigationView)findViewById(R.id.bnv);
        bnv.setSelectedItemId(R.id.SemNav);

        bnv.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch(item.getItemId()){
                    case R.id.LabsNav:
                        startActivity(new Intent(getApplicationContext(),MainActivity.class));
                        overridePendingTransition(0,0);
                        return true;
                    case R.id.SemNav:

                        return true;
                    case R.id.FacultyNav:
                        startActivity(new Intent(getApplicationContext(),Faculty.class));
                        overridePendingTransition(0,0);
                        return true;

                }
                return false;
            }
        });
        buttonConfirm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String URLsem="https://team2api.herokuapp.com/sem";

                final String user_idsem = Useridsem.getText().toString();
                final String room_idsem=Roomidsem.getText().toString();
                final String purposeSem=purpose.getText().toString();
                final String club_name=spinner.getSelectedItem().toString();
                JSONObject semdetails = new JSONObject();
                try {
                    semdetails.put("club_name",club_name);
                    semdetails.put("user_id", user_idsem);
                    semdetails.put("room_id",room_idsem);
                    semdetails.put("purpose",purposeSem);
                } catch (JSONException e) {
                    e.printStackTrace();
                }
                SembookingRequest = new JsonObjectRequest(Request.Method.POST,
                        URLsem,
                        semdetails,
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
                                Toast toast = Toast.makeText(getApplicationContext(), "Invalid Details", Toast.LENGTH_LONG);
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
                        params.put("club_name",club_name);
                        params.put("user_id", user_idsem);
                        params.put("room_id",room_idsem);
                        params.put("purpose",purposeSem);
                        return params;
                    }

                };
                queueb.add(SembookingRequest);



            }
        });




        List<String> clubs = new ArrayList<>();
        clubs.add(0,"CHOOSE THE CLUB");
        clubs.add("COSC");
        clubs.add("IEEE");
        clubs.add("Chaitanya Smruthi");
        clubs.add("Sports");
        clubs.add("Street Cause");
        clubs.add("Litratri");

        //style and populate the spinner
        ArrayAdapter<String> dataAdapter;
        dataAdapter = new ArrayAdapter(this,android.R.layout.simple_spinner_item, clubs);

        //dropdown layout style
        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        //attaching data adapter to spinner
        spinner.setAdapter(dataAdapter);

        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {

                if (parent.getItemAtPosition(position).equals("CHOOSE THE CLUB"))
                {
                    //do nothing
                }
                else
                {
                    //on selecting a spinner item
                    String item = parent.getItemAtPosition(position).toString();
                    //show selected spinner item
                    Toast.makeText(parent.getContext(),"Selected: "+item, Toast.LENGTH_SHORT).show();


                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
                //todo Auto-generated method stub

            }
        });

    }

    private TextWatcher loginTextWatcher = new TextWatcher() {
        @Override
        public void beforeTextChanged(CharSequence s, int start, int count, int after) {

        }

        @Override
        public void onTextChanged(CharSequence s, int start, int before, int count) {
            String hallinput = seminar.getText().toString();
            String purposeinput = purpose.getText().toString();

            buttonConfirm.setEnabled(!hallinput.isEmpty() && !purposeinput.isEmpty());

        }

        @Override
        public void afterTextChanged(Editable s) {

        }
    };
}
