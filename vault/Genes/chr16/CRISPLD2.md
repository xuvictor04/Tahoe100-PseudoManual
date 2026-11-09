---
symbol: "CRISPLD2"
type: "gene"
col: 2333
ensembl_id: "ENSG00000103196"
name: "cysteine rich secretory protein LCCL domain containing 2"
location: "16q24.1"
module: 93
arm: "+"
pooled_cpm: 13.91
n_lines_expressing: 38
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# CRISPLD2

*cysteine rich secretory protein LCCL domain containing 2* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 33.1× (z +41.7, q 0e+00, up in 36 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.610×; ⚠ position not correctable); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW 900 0.0806×); [[Elimusertib hydrochloride (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0501×; ⚠ toxic).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA2]] (+0.55, fdr 3e-05), [[HAPLN3]] (+0.51, fdr 3e-05), [[FBLN2]] (+0.50, fdr 2e-05); moves opposite to [[CDADC1]] (-0.47, fdr 5e-05), [[C12orf4]] (-0.47, fdr 1e-04), [[ZNF214]] (-0.45, fdr 0.001, ⚠ not reproduced), [[CCDC66]] (-0.44, fdr 1e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2333.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **33.1×** | +41.7 | 0e+00 | 36/36 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **21.0×** | +34.7 | 0e+00 | 36/36 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **10.0×** | +27.5 | 0e+00 | 35/36 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **7.47×** | +24.0 | 0e+00 | 26/34 (HOP62, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.81×** | +22.5 | 0e+00 | 26/34 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.29×** | +20.1 | 0e+00 | 28/34 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.28×** | +20.0 | 0e+00 | 32/35 (HOP62, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.18×** | +13.8 | 3e-41 | 18/27 (SW480, SNU-423, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.81×** | +12.3 | 7e-33 | 26/36 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.88×** | +11.7 | 1e-29 | 12/22 (SNU-423, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.58×** | +10.9 | 9e-26 | 9/17 (A498, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +10.0 | 6e-22 | 16/34 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.31×** | +9.6 | 5e-20 | 20/32 (A498, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.19×** | +8.9 | 2e-17 | 19/33 (A498, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **2.16×** | +8.8 | 4e-17 | 18/31 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +8.6 | 3e-16 | 20/34 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +8.6 | 3e-16 | 22/35 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.43×** | +7.7 | 5e-13 | 21/35 (J82, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.7 | 3e-07 | 16/36 (A549, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +4.8 | 4e-05 | 11/33 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.03×** | +4.4 | 3e-04 | 7/33 (SW480, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2333.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.610×; ⚠ position not correctable); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (SW 900 0.0806×); [[Elimusertib hydrochloride (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0501×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.820× | -3.4 | 0.40 | 14/36 (SHP-77, hTERT-HPNE, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.768× | -3.2 | 0.43 | 14/35 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.768× | -3.0 | 0.44 | 13/32 (HOP62, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.92 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2333. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.5 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 64.9× (z +21.9) | — |
| [[SW480 (line)]] | alt | 6.04 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 51.0× (z +20.1) | — |
| [[J82 (line)]] | alt | 26.3 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 31.1× (z +21.3) | — |
| [[A-172 (line)]] | wt | 9.34 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 36.0× (z +14.5) | — |
| [[A498 (line)]] | wt | 42.6 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 9.01 | 6 | 0 | [[Auranofin (drug)]] 5 µM 15.7× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 6.51 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 74.3× (z +14.1) | — |
| [[SW 900 (line)]] | alt | 12.5 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 39.8× (z +14.3) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0806× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 9.37 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 31.4× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 9.96 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 27.9× (z +18.6) | — |
| [[SW1417 (line)]] | alt | 7.15 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 59.6× (z +15.7) | — |
| [[A549 (line)]] | wt | 5.00 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 124× (z +15.2) | — |
| [[H4 (line)]] | wt | 23.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 38.8× (z +15.0) | — |
| [[HS-578T (line)]] | alt | 102 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 15.6× (z +18.7) | — |
| [[hTERT-HPNE (line)]] | wt | 66.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 20.1× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 81.2× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 13.8× (z +14.4) | [[Adagrasib (drug)]] 0.05 µM 0.610× (z -9.5) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 36.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 18.1× (z +14.8) | — |
| [[SNU-423 (line)]] | alt | 16.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 34.9× (z +14.9) | — |
| [[BT-474 (line)]] | alt | 11.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.0× (z +10.7) | — |
| [[C32 (line)]] | wt | 3.71 | 3 | 0 | [[Auranofin (drug)]] 5 µM 72.9× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 6.61 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 97.4× (z +14.4) | — |
| [[AsPC-1 (line)]] | alt | 7.95 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 35.8× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 10.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.6× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 28.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.3× (z +11.8) | — |
| [[KATO III (line)]] | alt | 21.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 18.5× (z +13.6) | — |
| [[LS 180 (line)]] | wt | 5.97 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 18.3× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 7.04 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 48.0× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 8.19 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 30.9× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 5.09 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 26.1× (z +9.8) | — |
| [[A-427 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 78.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2333), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA2]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[HAPLN3]] | +0.51 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[FBLN2]] | +0.50 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[ENPP2]] | +0.49 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[HAP1]] | +0.48 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[PRSS22]] | +0.48 | +0.37 / +0.32 | both halves | 2e-04 |  |
| [[NPTXR]] | +0.47 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[EMP1]] | +0.47 | +0.25 / +0.51 | both halves | 4e-04 |  |
| [[TEX15]] | +0.47 | +0.28 / +0.56 | both halves | 3e-04 |  |
| [[SDC4]] | +0.46 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[STON2]] | +0.46 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[GCH1]] | +0.46 | +0.35 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDADC1]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[C12orf4]] | -0.47 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ZNF214]] | -0.45 | -0.17 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[CCDC66]] | -0.44 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[OBI1]] | -0.44 | -0.19 / -0.35 | ⚠ not reproduced | 8e-04 |  |
| [[ZNF223]] | -0.44 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[LETMD1]] | -0.43 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[CBY1]] | -0.43 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[VPS33A]] | -0.42 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[TMLHE]] | -0.42 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[WDR53]] | -0.41 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[MORN4]] | -0.41 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[LSM8]] | -0.41 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[TRAPPC13]] | -0.41 | -0.33 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CRISPLD2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENPP2]] | B | ENPP2 activity raises CRISPLD2's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without ENPP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.3, 36.9); signed map (21.0, 20.0). **Vector** length 76.0, 14.6% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +20.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +24.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +4.3 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.9 | +11.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | cysteine rich secretory protein LCCL domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,819,985-84,920,768 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434B044, LGL1; previously LCRISP2 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0B8](https://www.uniprot.org/uniprotkb/Q9H0B8) (Cysteine-rich secretory protein LCCL domain-containing 2):

> Promotes matrix assembly.

**Summary**, from NCBI Gene [83716](https://www.ncbi.nlm.nih.gov/gene/83716):

> Predicted to enable glycosaminoglycan binding activity. Involved in face morphogenesis. Located in transport vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25248) · Entrez [83716](https://www.ncbi.nlm.nih.gov/gene/83716) · UniProt [Q9H0B8](https://www.uniprot.org/uniprotkb/Q9H0B8) · Ensembl [ENSG00000103196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103196)

## Data

Gene col 2333: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2333); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2333, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2333]; `tensor/DDL_lfc|DDL_z.npy` [2333]; `embed/gene_vectors.npy` [2333]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2333 or target_col == 2333). Every well: [[CRISPLD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRISPLD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
