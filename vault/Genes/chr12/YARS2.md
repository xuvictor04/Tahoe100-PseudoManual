---
symbol: "YARS2"
type: "gene"
col: 6261
ensembl_id: "ENSG00000139131"
name: "tyrosyl-tRNA synthetase 2"
location: "12p11.21"
module: 23
arm: "+"
pooled_cpm: 37.64
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# YARS2

*tyrosyl-tRNA synthetase 2* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.98× (z +12.3, q 3e-32, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.482× (z -15.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFF-DT]] (+0.71, fdr 1e-04), [[MAIP1]] (+0.70, fdr 3e-05), [[ZNF460-AS1]] (+0.69, fdr 4e-05); moves opposite to [[CEP131]] (-0.66, fdr 2e-04), [[KANK2]] (-0.65, fdr 7e-05), [[RHPN1]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +12.3 | 3e-32 | 40/48 (HOP62, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +12.2 | 1e-31 | 32/48 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +8.6 | 1e-15 | 36/48 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +8.4 | 4e-15 | 32/48 (SW 900, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +8.4 | 7e-15 | 35/47 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.7 | 1e-09 | 30/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +6.4 | 8e-09 | 22/47 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +6.4 | 8e-09 | 28/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +6.4 | 1e-08 | 25/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.2 | 3e-08 | 24/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +5.4 | 3e-06 | 23/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.9 | 4e-05 | 21/47 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.9 | 5e-05 | 19/48 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.9 | 5e-05 | 20/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.6 | 1e-04 | 12/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 2e-04 | 19/48 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +4.4 | 3e-04 | 16/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.025 | 8/48 (HT-29, LS 180, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.3 | 0.025 | 13/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.482×** | -15.8 | 0e+00 | 47/48 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.500×** | -15.0 | 0e+00 | 47/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.517×** | -14.3 | 5e-44 | 40/48 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -8.4 | 8e-15 | 37/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -6.6 | 4e-09 | 3/48 (MIA PaCa-2, SW 1088, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -6.3 | 2e-08 | 27/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.778×** | -5.4 | 4e-06 | 28/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.781×** | -5.4 | 6e-06 | 22/46 (RKO, SNU-423, …) | two highest doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.638×** | -5.1 | 2e-05 | 21/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.833×** | -3.8 | 0.007 | 16/39 (Panc 03.27, A498, …) | two highest doses | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.759×** | -3.1 | 0.088 | 9/48 (SW 1271, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 5 µM |  | 0.767× | -3.0 | 0.12 | 11/44 (HepG2/C3A, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.871× | -3.0 | 0.12 | 10/48 (A-172, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 63.9 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.76× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -12.7) |
| [[RKO (line)]] | wt | 77.1 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.227× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 25.8 | 2 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 5.44× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.379× (z -10.5) |
| [[PANC-1 (line)]] | alt | 50.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.371× (z -11.7) |
| [[SW480 (line)]] | alt | 56.1 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.53× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.332× (z -14.8) |
| [[LoVo (line)]] | wt | 59.9 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 5.81× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.355× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 51.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -10.9) |
| [[A-427 (line)]] | wt | 55.5 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.4) |
| [[SW 900 (line)]] | alt | 52.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.0) | — |
| [[A498 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 22.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.5) | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.147× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 47.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -9.1) |
| [[LS 180 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.6) | — |
| [[A-172 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | +0.71 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[MAIP1]] | +0.70 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZNF460-AS1]] | +0.69 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[THBS4]] | +0.66 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[ZFHX2-AS1]] | +0.66 | +0.48 / +0.26 | both halves | 4e-04 |  |
| [[MYLK-AS1]] | +0.66 | +0.49 / +0.28 | both halves | 3e-04 |  |
| [[MTRF1]] | +0.66 | +0.54 / +0.49 | both halves | 1e-05 | STRING 571 |
| [[TAS2R4]] | +0.65 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[ANKAR]] | +0.65 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[SMIM15-AS1]] | +0.65 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[ATE1OSP]] | +0.65 | +0.44 / +0.27 | both halves | 3e-04 |  |
| [[PBLD]] | +0.64 | +0.38 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP131]] | -0.66 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[KANK2]] | -0.65 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[RHPN1]] | -0.65 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[GNAI2]] | -0.64 | -0.45 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[KCTD17]] | -0.63 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[TCIRG1]] | -0.63 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[SLC26A6]] | -0.62 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[PLPPR2]] | -0.62 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.62 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[STUB1]] | -0.61 | -0.35 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[SPAG9]] | -0.61 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[DHTKD1]] | -0.60 | -0.40 / -0.21 | both halves | 7e-04 |  |
| [[PEDS1]] | -0.60 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[MATCAP1]] | -0.59 | -0.49 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises YARS2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises YARS2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DENND3]] | B | DENND3 activity lowers YARS2's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 1.44× higher at baseline in the lines without DENND3 | 0.0999 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-1.4, 18.1); signed map (23.3, -12.8). **Vector** length 100, 23.5% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +12.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.0 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.1 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.9 | -15.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.4 | -15.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tyrosyl-tRNA synthetase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:32,727,490-32,755,897 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13995, CGI-04, mt-TyrRS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Z4](https://www.uniprot.org/uniprotkb/Q9Y2Z4) (Tyrosine--tRNA ligase, mitochondrial):

> Catalyzes the attachment of tyrosine to tRNA(Tyr) in a two-step reaction: tyrosine is first activated by ATP to form Tyr-AMP and then transferred to the acceptor end of tRNA(Tyr).

**Summary**, from NCBI Gene [51067](https://www.ncbi.nlm.nih.gov/gene/51067):

> This gene encodes a mitochondrial protein that catalyzes the attachment of tyrosine to tRNA(Tyr). Mutations in this gene are associated with myopathy with lactic acidosis and sideroblastic anemia type 2 (MLASA2). [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:24249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24249) · Entrez [51067](https://www.ncbi.nlm.nih.gov/gene/51067) · UniProt [Q9Y2Z4](https://www.uniprot.org/uniprotkb/Q9Y2Z4) · Ensembl [ENSG00000139131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139131)

## Data

Gene col 6261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6261); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6261]; `tensor/DDL_lfc|DDL_z.npy` [6261]; `embed/gene_vectors.npy` [6261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6261 or target_col == 6261). Every well: [[YARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
