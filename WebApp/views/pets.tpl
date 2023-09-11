<html>
    <body>
        <h1>List of Pets</h1>
        <ul>
<<<<<<< HEAD
        % for item in data:
            <li>{{item[1] + ' - ' + item[2]}}</li>
=======
        % for pet in pets:
            <li>{{pet['name'] + ' - ' + pet['kind']}}</li>
>>>>>>> origin/main
        % end
        </ul>
        <h1>Table of Pets</h1>
        <table>
<<<<<<< HEAD
        % for name in names[1:]:
            <th>{{name}}</th>
        % end
        % for item in data:
            <tr>
                <td>{{item[1]}}</td>
                <td>{{item[2]}}</td>
=======
        % for pet in pets:
            <tr>
                <td>{{pet['name']}}</td>
                <td>{{pet['kind']}}</td>
>>>>>>> origin/main
            <tr>
        % end
        </table>
    </body>
</html>


