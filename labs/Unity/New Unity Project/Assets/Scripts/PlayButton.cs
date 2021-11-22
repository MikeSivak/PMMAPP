using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class PlayButton : MonoBehaviour
{
    // Button onclick functions
    public void Play_OnClick()
    {
        SceneManager.LoadScene("SampleScene");
    }
}
