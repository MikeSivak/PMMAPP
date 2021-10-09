using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

public class NewBehaviourScript : MonoBehaviour, IPointerClickHandler
{
    private Rigidbody rb;
    public float force = 1.0f;
    // public InputField field;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    //Detect if a click occurs
    public void OnPointerClick(PointerEventData pointerEventData)
    {
        // if (!float.TryParse(field.text, out force))
        // {
        //     force = 0.1f;
        // }
        //Output to console the clicked GameObject's name and the following message. You can replace this with your own actions for when clicking the GameObject.
        Debug.Log(name + " Game Object Clicked!");
        rb.AddForce(0, 0, force, ForceMode.Impulse);
        GetComponent<Renderer>().material.color = Random.ColorHSV(0f, 1f, 1f, 1f, 0.5f, 1f);
    }
}
