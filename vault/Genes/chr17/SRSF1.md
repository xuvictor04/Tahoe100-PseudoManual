---
symbol: "SRSF1"
type: "gene"
col: 5865
ensembl_id: "ENSG00000136450"
name: "serine and arginine rich splicing factor 1"
location: "17q22"
module: 3
arm: "-"
pooled_cpm: 96.34
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SRSF1

*serine and arginine rich splicing factor 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +11.0, q 3e-25, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.536× (z -8.4, q 4e-14, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.78, fdr 1e-05), [[EWSR1]] (+0.75, fdr 1e-05), [[ILF3]] (+0.70, fdr 7e-06); moves opposite to [[POLR2J]] (-0.80, fdr 1e-05, ⚠ POLR2J in the vector space only through flagged drug-doses), [[RNF181]] (-0.77, fdr 1e-05), [[LIN7B]] (-0.71, fdr 1e-05), [[TMEM191A-1]] (-0.70, fdr 4e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +11.0 | 3e-25 | 44/48 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +8.8 | 3e-16 | 45/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +7.9 | 5e-13 | 42/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.74×** | +7.4 | 2e-11 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +7.4 | 2e-11 | 40/48 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +7.4 | 2e-11 | 41/45 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.1 | 1e-10 | 36/44 (A-172, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.0 | 2e-10 | 39/49 (A-172, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +5.8 | 5e-07 | 39/47 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +5.7 | 8e-07 | 36/48 (SK-MEL-2, AN3 CA, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +5.6 | 1e-06 | 38/49 (NCI-H1573, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +5.5 | 2e-06 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.40×** | +4.2 | 0.001 | 32/47 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.2 | 0.001 | 35/48 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.6 | 0.011 | 31/48 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.536×** | -8.4 | 4e-14 | 48/48 (HEC-1-A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -6.6 | 9e-09 | 44/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.619×** | -6.4 | 2e-08 | 40/48 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.656×** | -5.7 | 2e-06 | 41/48 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -4.4 | 0.001 | 36/48 (NCI-H460, A-172, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -4.1 | 0.004 | 34/48 (hTERT-HPNE, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | **0.759×** | -3.7 | 0.016 | 37/49 (HEC-1-A, KATO III, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **0.776×** | -3.3 | 0.071 | 26/48 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.087 | 30/48 (NCI-H460, Panc 03.27, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.4 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 4.18× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 101 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 91.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 120 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 66.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 93.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 68.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +14.6) | — |
| [[SW480 (line)]] | alt | 127 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.45× (z +9.4) | — |
| [[A-172 (line)]] | wt | 58.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +10.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 53.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 78.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 103 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.23× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 129 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 132 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.8) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.392× (z -9.9) |
| [[A498 (line)]] | wt | 89.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 99.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 149 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -9.5) |
| [[HOP62 (line)]] | alt | 85.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 79.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.5) | — |
| [[J82 (line)]] | alt | 94.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.0) | — |
| [[LoVo (line)]] | wt | 87.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 99.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 97.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.153× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 73.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 81.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 91.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 95.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 69.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.6) | — |
| [[A-427 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 162 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.78 | +0.56 / +0.80 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 998 |
| [[EWSR1]] | +0.75 | +0.53 / +0.76 | both halves | 1e-05 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 799 |
| [[ILF3]] | +0.70 | +0.58 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 787 |
| [[SFPQ]] | +0.70 | +0.58 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 872 |
| [[DDX3X]] | +0.70 | +0.51 / +0.66 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 570 |
| [[HNRNPA3]] | +0.70 | +0.46 / +0.81 | both halves | 2e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 918 |
| [[FUBP1]] | +0.70 | +0.54 / +0.65 | both halves | 1e-05 | STRING 628 |
| [[CBX5]] | +0.69 | +0.57 / +0.70 | both halves | 9e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[HNRNPL]] | +0.69 | +0.55 / +0.61 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 945 |
| [[SRSF6]] | +0.69 | +0.57 / +0.65 | both halves | 8e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 987 |
| [[SSU72]] | +0.68 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[HNRNPM]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 956 |

## Genes that move opposite

*62 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J]] ⚠ | -0.80 | -0.53 / -0.81 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 581; ⚠ in the vector space only through flagged drug-doses |
| [[RNF181]] | -0.77 | -0.55 / -0.77 | both halves | 1e-05 |  |
| [[LIN7B]] | -0.71 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | -0.70 | -0.42 / -0.75 | both halves | 4e-05 |  |
| [[COMMD6]] | -0.70 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.69 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[CAMLG]] | -0.68 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.68 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[SNAPC2]] | -0.68 | -0.39 / -0.68 | both halves | 6e-05 |  |
| [[ING2]] | -0.67 | -0.49 / -0.73 | both halves | 1e-05 |  |
| [[RPP21]] | -0.67 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[TMEM256]] | -0.66 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[NUDT22]] | -0.66 | -0.38 / -0.66 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SRSF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.764). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.2, -24.7); signed map (14.7, -38.1). **Vector** length 130, 43.8% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +13.5 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.7 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.8 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.2 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.8 | -8.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.4 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.0 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,000,919-58,007,346 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASF, SF2, SRp30a, SF2p33, MGC5228; previously SFRS1 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 12 pathways, smallest: mRNA Splicing - Minor Pathway; Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07955](https://www.uniprot.org/uniprotkb/Q07955) (Serine/arginine-rich splicing factor 1):

> Plays a role in preventing exon skipping, ensuring the accuracy of splicing and regulating alternative splicing. Interacts with other spliceosomal components, via the RS domains, to form a bridge between the 5'- and 3'-splice site binding components, U1 snRNP and U2AF. Can stimulate binding of U1 snRNP to a 5'-splice site-containing pre-mRNA. Binds to purine-rich RNA sequences, either the octamer, 5'-RGAAGAAC-3' (r=A or G) or the decamers, AGGACAGAGC/AGGACGAAGC. Binds preferentially to the …

**Summary**, from NCBI Gene [6426](https://www.ncbi.nlm.nih.gov/gene/6426):

> This gene encodes a member of the arginine/serine-rich splicing factor protein family. The encoded protein can either activate or repress splicing, depending on its phosphorylation state and its interaction partners. Multiple transcript variants have been found for this gene. There is a pseudogene of this gene on chromosome 13. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:10780](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10780) · Entrez [6426](https://www.ncbi.nlm.nih.gov/gene/6426) · UniProt [Q07955](https://www.uniprot.org/uniprotkb/Q07955) · Ensembl [ENSG00000136450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136450)

## Data

Gene col 5865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5865); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5865]; `tensor/DDL_lfc|DDL_z.npy` [5865]; `embed/gene_vectors.npy` [5865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5865 or target_col == 5865). Every well: [[SRSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
