---
symbol: "SMC5-DT"
type: "gene"
col: 15597
ensembl_id: "ENSG00000268364"
name: ""
location: ""
module: 35
arm: "+"
pooled_cpm: 17.0
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# SMC5-DT

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.71× (z +9.5, q 7e-19, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.47× (z +6.9, q 2e-09, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.240× (z -17.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT6B]] (+0.73, fdr 7e-06), [[C2orf49-DT]] (+0.69, fdr 1e-05), [[MAMDC2-AS1]] (+0.68, fdr 7e-06, ⚠ same locus), [[DDX19A-DT]] (+0.67, fdr 7e-06); moves opposite to [[BTBD3]] (-0.56, fdr 2e-05), [[LIFR]] (-0.55, fdr 3e-04), [[TUBG2]] (-0.55, fdr 3e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MAMDC2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.71×** | +9.5 | 7e-19 | 37/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.9 | 2e-09 | 25/47 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.7 | 4e-04 | 21/48 (C32, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.45×** | +4.6 | 5e-04 | 20/48 (J82, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.010 | 17/47 (SW480, HOP62, …) | two highest doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.019 | 8/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.040 | 15/48 (H4, KATO III, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.049 | 10/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.049 | 13/48 (KATO III, SW480, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.055 | 11/48 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.055 | 9/47 (HS-578T, A-172, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.10 | 11/48 (SW480, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.240×** | -17.9 | 0e+00 | 45/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.265×** | -16.6 | 0e+00 | 43/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.310×** | -14.7 | 0e+00 | 45/46 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.311×** | -14.6 | 0e+00 | 45/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.456×** | -9.8 | 9e-21 | 39/47 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.481×** | -8.8 | 1e-16 | 33/47 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -8.2 | 3e-14 | 31/42 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.539×** | -7.7 | 8e-13 | 32/48 (H4, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.685×** | -6.7 | 1e-09 | 25/47 (A549, COLO 205, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -6.7 | 1e-09 | 31/48 (NCI-H23, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.601×** | -6.4 | 1e-08 | 29/47 (H4, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -5.4 | 4e-06 | 26/45 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.653×** | -5.0 | 2e-05 | 26/47 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.620×** | -5.0 | 2e-05 | 22/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.643×** | -4.6 | 1e-04 | 22/48 (NCI-H23, SNU-423, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.808×** | -3.8 | 0.005 | 16/48 (H4, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.760×** | -3.4 | 0.018 | 13/48 (SK-MEL-2, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.613×** | -3.2 | 0.039 | 14/47 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.710×** | -3.1 | 0.058 | 6/48 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -2.9 | 0.079 | 11/48 (NCI-H23, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 22.2 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -16.1) |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -12.7) |
| [[COLO 205 (line)]] | alt | 36.2 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0929× (z -15.5) |
| [[H4 (line)]] | wt | 25.1 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0210× (z -18.5) |
| [[KATO III (line)]] | alt | 33.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0494× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.236× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0846× (z -17.0) |
| [[SW480 (line)]] | alt | 20.0 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.175× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.184× (z -13.9) |
| [[A-427 (line)]] | wt | 16.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.218× (z -8.8) |
| [[A549 (line)]] | wt | 6.42 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.3) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Hesperidin (drug)]] 5 µM 0.0652× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -11.2) |
| [[J82 (line)]] | alt | 19.3 | 1 (1 ⚠) | 2 | [[Selinexor (drug)]] 5 µM 2.89× (z +9.2) ⚠ cell-cycle shift, explains ~43% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0946× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.108× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0936× (z -14.4) |
| [[RKO (line)]] | wt | 17.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -8.9) |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.162× (z -10.8) |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.156× (z -10.4) |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.139× (z -10.1) |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0528× (z -12.1) |
| [[A-172 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.8) ⚠ cell-cycle shift, explains ~95% of this change |
| [[AsPC-1 (line)]] | alt | 6.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0534× (z -11.4) |
| [[C32 (line)]] | wt | 17.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.94× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -8.5) |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 7.13 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0946× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0711× (z -11.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 9.82 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0939× (z -11.6) |
| [[A498 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6B]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[C2orf49-DT]] | +0.69 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MAMDC2-AS1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 | ⚠ same locus (18.1 kb, same strand: neighbours can correlate without regulation) |
| [[DDX19A-DT]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.66 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[YTHDF3]] | +0.65 | +0.26 / +0.56 | both halves | 4e-04 |  |
| [[PJVK]] | +0.64 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PTPN23-DT]] | +0.64 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[PGBD4]] | +0.64 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.63 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[PDCD6IP-DT]] | +0.62 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[GSK3B-DT]] | +0.62 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SUMO2P17]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD3]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[LIFR]] | -0.55 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[TUBG2]] | -0.55 | -0.50 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAMDC2-AS1]] | C | SMC5-DT's natural level strengthens MAMDC2-AS1's drug response | SMC5-DT's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.14; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.3, 11.8); signed map (23.0, -3.4). **Vector** length 68.2, 13.6% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +6.5 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +0.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.9 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -16.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

> [!warning] No registry record
> SMC5-DT has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15597); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15597]; `tensor/DDL_lfc|DDL_z.npy` [15597]; `embed/gene_vectors.npy` [15597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15597 or target_col == 15597). Every well: [[SMC5-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMC5-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
