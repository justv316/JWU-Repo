
# Powershell best practice is to name functions with the Verb-Noun scheme
# While using approved verbs per Get-Verb
# Powershell has no such practices for classes, but PascalCase is expected
class Album{
    # Create an album class with basic information
    [String]$Name
    [String]$Artist
    [String]$Genre
    # Expanding on the original functionality with feedback from the professor
    # This integer will be used in a function to 
    # determine the rankings automatically
    [Int]$PlayCount
    # The object constructor
    Album([String]$Name, [String]$Artist, [String]$Genre, [Int]$PlayCount){
        $This.Name = $Name
        $This.Artist = $Artist
        $This.Genre = $Genre
        $This.PlayCount = $PlayCount
    }
}

# Build: Creates an artifact (usually a binary or document) out of some set
# of input files (usually source code or declarative documents)
function Build-List{
    # Read the Contents of the text file
    # It would be more efficient to use a CSV file as we can then easily
    # write back to it as an ez database but isn't the point of this exercise.
    $text = Get-Content ./album.txt
    # Create an ArrayList in the scripts' scope so we can access it
    $script:albums = New-Object System.Collections.ArrayList
    # r?n is RegEx for Newline. Split the text around new lines
    # Changed to using comma delimited text file
    # Text is formatted as Album Name,Artist Name,Genre Name,Playcount
    # foreach line in the text file, instantiate an album object with
    # the information split around commans
    foreach ($z in $text.split("r?n")){
        $zplit = $z.split(",")
        $album = New-Object Album -ArgumentList $zplit
        [void]$albums.Add($album)
    }
}
# Search: Creates a reference to a resource in a container
function Search-List{
    # Strictly enforce param typing
    [CmdletBinding()]
    Param(
        # PowerShell allows us to easily, cleanly and safely pass user input as
        # functional input
        [String]$SearchTerm
    )
    # Return albums that match the search term
    $albums.Where({$_.Genre -eq $SearchTerm})
}

# Test: Verifies the operation or consistency of a resource
function Test-Input{
    # Helper functions are named in camal case to differentiate their use
    # as compared to cmdlets that perform actual work. 
    Param(
    $Value
    )
    # Our search terms can only be a genre we have access to
    $validInput = $albums.Genre
    if($validInput -contains $Value){
        return $Value
    }
    else{
        # We can simply make this a boolean
        return $False
    }
}

# Request: Asks for a resource or asks for permissions
function Request-Input{
    # Check if the albums variable exists and create it if not
    # This way we only need to create this list once per session
    if ($Null -eq $albums){
        Build-List
    }
    # while loop that takes the available genres from the text file
    # and automatically prints and formats them as selections
    $i = 1
    Write-Host("==== Make a Selection ====")
    while($i -le $albums.count){
        foreach($z in $albums.genre){
            Write-Host "$($i). $($z)"
            $i++
        }
    }
    # now that we've printed available selections, we can request input.
    $UserInput = Read-Host "-> "
    # & invokes the function with the input as its argument
    if(&Test-Input -Value $UserInput -not $False){
        # Return album matching the entered genre
        Search-List $UserInput
    }
    else{
        Clear-Host
        Write-Host "You must make a valid selection."
        Request-Input
    }
}
# After the script is loaded into memory we just have to call 1 function
# Request-Input

# We've now recreated the original example program
