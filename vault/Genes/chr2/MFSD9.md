---
symbol: "MFSD9"
type: "gene"
col: 5788
ensembl_id: "ENSG00000135953"
name: "solute carrier family 67 member 2"
location: "2q12.1"
module: 30
arm: "+"
pooled_cpm: 13.55
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MFSD9

*solute carrier family 67 member 2* — 2q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.37× (z +8.3, q 4e-14, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +8.2, q 8e-14, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -22.5, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKRN2]] (+0.71, fdr 7e-06), [[NBPF3]] (+0.71, fdr 7e-06), [[NFRKB]] (+0.69, fdr 7e-06); moves opposite to [[CACNA2D1]] (-0.65, fdr 2e-05), [[SDCBP2-AS1]] (-0.64, fdr 4e-05), [[EFCAB2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM154]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +8.3 | 4e-14 | 25/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +8.2 | 8e-14 | 27/48 (PANC-1, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +7.4 | 3e-11 | 21/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 2e-08 | 21/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +5.5 | 5e-06 | 14/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.4 | 5e-06 | 15/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +5.3 | 9e-06 | 19/47 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.29×** | +4.7 | 2e-04 | 8/47 (A549, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +4.5 | 4e-04 | 9/46 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.37×** | +4.2 | 0.002 | 8/37 (CFPAC-1, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.24×** | +4.1 | 0.003 | 8/46 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +4.0 | 0.003 | 10/47 (HOP62, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.021 | 4/44 (Panc 03.27, CFPAC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.023 | 4/48 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.033 | 8/48 (AsPC-1, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.038 | 6/47 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.040 | 4/44 (BT-474, SW 900, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.20× | +3.2 | 0.041 | 6/47 (NCI-H460, J82, …) | top dose only |  |
| [[Ivermectin (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.041 | 5/45 (NCI-H1792, AN3 CA, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.048 | 3/45 (SW 900, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.428×** | -22.5 | 0e+00 | 39/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -15.3 | 0e+00 | 37/44 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -14.8 | 0e+00 | 39/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -11.3 | 1e-27 | 28/47 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.534×** | -11.3 | 1e-27 | 31/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -11.1 | 9e-27 | 29/46 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -10.8 | 2e-25 | 18/25 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.544×** | -10.6 | 3e-24 | 17/30 (KATO III, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.650×** | -8.0 | 6e-14 | 23/47 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.658×** | -7.9 | 2e-13 | 26/43 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.661×** | -7.8 | 4e-13 | 21/36 (KATO III, LS 180, …) | all doses, flat | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -7.3 | 2e-11 | 27/46 (SK-MEL-2, C-33 A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -5.9 | 2e-07 | 4/48 (LS 180, HS-578T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.798×** | -4.2 | 9e-04 | 13/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.673×** | -3.9 | 0.004 | 11/47 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Valdecoxib (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.021 | 11/46 (RKO, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.879× | -3.4 | 0.021 | 10/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.895× | -3.0 | 0.090 | 8/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.2) |
| [[LS 180 (line)]] | wt | 30.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.6) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.1) |
| [[SW480 (line)]] | alt | 25.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.5) |
| [[KATO III (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0745× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.3) |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.3) |
| [[SNU-423 (line)]] | alt | 8.10 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0625× (z -13.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.170× (z -9.7) |
| [[A-172 (line)]] | wt | 4.76 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0937× (z -8.7) |
| [[HOP62 (line)]] | alt | 9.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.5) |
| [[Hs 766T (line)]] | wt | 6.33 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -8.6) |
| [[J82 (line)]] | alt | 6.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 7.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.6) |
| [[RKO (line)]] | wt | 9.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -8.5) |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0914× (z -9.0) |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN2]] | +0.71 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NBPF3]] | +0.71 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[NFRKB]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NDUFA12]] | +0.68 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[FAM104A]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[IQSEC2]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RNF216P1]] | +0.64 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[RTCA]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA2D1]] | -0.65 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SDCBP2-AS1]] | -0.64 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[EFCAB2]] | -0.62 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[CUX1]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PCNT]] | -0.61 | -0.40 / -0.66 | both halves | 4e-05 |  |
| [[LINC01135]] | -0.61 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[TRAF3IP2-AS1]] | -0.61 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PKN2-AS1]] | -0.60 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[ZNF337-AS1]] | -0.60 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[PSMD6-AS1]] | -0.60 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[HIVEP1]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[HIVEP2-DT]] | -0.59 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM154]] | B | TMEM154 activity raises MFSD9's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 1.19× lower at baseline in the lines without TMEM154 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.9, -6.7); signed map (-35.4, -5.3). **Vector** length 84.2, 16.0% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.4 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | -0.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -22.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -15.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -14.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[XRK3F2 (drug)]] 5 µM |  | -1.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 67 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.1 — chr2:102,714,630-102,736,888 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11332; previously MFSD9 |
| Gene groups (HGNC) | Solute carrier family 67 |
| Matched by | ensembl_id |

UniProt [Q8NBP5](https://www.uniprot.org/uniprotkb/Q8NBP5) carries no function annotation.

**Summary**, from NCBI Gene [84804](https://www.ncbi.nlm.nih.gov/gene/84804):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28158) · Entrez [84804](https://www.ncbi.nlm.nih.gov/gene/84804) · UniProt [Q8NBP5](https://www.uniprot.org/uniprotkb/Q8NBP5) · Ensembl [ENSG00000135953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135953)

## Data

Gene col 5788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5788); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5788]; `tensor/DDL_lfc|DDL_z.npy` [5788]; `embed/gene_vectors.npy` [5788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5788 or target_col == 5788). Every well: [[MFSD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
