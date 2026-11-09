---
symbol: "RAB11FIP3"
type: "gene"
col: 1629
ensembl_id: "ENSG00000090565"
name: "RAB11 family interacting protein 3"
location: "16p13.3"
module: 25
arm: "-"
pooled_cpm: 72.71
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# RAB11FIP3

*RAB11 family interacting protein 3* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +7.5, q 3e-11, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.439× (z -16.0, q 0e+00, down in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.570× (z -10.9, q 1e-25, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RILPL1]] (+0.80, fdr 7e-06), [[IL17RA]] (+0.62, fdr 1e-05), [[AXIN1]] (+0.61, fdr 5e-05); moves opposite to [[DLD]] (-0.59, fdr 1e-05), [[RBBP9]] (-0.59, fdr 1e-05), [[SRP9]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GALNT5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.5 | 3e-11 | 28/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 4e-05 | 33/47 (SW480, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 3e-04 | 25/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.004 | 21/47 (LoVo, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.011 | 24/47 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.053 | 15/47 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.13× | +3.2 | 0.095 | 12/47 (A498, PANC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.1 | 0.15 | 12/47 (NCI-H460, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1629.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.439×** | -16.0 | 0e+00 | 34/43 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.456×** | -15.9 | 0e+00 | 37/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.500×** | -12.9 | 6e-36 | 35/44 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.570×** | -10.9 | 1e-25 | 33/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.459×** | -8.2 | 2e-14 | 33/48 (hTERT-HPNE, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.760×** | -5.5 | 3e-06 | 28/47 (PANC-1, A-172, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.829×** | -4.6 | 3e-04 | 18/47 (SW48, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.795×** | -4.4 | 7e-04 | 23/46 (C32, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.807×** | -4.3 | 0.001 | 21/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -4.2 | 0.002 | 0/49 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.808×** | -4.1 | 0.002 | 20/46 (HepG2/C3A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.686×** | -4.0 | 0.003 | 16/37 (BT-474, C32, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.705×** | -3.7 | 0.010 | 24/47 (hTERT-HPNE, SW 1088, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.834× | -3.6 | 0.011 | 20/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.846× | -3.3 | 0.032 | 21/47 (A-427, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.851× | -3.2 | 0.042 | 20/47 (HepG2/C3A, SK-MEL-2, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.852× | -3.2 | 0.042 | 10/48 (PANC-1, RKO, …) | two highest doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.084 | 17/47 (SW480, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 54.6 | 12 | 6 (5 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.65× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.255× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 95.6 | 3 (1 ⚠) | 9 (8 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.455× (z -10.1) |
| [[A-172 (line)]] | wt | 203 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -19.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.329× (z -12.2) |
| [[C32 (line)]] | wt | 106 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.374× (z -10.8) |
| [[A-427 (line)]] | wt | 119 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.415× (z -10.6) |
| [[A549 (line)]] | wt | 81.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.352× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.238× (z -13.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.310× (z -11.5) |
| [[LS 180 (line)]] | wt | 49.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 86.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -16.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 82.6 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 192 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -17.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 96.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 85.4 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -12.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.337× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.465× (z -8.7) |
| [[SNU-1 (line)]] | wt | 111 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.487× (z -8.5) |
| [[HCT15 (line)]] | alt | 92.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -11.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 62.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 63.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 67.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 76.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.348× (z -8.8) |
| [[SNU-423 (line)]] | alt | 68.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.365× (z -9.7) |
| [[SW48 (line)]] | wt | 130 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.473× (z -9.1) |
| [[AN3 CA (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.354× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 59.8 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0739× (z -9.6) |
| [[SW480 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.448× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RILPL1]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[IL17RA]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[AXIN1]] | +0.61 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[UBE2D2]] | +0.60 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[CSNK1G2]] | +0.59 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[HIC2]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[PHF20]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.58 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[MZT2A]] | +0.56 | +0.36 / +0.61 | both halves | 1e-04 |  |
| [[ZMYND19]] | +0.56 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[TPRN]] | +0.56 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[FAM193A]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLD]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[RBBP9]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SRP9]] | -0.59 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[TMEM30A]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.56 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[GCOM1]] | -0.56 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[SYNJ2BP]] | -0.55 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[NRAS]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TSPAN6]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ALG10B]] | -0.53 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[DNAH7]] | -0.52 | -0.37 / -0.53 | both halves | 8e-05 | same gene group |
| [[DR1]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT5]] | B | GALNT5 activity lowers RAB11FIP3's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 1.84× higher at baseline in the lines without GALNT5 | 0.004 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[SRPX2]] | B | SRPX2 activity lowers RAB11FIP3's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.32× higher at baseline in the lines without SRPX2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[RILPL1]] | C | RILPL1's natural level strengthens RAB11FIP3's drug response | RILPL1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.52; direction not clear | 0.090 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TP53]] | C | TP53 activity strengthens RAB11FIP3's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.56× as strongly (z diff +2.03); rises at some drug-doses, falls at others (44% from rises): Doxorubicin (hydrochloride) 5 µM: 0.96x vs 1.60x (z diff +3.9); Dinaciclib 5 µM: 0.55x vs 0.38x (z diff +3.4); Idarubicin (hydrochloride) 5 µM: 1.23x vs 1.50x (z diff +3.0) | 0.873 over the table, 0.070 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.9, -3.7); signed map (-25.9, 6.9). **Vector** length 118, 32.5% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +5.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.8 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.7 | -12.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.2 | -4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -16.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -15.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RAB11 family interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:425,649-523,011 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0665, Rab11-FIP3, eferin |
| Gene groups (HGNC) | EF-hand domain containing; RAB11 binding domain containing |
| Reactome | 5 pathways, smallest: VxPx cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [O75154](https://www.uniprot.org/uniprotkb/O75154) (Rab11 family-interacting protein 3):

> Downstream effector molecule for Rab11 GTPase which is involved in endocytic trafficking, cytokinesis and intracellular ciliogenesis by participating in membrane delivery. Recruited by Rab11 to endosomes where it links Rab11 to dynein motor complex. The functional Rab11-RAB11FIP3-dynein complex regulates the movement of peripheral sorting endosomes (SE) along microtubule tracks toward the microtubule organizing center/centrosome, generating the endocytic recycling compartment (ERC) during …

**Summary**, from NCBI Gene [9727](https://www.ncbi.nlm.nih.gov/gene/9727):

> Proteins of the large Rab GTPase family (see RAB1A; MIM 179508) have regulatory roles in the formation, targeting, and fusion of intracellular transport vesicles. RAB11FIP3 is one of many proteins that interact with and regulate Rab GTPases (Hales et al., 2001 [PubMed 11495908]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17224) · Entrez [9727](https://www.ncbi.nlm.nih.gov/gene/9727) · UniProt [O75154](https://www.uniprot.org/uniprotkb/O75154) · Ensembl [ENSG00000090565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090565)

## Data

Gene col 1629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1629); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1629]; `tensor/DDL_lfc|DDL_z.npy` [1629]; `embed/gene_vectors.npy` [1629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1629 or target_col == 1629). Every well: [[RAB11FIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB11FIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
