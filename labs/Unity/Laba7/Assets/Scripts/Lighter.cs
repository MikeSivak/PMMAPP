using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Lighter : MonoBehaviour
{
    public GameObject Light;
    void Start()
    {
        Light.SetActive(false);
    }


    void OnTriggerEnter(Collider col)
    {
        if (col.tag == "Player")
        {
            Light.SetActive(true);
        }
    }

    void OnTriggerExit(Collider col)
    {
        if (col.tag == "Player")
        {
            Light.SetActive(false);
        }
    }
}
