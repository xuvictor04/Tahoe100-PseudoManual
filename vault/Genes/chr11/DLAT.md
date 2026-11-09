---
symbol: "DLAT"
type: "gene"
col: 7460
ensembl_id: "ENSG00000150768"
name: "dihydrolipoamide S-acetyltransferase"
location: "11q23.1"
module: 4
arm: "+"
pooled_cpm: 29.87
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DLAT

*dihydrolipoamide S-acetyltransferase* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.80× (z +11.1, q 9e-26, up in 28 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.41× (z +9.6, q 2e-19, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.491× (z -13.9, q 4e-41, down in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.558× (z -11.4, q 2e-27, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHB1]] (+0.73, fdr 7e-06), [[AGPS]] (+0.73, fdr 7e-06), [[MRPL3]] (+0.71, fdr 7e-06); moves opposite to [[CATSPERG]] (-0.67, fdr 7e-06), [[TNRC6C]] (-0.66, fdr 7e-06), [[EIF1B]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.80×** | +11.1 | 9e-26 | 28/37 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.75×** | +11.0 | 1e-25 | 33/43 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +9.6 | 2e-19 | 35/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.43×** | +6.5 | 8e-09 | 20/41 (Hs 766T, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.2 | 7e-08 | 24/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.37×** | +6.1 | 7e-08 | 25/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.34×** | +5.8 | 4e-07 | 26/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +5.8 | 6e-07 | 22/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.33×** | +5.7 | 8e-07 | 25/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 3e-05 | 22/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +5.0 | 4e-05 | 22/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +4.9 | 5e-05 | 21/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.28×** | +4.7 | 1e-04 | 19/46 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +4.5 | 3e-04 | 17/47 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 8e-04 | 13/48 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.075 | 11/48 (Hs 766T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.0 | 0.078 | 15/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.090 | 8/47 (A498, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -13.9 | 4e-41 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.558×** | -11.4 | 2e-27 | 40/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -10.7 | 1e-24 | 34/48 (AsPC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.584×** | -10.5 | 1e-23 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -9.2 | 3e-18 | 32/47 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -5.8 | 6e-07 | 24/47 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.6 | 3e-04 | 20/47 (COLO 205, NCI-H460, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -4.5 | 4e-04 | 21/48 (BT-474, SHP-77, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.788×** | -4.4 | 8e-04 | 18/48 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.854× | -4.3 | 1e-03 | 14/48 (PANC-1, SNU-1, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.817×** | -3.9 | 0.004 | 19/47 (SNU-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.686×** | -3.8 | 0.006 | 16/47 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.825×** | -3.7 | 0.009 | 11/47 (SK-MEL-2, KATO III, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.5 | 0.019 | 15/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.5 | 0.019 | 14/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.020 | 15/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.851× | -3.1 | 0.059 | 12/47 (KATO III, C-33 A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.060 | 10/48 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -8.5) |
| [[Hs 766T (line)]] | wt | 40.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 37.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.80× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 47.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.338× (z -12.8) |
| [[SNU-1 (line)]] | wt | 44.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.7) |
| [[A498 (line)]] | wt | 23.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -10.2) |
| [[SW480 (line)]] | alt | 47.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.379× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.485× (z -9.1) |
| [[A-427 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -9.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 20.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -13.7) |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -15.2) ⚠ toxic; cell-cycle shift, explains ~54% of this change |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 58.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.77× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHB1]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[AGPS]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[SF3A3]] | +0.71 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[WDR36]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CCT2]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[RITA1]] | +0.71 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[GOT2]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 480 |
| [[AGK]] | +0.71 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[API5]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[IPO8]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[DLD]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999 |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERG]] | -0.67 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.66 | -0.64 / -0.58 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |
| [[EIF1B]] | -0.66 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[CD63]] | -0.65 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[MIA]] | -0.64 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[EIF1]] | -0.62 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[SPATC1]] | -0.61 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[PP2D1]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[SMIM14]] | -0.61 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[TESK2]] | -0.61 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[STX5]] | -0.60 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[HIC2]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DLAT's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.2, -34.9); signed map (-15.5, -44.8). **Vector** length 107, 25.7% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.51 to 8); *tRNA processing* (reactome, mean cos +0.51 to 10); *Folding of actin by CCT/TriC* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.3 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.3 | +11.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -10.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.6 | -13.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.8 | -11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.7 | -9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | dihydrolipoamide S-acetyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:112,025,033-112,064,404 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDC-E2, E2; previously DLTA |
| Gene groups (HGNC) | Pyruvate dehydrogenase complex subunits; Acyltransferases |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 8 pathways, smallest: PDH complex synthesizes acetyl-CoA from PYR; Protein lipoylation; Regulation of pyruvate dehydrogenase (PDH) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P10515](https://www.uniprot.org/uniprotkb/P10515) (Dihydrolipoyllysine-residue acetyltransferase component of pyruvate dehydrogenase complex, mitochondrial):

> The pyruvate dehydrogenase (PDH) complex, catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2), and thereby links cytoplasmic glycolysis and the mitochondrial tricarboxylic acid (TCA) cycle (Probable). It contains multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and dihydrolipoamide dehydrogenase (E3); (Probable). Within this complex, the catalytic function of this enzyme is to accept, and to transfer to coenzyme …

**Summary**, from NCBI Gene [1737](https://www.ncbi.nlm.nih.gov/gene/1737):

> This gene encodes component E2 of the multi-enzyme pyruvate dehydrogenase complex (PDC). PDC resides in the inner mitochondrial membrane and catalyzes the conversion of pyruvate to acetyl coenzyme A. The protein product of this gene, dihydrolipoamide acetyltransferase, accepts acetyl groups formed by the oxidative decarboxylation of pyruvate and transfers them to coenzyme A. Dihydrolipoamide acetyltransferase is the antigen for antimitochondrial antibodies. These autoantibodies are present in …

**Accessions** — [HGNC:2896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2896) · Entrez [1737](https://www.ncbi.nlm.nih.gov/gene/1737) · UniProt [P10515](https://www.uniprot.org/uniprotkb/P10515) · Ensembl [ENSG00000150768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150768)

## Data

Gene col 7460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7460); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7460]; `tensor/DDL_lfc|DDL_z.npy` [7460]; `embed/gene_vectors.npy` [7460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7460 or target_col == 7460). Every well: [[DLAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
