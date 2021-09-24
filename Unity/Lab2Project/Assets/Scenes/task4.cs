using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class task4 : MonoBehaviour
{
    public float speed = 5;
    private Rigidbody rb;
    //public GameObject player;
    public Material sphereMaterial;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();

    }

    // Update is called once per frame
    void Update()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");
        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);
        //transform.position = Vector3.MoveTowards(transform.position, player.transform.position, Time.deltaTime);
        rb.AddForce(movement * speed);
        //task6

    }

}
