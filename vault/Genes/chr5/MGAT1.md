---
symbol: "MGAT1"
type: "gene"
col: 5209
ensembl_id: "ENSG00000131446"
name: "alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase"
location: "5q35.3"
module: 40
arm: "+"
pooled_cpm: 45.2
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# MGAT1

*alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.38× (z +6.9, q 3e-09, up in 30 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +6.3, q 7e-08, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.334× (z -23.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BET1L]] (+0.77, fdr 7e-06), [[MED26]] (+0.72, fdr 7e-06), [[SSR2]] (+0.72, fdr 7e-06); moves opposite to [[YTHDC2]] (-0.64, fdr 7e-06), [[DST]] (-0.61, fdr 1e-05), [[ATRX]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.9 | 3e-09 | 30/47 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.3 | 7e-08 | 25/47 (KATO III, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +6.1 | 1e-07 | 24/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.1 | 4e-05 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 8e-05 | 21/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.010 | 19/47 (H4, SW 900, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.012 | 11/48 (LOX-IMVI, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.083 | 15/48 (PANC-1, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.334×** | -23.3 | 0e+00 | 46/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.473×** | -22.4 | 0e+00 | 44/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.548×** | -13.3 | 2e-38 | 41/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -12.9 | 9e-36 | 36/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -12.3 | 2e-32 | 26/38 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.604×** | -11.2 | 5e-27 | 34/47 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.677×** | -8.6 | 4e-16 | 34/48 (HOP62, SW 1088, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.695×** | -8.1 | 5e-14 | 30/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.723×** | -6.6 | 2e-09 | 26/42 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -6.3 | 1e-08 | 30/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.771×** | -5.8 | 5e-07 | 23/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.816×** | -4.3 | 1e-03 | 21/48 (H4, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | 0.854× | -3.5 | 0.021 | 18/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.851× | -3.4 | 0.023 | 18/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.859× | -3.4 | 0.029 | 11/48 (COLO 205, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.857× | -3.3 | 0.035 | 16/48 (CHP-212, SW 900, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.858× | -3.3 | 0.038 | 16/47 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -15.0) |
| [[SW 900 (line)]] | alt | 104 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -16.1) |
| [[HOP62 (line)]] | alt | 57.6 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -18.0) |
| [[HS-578T (line)]] | alt | 72.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.4) |
| [[A-172 (line)]] | wt | 43.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -23.4) |
| [[NCI-H2030 (line)]] | alt | 56.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 45.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 56.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.338× (z -11.0) |
| [[PANC-1 (line)]] | alt | 45.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -21.7) |
| [[SW480 (line)]] | alt | 41.4 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -14.2) |
| [[A549 (line)]] | wt | 36.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.4) |
| [[C32 (line)]] | wt | 52.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.189× (z -12.3) |
| [[KATO III (line)]] | alt | 43.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.380× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[LOX-IMVI (line)]] | wt | 43.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 35.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -12.3) |
| [[A-427 (line)]] | wt | 44.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.1) |
| [[A498 (line)]] | wt | 48.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -14.2) |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0879× (z -11.6) |
| [[J82 (line)]] | alt | 48.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.6) |
| [[LoVo (line)]] | wt | 55.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.284× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 40.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.330× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 38.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -19.5) |
| [[RKO (line)]] | wt | 29.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -17.4) |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.0) |
| [[SW48 (line)]] | wt | 26.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -12.6) |
| [[COLO 205 (line)]] | alt | 75.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.258× (z -10.2) |
| [[H4 (line)]] | wt | 79.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.9) |
| [[HCT15 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -13.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 49.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -9.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 42.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 51.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.293× (z -9.6) |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -14.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 42.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -11.7) |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -11.4) |
| [[SW 1088 (line)]] | alt | 73.4 | 0 | 1 | — | [[Econazole (drug)]] 0.5 µM 0.0711× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1L]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[MED26]] | +0.72 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SSR2]] | +0.72 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[SOCS7]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SYVN1]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TXNDC11]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ATG101]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[MOGS]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 452 |
| [[SLC35E1]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.67 | +0.57 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[DST]] | -0.61 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[ATRX]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.58 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TIA1]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises MGAT1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.743). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.0, -30.5); signed map (-46.4, 8.5). **Vector** length 114, 28.7% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +6.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.1 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.4 | -23.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.1 | -11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.7 | -12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -22.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -13.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -8.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:180,784,780-180,815,652 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GNT-1, GLCNAC-TI, GnTI; previously MGAT, GLYT1 |
| Gene groups (HGNC) | Mannosyl-glycoprotein N-acetylglucosaminyltransferases |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 12 pathways, smallest: Maturation of spike protein_9683686; N-glycan trimming and elongation in the cis-Golgi; Translation of Structural Proteins_9683701 |
| Matched by | ensembl_id |

**Function**, from UniProt [P26572](https://www.uniprot.org/uniprotkb/P26572) (Alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase):

> Initiates complex N-linked carbohydrate formation. Essential for the conversion of high-mannose to hybrid and complex N-glycans.

**Summary**, from NCBI Gene [4245](https://www.ncbi.nlm.nih.gov/gene/4245):

> There are believed to be over 100 different glycosyltransferases involved in the synthesis of protein-bound and lipid-bound oligosaccharides. UDP-N-acetylglucosamine:alpha-3-D-mannoside beta-1,2-N-acetylglucosaminyltransferase I is a medial-Golgi enzyme essential for the synthesis of hybrid and complex N-glycans. The protein, encoded by a single exon, shows typical features of a type II transmembrane protein. The protein is believed to be essential for normal embryogenesis. Several variants …

**Accessions** — [HGNC:7044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7044) · Entrez [4245](https://www.ncbi.nlm.nih.gov/gene/4245) · UniProt [P26572](https://www.uniprot.org/uniprotkb/P26572) · Ensembl [ENSG00000131446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131446)

## Data

Gene col 5209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5209); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5209]; `tensor/DDL_lfc|DDL_z.npy` [5209]; `embed/gene_vectors.npy` [5209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5209 or target_col == 5209). Every well: [[MGAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
