using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Task2 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    void OnCollisionEnter(Collision myCollision)
    {
        if(myCollision.gameObject.name=="Floor")
        {
            Debug.Log("Hit the floor");
        }
        else if (myCollision.gameObject.name=="Wall")
        {
            Debug.Log("Hit the wall");

        }
    }
}
