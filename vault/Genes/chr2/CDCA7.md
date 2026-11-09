---
symbol: "CDCA7"
type: "gene"
col: 6867
ensembl_id: "ENSG00000144354"
name: "cell division cycle associated 7"
location: "2q31.1"
module: 6
arm: "+"
pooled_cpm: 12.42
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 35
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CDCA7

*cell division cycle associated 7* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.34× (z +14.7, q 0e+00, up in 16 of 18 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.42× (z +4.3, q 9e-04, up in 11 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -13.0, q 6e-36, down in 29 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3]] (+0.83, fdr 7e-06), [[RANBP1]] (+0.81, fdr 7e-06), [[DDX11]] (+0.80, fdr 7e-06); moves opposite to [[ATP6V1G1]] (-0.69, fdr 7e-06), [[PIN4]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 35 go from it, the strongest it → [[ATL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.34×** | +14.7 | 0e+00 | 16/18 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **3.14×** | +14.5 | 6e-45 | 25/30 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.76×** | +11.9 | 3e-30 | 20/23 (HT-29, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.90×** | +7.8 | 1e-12 | 24/33 (SW480, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.71×** | +6.5 | 7e-09 | 19/33 (A549, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.63×** | +6.1 | 8e-08 | 16/41 (HT-29, C32, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.5 | 3e-06 | 7/42 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.55×** | +5.3 | 8e-06 | 17/39 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +5.0 | 3e-05 | 15/41 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.29×** | +4.5 | 4e-04 | 10/42 (PANC-1, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.4 | 5e-04 | 6/16 (A549, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +4.4 | 5e-04 | 13/41 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +4.3 | 9e-04 | 11/40 (LS 180, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +4.2 | 0.001 | 9/41 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.39×** | +4.1 | 0.001 | 13/40 (SW480, NCI-H460, …) | two highest doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.017 | 5/40 (NCI-H460, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.065 | 6/36 (A498, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.072 | 10/41 (A549, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -13.0 | 6e-36 | 29/39 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.550×** | -7.6 | 9e-12 | 25/40 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.654×** | -5.4 | 1e-05 | 18/38 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -4.5 | 8e-04 | 14/39 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.782×** | -4.4 | 0.001 | 15/41 (KATO III, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.013 | 15/39 (HEC-1-A, HCT15, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.744×** | -3.8 | 0.014 | 15/39 (Panc 03.27, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.712×** | -3.7 | 0.014 | 15/41 (HEC-1-A, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.563×** | -3.4 | 0.037 | 7/41 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.778×** | -3.4 | 0.041 | 10/42 (COLO 205, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.760×** | -3.3 | 0.047 | 15/39 (COLO 205, A498, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.696×** | -3.3 | 0.047 | 7/42 (SK-MEL-2, SW480, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -3.2 | 0.050 | 11/38 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.050 | 13/41 (SW48, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.050 | 15/40 (HEC-1-A, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Posaconazole (drug)]] 5 µM |  | **0.773×** | -3.2 | 0.056 | 4/41 (NCI-H2347, HT-29, …) | top dose only | plate-row cell shift |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.774×** | -3.1 | 0.069 | 6/41 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.603×** | -3.0 | 0.076 | 12/41 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.848× | -3.0 | 0.085 | 9/42 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.794×** | -2.9 | 0.092 | 4/41 (SK-MEL-2, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.82 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0446× (z -22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0509× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 24.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.6) |
| [[PANC-1 (line)]] | alt | 18.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -10.4) |
| [[A498 (line)]] | wt | 20.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 32.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -17.2) |
| [[A-427 (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.4) |
| [[Hs 766T (line)]] | wt | 7.17 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 5 µM 0.172× (z -9.6) |
| [[HT-29 (line)]] | alt | 9.54 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.131× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -17.6) |
| [[SW48 (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.5) |
| [[SW480 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.5) |
| [[A-172 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3]] | +0.83 | +0.81 / +0.83 | both halves | 7e-06 | STRING 481 |
| [[RANBP1]] | +0.81 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[DDX11]] | +0.80 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | STRING 553 |
| [[MCM4]] | +0.78 | +0.73 / +0.79 | both halves | 7e-06 | STRING 583 |
| [[MTHFD1]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[MCM6]] | +0.77 | +0.81 / +0.74 | both halves | 7e-06 | STRING 583 |
| [[CENPM]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.75 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[DDX12P]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[TMEM109]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[POLA1]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.69 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[PIN4]] | -0.64 | -0.66 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises CDCA7's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.41× lower at baseline in the lines without E2F2 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CDCA7's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.72× lower at baseline in the lines without CDC25A | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[WNK2]] | B | WNK2 activity raises CDCA7's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without WNK2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[E2F8]] | B | E2F8 activity raises CDCA7's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.56× lower at baseline in the lines without E2F8 | 0.082 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises CDCA7's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without ZNF367 | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 35, C 0. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATL2]] | B | CDCA7 activity raises ATL2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without CDCA7 | 0.013 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[CASP2]] | B | CDCA7 activity raises CASP2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without CDCA7 | 0.019 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[NUDT15]] | B | CDCA7 activity raises NUDT15's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without CDCA7 | 0.023 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[ATAD2]] | B | CDCA7 activity raises ATAD2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without CDCA7 | 0.024 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[CENPM]] | B | CDCA7 activity raises CENPM's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without CDCA7 | 0.035 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[NCAPG2]] | B | CDCA7 activity raises NCAPG2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without CDCA7 | 0.038 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[WDHD1]] | B | CDCA7 activity raises WDHD1's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.14× lower at baseline in the lines without CDCA7 | 0.045 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[MCM8]] | B | CDCA7 activity raises MCM8's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without CDCA7 | 0.046 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[POLE2]] | B | CDCA7 activity raises POLE2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.19× lower at baseline in the lines without CDCA7 | 0.047 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[XRCC2]] | B | CDCA7 activity raises XRCC2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without CDCA7 | 0.048 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[SNRPB2]] | B | CDCA7 activity raises SNRPB2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CDCA7 | 0.055 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[SKA3]] | B | CDCA7 activity raises SKA3's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.37× lower at baseline in the lines without CDCA7 | 0.058 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.4, -42.1); signed map (-33.4, -44.4). **Vector** length 96.6, 23.4% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.59 to 65); *DNA strand elongation* (reactome, mean cos +0.63 to 28); *DNA Replication* (reactome, mean cos +0.60 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +5.0 | +11.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | +4.8 | +6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +4.2 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.1 | +14.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -7.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.0 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle associated 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:173,354,820-173,368,997 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14736, JPO1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWT1](https://www.uniprot.org/uniprotkb/Q9BWT1) (Cell division cycle-associated protein 7):

> Participates in MYC-mediated cell transformation and apoptosis; induces anchorage-independent growth and clonogenicity in lymphoblastoid cells. Insufficient to induce tumorigenicity when overexpressed but contributes to MYC-mediated tumorigenesis. Also functions as a critical cofactor for the chromatin remodeler HELLS, facilitating its recruitment to specific genomic regions to maintain DNA methylation patterns and heterochromatin integrity. Recognizes hemimethylated CpG within nucleosomes …

**Summary**, from NCBI Gene [83879](https://www.ncbi.nlm.nih.gov/gene/83879):

> This gene was identified as a c-Myc responsive gene, and behaves as a direct c-Myc target gene. Overexpression of this gene is found to enhance the transformation of lymphoblastoid cells, and it complements a transformation-defective Myc Box II mutant, suggesting its involvement in c-Myc-mediated cell transformation. Two alternatively spliced transcript variants encoding distinct isoforms have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14628) · Entrez [83879](https://www.ncbi.nlm.nih.gov/gene/83879) · UniProt [Q9BWT1](https://www.uniprot.org/uniprotkb/Q9BWT1) · Ensembl [ENSG00000144354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144354)

## Data

Gene col 6867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6867); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6867]; `tensor/DDL_lfc|DDL_z.npy` [6867]; `embed/gene_vectors.npy` [6867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6867 or target_col == 6867). Every well: [[CDCA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
