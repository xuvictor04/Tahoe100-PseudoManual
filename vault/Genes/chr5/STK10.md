---
symbol: "STK10"
type: "gene"
col: 1030
ensembl_id: "ENSG00000072786"
name: "serine/threonine kinase 10"
location: "5q35.1"
module: 101
arm: "+"
pooled_cpm: 96.0
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 35
n_dd_up_clean: 7
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# STK10

*serine/threonine kinase 10* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +12.2, q 3e-31, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.567× (z -11.0, q 3e-25, down in 33 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.601× (z -9.8, q 3e-20, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD1]] (+0.69, fdr 7e-06), [[TUBB6]] (+0.68, fdr 7e-06), [[HBEGF]] (+0.65, fdr 7e-06); moves opposite to [[TNRC6A]] (-0.58, fdr 1e-05), [[RHOXF1]] (-0.57, fdr 1e-05), [[MBNL2]] (-0.56, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CLCF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +12.2 | 3e-31 | 33/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +8.3 | 4e-14 | 28/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +5.4 | 9e-06 | 26/48 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.4 | 9e-06 | 25/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 1e-05 | 28/47 (SW 900, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.77×** | +5.1 | 3e-05 | 28/48 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +4.3 | 0.002 | 21/47 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.025 | 15/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.035 | 18/48 (NCI-H1573, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.047 | 18/48 (A498, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.19× | +3.3 | 0.048 | 22/47 (H4, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1030.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.567×** | -11.0 | 3e-25 | 33/49 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.601×** | -9.8 | 3e-20 | 30/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -9.8 | 3e-20 | 27/40 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -8.6 | 2e-15 | 33/43 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.645×** | -8.4 | 3e-15 | 27/48 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -8.3 | 1e-14 | 28/48 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.424×** | -7.6 | 2e-12 | 41/47 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.661×** | -7.4 | 1e-11 | 30/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.737×** | -7.1 | 6e-11 | 30/48 (AsPC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.771×** | -7.1 | 8e-11 | 27/48 (SK-MEL-2, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.695×** | -6.8 | 7e-10 | 29/48 (SK-MEL-2, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.717×** | -6.4 | 7e-09 | 32/48 (HOP62, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.719×** | -6.4 | 8e-09 | 26/49 (AsPC-1, SK-MEL-2, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -6.1 | 4e-08 | 27/47 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.722×** | -6.0 | 6e-08 | 25/47 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.736×** | -5.9 | 1e-07 | 29/49 (SNU-423, HOP62, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.746×** | -5.6 | 6e-07 | 26/48 (HS-578T, H4, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.812×** | -5.6 | 7e-07 | 24/48 (NCI-H2347, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.781×** | -5.4 | 2e-06 | 26/50 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 261 | 0 | 14 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.166× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 294 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.258× (z -17.0) |
| [[HOP62 (line)]] | alt | 191 | 1 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.281× (z -12.4) |
| [[HS-578T (line)]] | alt | 213 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -20.2) |
| [[RPMI-7951 (line)]] | alt | 294 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -14.7) |
| [[A498 (line)]] | wt | 102 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.481× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 144 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.8) | [[Trametinib (drug)]] 5 µM 0.342× (z -11.6) |
| [[J82 (line)]] | alt | 135 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 97.2 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 85.5 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.1) | [[Binimetinib (drug)]] 0.5 µM 0.422× (z -9.9) |
| [[A549 (line)]] | wt | 63.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -15.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 212 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.367× (z -8.9) |
| [[PANC-1 (line)]] | alt | 68.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +24.7) | — |
| [[SW480 (line)]] | alt | 81.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 0.467× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 99.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0911× (z -18.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 83.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 83.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 113 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 3.65× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.309× (z -10.4) |
| [[SW 900 (line)]] | alt | 200 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 103 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 119 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.5) | [[Ponatinib (drug)]] 5 µM 0.249× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 50.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +20.4) | — |
| [[SNU-423 (line)]] | alt | 71.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +18.0) | — |
| [[SW 1088 (line)]] | alt | 211 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0495× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.135× (z -9.0) |
| [[AN3 CA (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0896× (z -9.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 1 | — | [[Erlotinib (drug)]] 0.5 µM 0.194× (z -9.0) |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.103× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 47.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 56.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +18.1) | — |
| [[NCI-H23 (line)]] | alt | 41.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 98.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -10.1) |
| [[SHP-77 (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0965× (z -10.4) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TUBB6]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[DRAP1]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[NIPAL1]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[HRH1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[KCTD5]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[FOSL1]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[KLF12]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PHLDA2]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ABR]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 | pathway: RHOA GTPase cycle |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6A]] | -0.58 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[RHOXF1]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[MBNL2]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NDUFV2]] | -0.56 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[PON2]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TMEM245]] | -0.54 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[KCTD3]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PUM2]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[RPP30]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCF1]] | B | CLCF1 activity raises STK10's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without CLCF1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[MANCR]] | B | MANCR activity raises STK10's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.92× lower at baseline in the lines without MANCR | 0.028 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[RAI14]] | B | RAI14 activity raises STK10's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without RAI14 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[ADAM19]] | B | ADAM19 activity raises STK10's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.91× lower at baseline in the lines without ADAM19 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[FRMD6]] | B | FRMD6 activity raises STK10's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without FRMD6 | 0.057 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[IL1B]] | B | IL1B activity raises STK10's level | lines that do not express IL1B (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without IL1B | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[C13orf46]] | B | C13orf46 activity raises STK10's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without C13orf46 | 0.061 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[NAV2]] | B | NAV2 activity raises STK10's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without NAV2 | 0.063 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[PTHLH]] | B | PTHLH activity raises STK10's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 1.81× lower at baseline in the lines without PTHLH | 0.070 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[LGR4]] | B | LGR4 activity lowers STK10's level | lines that do not express LGR4 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without LGR4 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MARCHF3]] | B | MARCHF3 activity raises STK10's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 1.85× lower at baseline in the lines without MARCHF3 | 0.096 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[MTSS1]] | B | MTSS1 activity raises STK10's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without MTSS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, -1.4); signed map (-0.9, 33.9). **Vector** length 142, 49.4% of its response variance represented; |z| ≥ 3 in 1,911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.3 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.8 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.7 | +5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -1.0 |
| fall | [[NG25 (drug)]] 5 µM |  | -8.3 | -7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.1 | -6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.0 | -7.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.9 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.8 | -7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.6 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.5 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,042,079-172,188,224 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOK, PRO2729 |
| Gene groups (HGNC) | SLK/STK10 kinase family |
| Reactome | 8 pathways, smallest: RHOB GTPase cycle; RHOC GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O94804](https://www.uniprot.org/uniprotkb/O94804) (Serine/threonine-protein kinase 10):

> Serine/threonine-protein kinase involved in regulation of lymphocyte migration. Phosphorylates MSN, and possibly PLK1. Involved in regulation of lymphocyte migration by mediating phosphorylation of ERM proteins such as MSN. Acts as a negative regulator of MAP3K1/MEKK1. May also act as a cell cycle regulator by acting as a polo kinase kinase: mediates phosphorylation of PLK1 in vitro; however such data require additional evidence in vivo.

**Summary**, from NCBI Gene [6793](https://www.ncbi.nlm.nih.gov/gene/6793):

> This gene encodes a member of the Ste20 family of serine/threonine protein kinases, and is similar to several known polo-like kinase kinases. The protein can associate with and phosphorylate polo-like kinase 1, and overexpression of a kinase-dead version of the protein interferes with normal cell cycle progression. The kinase can also negatively regulate interleukin 2 expression in T-cells via the mitogen activated protein kinase kinase 1 pathway. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11388](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11388) · Entrez [6793](https://www.ncbi.nlm.nih.gov/gene/6793) · UniProt [O94804](https://www.uniprot.org/uniprotkb/O94804) · Ensembl [ENSG00000072786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072786)

## Data

Gene col 1030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1030); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1030]; `tensor/DDL_lfc|DDL_z.npy` [1030]; `embed/gene_vectors.npy` [1030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1030 or target_col == 1030). Every well: [[STK10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
