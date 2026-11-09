---
symbol: "NR3C2"
type: "gene"
col: 7542
ensembl_id: "ENSG00000151623"
name: "nuclear receptor subfamily 3 group C member 2"
location: "4q31.23"
module: 44
arm: "+"
pooled_cpm: 36.65
n_lines_expressing: 35
n_dd_up: 31
n_dd_down: 21
n_dd_up_clean: 29
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 40
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# NR3C2

*nuclear receptor subfamily 3 group C member 2* — 4q31.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.57× (z +22.2, q 0e+00, up in 28 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.581× (z -8.0, q 1e-12, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP8A1]] (+0.68, fdr 1e-05), [[ATP8B1]] (+0.67, fdr 7e-06), [[CDON]] (+0.63, fdr 1e-05); moves opposite to [[DNAJC11]] (-0.61, fdr 3e-05), [[RPAP1]] (-0.57, fdr 3e-05), [[DPH5-DT]] (-0.56, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ANOS1]] → it (grade B ⚠); 40 go from it, the strongest it → [[ATP8B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.57×** | +22.2 | 0e+00 | 28/33 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.63×** | +20.0 | 0e+00 | 30/33 (SW1417, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.59×** | +18.6 | 0e+00 | 30/33 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.43×** | +18.0 | 0e+00 | 27/33 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.37×** | +17.7 | 0e+00 | 30/33 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +13.7 | 1e-40 | 16/31 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.35×** | +12.4 | 1e-33 | 28/33 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.91×** | +9.4 | 3e-19 | 23/33 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **3.64×** | +8.4 | 3e-15 | 27/33 (NCI-H1573, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +6.8 | 8e-10 | 17/33 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.8 | 1e-04 | 14/33 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 2e-04 | 15/33 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.5 | 4e-04 | 13/33 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +4.4 | 4e-04 | 14/33 (SK-MEL-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 5e-04 | 16/33 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.37×** | +4.2 | 1e-03 | 17/33 (SK-MEL-2, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -8.0 | 1e-12 | 25/33 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.590×** | -7.7 | 3e-12 | 24/33 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.349×** | -6.8 | 1e-09 | 13/18 (SW 900, A-172, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.643×** | -6.5 | 1e-08 | 17/33 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.652×** | -6.3 | 4e-08 | 21/33 (LoVo, A498, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -5.5 | 5e-06 | 20/31 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.703×** | -5.2 | 2e-05 | 19/33 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -5.0 | 5e-05 | 18/32 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.716×** | -4.9 | 6e-05 | 17/33 (LoVo, SW 1271, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.746×** | -4.3 | 1e-03 | 13/33 (A498, LOX-IMVI, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.753×** | -4.0 | 0.003 | 18/33 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.574×** | -3.6 | 0.014 | 9/32 (LoVo, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -3.5 | 0.017 | 18/33 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.791×** | -3.4 | 0.023 | 18/33 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -3.4 | 0.023 | 13/33 (HT-29, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.631×** | -3.0 | 0.086 | 8/33 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.816×** | -3.0 | 0.086 | 8/33 (HT-29, A-427, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -3.0 | 0.086 | 11/33 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.818×** | -3.0 | 0.090 | 19/33 (HT-29, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.757×** | -2.9 | 0.097 | 3/33 (LoVo, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 95.2 | 0 | 17 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0618× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 0.185× (z -10.9) |
| [[LoVo (line)]] | wt | 104 | 0 | 13 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.275× (z -11.6) |
| [[HT-29 (line)]] | alt | 109 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.342× (z -9.5) |
| [[A-172 (line)]] | wt | 52.5 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.227× (z -11.0) |
| [[A498 (line)]] | wt | 22.8 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.35× (z +10.5) | [[Harringtonine (drug)]] 0.5 µM 0.213× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 272 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -14.6) |
| [[A-427 (line)]] | wt | 11.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.18× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.57× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0635× (z -14.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 68.1 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 147 | 1 (1 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.99× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 16.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.40× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 41.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0686× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.159× (z -9.2) |
| [[SW 900 (line)]] | alt | 56.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[C32 (line)]] | wt | 10.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.50× (z +9.0) | — |
| [[KATO III (line)]] | alt | 25.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.19× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 18.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 29.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0974× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[BT-474 (line)]] | alt | 12.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.1) | — |
| [[H4 (line)]] | wt | 13.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.114× (z -8.7) |
| [[Hs 766T (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[J82 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.283× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW1417 (line)]] | alt | 9.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.37× (z +11.2) | — |
| [[A549 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.54 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8A1]] | +0.68 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CDON]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MPP7]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CYRIA]] | +0.57 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[SNX30]] | +0.57 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[TSPAN33]] | +0.57 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[GPR160]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[MGAT4A]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[YPEL2]] | +0.55 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RHPN2]] | +0.55 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[CXADR]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.61 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[RPAP1]] | -0.57 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DPH5-DT]] | -0.56 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[WDR33]] | -0.56 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.56 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZNF621]] | -0.55 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[TRMT6]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SPRY3]] | -0.55 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[PRORP]] | -0.55 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[EMG1]] | -0.55 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF577]] | -0.55 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[MTHFSD]] | -0.55 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANOS1]] | B | ANOS1 activity raises NR3C2's level | lines that do not express ANOS1 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without ANOS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000268119, ZYG11A, KRT7 |
| [[ATP8B1]] | B | ATP8B1 activity raises NR3C2's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without ATP8B1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises NR3C2's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.43× lower at baseline in the lines without TNFRSF11A | 0.082 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[LRIG1]] | B | LRIG1 activity raises NR3C2's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without LRIG1 | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers NR3C2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDS1]] | C | CDS1 activity raises NR3C2's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without CDS1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 39, C 1. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP8B1]] | B | NR3C2 activity raises ATP8B1's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 3.58× lower at baseline in the lines without NR3C2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[MPP7]] | B | NR3C2 activity raises MPP7's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.46× lower at baseline in the lines without NR3C2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[TNFRSF11A]] | B | NR3C2 activity raises TNFRSF11A's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without NR3C2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[SELENOP]] | B | NR3C2 activity raises SELENOP's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without NR3C2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[CNGA1]] | B | NR3C2 activity raises CNGA1's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.85× lower at baseline in the lines without NR3C2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[DYRK2]] | B | NR3C2 activity raises DYRK2's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without NR3C2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[UTP20]] | B | NR3C2 activity lowers UTP20's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.49× higher at baseline in the lines without NR3C2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[C4orf19]] | B | NR3C2 activity raises C4orf19's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without NR3C2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[FBXO33]] | B | NR3C2 activity raises FBXO33's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without NR3C2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[MAPRE2]] | B | NR3C2 activity raises MAPRE2's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.69× lower at baseline in the lines without NR3C2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[TJP3]] | B | NR3C2 activity raises TJP3's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without NR3C2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[KLHL32]] | B | NR3C2 activity raises KLHL32's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.83× lower at baseline in the lines without NR3C2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, 5.4); signed map (50.9, 4.1). **Vector** length 85.1, 19.1% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +20.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +17.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +12.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +8.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.9 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +9.4 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.8 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.6 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 3 group C member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.23 — chr4:148,078,762-148,444,698 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MR; previously MLR |
| Gene groups (HGNC) | Nuclear receptor subfamily 3 group C |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 7 pathways, smallest: SUMOylation of intracellular receptors; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P08235](https://www.uniprot.org/uniprotkb/P08235) (Mineralocorticoid receptor):

> Receptor for both mineralocorticoids (MC) such as aldosterone and glucocorticoids (GC) such as corticosterone or cortisol. Binds to mineralocorticoid response elements (MRE) and transactivates target genes. The effect of MC is to increase ion and water transport and thus raise extracellular fluid volume and blood pressure and lower potassium levels.

**Summary**, from NCBI Gene [4306](https://www.ncbi.nlm.nih.gov/gene/4306):

> This gene encodes the mineralocorticoid receptor, which mediates aldosterone actions on salt and water balance within restricted target cells. The protein functions as a ligand-dependent transcription factor that binds to mineralocorticoid response elements in order to transactivate target genes. Mutations in this gene cause autosomal dominant pseudohypoaldosteronism type I, a disorder characterized by urinary salt wasting. Defects in this gene are also associated with early onset hypertension …

**Accessions** — [HGNC:7979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7979) · Entrez [4306](https://www.ncbi.nlm.nih.gov/gene/4306) · UniProt [P08235](https://www.uniprot.org/uniprotkb/P08235) · Ensembl [ENSG00000151623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151623)

## Data

Gene col 7542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7542); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7542]; `tensor/DDL_lfc|DDL_z.npy` [7542]; `embed/gene_vectors.npy` [7542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7542 or target_col == 7542). Every well: [[NR3C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR3C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
