---
symbol: "SYT9"
type: "gene"
col: 9998
ensembl_id: "ENSG00000170743"
name: "synaptotagmin 9"
location: "11p15.4"
module: 110
arm: "+"
pooled_cpm: 5.88
n_lines_expressing: 15
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# SYT9

*synaptotagmin 9* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.22× (z +11.1, q 6e-26, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +10.7, q 3e-24, up in 0 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CHP-212 0.138×, PANC-1 0.389×, LOX-IMVI 0.260×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.114×, PANC-1 0.346×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.194×, J82 0.115×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NETO1]] (+0.61, fdr 7e-06), [[EVC]] (+0.58, fdr 2e-05), [[CCNYL2]] (+0.58, fdr 4e-05); moves opposite to [[ADI1]] (-0.41, fdr 4e-04).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[OCA2]] → it (grade B ⚠); 4 go from it, the strongest it → [[ANKRD20A4P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +11.1 | 6e-26 | 0/8 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +10.7 | 3e-24 | 0/9 | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +10.2 | 3e-22 | 0/7 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.1 | 1e-17 | 0/6 | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.7 | 2e-12 | 6/12 (PANC-1, J82, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +6.0 | 2e-07 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.7 | 9e-07 | 3/8 (CFPAC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.4 | 5e-06 | 5/10 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.0 | 3e-05 | 0/9 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 8e-04 | 5/12 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.007 | 1/11 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.007 | 6/12 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.74×** | +3.8 | 0.008 | 1/7 (BT-474) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.7 | 0.010 | 0/6 | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.017 | 1/9 (NCI-H1573) | inconsistent across doses | low cells (technical?) |
| [[Pioglitazone (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.020 | 0/12 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.035 | 2/9 (BT-474, NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.056 | 4/9 (PANC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.067 | 0/12 | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.40×** | +2.9 | 0.089 | 2/9 (BT-474, A549) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CHP-212 0.138×, PANC-1 0.389×, LOX-IMVI 0.260×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.114×, PANC-1 0.346×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.194×, J82 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.680× | -3.4 | 0.36 | 1/12 (BT-474) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.701× | -3.2 | 0.46 | 1/12 (BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 82.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.6) |
| [[PANC-1 (line)]] | alt | 40.3 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -12.5) |
| [[BT-474 (line)]] | alt | 13.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +8.7) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.206× (z -8.5) |
| [[J82 (line)]] | alt | 7.21 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0937× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -8.8) |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -10.9) |
| [[A-172 (line)]] | wt | 0.671 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.673 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.869 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.705 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NETO1]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[EVC]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[CCNYL2]] | +0.58 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[LPAR3]] | +0.58 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ZNF677]] | +0.57 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[CCNYL2-1]] | +0.56 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[KIAA1549L]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD20A7P]] | +0.55 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[NTNG1]] | +0.54 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[LNCOG]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[CARD18]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LRFN5]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADI1]] | -0.41 | -0.25 / -0.38 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OCA2]] | B | OCA2 activity raises SYT9's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without OCA2 | 0.093 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[NOL4]] | C | NOL4 activity raises SYT9's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without NOL4 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[SLC6A17]] | C | SLC6A17 activity raises SYT9's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without SLC6A17 | 0.094 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A4P]] | B | SYT9 activity raises ANKRD20A4P's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 1.83× lower at baseline in the lines without SYT9 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8 |
| [[ANKRD20A7P]] | C | SYT9 activity raises ANKRD20A7P's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 1.83× lower at baseline in the lines without SYT9 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8; co-absent with the target |
| [[KCNQ3]] | C | SYT9 activity raises KCNQ3's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 2.49× lower at baseline in the lines without SYT9 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8; co-absent with the target |
| [[NOL4]] | C | SYT9 activity raises NOL4's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without SYT9 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8; co-absent with the target |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 23.5); signed map (20.1, 45.7). **Vector** length 34.9, 8.91% of its response variance represented; |z| ≥ 3 in 359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.8 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.7 | -1.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:7,238,778-7,469,043 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Synaptotagmins |
| Reactome | 7 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Cargo recognition for clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SS6](https://www.uniprot.org/uniprotkb/Q86SS6) (Synaptotagmin-9):

> May be involved in Ca(2+)-dependent exocytosis of secretory vesicles through Ca(2+) and phospholipid binding to the C2 domain or may serve as Ca(2+) sensors in the process of vesicular trafficking and exocytosis.

**Summary**, from NCBI Gene [143425](https://www.ncbi.nlm.nih.gov/gene/143425):

> Predicted to enable SNARE binding activity; calcium ion sensor activity; and calcium-dependent phospholipid binding activity. Predicted to be involved in chemical synaptic transmission; regulation of vesicle-mediated transport; and vesicle-mediated transport. Predicted to be located in clathrin-coated endocytic vesicle membrane. Predicted to be active in dense core granule; exocytic vesicle; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19265) · Entrez [143425](https://www.ncbi.nlm.nih.gov/gene/143425) · UniProt [Q86SS6](https://www.uniprot.org/uniprotkb/Q86SS6) · Ensembl [ENSG00000170743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170743)

## Data

Gene col 9998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9998); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9998]; `tensor/DDL_lfc|DDL_z.npy` [9998]; `embed/gene_vectors.npy` [9998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9998 or target_col == 9998). Every well: [[SYT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
