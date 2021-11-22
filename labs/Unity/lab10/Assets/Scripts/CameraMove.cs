using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class CameraMove : MonoBehaviour
{
    float mouseSensitivity = 100.0f;
    float clampAngle = 80.0f;

    float rotationY = 0.0f;
    float rotationX = 0.0f;
    float speed = 5.0f;

    // Start is called before the first frame update
    void Start()
    {
        Vector3 rotation = transform.localRotation.eulerAngles;
        rotationY = rotation.y;
        rotationX = rotation.x;
           
    }

    // Update is called once per frame
    void Update()
    {
        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");

        rotationY += mouseX * mouseSensitivity * Time.deltaTime * speed;
        rotationX += mouseY * mouseSensitivity * Time.deltaTime * speed;

        Quaternion localRotation = Quaternion.Euler(-rotationX, rotationY, 0.0f);
        transform.rotation = localRotation;
    }
}