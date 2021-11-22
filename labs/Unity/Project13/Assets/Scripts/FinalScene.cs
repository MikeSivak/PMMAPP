using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class FinalScene : MonoBehaviour
{
    
    // Button onclick functions
    public void Play_OnClick()
    {
        SceneManager.LoadScene("SampleScene");
    }
    public void Play_OnClick1()
    {
        SceneManager.LoadScene("MainMenu");
    }
}