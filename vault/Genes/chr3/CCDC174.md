---
symbol: "CCDC174"
type: "gene"
col: 7838
ensembl_id: "ENSG00000154781"
name: "coiled-coil domain containing 174"
location: "3p25.1"
module: 12
arm: "+"
pooled_cpm: 46.46
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CCDC174

*coiled-coil domain containing 174* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.73× (z +23.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.583× (z -6.6, q 3e-08, down in 27 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.658× (z -5.3, q 1e-05, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNW1]] (+0.87, fdr 7e-06), [[C1orf131]] (+0.83, fdr 7e-06), [[NFKBIL1]] (+0.81, fdr 7e-06); moves opposite to [[RBBP7]] (-0.73, fdr 7e-06), [[MAPK9]] (-0.72, fdr 7e-06), [[SELENON]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +23.6 | 0e+00 | 48/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.03×** | +17.6 | 0e+00 | 48/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.34×** | +14.7 | 0e+00 | 47/48 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.38×** | +10.4 | 4e-23 | 47/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.08×** | +9.3 | 2e-18 | 44/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.58×** | +8.4 | 3e-15 | 44/49 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.3 | 0.001 | 31/48 (BT-474, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.7 | 0.013 | 28/47 (RKO, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | 1.28× | +3.1 | 0.10 | 19/48 (H4, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.12 | 18/48 (SNU-423, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -6.6 | 3e-08 | 27/41 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.628×** | -5.9 | 7e-07 | 40/48 (SW1417, NCI-H1792, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -5.9 | 7e-07 | 32/49 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.658×** | -5.3 | 1e-05 | 38/48 (SW1417, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -5.1 | 4e-05 | 34/48 (H4, A-172, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.655×** | -5.0 | 6e-05 | 30/45 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.705×** | -4.4 | 7e-04 | 29/48 (SW1417, KATO III, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.807×** | -3.9 | 0.007 | 25/48 (RKO, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.730×** | -3.9 | 0.007 | 24/48 (hTERT-HPNE, RKO, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.007 | 22/48 (LS 180, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.631× | -3.1 | 0.12 | 16/48 (SNU-423, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 41.8 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.03× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 50.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 40.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 60.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +20.9) | — |
| [[RKO (line)]] | wt | 48.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.98× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 48.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +16.1) | — |
| [[A549 (line)]] | wt | 62.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +22.9) | — |
| [[HS-578T (line)]] | alt | 45.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 54.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -19.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +17.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +17.0) | — |
| [[NCI-H2030 (line)]] | alt | 42.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +20.2) | — |
| [[NCI-H2347 (line)]] | alt | 47.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 41.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -15.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 53.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +18.3) | — |
| [[A498 (line)]] | wt | 32.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 42.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 50.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +21.6) | — |
| [[HT-29 (line)]] | alt | 32.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +17.4) | — |
| [[LOX-IMVI (line)]] | wt | 35.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 53.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +15.3) | — |
| [[Panc 03.27 (line)]] | alt | 49.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 68.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 47.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 66.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 34.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +16.5) | — |
| [[C32 (line)]] | wt | 41.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +14.4) | — |
| [[H4 (line)]] | wt | 55.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.06× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 82.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 48.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -15.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 44.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +16.5) | — |
| [[NCI-H23 (line)]] | alt | 48.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +14.2) | — |
| [[SW48 (line)]] | wt | 42.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.2) | — |
| [[AN3 CA (line)]] | alt | 53.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 44.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 37.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 53.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -10.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 48.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 56.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 49.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[SW 1271 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNW1]] | +0.87 | +0.87 / +0.82 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.83 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.81 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[PEX12]] | +0.81 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[MED18]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[PPIG]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[PHAX]] | +0.80 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.80 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[COIL]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[NRBF2]] | +0.79 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.79 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.78 | +0.83 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP7]] | -0.73 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.72 | -0.58 / -0.73 | both halves | 7e-06 |  |
| [[SELENON]] | -0.71 | -0.71 / -0.66 | both halves | 7e-06 |  |
| [[ADAM15]] | -0.70 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NUTF2]] | -0.69 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[FKBP1A]] | -0.69 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[CDK2]] | -0.68 | -0.74 / -0.54 | both halves | 1e-05 |  |
| [[PPT1]] | -0.68 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[COLGALT1]] | -0.68 | -0.64 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CCDC174's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CCDC174's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.894). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.9, 2.9); signed map (0.2, -16.7). **Vector** length 149, 51.3% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.62 to 17); *mRNA Splicing* (reactome, mean cos +0.62 to 17); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.59 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.4 | +17.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +12.3 | +23.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.1 | +14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.4 | +9.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.5 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.1 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.9 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.7 | -1.6 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 174 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,651,762-14,672,659 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33839, ctr1; previously C3orf19 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PII3](https://www.uniprot.org/uniprotkb/Q6PII3) (Coiled-coil domain-containing protein 174):

> Probably involved in neuronal development.

**Summary**, from NCBI Gene [51244](https://www.ncbi.nlm.nih.gov/gene/51244):

> The protein encoded by this gene is found in the nucleus, where it interacts with eukaryotic translation initiation factor 4A, isoform 3. The encoded protein appears to be a part of the exon junction complex, which is involved in RNA processing, translation, and nonsense-mediated mRNA decay. A mutation in this gene has been associated with infantile hypotonia with psychomotor retardation. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:28033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28033) · Entrez [51244](https://www.ncbi.nlm.nih.gov/gene/51244) · UniProt [Q6PII3](https://www.uniprot.org/uniprotkb/Q6PII3) · Ensembl [ENSG00000154781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154781)

## Data

Gene col 7838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7838); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7838]; `tensor/DDL_lfc|DDL_z.npy` [7838]; `embed/gene_vectors.npy` [7838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7838 or target_col == 7838). Every well: [[CCDC174 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC174.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
