using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Task4 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    void OnCollisionEnter(Collision otherObj)
    {
        if (otherObj.gameObject.tag == "Missile")
        {
            Destroy(otherObj.gameObject);
        }
        else if (otherObj.gameObject.tag == "Destroy")
        {
            Destroy(this.gameObject);
        }
    }
}
