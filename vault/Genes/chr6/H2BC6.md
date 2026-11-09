---
symbol: "H2BC6"
type: "gene"
col: 15814
ensembl_id: "ENSG00000274290"
name: "H2B clustered histone 6"
location: "6p22.2"
module: null
arm: null
pooled_cpm: 5.69
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 0
n_dd_up_clean: 33
n_dd_down_clean: 0
in_vector_space: false
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# H2BC6

*H2B clustered histone 6* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 24.3× (z +46.8, q 0e+00, up in 41 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.113×; ⚠ cell-cycle shift, explains ~55% of this change); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0832×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0924×).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **24.3×** | +46.8 | 0e+00 | 41/41 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **13.4×** | +26.9 | 0e+00 | 34/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.00×** | +20.3 | 0e+00 | 38/39 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **6.93×** | +19.3 | 0e+00 | 42/43 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.72×** | +19.3 | 0e+00 | 38/48 (HOP62, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.60×** | +9.9 | 4e-21 | 33/43 (A-172, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +9.3 | 1e-18 | 4/8 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +9.3 | 1e-18 | 19/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.36×** | +8.9 | 3e-17 | 29/46 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **2.22×** | +8.3 | 8e-15 | 29/47 (A-172, NCI-H1573, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.14×** | +7.9 | 2e-13 | 26/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.9 | 2e-13 | 8/14 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **2.07×** | +7.6 | 2e-12 | 31/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +7.5 | 2e-12 | 19/45 (PANC-1, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +7.5 | 2e-12 | 25/47 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **1.48×** | +5.8 | 3e-07 | 20/47 (SW480, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.6 | 6e-07 | 17/48 (A498, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.80×** | +5.6 | 8e-07 | 14/44 (SW480, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15814.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1573 0.113×; ⚠ cell-cycle shift, explains ~55% of this change); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0832×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.0924×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.732× | -3.2 | 0.37 | 13/46 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.738× | -3.1 | 0.37 | 8/47 (SNU-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.723× | -3.1 | 0.37 | 6/46 (NCI-H661, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.61 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +26.6) | — |
| [[A-172 (line)]] | wt | 9.50 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 7.58 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.3× (z +23.6) | — |
| [[KATO III (line)]] | alt | 8.60 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +17.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.69 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +11.3) | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0832× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 2.70 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 78.4× (z +22.7) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0924× (z -8.5) |
| [[C32 (line)]] | wt | 4.07 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 90.3× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 3.22 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.0× (z +14.5) | — |
| [[LoVo (line)]] | wt | 5.71 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.2× (z +22.0) | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +15.3) | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -10.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H23 (line)]] | alt | 12.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.5× (z +20.4) | — |
| [[NCI-H2347 (line)]] | alt | 3.06 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.2× (z +16.4) | — |
| [[SW480 (line)]] | alt | 6.42 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +23.1) | — |
| [[A498 (line)]] | wt | 2.88 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.3× (z +17.4) | — |
| [[COLO 205 (line)]] | alt | 5.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.1× (z +15.8) | — |
| [[hTERT-HPNE (line)]] | wt | 4.45 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.4× (z +15.3) | — |
| [[J82 (line)]] | alt | 6.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.0× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 3.85 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.7× (z +19.5) | — |
| [[LS 180 (line)]] | wt | 2.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.4× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 7.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +20.7) | — |
| [[Panc 03.27 (line)]] | alt | 5.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 6.30 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +14.2) | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +17.9) | — |
| [[SW 900 (line)]] | alt | 4.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +12.5) | — |
| [[A549 (line)]] | wt | 6.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 2.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 9.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +13.6) | — |
| [[HCT15 (line)]] | alt | 3.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 4.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.2× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 7.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 2.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.5× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 34.3× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 5.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.94× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 6.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +15.1) | — |
| [[SW 1271 (line)]] | alt | 7.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.5× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 3.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.56× (z +10.4) | — |
| [[SW48 (line)]] | wt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +11.3) | — |
| [[A-427 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.75 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers H2BC6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | H2B clustered histone 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,172,059-26,184,655 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H2B/h, H2B.h; previously H2BFH, HIST1H2BE |
| Gene groups (HGNC) | H2B histones; Proteins encoded by multiple genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P62807](https://www.uniprot.org/uniprotkb/P62807) (Histone H2B type 1-C/E/F/G/I):

> Core component of nucleosome. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling.; Has broad antibacterial activity. May contribute to the …

**Summary**, from NCBI Gene [8344](https://www.ncbi.nlm.nih.gov/gene/8344):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of chromatin into higher order structures. The protein has antibacterial and antifungal …

**Accessions** — [HGNC:4753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4753) · Entrez [8344](https://www.ncbi.nlm.nih.gov/gene/8344) · UniProt [P62807](https://www.uniprot.org/uniprotkb/P62807) · Ensembl [ENSG00000274290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274290)

## Data

Gene col 15814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15814); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15814, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15814]; `tensor/DDL_lfc|DDL_z.npy` [15814]; `embed/gene_vectors.npy` [15814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15814 or target_col == 15814). Every well: [[H2BC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2BC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
