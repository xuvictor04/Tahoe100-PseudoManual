---
symbol: "FAM210B"
type: "gene"
col: 4476
ensembl_id: "ENSG00000124098"
name: "mitochondrial inner membrane structural 2"
location: "20q13.2"
module: 29
arm: "+"
pooled_cpm: 16.75
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# FAM210B

*mitochondrial inner membrane structural 2* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.80× (z +17.0, q 0e+00, up in 36 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.46× (z +9.8, q 2e-20, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.290× (z -18.9, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GM2A]] (+0.70, fdr 7e-06), [[CCNG1]] (+0.69, fdr 7e-06), [[TSPAN6]] (+0.68, fdr 7e-06); moves opposite to [[NSRP1]] (-0.65, fdr 1e-05), [[EIF3J]] (-0.56, fdr 1e-05), [[KCNJ14]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.80×** | +17.0 | 0e+00 | 36/37 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.30×** | +15.2 | 0e+00 | 26/27 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +11.5 | 2e-28 | 32/34 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +9.8 | 2e-20 | 41/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +8.7 | 4e-16 | 36/48 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.02×** | +7.7 | 2e-12 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.0 | 2e-10 | 35/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.75×** | +6.1 | 7e-08 | 32/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +4.7 | 1e-04 | 27/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.41×** | +3.6 | 0.016 | 21/48 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.41×** | +3.6 | 0.018 | 15/45 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.020 | 16/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.82×** | +3.4 | 0.028 | 8/42 (NCI-H2347, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.3 | 0.033 | 17/42 (BT-474, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +3.2 | 0.046 | 13/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.046 | 8/42 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.056 | 12/45 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.071 | 16/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.290×** | -18.9 | 0e+00 | 42/45 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.347×** | -11.4 | 9e-28 | 42/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.422×** | -8.9 | 7e-17 | 37/46 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.536×** | -6.7 | 2e-09 | 35/47 (SW 900, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.564×** | -6.2 | 8e-08 | 33/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.606×** | -5.4 | 7e-06 | 25/47 (SW480, C32, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.592×** | -5.3 | 8e-06 | 24/47 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.602×** | -5.2 | 2e-05 | 29/48 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -5.1 | 3e-05 | 29/46 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -4.8 | 9e-05 | 27/47 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -3.9 | 0.005 | 21/47 (AN3 CA, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -3.7 | 0.012 | 20/47 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.720×** | -3.5 | 0.019 | 21/46 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.555×** | -3.3 | 0.038 | 16/46 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.567×** | -3.2 | 0.053 | 13/47 (RKO, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.734×** | -3.1 | 0.062 | 13/48 (SW 1088, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.9 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 29.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -19.5) |
| [[HOP62 (line)]] | alt | 11.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.6) |
| [[KATO III (line)]] | alt | 21.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 7.71× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.0) |
| [[SW1417 (line)]] | alt | 46.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.1) |
| [[BT-474 (line)]] | alt | 62.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.2) |
| [[C-33 A (line)]] | alt | 25.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 62.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.3) |
| [[Hs 766T (line)]] | wt | 33.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.04× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 13.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.5) |
| [[SNU-423 (line)]] | alt | 24.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 9.30 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.85× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 9.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.0) |
| [[LoVo (line)]] | wt | 7.04 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.84× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.3) |
| [[LS 180 (line)]] | wt | 19.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 6.83 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0820× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0727× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 13.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +9.6) ⚠ toxic; transcription drop | [[TAK-901 (drug)]] 0.05 µM 0.191× (z -8.5) |
| [[PANC-1 (line)]] | alt | 7.06 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.67× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.4) |
| [[RKO (line)]] | wt | 30.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.7) |
| [[SHP-77 (line)]] | alt | 45.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.3) |
| [[A498 (line)]] | wt | 5.53 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.47× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 9.62 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 8.05 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 7.33 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.68× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 6.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0766× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 8.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -11.6) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GM2A]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CCNG1]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CREG1]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PCYOX1]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[BRD3OS]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ABRAXAS1]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PEBP1]] | +0.65 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[CNPY3]] | +0.63 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PPT1]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSRP1]] | -0.65 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[CHRNA10]] | -0.56 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[TAF1]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[UBE2CP5]] | -0.55 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[ZNF75A]] | -0.55 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[MIRLET7IHG]] | -0.55 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[MATN1-AS1]] | -0.55 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[WASHC1]] | -0.54 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[C3orf20]] | -0.54 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[WNK4]] | -0.54 | -0.57 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-19.2, -18.9); signed map (-51.6, -8.7). **Vector** length 88.1, 21.9% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.0 | +8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +3.4 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +9.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | +6.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.9 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +0.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -18.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial inner membrane structural 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:56,358,974-56,368,663 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1167H4.1, DKFZP434A1114; previously C20orf108, FAM210B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KR6](https://www.uniprot.org/uniprotkb/Q96KR6) (Mitochondrial inner membrane scaffold 2):

> Mitochondrial inner membrane adapter protein essential for terminal erythroid differentiation and heme biosynthesis. Facilitates formation of an oligomeric mitochondrial iron transport complex required for iron acquisition during heme synthesis, although it does not function as a direct iron transporter (By similarity). Directly interacts with terminal heme synthesis enzymes PPOX and FECH to enhance ferrochelatase activity and couple iron import with heme synthesis (By similarity). Regulates …

**Summary**, from NCBI Gene [116151](https://www.ncbi.nlm.nih.gov/gene/116151):

> Involved in cellular response to estradiol stimulus and positive regulation of erythrocyte differentiation. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16102) · Entrez [116151](https://www.ncbi.nlm.nih.gov/gene/116151) · UniProt [Q96KR6](https://www.uniprot.org/uniprotkb/Q96KR6) · Ensembl [ENSG00000124098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124098)

## Data

Gene col 4476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4476); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4476]; `tensor/DDL_lfc|DDL_z.npy` [4476]; `embed/gene_vectors.npy` [4476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4476 or target_col == 4476). Every well: [[FAM210B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM210B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
