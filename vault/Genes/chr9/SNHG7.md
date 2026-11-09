---
symbol: "SNHG7"
type: "gene"
col: 13883
ensembl_id: "ENSG00000233016"
name: "small nucleolar RNA host gene 7"
location: "9q34.3"
module: 24
arm: "+"
pooled_cpm: 42.09
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SNHG7

*small nucleolar RNA host gene 7* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.01× (z +4.4, q 0.006, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.301× (z -4.0, q 0.043, down in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.0878×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.143×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4A-AS1]] (+0.92, fdr 7e-06), [[SNHG32]] (+0.85, fdr 7e-06), [[SNHG12]] (+0.84, fdr 7e-06); moves opposite to [[PSME3]] (-0.73, fdr 1e-05), [[DR1]] (-0.70, fdr 1e-05), [[TARDBP]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +4.4 | 0.006 | 43/48 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +4.1 | 0.010 | 44/48 (HT-29, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +3.9 | 0.017 | 37/48 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.5 | 0.064 | 33/47 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.67× | +3.2 | 0.16 | 27/46 (C32, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.41× | +3.1 | 0.17 | 28/48 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.66× | +3.1 | 0.17 | 31/45 (BT-474, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.22× | +3.0 | 0.17 | 39/46 (CFPAC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13883.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.0878×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.143×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.301×** | -4.0 | 0.043 | 37/49 (A549, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.572× | -3.5 | 0.11 | 35/48 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.357× | -3.4 | 0.11 | 37/46 (C-33 A, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.687× | -3.4 | 0.11 | 31/48 (SNU-1, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 22.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +9.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.45× (z +9.1) | — |
| [[A549 (line)]] | wt | 63.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -11.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 62.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | same gene group |
| [[SNHG32]] | +0.85 | +0.85 / +0.88 | both halves | 7e-06 | same gene group |
| [[SNHG12]] | +0.84 | +0.87 / +0.86 | both halves | 7e-06 | same gene group |
| [[SNHG6]] | +0.84 | +0.81 / +0.85 | both halves | 7e-06 | same gene group |
| [[NACA4P]] ⚠ | +0.83 | +0.68 / +0.85 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG8]] | +0.83 | +0.79 / +0.88 | both halves | 7e-06 | same gene group |
| [[CAMLG]] | +0.83 | +0.63 / +0.88 | both halves | 7e-06 |  |
| [[GAS5]] | +0.79 | +0.70 / +0.82 | both halves | 7e-06 | same gene group |
| [[RPL18]] ⚠ | +0.78 | +0.52 / +0.85 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZFAS1]] | +0.78 | +0.78 / +0.79 | both halves | 7e-06 | same gene group |
| [[TAF1D]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[RPS27]] | +0.76 | +0.55 / +0.81 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.76 | +0.61 / +0.80 | both halves | 7e-06 | same gene group |
| [[RPL36]] | +0.75 | +0.49 / +0.83 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.73 | -0.53 / -0.76 | both halves | 1e-05 |  |
| [[DR1]] | -0.70 | -0.51 / -0.71 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.69 | -0.46 / -0.73 | both halves | 3e-05 |  |
| [[VMA21]] | -0.68 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[GPAA1]] | -0.68 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.66 | -0.43 / -0.72 | both halves | 3e-05 |  |
| [[ERLIN2]] | -0.66 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[SRP9]] | -0.65 | -0.57 / -0.72 | both halves | 9e-06 |  |
| [[NUP188]] | -0.65 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[GNG12]] | -0.65 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.65 | -0.61 / -0.70 | both halves | 7e-06 |  |
| [[POGLUT3]] | -0.65 | -0.49 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SNHG7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.0, -28.5); signed map (-15.4, -2.3). **Vector** length 119, 47.1% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.9 | +1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.6 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.1 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.6 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.4 | -0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -1.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.8 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 7 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q34.3 — chr9:136,721,366-136,728,184 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MGC16037, NCRNA00061 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [84973](https://www.ncbi.nlm.nih.gov/gene/84973):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28254) · Entrez [84973](https://www.ncbi.nlm.nih.gov/gene/84973) · Ensembl [ENSG00000233016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233016)

## Data

Gene col 13883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13883); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13883]; `tensor/DDL_lfc|DDL_z.npy` [13883]; `embed/gene_vectors.npy` [13883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13883 or target_col == 13883). Every well: [[SNHG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
