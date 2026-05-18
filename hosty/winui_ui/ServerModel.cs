using System.Text.Json.Serialization;

namespace winui_ui
{
    public class ServerModel
    {
        [JsonPropertyName("id")]
        public string Id { get; set; } = string.Empty;

        [JsonPropertyName("name")]
        public string Name { get; set; } = string.Empty;

        [JsonPropertyName("mc_version")]
        public string McVersion { get; set; } = string.Empty;

        [JsonPropertyName("loader_version")]
        public string LoaderVersion { get; set; } = string.Empty;

        [JsonPropertyName("ram_mb")]
        public int RamMb { get; set; }

        [JsonPropertyName("java_version")]
        public int JavaVersion { get; set; }

        [JsonPropertyName("icon_path")]
        public string IconPath { get; set; } = string.Empty;

        [JsonPropertyName("created_at")]
        public string CreatedAt { get; set; } = string.Empty;

        [JsonPropertyName("path")]
        public string Path { get; set; } = string.Empty;

        [JsonPropertyName("autostart")]
        public bool AutoStart { get; set; }
    }
}
