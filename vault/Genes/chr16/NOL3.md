---
symbol: "NOL3"
type: "gene"
col: 6464
ensembl_id: "ENSG00000140939"
name: "nucleolar protein 3"
location: "16q22.1"
module: 144
arm: "+"
pooled_cpm: 51.62
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 38
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# NOL3

*nucleolar protein 3* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.40× (z +4.3, q 0.008, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.215× (z -28.8, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRADD]] (+0.63, fdr 1e-05, ⚠ same locus), [[FUT11]] (+0.62, fdr 1e-05), [[WSB1]] (+0.61, fdr 7e-06), [[C4orf47]] (+0.61, fdr 1e-05); moves opposite to [[TFDP1]] (-0.61, fdr 1e-05), [[TMEM33]] (-0.58, fdr 1e-05), [[GLO1]] (-0.57, fdr 5e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[HSF4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.008 | 27/46 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.057 | 24/45 (NCI-H1792, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.25× | +3.4 | 0.10 | 21/46 (A-427, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.29× | +3.3 | 0.10 | 24/45 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.42× | +3.3 | 0.10 | 22/45 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.25× | +3.1 | 0.16 | 19/47 (NCI-H23, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.18 | 18/46 (KATO III, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.215×** | -28.8 | 0e+00 | 44/45 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.244×** | -18.8 | 0e+00 | 46/46 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.269×** | -17.5 | 0e+00 | 45/46 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.271×** | -17.4 | 0e+00 | 45/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.336×** | -14.5 | 1e-45 | 44/46 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.344×** | -14.2 | 2e-43 | 41/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.352×** | -13.9 | 8e-42 | 45/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.379×** | -12.4 | 3e-33 | 41/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.398×** | -12.2 | 1e-32 | 42/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.421×** | -11.5 | 1e-28 | 40/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.455×** | -10.0 | 5e-22 | 39/44 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.269×** | -9.1 | 4e-18 | 41/47 (HT-29, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.515×** | -8.8 | 6e-17 | 42/46 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -8.6 | 2e-16 | 35/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.635×** | -8.5 | 8e-16 | 34/46 (A549, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.312×** | -8.1 | 2e-14 | 41/45 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.592×** | -6.9 | 1e-10 | 37/46 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 90.4 | 0 | 20 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -28.1) |
| [[NCI-H460 (line)]] | wt | 104 | 0 | 20 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -27.9) |
| [[C32 (line)]] | wt | 95.7 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -24.8) |
| [[PANC-1 (line)]] | alt | 37.1 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -19.2) |
| [[SW480 (line)]] | alt | 68.6 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -24.5) |
| [[COLO 205 (line)]] | alt | 74.8 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 80.4 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -23.8) |
| [[NCI-H1573 (line)]] | alt | 75.2 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -23.1) |
| [[RPMI-7951 (line)]] | alt | 65.7 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0458× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.166× (z -19.2) |
| [[A-172 (line)]] | wt | 60.9 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 82.1 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -22.2) |
| [[HOP62 (line)]] | alt | 70.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -22.3) |
| [[A549 (line)]] | wt | 50.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -19.6) |
| [[CHP-212 (line)]] | wt | 97.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0774× (z -19.7) |
| [[H4 (line)]] | wt | 67.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -10.9) |
| [[Hs 766T (line)]] | wt | 67.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -22.4) |
| [[HCT15 (line)]] | alt | 108 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -19.5) |
| [[NCI-H23 (line)]] | alt | 42.2 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.1) |
| [[BT-474 (line)]] | alt | 54.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.3) |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.4) |
| [[KATO III (line)]] | alt | 45.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -22.5) |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 63.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -21.5) |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -8.9) |
| [[J82 (line)]] | alt | 40.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -19.6) |
| [[LS 180 (line)]] | wt | 44.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.199× (z -13.3) |
| [[RKO (line)]] | wt | 35.0 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0927× (z -15.8) |
| [[SW 900 (line)]] | alt | 47.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.3) |
| [[A-427 (line)]] | wt | 32.9 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.202× (z -10.8) |
| [[A498 (line)]] | wt | 56.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.2) |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -16.1) |
| [[SW 1271 (line)]] | alt | 100.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -12.0) |
| [[SW48 (line)]] | wt | 33.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 27.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.3) |
| [[SW 1088 (line)]] | alt | 68.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.1) |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.8) |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -8.6) |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRADD]] | +0.63 | +0.53 / +0.71 | both halves | 1e-05 | STRING 406; ⚠ same locus (10.2 kb: neighbours can correlate without regulation) |
| [[FUT11]] | +0.62 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[WSB1]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[C4orf47]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[KDM2A]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[CWC25]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ING2]] | +0.58 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[HMGCL]] | +0.58 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[INAFM1]] | +0.57 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[RNF181]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFDP1]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.58 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[GLO1]] | -0.57 | -0.39 / -0.67 | both halves | 5e-05 |  |
| [[ICMT]] | -0.56 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[DCTD]] | -0.56 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MACROH2A1]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[UBE2E3]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[VMA21]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[EEF1E1]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[MTAP]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSF4]] | C | NOL3's natural level strengthens HSF4's drug response | NOL3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.57; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.8, -32.5); signed map (-31.9, 26.3). **Vector** length 81.9, 25.1% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +3.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | -28.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.1 | -8.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -3.4 | -3.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.3 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -13.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.0 | -10.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -3.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,170,154-67,175,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARC, NOP30, MYP, CARD2 |
| Gene groups (HGNC) | Caspase recruitment domain containing |
| Hallmark sets | GLYCOLYSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [O60936](https://www.uniprot.org/uniprotkb/O60936) (Nucleolar protein 3):

> [Isoform 1]: May be involved in RNA splicing.; [Isoform 2]: Functions as an apoptosis repressor that blocks multiple modes of cell death. Inhibits extrinsic apoptotic pathways through two different ways. Firstly by interacting with FAS and FADD upon FAS activation blocking death-inducing signaling complex (DISC) assembly (By similarity). Secondly by interacting with CASP8 in a mitochondria localization- and phosphorylation-dependent manner, limiting the amount of soluble CASP8 available for …

**Summary**, from NCBI Gene [8996](https://www.ncbi.nlm.nih.gov/gene/8996):

> This gene encodes an anti-apoptotic protein that has been shown to down-regulate the enzyme activities of caspase 2, caspase 8 and tumor protein p53. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:7869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7869) · Entrez [8996](https://www.ncbi.nlm.nih.gov/gene/8996) · UniProt [O60936](https://www.uniprot.org/uniprotkb/O60936) · Ensembl [ENSG00000140939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140939)

## Data

Gene col 6464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6464); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6464]; `tensor/DDL_lfc|DDL_z.npy` [6464]; `embed/gene_vectors.npy` [6464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6464 or target_col == 6464). Every well: [[NOL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
