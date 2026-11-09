---
symbol: "ZFAT"
type: "gene"
col: 840
ensembl_id: "ENSG00000066827"
name: "zinc finger and AT-hook domain containing"
location: "8q24.22"
module: 36
arm: "+"
pooled_cpm: 31.24
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ZFAT

*zinc finger and AT-hook domain containing* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.09× (z +10.4, q 9e-23, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.456× (z -10.5, q 4e-23, down in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.641× (z -8.9, q 9e-17, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF407]] (+0.60, fdr 1e-05), [[ZBTB40]] (+0.54, fdr 4e-05), [[C2CD3]] (+0.53, fdr 4e-05); moves opposite to [[SHARPIN]] (-0.54, fdr 8e-05), [[TGDS]] (-0.50, fdr 2e-05), [[CDK7]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.09×** | +10.4 | 9e-23 | 43/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.03×** | +10.0 | 4e-21 | 42/47 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.97×** | +9.6 | 1e-19 | 40/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.30×** | +8.8 | 2e-16 | 40/47 (HT-29, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.64×** | +7.0 | 4e-10 | 32/47 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +6.7 | 2e-09 | 38/48 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.1 | 7e-08 | 29/46 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +5.8 | 5e-07 | 26/47 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.48×** | +5.6 | 1e-06 | 27/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +5.2 | 9e-06 | 24/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.6 | 0.016 | 14/32 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 1.18× | +3.4 | 0.035 | 9/48 (PANC-1, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.456×** | -10.5 | 4e-23 | 36/45 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -9.4 | 2e-18 | 29/38 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -8.9 | 9e-17 | 33/48 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -8.2 | 4e-14 | 39/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.563×** | -8.1 | 5e-14 | 37/48 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -7.8 | 6e-13 | 33/47 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -6.8 | 1e-09 | 34/48 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.601×** | -6.7 | 2e-09 | 28/42 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.680×** | -5.5 | 3e-06 | 31/48 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -5.1 | 2e-05 | 28/46 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.715×** | -4.8 | 1e-04 | 27/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.4 | 4e-04 | 23/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.732×** | -4.4 | 4e-04 | 23/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.739×** | -4.3 | 7e-04 | 24/47 (J82, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.067 | 12/48 (A549, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 59.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -8.6) |
| [[PANC-1 (line)]] | alt | 26.9 | 3 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.02× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -12.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 41.6 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.80× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.0) |
| [[SNU-1 (line)]] | wt | 51.5 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -12.1) |
| [[SW480 (line)]] | alt | 35.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.90× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -9.4) |
| [[A549 (line)]] | wt | 28.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.7) | [[Simotinib (drug)]] 5 µM 0.243× (z -9.2) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 29.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.268× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 49.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 41.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.56× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 50.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -11.5) |
| [[A498 (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 26.8 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.40× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.108× (z -10.1) |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -13.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -10.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0965× (z -11.9) |
| [[J82 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -18.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 1 | — | [[Berbamine (drug)]] 5 µM 0.257× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0645× (z -8.7) |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0791× (z -15.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -9.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[A-427 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 | same gene group |
| [[ZBTB40]] | +0.54 | +0.42 / +0.42 | both halves | 4e-05 | same gene group |
| [[C2CD3]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[NRDE2]] | +0.51 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[SETD1A]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[TRRAP]] | +0.49 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[CLPB]] | +0.47 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[B9D2]] | +0.45 | +0.51 / +0.28 | both halves | 3e-04 |  |
| [[HSPBP1]] | +0.45 | +0.42 / +0.37 | both halves | 9e-05 |  |
| [[TAS2R14]] | +0.45 | +0.45 / +0.32 | both halves | 2e-04 |  |
| [[ATXN7L3B]] | +0.45 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[NF1]] | +0.45 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHARPIN]] | -0.54 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[TGDS]] | -0.50 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CDK7]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SH3GLB1]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ABI1]] | -0.48 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[LNX2]] | -0.48 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ZC2HC1A]] | -0.47 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[RAB18]] | -0.47 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[MPHOSPH8]] | -0.45 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PDCD5]] | -0.44 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[ATP11B]] | -0.43 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[PARL]] | -0.43 | -0.36 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZFAT's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.199). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-9.9, -52.6); signed map (9.9, -44.9). **Vector** length 73.9, 16.0% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.2 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.3 | +0.4 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and AT-hook domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:134,477,788-134,713,049 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1485; previously ZNF406, ZFAT1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P243](https://www.uniprot.org/uniprotkb/Q9P243) (Zinc finger protein ZFAT):

> May be involved in transcriptional regulation. Overexpression causes down-regulation of a number of genes involved in the immune response. Some genes are also up-regulated (By similarity).

**Summary**, from NCBI Gene [57623](https://www.ncbi.nlm.nih.gov/gene/57623):

> This gene encodes a protein that likely binds DNA and functions as a transcriptional regulator involved in apoptosis and cell survival. This gene resides in a susceptibility locus for autoimmune thyroid disease (AITD) on chromosome 8q24. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:19899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19899) · Entrez [57623](https://www.ncbi.nlm.nih.gov/gene/57623) · UniProt [Q9P243](https://www.uniprot.org/uniprotkb/Q9P243) · Ensembl [ENSG00000066827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066827)

## Data

Gene col 840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 840); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 840]; `tensor/DDL_lfc|DDL_z.npy` [840]; `embed/gene_vectors.npy` [840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 840 or target_col == 840). Every well: [[ZFAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
