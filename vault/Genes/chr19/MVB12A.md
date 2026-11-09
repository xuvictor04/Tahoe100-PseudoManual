---
symbol: "MVB12A"
type: "gene"
col: 6586
ensembl_id: "ENSG00000141971"
name: "multivesicular body subunit 12A"
location: "19p13.11"
module: 32
arm: "+"
pooled_cpm: 23.21
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# MVB12A

*multivesicular body subunit 12A* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.70× (z +6.9, q 2e-09, up in 24 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.31× (z +3.6, q 0.069, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 5.31×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.348× (z -19.6, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BST2]] (+0.75, fdr 7e-06, ⚠ same locus), [[CCDC194]] (+0.74, fdr 7e-06, ⚠ same locus), [[UBE2L6]] (+0.70, fdr 1e-05), [[STAT2]] (+0.70, fdr 1e-05), [[SHFL]] (+0.69, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CCDC194]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6586.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 5.31×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.9 | 2e-09 | 24/43 (J82, H4, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.7 | 4e-06 | 18/31 (NCI-H460, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.069 | 19/48 (A-427, HT-29, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.24 | 7/45 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.40× | +3.0 | 0.24 | 10/44 (NCI-H23, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.0 | 0.24 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -19.6 | 0e+00 | 44/47 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.470×** | -9.9 | 1e-20 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.480×** | -9.6 | 1e-19 | 39/47 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.550×** | -7.8 | 7e-13 | 37/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.564×** | -7.5 | 6e-12 | 31/46 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -6.3 | 2e-08 | 34/48 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.718×** | -6.1 | 6e-08 | 24/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -6.1 | 6e-08 | 31/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.625×** | -5.9 | 2e-07 | 29/47 (RPMI-7951, A498, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.430×** | -5.8 | 4e-07 | 30/45 (Hs 766T, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.705×** | -4.6 | 2e-04 | 25/47 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.759×** | -3.6 | 0.015 | 18/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.763×** | -3.6 | 0.017 | 17/47 (LOX-IMVI, AN3 CA, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -3.3 | 0.038 | 19/44 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.767×** | -3.3 | 0.038 | 17/47 (SW48, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.784×** | -3.2 | 0.050 | 16/48 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.790×** | -3.1 | 0.068 | 12/48 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 57.6 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -13.9) ⚠ toxic · without an alert: [[Tofacitinib (drug)]] 5 µM 0.395× (z -10.9) |
| [[SW480 (line)]] | alt | 14.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.5) |
| [[A498 (line)]] | wt | 27.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -20.7) |
| [[COLO 205 (line)]] | alt | 75.5 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.225× (z -10.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -9.5) |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -19.5) |
| [[SNU-423 (line)]] | alt | 31.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -16.1) |
| [[A-172 (line)]] | wt | 36.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.5) |
| [[A-427 (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.5) |
| [[A549 (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.1) |
| [[H4 (line)]] | wt | 34.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -10.9) |
| [[J82 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.1) |
| [[KATO III (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0698× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0771× (z -21.1) |
| [[NCI-H2030 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 9.78 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.31× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 64.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.3) |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.341× (z -8.6) |
| [[RKO (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.0) |
| [[SHP-77 (line)]] | alt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.7) |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.8) |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BST2]] | +0.75 | +0.61 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[CCDC194]] | +0.74 | +0.61 / +0.85 | both halves | 7e-06 | ⚠ same locus (11.5 kb: neighbours can correlate without regulation) |
| [[UBE2L6]] | +0.70 | +0.57 / +0.76 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[STAT2]] | +0.70 | +0.55 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SHFL]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[IFI35]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI6]] | +0.67 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[TMEM140]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 517 |
| [[OAS1]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[USP18]] | +0.65 | +0.49 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFITM1]] | +0.64 | +0.48 / +0.73 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[CMPK2]] | +0.63 | +0.52 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[RSAD2]] | +0.63 | +0.57 / +0.68 | both halves | 9e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[MX2]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC194]] | B | CCDC194 activity raises MVB12A's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without CCDC194 | 0.001 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[BST2]] | B | BST2 activity raises MVB12A's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without BST2 | 0.002 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[CCDC194]] | B | CCDC194 activity strengthens MVB12A's drug response | lines that do not express CCDC194 (19) vs lines expressing it (29) | the lines without CCDC194 respond 0.74× as strongly (z diff +1.05); strongest at Tofacitinib 5 µM: 0.98x vs 0.59x (z diff +3.3) | 0.016 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22; target measured in part of the lines; the reference differs; artifact flags |
| [[IFI27]] | B | IFI27 activity raises MVB12A's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.44× lower at baseline in the lines without IFI27 | 0.088 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[EPSTI1]] | B | EPSTI1 activity raises MVB12A's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without EPSTI1 | 0.094 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.1, 53.1); signed map (67.4, 30.3). **Vector** length 76.9, 16.0% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.54 to 60); *interferon* (control, mean cos +0.58 to 23); *Interferon Signaling* (reactome, mean cos +0.56 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.4 | -6.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -19.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | multivesicular body subunit 12A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,405,722-17,433,724 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32495; previously FAM125A |
| Gene groups (HGNC) | ESCRT-I |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 15 pathways, smallest: Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins; Assembly Of The HIV Virion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EY5](https://www.uniprot.org/uniprotkb/Q96EY5) (Multivesicular body subunit 12A):

> Component of the ESCRT-I complex, a regulator of vesicular trafficking process. Required for the sorting of endocytic ubiquitinated cargos into multivesicular bodies. May be involved in the ligand-mediated internalization and down-regulation of EGF receptor.

**Summary**, from NCBI Gene [93343](https://www.ncbi.nlm.nih.gov/gene/93343):

> Enables lipid binding activity and ubiquitin binding activity. Involved in regulation of epidermal growth factor receptor signaling pathway. Located in centrosome; cytosol; and vesicle. Part of ESCRT I complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25153) · Entrez [93343](https://www.ncbi.nlm.nih.gov/gene/93343) · UniProt [Q96EY5](https://www.uniprot.org/uniprotkb/Q96EY5) · Ensembl [ENSG00000141971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141971)

## Data

Gene col 6586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6586); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6586]; `tensor/DDL_lfc|DDL_z.npy` [6586]; `embed/gene_vectors.npy` [6586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6586 or target_col == 6586). Every well: [[MVB12A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MVB12A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
