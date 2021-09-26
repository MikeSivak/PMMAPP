using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    // Start is called before the first frame update
    public string MyName = "Mike";
    void Start()
    {
        Debug.Log("Hello, World!");
        Rigidbody rb = GetComponent<Rigidbody>();

        rb.mass = 10f;

        gameObject.GetComponent<Transform>().position = new Vector3(2,2,2);
        // transform.position= new Vector3(2,2,2);
    }

    // Update is called once per frame
    void Update()
    {
        Debug.Log("������, ����������!");
    }
}
