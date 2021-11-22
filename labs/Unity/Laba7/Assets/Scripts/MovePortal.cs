
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovePortal : MonoBehaviour
{


    public GameObject objToTP;
    public Transform tpLocation;
    public AudioClip clip;

    // Use this for initialization
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(0.0f, 45.0f * Time.deltaTime, 0.0f);
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Camera1")
        {
            objToTP.transform.position = tpLocation.transform.position;
            GetComponent<AudioSource>().PlayOneShot(clip);
        }
    }
}
