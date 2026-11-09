---
symbol: "XKR7"
type: "gene"
col: 15309
ensembl_id: "ENSG00000260903"
name: "XK related 7"
location: "20q11.21"
module: 61
arm: "+"
pooled_cpm: 3.03
n_lines_expressing: 11
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 11
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# XKR7

*XK related 7* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.31× (z +14.4, q 5e-44, up in 3 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.283×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.310×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPF1]] (+0.60, fdr 1e-05), [[SRRM3]] (+0.58, fdr 7e-05), [[COL22A1]] (+0.52, fdr 4e-05); moves opposite to [[NUDT3]] (-0.46, fdr 1e-04), [[CLNS1A]] (-0.44, fdr 2e-04), [[PPIP5K2]] (-0.43, fdr 2e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[SRRM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15309.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.31×** | +14.4 | 5e-44 | 3/6 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.94×** | +13.7 | 2e-40 | 4/6 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.81×** | +10.4 | 3e-23 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.32×** | +9.0 | 3e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.91×** | +7.8 | 9e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.88×** | +6.5 | 7e-09 | 8/8 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.5 | 3e-06 | 2/8 (NCI-H23, PANC-1) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.07×** | +4.9 | 7e-05 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +4.6 | 2e-04 | 2/6 (KATO III, SW480) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.96×** | +4.4 | 5e-04 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +4.4 | 6e-04 | 8/8 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +4.3 | 9e-04 | 1/4 (SHP-77) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +4.1 | 0.002 | 0/5 | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +3.8 | 0.006 | 0/6 | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.37×** | +3.8 | 0.006 | 1/6 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.84×** | +3.7 | 0.007 | 0/7 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.012 | 1/8 (SW1417) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.83×** | +3.5 | 0.014 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +3.4 | 0.019 | 3/6 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.17×** | +3.4 | 0.019 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +3.3 | 0.021 | 0/6 | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.0 | 0.060 | 0/6 | top dose only | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.93×** | +2.9 | 0.088 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15309.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.283×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW1417 0.310×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.569× | -3.3 | 0.65 | 1/9 (NCI-H661) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15309. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 75.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.947 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15309), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPF1]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SRRM3]] | +0.58 | +0.59 / +0.37 | both halves | 7e-05 |  |
| [[COL22A1]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[SYN1]] | +0.49 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[LFNG]] | +0.49 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[GON7]] | +0.48 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[VAV1]] | +0.48 | +0.43 / +0.32 | both halves | 2e-04 |  |
| [[CHGB]] | +0.48 | +0.59 / +0.23 | both halves | 5e-04 |  |
| [[MAP1S]] | +0.48 | +0.35 / +0.38 | both halves | 1e-04 |  |
| [[ATP1A3]] | +0.48 | +0.56 / +0.24 | both halves | 4e-04 |  |
| [[C1QL1]] | +0.47 | +0.20 / +0.42 | both halves | 7e-04 |  |
| [[OLFM1]] | +0.47 | +0.29 / +0.48 | both halves | 3e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT3]] | -0.46 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[CLNS1A]] | -0.44 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[PPIP5K2]] | -0.43 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[METTL4]] | -0.41 | -0.31 / -0.26 | both halves | 4e-04 |  |
| [[CEP20]] | -0.41 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[NARS1]] | -0.41 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[TBC1D5]] | -0.41 | -0.33 / -0.23 | both halves | 5e-04 |  |
| [[GHITM]] | -0.40 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[USP45]] | -0.40 | -0.14 / -0.32 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers XKR7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CHGB]] | C | CHGB activity raises XKR7's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without CHGB | 0.028 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[RAB3C]] | C | RAB3C activity raises XKR7's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without RAB3C | 0.059 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[AFF2]] | C | AFF2 activity raises XKR7's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without AFF2 | 0.084 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises XKR7's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 1.48× lower at baseline in the lines without COL22A1 | 0.087 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[ACKR3]] | C | ACKR3 activity raises XKR7's level | lines that do not express ACKR3 (30) vs lines expressing it (20) | 1.41× lower at baseline in the lines without ACKR3 | 0.091 | ⚠ within organs, on part of the lines; also absent: IGFN1, ITGA11, NCAM1; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | XKR7 activity raises SRRM3's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 3.32× lower at baseline in the lines without XKR7 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[PAX5]] | B | XKR7 activity raises PAX5's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.81× lower at baseline in the lines without XKR7 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[CPLX1]] | B | XKR7 activity raises CPLX1's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without XKR7 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[PADI2]] | B | XKR7 activity strengthens PADI2's drug response | lines that do not express XKR7 (19) vs lines expressing it (6) | the lines without XKR7 respond 0.70× as strongly (z diff +1.52); strongest at Dinaciclib 5 µM: 1.06x vs 2.59x (z diff +5.1) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5; target measured in part of the lines; artifact flags |
| [[LRWD1]] | B | XKR7 activity raises LRWD1's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.23× lower at baseline in the lines without XKR7 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[FSD1]] | B | XKR7 activity raises FSD1's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.55× lower at baseline in the lines without XKR7 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[DLX2]] | B | XKR7 activity raises DLX2's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.63× lower at baseline in the lines without XKR7 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[SMPD3]] | B | XKR7 activity raises SMPD3's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without XKR7 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[RNASEH2A]] | B | XKR7 activity raises RNASEH2A's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 1.39× lower at baseline in the lines without XKR7 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[CHGB]] | C | XKR7 activity raises CHGB's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 3.81× lower at baseline in the lines without XKR7 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5; co-absent with the target |
| [[RAB3C]] | C | XKR7 activity raises RAB3C's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.30× lower at baseline in the lines without XKR7 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.7, 34.9); signed map (27.4, 18.0). **Vector** length 16.4, 3.78% of its response variance represented; |z| ≥ 3 in 156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.8 | +13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +3.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +3.7 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -3.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | XK related 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:31,968,151-32,003,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ310O13.4; previously C20orf159 |
| Gene groups (HGNC) | XK related family |
| Matched by | ensembl_id |

UniProt [Q5GH72](https://www.uniprot.org/uniprotkb/Q5GH72) carries no function annotation.

**Summary**, from NCBI Gene [343702](https://www.ncbi.nlm.nih.gov/gene/343702):

> Predicted to be involved in apoptotic process involved in development; engulfment of apoptotic cell; and phosphatidylserine exposure on apoptotic cell surface. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23062) · Entrez [343702](https://www.ncbi.nlm.nih.gov/gene/343702) · UniProt [Q5GH72](https://www.uniprot.org/uniprotkb/Q5GH72) · Ensembl [ENSG00000260903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260903)

## Data

Gene col 15309: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15309); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15309, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15309]; `tensor/DDL_lfc|DDL_z.npy` [15309]; `embed/gene_vectors.npy` [15309]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15309 or target_col == 15309). Every well: [[XKR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XKR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
