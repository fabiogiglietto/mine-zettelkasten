import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "MINE Zettelkasten",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "fabiogiglietto.github.io/mine-zettelkasten",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      // FG brand identity — Saira (DIN-style grotesque) for display/text/UI,
      // IBM Plex Mono for the "machine voice" (code, metadata). See the brand
      // sheet at static/brand.html for the full token set.
      typography: {
        header: { name: "Saira", weights: [300, 400, 500, 600, 700] },
        body: { name: "Saira", weights: [300, 400, 500, 600] },
        code: { name: "IBM Plex Mono", weights: [400, 500, 600] },
      },
      colors: {
        // MINE identity (mine.uniurb.it): the bold red wordmark as the signal,
        // on a crisp near-white ground, with gold + teal-blue as the secondary
        // brand colors (from the network-node graphic). Light = red on white.
        lightMode: {
          light: "#fcfcfb", // page background — crisp near-white
          lightgray: "#e4e3df", // borders / hr — hairline
          gray: "#6c7175", // muted / mono voice — steel grey
          darkgray: "#32363a", // body text — slate
          dark: "#1f2022", // headings / strong — near-black
          secondary: "#d4283a", // links — MINE red (signal)
          tertiary: "#a81f2d", // link hover / visited — deep red
          highlight: "rgba(212, 40, 58, 0.10)", // internal-link / search bg — red wash
          textHighlight: "#f0b04055", // ==mark== — MINE gold wash
        },
        // Dark = the "reversed on slate" treatment: deep teal-slate ground,
        // light slate-grey text, MINE red preserved (brightened) as the signal.
        darkMode: {
          light: "#15191c", // page background — deep teal-slate
          lightgray: "#2e353a", // borders / hr
          gray: "#868d93", // muted
          darkgray: "#cdd2d5", // body text — light slate-grey
          dark: "#f3f4f2", // headings / strong — near-white
          secondary: "#f2545b", // links — brightened MINE red
          tertiary: "#ff8a90", // link hover / visited — light red
          highlight: "rgba(242, 84, 91, 0.15)",
          textHighlight: "#f0b04055", // gold wash
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
