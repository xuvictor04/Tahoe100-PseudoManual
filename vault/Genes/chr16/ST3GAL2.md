---
symbol: "ST3GAL2"
type: "gene"
col: 8062
ensembl_id: "ENSG00000157350"
name: "ST3 beta-galactoside alpha-2,3-sialyltransferase 2"
location: "16q22.1"
module: 192
arm: "+"
pooled_cpm: 43.72
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# ST3GAL2

*ST3 beta-galactoside alpha-2,3-sialyltransferase 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +7.5, q 5e-11, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.467× (z -16.9, q 0e+00, down in 30 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.735× (z -10.1, q 6e-22, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLE3]] (+0.57, fdr 4e-05), [[PLIN3]] (+0.55, fdr 3e-05), [[IRF2BPL]] (+0.55, fdr 2e-05); moves opposite to [[SPTLC1]] (-0.53, fdr 4e-05), [[CA5BP1-1]] (-0.51, fdr 2e-04), [[CPNE1]] (-0.50, fdr 3e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ANXA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +7.5 | 5e-11 | 26/46 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +5.9 | 8e-07 | 24/46 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.8 | 2e-06 | 22/46 (LS 180, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +5.4 | 1e-05 | 19/46 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 1e-04 | 22/46 (NCI-H23, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.1 | 0.004 | 16/46 (CFPAC-1, SW1417, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.015 | 11/46 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.7 | 0.015 | 15/45 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.015 | 4/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.028 | 14/45 (NCI-H2030, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.030 | 6/46 (SW1417, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.064 | 11/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -16.9 | 0e+00 | 30/37 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.501×** | -16.0 | 0e+00 | 32/44 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.509×** | -12.6 | 7e-34 | 28/39 (hTERT-HPNE, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.735×** | -10.1 | 6e-22 | 25/46 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.732×** | -7.2 | 5e-11 | 25/46 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.589×** | -6.4 | 1e-08 | 23/46 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -6.1 | 7e-08 | 28/45 (SHP-77, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -4.9 | 7e-05 | 18/46 (A498, J82, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.833×** | -4.3 | 0.001 | 17/46 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -4.2 | 0.002 | 21/46 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.852× | -3.7 | 0.009 | 11/45 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.860× | -3.5 | 0.020 | 16/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.900× | -3.5 | 0.020 | 16/46 (KATO III, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.856× | -3.5 | 0.020 | 17/46 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.866× | -3.4 | 0.029 | 12/45 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.875× | -3.1 | 0.065 | 7/46 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.878× | -3.0 | 0.078 | 12/46 (HOP62, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 96.2 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 63.3 | 0 | 7 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.383× (z -11.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 71.9 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.175× (z -10.4) |
| [[C32 (line)]] | wt | 52.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0607× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.269× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 82.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.8) |
| [[SW 900 (line)]] | alt | 82.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.7) |
| [[A498 (line)]] | wt | 116 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -13.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 31.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.496× (z -8.6) |
| [[SW480 (line)]] | alt | 70.9 | 1 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.96× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.144× (z -24.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 35.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.589× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 65.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.2) |
| [[AN3 CA (line)]] | alt | 50.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Orlistat (drug)]] 0.05 µM 0.0833× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 37.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.8) |
| [[SNU-423 (line)]] | alt | 54.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0757× (z -10.9) |
| [[A-172 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -14.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -10.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0702× (z -13.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.552× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 16.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.24× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 12.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.94× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0956× (z -15.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -11.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.116× (z -17.3) ⚠ toxic |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLE3]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PLIN3]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[IRF2BPL]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[RHBDF2]] | +0.53 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SH2B3]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[IER5L]] | +0.52 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[RUNX3]] | +0.51 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[ZNRF1]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[FAM89B]] | +0.50 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[ZBTB7A]] | +0.50 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[UPK1A-AS1]] | +0.50 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[SMOX]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC1]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 | pathway: Sphingolipid metabolism |
| [[CA5BP1-1]] | -0.51 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[CPNE1]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MYO5C]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[HDHD2]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ZNF460]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SRP72]] | -0.49 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[ANXA3]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZNF252P]] | -0.48 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[BROX]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SBDSP1]] | -0.48 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[LARS1]] | -0.48 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA3]] | B | ANXA3 activity lowers ST3GAL2's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.89× higher at baseline in the lines without ANXA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[RNF220]] | B | RNF220 activity raises ST3GAL2's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 1.61× lower at baseline in the lines without RNF220 | 0.038 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[ZCCHC24]] | B | ZCCHC24 activity raises ST3GAL2's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without ZCCHC24 | 0.084 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[SH2B3]] | B | SH2B3 activity raises ST3GAL2's level | lines that do not express SH2B3 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without SH2B3 | 0.089 | ⚠ within organs, on part of the lines; also absent: VAT1, CEP112, FCHSD1; maybe low, not absent; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ST3GAL2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ST3GAL2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, -4.3); signed map (-22.6, 21.1). **Vector** length 110, 27.2% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.5 | -16.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.0 | -16.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -3.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.5 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ST3 beta-galactoside alpha-2,3-sialyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,375,977-70,439,237 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ST3GALII, ST3GalA.2; previously SIAT4B |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 25 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Glycosphingolipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16842](https://www.uniprot.org/uniprotkb/Q16842) (CMP-N-acetylneuraminate-beta-galactosamide-alpha-2,3-sialyltransferase 2):

> A beta-galactoside alpha2-3 sialyltransferase primarily involved in terminal sialylation of ganglio and globo series glycolipids. Catalyzes the transfer of sialic acid (N-acetyl-neuraminic acid; Neu5Ac) from the nucleotide sugar donor CMP-Neu5Ac onto acceptor Galbeta-(1->3)-GalNAc-terminated glycoconjugates through an alpha2-3 linkage. Sialylates GM1/GM1a, GA1/asialo-GM1 and GD1b gangliosides to form GD1a, GM1b and GT1b, respectively. Together with ST3GAL3, primarily responsible for …

**Summary**, from NCBI Gene [6483](https://www.ncbi.nlm.nih.gov/gene/6483):

> The protein encoded by this gene is a type II membrane protein that catalyzes the transfer of sialic acid from CMP-sialic acid to galactose-containing substrates. The encoded protein is normally found in the Golgi but can be proteolytically processed to a soluble form. This protein, which is a member of glycosyltransferase family 29, can use the same acceptor substrates as does sialyltransferase 4A. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10863) · Entrez [6483](https://www.ncbi.nlm.nih.gov/gene/6483) · UniProt [Q16842](https://www.uniprot.org/uniprotkb/Q16842) · Ensembl [ENSG00000157350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157350)

## Data

Gene col 8062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8062); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8062]; `tensor/DDL_lfc|DDL_z.npy` [8062]; `embed/gene_vectors.npy` [8062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8062 or target_col == 8062). Every well: [[ST3GAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST3GAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
