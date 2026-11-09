---
symbol: "SMARCA1"
type: "gene"
col: 2206
ensembl_id: "ENSG00000102038"
name: "SNF2 related chromatin remodeling ATPase 1"
location: "Xq25-q26.1"
module: 77
arm: "-"
pooled_cpm: 82.92
n_lines_expressing: 37
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# SMARCA1

*SNF2 related chromatin remodeling ATPase 1* — Xq25-q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.72× (z +10.2, q 2e-21, up in 24 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 0.5 µM: 1.39× (z +6.3, q 5e-08, up in 25 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.313× (z -22.5, q 0e+00, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATRX]] (+0.64, fdr 1e-05), [[IFT81]] (+0.64, fdr 1e-05), [[CACNA2D1]] (+0.59, fdr 1e-05); moves opposite to [[EEF1AKMT4]] (-0.66, fdr 1e-05), [[TSEN54]] (-0.64, fdr 2e-05), [[FOXK2]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DNAJC18]] → it (grade C ⚠); 1 goes from it, the strongest it → [[ZXDC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +10.2 | 2e-21 | 24/33 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.3 | 9e-11 | 24/35 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 5e-08 | 25/35 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[NG25 (drug)]] 5 µM |  | **1.74×** | +5.6 | 3e-06 | 25/34 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +5.4 | 8e-06 | 19/33 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +4.8 | 1e-04 | 15/35 (SW480, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 17/34 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.12 | 14/35 (PANC-1, HEC-1-A, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.19× | +3.1 | 0.13 | 10/36 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.313×** | -22.5 | 0e+00 | 35/35 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.339×** | -21.0 | 0e+00 | 33/35 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.347×** | -20.5 | 0e+00 | 33/35 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.478×** | -14.3 | 3e-44 | 33/35 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -12.8 | 3e-35 | 29/35 (Hs 766T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.524×** | -12.5 | 4e-34 | 32/35 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.531×** | -11.8 | 2e-30 | 28/34 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.635×** | -7.4 | 7e-12 | 28/35 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.488×** | -7.3 | 2e-11 | 28/36 (HEC-1-A, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.693×** | -6.8 | 4e-10 | 21/35 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.531×** | -6.4 | 7e-09 | 25/35 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -5.7 | 5e-07 | 22/36 (Hs 766T, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.731×** | -4.3 | 6e-04 | 20/34 (CHP-212, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.801×** | -4.3 | 7e-04 | 20/35 (NCI-H2347, SW 1088, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.670×** | -4.1 | 0.002 | 17/29 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.674×** | -4.0 | 0.002 | 18/35 (A-427, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.813×** | -3.9 | 0.004 | 18/35 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.820×** | -3.9 | 0.004 | 18/35 (SW480, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 102 | 4 (4 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -17.1) |
| [[HOP62 (line)]] | alt | 190 | 1 (1 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.2) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 5 µM 0.270× (z -19.9) |
| [[PANC-1 (line)]] | alt | 203 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -14.5) |
| [[Hs 766T (line)]] | wt | 177 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -15.1) |
| [[SNU-423 (line)]] | alt | 255 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.227× (z -17.6) |
| [[A-172 (line)]] | wt | 95.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -20.3) |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -13.9) |
| [[A-427 (line)]] | wt | 97.6 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.308× (z -13.5) |
| [[A549 (line)]] | wt | 118 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.6) ⚠ cell-cycle shift, explains ~17% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.1) |
| [[J82 (line)]] | alt | 46.7 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.3) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 5 µM 0.387× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 99.2 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.228× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 125 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -15.0) |
| [[SHP-77 (line)]] | alt | 133 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -12.3) |
| [[SW480 (line)]] | alt | 74.6 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.292× (z -15.5) |
| [[H4 (line)]] | wt | 103 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 191 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 194 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.274× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 73.7 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.201× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 83.3 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.9) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 5 µM 0.416× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 98.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -10.7) |
| [[HT-29 (line)]] | alt | 50.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 96.0 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.318× (z -11.4) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.340× (z -11.2) |
| [[AN3 CA (line)]] | alt | 257 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.6) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -11.2) |
| [[C-33 A (line)]] | alt | 134 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.424× (z -9.8) |
| [[CHP-212 (line)]] | wt | 96.8 | 0 | 2 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0505× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 42.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.337× (z -10.4) |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -9.2) |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.239× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.242× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.268× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.24 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRX]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 | same gene group; STRING 407 |
| [[IFT81]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CHD3]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 | same gene group; STRING 764 |
| [[STAG2]] | +0.58 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[SLC36A4]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SUCLG2-DT]] | +0.58 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[GALC]] | +0.57 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[ZNF655]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[HUWE1]] | +0.57 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[HMGN2]] | +0.57 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[MTERF2]] | +0.56 | +0.46 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT4]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[TSEN54]] | -0.64 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[FOXK2]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[SDHAF1]] | -0.58 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TMEM120B]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MPG]] | -0.57 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[ZMYND19]] | -0.56 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[SLC37A3]] | -0.56 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[MGAT1]] | -0.56 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[HM13]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TAF5L]] | -0.55 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAJC18]] | C | DNAJC18 activity raises SMARCA1's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 8.37× lower at baseline in the lines without DNAJC18 | 0.024 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |
| [[ZNF549]] | C | ZNF549 activity raises SMARCA1's level | lines that do not express ZNF549 (17) vs lines expressing it (33) | 4.95× lower at baseline in the lines without ZNF549 | 0.041 | ⚠ within organs, on part of the lines; also absent: SDK2, SNRPN, CHST10; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZXDC]] | B | SMARCA1 activity raises ZXDC's level | lines that do not express SMARCA1 (13) vs lines expressing it (37) | 1.10× lower at baseline in the lines without SMARCA1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2; also absent: ENSG00000268163, ZNF772, SNRPN |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-15.7, 4.5); signed map (17.3, -35.6). **Vector** length 111, 31.5% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +7.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +7.4 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.4 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +0.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -11.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -6.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.0 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | SNF2 related chromatin remodeling ATPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq25-q26.1 — chrX:129,446,501-129,523,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SNF2LB, NURF140, ISWI, SWI, hSNF2L; previously SNF2L1, SNF2L |
| Gene groups (HGNC) | Myb/SANT domain containing; SNF2 related family; NURF complex; CERF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P28370](https://www.uniprot.org/uniprotkb/P28370) (SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 1):

> [Isoform 1]: ATPase that possesses intrinsic ATP-dependent chromatin-remodeling activity. ATPase activity is substrate-dependent, and is increased when nucleosomes are the substrate, but is also catalytically active when DNA alone is the substrate. Catalytic subunit of ISWI chromatin-remodeling complexes, which form ordered nucleosome arrays on chromatin and facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair. Within the ISWI …

**Summary**, from NCBI Gene [6594](https://www.ncbi.nlm.nih.gov/gene/6594):

> This gene encodes a member of the SWI/SNF family of proteins. The encoded protein is an ATPase which is expressed in diverse tissues and contributes to the chromatin remodeling complex that is involved in transcription. The protein may also play a role in DNA damage, growth inhibition and apoptosis of cancer cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:11097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11097) · Entrez [6594](https://www.ncbi.nlm.nih.gov/gene/6594) · UniProt [P28370](https://www.uniprot.org/uniprotkb/P28370) · Ensembl [ENSG00000102038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102038)

## Data

Gene col 2206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2206); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2206]; `tensor/DDL_lfc|DDL_z.npy` [2206]; `embed/gene_vectors.npy` [2206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2206 or target_col == 2206). Every well: [[SMARCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMARCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
