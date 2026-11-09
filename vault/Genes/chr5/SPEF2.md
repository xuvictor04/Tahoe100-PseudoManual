---
symbol: "SPEF2"
type: "gene"
col: 7644
ensembl_id: "ENSG00000152582"
name: "sperm flagellar and cilia associated 2"
location: "5p13.2"
module: 28
arm: "+"
pooled_cpm: 14.54
n_lines_expressing: 43
n_dd_up: 23
n_dd_down: 27
n_dd_up_clean: 20
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SPEF2

*sperm flagellar and cilia associated 2* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +8.0, q 6e-13, up in 22 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.264× (z -14.9, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA5]] (+0.65, fdr 1e-05), [[MKS1]] (+0.62, fdr 1e-05), [[TTC26]] (+0.60, fdr 1e-05); moves opposite to [[PRDX1]] (-0.57, fdr 1e-05), [[TXN]] (-0.54, fdr 1e-05), [[SNTB2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +8.0 | 6e-13 | 22/40 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +7.1 | 3e-10 | 27/41 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.71×** | +6.0 | 4e-07 | 25/41 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.8 | 7e-07 | 27/41 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.40×** | +5.3 | 2e-05 | 21/41 (LoVo, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 9e-05 | 22/41 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 2e-04 | 20/41 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 2e-04 | 19/41 (NCI-H23, A-427, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.50×** | +4.1 | 0.002 | 17/41 (NCI-H23, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.49×** | +4.1 | 0.002 | 16/41 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.01×** | +4.1 | 0.002 | 14/41 (LoVo, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.003 | 16/40 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.007 | 11/41 (NCI-H23, LOX-IMVI, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.88×** | +3.7 | 0.009 | 11/40 (NCI-H23, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.009 | 19/41 (NCI-H23, LS 180, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +3.7 | 0.009 | 14/41 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.009 | 14/41 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7644.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.264×** | -14.9 | 0e+00 | 40/41 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.314×** | -13.0 | 6e-36 | 35/39 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.381×** | -10.8 | 7e-25 | 37/41 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.407×** | -10.1 | 1e-21 | 35/41 (HCT15, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.417×** | -9.8 | 1e-20 | 31/41 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.424×** | -9.6 | 8e-20 | 33/41 (H4, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.453×** | -8.5 | 1e-15 | 27/38 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.269×** | -7.7 | 1e-12 | 32/40 (HS-578T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.730×** | -5.0 | 4e-05 | 22/41 (CFPAC-1, SW 1271, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.556×** | -4.8 | 7e-05 | 18/41 (SW480, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.651×** | -4.8 | 8e-05 | 26/41 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.662×** | -4.6 | 2e-04 | 20/41 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.675×** | -4.4 | 5e-04 | 18/40 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.644×** | -4.3 | 7e-04 | 17/40 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.481×** | -4.3 | 7e-04 | 18/38 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.717×** | -3.6 | 0.010 | 16/41 (AN3 CA, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.728×** | -3.6 | 0.011 | 13/41 (NCI-H2030, HCT15, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.733×** | -3.5 | 0.014 | 14/41 (NCI-H23, H4, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.707×** | -3.4 | 0.018 | 10/40 (Hs 766T, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 27.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0780× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 58.9 | 1 (1 ⚠) | 5 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.61× (z +12.0) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -15.0) |
| [[SW480 (line)]] | alt | 27.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0534× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0858× (z -16.3) |
| [[H4 (line)]] | wt | 38.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0665× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 31.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -10.6) |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0275× (z -15.1) |
| [[LoVo (line)]] | wt | 14.0 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +13.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -10.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -10.5) |
| [[A549 (line)]] | wt | 26.7 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -11.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.238× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -12.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -9.2) |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0489× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -9.7) |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -10.0) |
| [[A-427 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0929× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0304× (z -9.4) |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0594× (z -11.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -8.8) |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0976× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.144× (z -8.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.9) |
| [[SNU-423 (line)]] | alt | 9.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0531× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[MKS1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TTC26]] | +0.60 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[OSGEP]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ABITRAM]] | +0.58 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[NPHP1]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TMEM254]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[DDX1]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CCDC191]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RNF214]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[FAR2P1]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[TTC12]] | +0.54 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TXN]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SNTB2]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CCDC168]] | -0.53 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DOCK9]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ARPC1B]] | -0.52 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[L3MBTL3]] | -0.51 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[PRDM10]] | -0.51 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[KLHL25]] | -0.51 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[MED12L]] | -0.50 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MEGF11]] | -0.49 | -0.27 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers SPEF2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DNAAF11]] | B | DNAAF11 activity raises SPEF2's level | lines that do not express DNAAF11 (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without DNAAF11 | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TEX9]] | C | TEX9 activity raises SPEF2's level | lines that do not express TEX9 (3) vs lines expressing it (47) | 4.57× lower at baseline in the lines without TEX9 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: ZMAT3, PDE4C, LCA5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.8, 1.9); signed map (-20.6, -16.3). **Vector** length 76.3, 16.2% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +5.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.7 | -9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -3.5 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.3 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | sperm flagellar and cilia associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:35,617,844-35,814,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KPL2, FLJ23577, CT122 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C093](https://www.uniprot.org/uniprotkb/Q9C093) (Sperm flagella and cilia-associated protein 2):

> Required for correct axoneme development in spermatozoa. Important for normal development of the manchette and sperm head morphology. Essential for male fertility. Plays a role in localization of the intraflagellar transport protein IFT20 to the manchette, suggesting function as an adapter for dynein-mediated protein transport during spermatogenesis. Plays a role in bone growth where it seems to be required for normal osteoblast differentiation (By similarity). Required for normal beat …

**Summary**, from NCBI Gene [79925](https://www.ncbi.nlm.nih.gov/gene/79925):

> Involved in sperm axoneme assembly. Located in sperm flagellum. Implicated in spermatogenic failure 43. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26293) · Entrez [79925](https://www.ncbi.nlm.nih.gov/gene/79925) · UniProt [Q9C093](https://www.uniprot.org/uniprotkb/Q9C093) · Ensembl [ENSG00000152582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152582)

## Data

Gene col 7644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7644); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7644]; `tensor/DDL_lfc|DDL_z.npy` [7644]; `embed/gene_vectors.npy` [7644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7644 or target_col == 7644). Every well: [[SPEF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPEF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
