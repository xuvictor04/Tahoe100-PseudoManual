---
symbol: "GRN"
type: "gene"
col: 398
ensembl_id: "ENSG00000030582"
name: "granulin precursor"
location: "17q21.31"
module: 50
arm: "+"
pooled_cpm: 46.82
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# GRN

*granulin precursor* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +9.7, q 2e-19, up in 44 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +8.6, q 1e-15, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.421× (z -10.1, q 3e-21, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSA]] (+0.78, fdr 7e-06), [[CTSD]] (+0.78, fdr 7e-06), [[PCYOX1]] (+0.75, fdr 7e-06); moves opposite to [[TMA16]] (-0.63, fdr 1e-05), [[BRIX1]] (-0.62, fdr 9e-06), [[TCERG1]] (-0.58, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +9.7 | 2e-19 | 44/46 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.8 | 3e-16 | 30/39 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.6 | 1e-15 | 44/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +6.7 | 3e-09 | 40/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.4 | 1e-08 | 37/48 (SW480, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +5.5 | 5e-06 | 37/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.0 | 4e-05 | 30/47 (SK-MEL-2, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +4.5 | 4e-04 | 34/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.4 | 8e-04 | 28/42 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.003 | 29/48 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.020 | 25/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.025 | 26/48 (KATO III, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.093 | 24/48 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -10.1 | 3e-21 | 41/47 (HOP62, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.476×** | -8.3 | 2e-14 | 44/48 (HOP62, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.605×** | -8.1 | 7e-14 | 36/47 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.531×** | -7.4 | 2e-11 | 42/48 (SNU-1, MIA PaCa-2, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.548×** | -7.0 | 3e-10 | 42/48 (AsPC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.571×** | -6.3 | 3e-08 | 33/48 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.584×** | -6.3 | 3e-08 | 38/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.535×** | -3.8 | 0.009 | 26/48 (NCI-H23, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.706×** | -3.8 | 0.011 | 30/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -3.4 | 0.036 | 25/48 (J82, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.060 | 21/48 (CFPAC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.061 | 24/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.611× | -3.0 | 0.12 | 25/48 (SNU-1, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 84.3 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.8) | [[Verteporfin (drug)]] 5 µM 0.395× (z -9.2) |
| [[A549 (line)]] | wt | 40.1 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 39.2 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.2) |
| [[PANC-1 (line)]] | alt | 23.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.2) |
| [[HOP62 (line)]] | alt | 44.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -15.4) |
| [[LoVo (line)]] | wt | 22.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 44.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -14.0) |
| [[SW480 (line)]] | alt | 28.6 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.0) | [[Harringtonine (drug)]] 0.5 µM 0.342× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 35.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.162× (z -12.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.8) |
| [[C-33 A (line)]] | alt | 18.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.47× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 71.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 45.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 58.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.0) |
| [[J82 (line)]] | alt | 76.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +8.7) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.346× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 35.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 55.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.7) |
| [[SHP-77 (line)]] | alt | 48.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -10.4) |
| [[A-172 (line)]] | wt | 71.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.365× (z -9.2) |
| [[A-427 (line)]] | wt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 57.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -9.3) |
| [[H4 (line)]] | wt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -8.8) |
| [[HS-578T (line)]] | alt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -9.0) |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSA]] | +0.78 | +0.86 / +0.70 | both halves | 7e-06 | STRING 539 |
| [[CTSD]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 | STRING 866 |
| [[PCYOX1]] | +0.75 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[PSAP]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 | STRING 856 |
| [[ITM2B]] | +0.71 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[GM2A]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CDIPT]] | +0.68 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[GNS]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 | STRING 442 |
| [[ATP6AP1]] | +0.67 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[TMED4]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[OS9]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.66 | +0.73 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMA16]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[BRIX1]] | -0.62 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[TCERG1]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[EIF5B]] | -0.57 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[DPH5]] | -0.54 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[GPATCH4]] | -0.53 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[FBXW8]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CEP83]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[EIF3J]] | -0.52 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[MRPL58]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRN's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, -19.6); signed map (-51.0, -8.2). **Vector** length 115, 35.4% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.51 to 12); *Glycosphingolipid catabolism* (reactome, mean cos +0.58 to 5); *Degradation of the extracellular matrix* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +6.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.9 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.2 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.6 | -10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.5 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -6.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.2 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -5.0 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | granulin precursor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,345,246-44,353,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCDGF, PGRN, CLN11 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P28799](https://www.uniprot.org/uniprotkb/P28799) (Progranulin):

> Secreted protein that acts as a key regulator of lysosomal function and as a growth factor involved in inflammation, wound healing and cell proliferation. Regulates protein trafficking to lysosomes, and also the activity of lysosomal enzymes. Also facilitates the acidification of lysosomes, causing degradation of mature CTSD by CTSB. In addition, functions as a wound-related growth factor that acts directly on dermal fibroblasts and endothelial cells to promote division, migration and the …

**Summary**, from NCBI Gene [2896](https://www.ncbi.nlm.nih.gov/gene/2896):

> Granulins are a family of secreted, glycosylated peptides that are cleaved from a single precursor protein with 7.5 repeats of a highly conserved 12-cysteine granulin/epithelin motif. The 88 kDa precursor protein, progranulin, is also called proepithelin and PC cell-derived growth factor. Cleavage of the signal peptide produces mature granulin which can be further cleaved into a variety of active, 6 kDa peptides. These smaller cleavage products are named granulin A, granulin B, granulin C, etc. …

**Accessions** — [HGNC:4601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4601) · Entrez [2896](https://www.ncbi.nlm.nih.gov/gene/2896) · UniProt [P28799](https://www.uniprot.org/uniprotkb/P28799) · Ensembl [ENSG00000030582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000030582)

## Data

Gene col 398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 398); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 398]; `tensor/DDL_lfc|DDL_z.npy` [398]; `embed/gene_vectors.npy` [398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 398 or target_col == 398). Every well: [[GRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
