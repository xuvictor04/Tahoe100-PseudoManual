---
symbol: "CDK18"
type: "gene"
col: 3890
ensembl_id: "ENSG00000117266"
name: "cyclin dependent kinase 18"
location: "1q32.1"
module: 137
arm: "-"
pooled_cpm: 20.05
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 44
n_dd_up_clean: 4
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# CDK18

*cyclin dependent kinase 18* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +7.5, q 3e-11, up in 22 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.318× (z -26.2, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHO1]] (+0.67, fdr 1e-05), [[AHDC1]] (+0.67, fdr 1e-05), [[LRP1]] (+0.66, fdr 1e-05); moves opposite to [[SPRY3]] (-0.65, fdr 8e-05), [[UBTF]] (-0.65, fdr 1e-05), [[ZMYND11]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[BSPRY]] → it (grade B ⚠); 5 go from it, the strongest it → [[XACT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +7.5 | 3e-11 | 22/39 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 3e-07 | 20/37 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +5.4 | 1e-05 | 17/37 (HOP62, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.36×** | +5.0 | 8e-05 | 18/38 (A498, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +4.9 | 9e-05 | 11/39 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.35×** | +4.7 | 3e-04 | 15/38 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.16 | 8/39 (AsPC-1, KATO III, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.16 | 12/39 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.318×** | -26.2 | 0e+00 | 37/37 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.330×** | -25.3 | 0e+00 | 29/37 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.322×** | -18.3 | 0e+00 | 31/37 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.363×** | -15.7 | 0e+00 | 30/37 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.380×** | -15.6 | 0e+00 | 32/39 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.400×** | -14.2 | 8e-44 | 31/36 (C32, HCT15, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.415×** | -13.6 | 2e-40 | 31/38 (RPMI-7951, J82, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -12.5 | 7e-34 | 34/38 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -11.8 | 3e-30 | 29/38 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.516×** | -10.3 | 7e-23 | 28/39 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.554×** | -9.5 | 9e-20 | 25/32 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.589×** | -8.5 | 7e-16 | 24/37 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -8.4 | 2e-15 | 25/38 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.632×** | -7.1 | 6e-11 | 18/25 (HCT15, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -7.0 | 1e-10 | 20/35 (HT-29, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.493×** | -5.9 | 1e-07 | 16/37 (HS-578T, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.504×** | -5.8 | 3e-07 | 19/37 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.691×** | -5.7 | 4e-07 | 19/38 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -5.4 | 2e-06 | 18/38 (RPMI-7951, NCI-H23, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.731×** | -5.0 | 1e-05 | 19/38 (HOP62, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.3 | 0 | 11 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0957× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.244× (z -17.3) |
| [[HCT15 (line)]] | alt | 67.0 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0261× (z -23.0) |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0631× (z -18.3) |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -13.1) |
| [[J82 (line)]] | alt | 33.2 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -16.0) |
| [[KATO III (line)]] | alt | 17.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0311× (z -23.1) |
| [[HT-29 (line)]] | alt | 26.9 | 0 | 6 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0259× (z -24.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -21.2) |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -12.6) |
| [[A-172 (line)]] | wt | 127 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -12.7) |
| [[C32 (line)]] | wt | 36.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -14.6) |
| [[COLO 205 (line)]] | alt | 23.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0242× (z -20.8) |
| [[LoVo (line)]] | wt | 19.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -20.8) |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0405× (z -18.7) |
| [[HEC-1-A (line)]] | alt | 30.6 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -15.6) |
| [[HOP62 (line)]] | alt | 16.7 | 1 (1 ⚠) | 3 | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +9.1) ⚠ position not correctable | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -11.9) |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.9) |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -18.6) |
| [[NCI-H2347 (line)]] | alt | 38.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -14.8) |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.8) |
| [[SW48 (line)]] | wt | 22.0 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0770× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 9.75 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0782× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -9.0) |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.1) |
| [[A498 (line)]] | wt | 44.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 30.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.5) |
| [[RKO (line)]] | wt | 10.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0968× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -11.9) |
| [[A-427 (line)]] | wt | 7.80 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 8.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -8.9) |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0639× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0681× (z -10.4) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 6.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHO1]] | +0.67 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.67 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[LRP1]] | +0.66 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[GPR160]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CDON]] | +0.66 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.63 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[FHIP1A]] | +0.63 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.62 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TNNI3]] | +0.62 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[PFKFB4]] | +0.61 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[RFX2]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RASAL1]] | +0.60 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY3]] | -0.65 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[UBTF]] | -0.65 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.65 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[EFCAB2]] | -0.63 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[AVEN]] | -0.62 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[MSANTD2]] | -0.62 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[PCBD2]] | -0.60 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[KIF27]] | -0.58 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[PPP3CB-AS1]] | -0.57 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ATE1]] | -0.57 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[N4BP2]] | -0.57 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ST7L]] | -0.56 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSPRY]] | B | BSPRY activity raises CDK18's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without BSPRY | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[SPNS2]] | B | SPNS2 activity raises CDK18's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without SPNS2 | 0.022 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[MSRB3]] | B | MSRB3 activity lowers CDK18's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 2.01× higher at baseline in the lines without MSRB3 | 0.034 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[RAB39A]] | B | RAB39A activity lowers CDK18's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 1.62× higher at baseline in the lines without RAB39A | 0.035 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent |
| [[ENPP5]] | B | ENPP5 activity raises CDK18's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without ENPP5 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises CDK18's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.73× lower at baseline in the lines without TNFRSF11A | 0.052 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[ESPN]] | B | ESPN activity raises CDK18's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.51× lower at baseline in the lines without ESPN | 0.068 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XACT]] | B | CDK18 activity raises XACT's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without CDK18 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[NDRG1]] | B | CDK18 activity raises NDRG1's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 2.98× lower at baseline in the lines without CDK18 | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[TNFRSF11A]] | B | CDK18 activity raises TNFRSF11A's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 2.26× lower at baseline in the lines without CDK18 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[ANXA2R-OT1]] | B | CDK18 activity lowers ANXA2R-OT1's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without CDK18 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[CD47]] | B | CDK18 activity raises CD47's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 1.61× lower at baseline in the lines without CDK18 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **-** arm (projection on the module's main direction -0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (10.6, -10.4); signed map (-31.2, 21.6). **Vector** length 104, 25.8% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +5.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -18.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -26.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,504,596-205,532,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCTAIRE3; previously PCTK3 |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07002](https://www.uniprot.org/uniprotkb/Q07002) (Cyclin-dependent kinase 18):

> May play a role in signal transduction cascades in terminally differentiated cells.

**Summary**, from NCBI Gene [5129](https://www.ncbi.nlm.nih.gov/gene/5129):

> Predicted to enable cyclin-dependent protein serine/threonine kinase activity. Involved in positive regulation of myelination. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8751) · Entrez [5129](https://www.ncbi.nlm.nih.gov/gene/5129) · UniProt [Q07002](https://www.uniprot.org/uniprotkb/Q07002) · Ensembl [ENSG00000117266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117266)

## Data

Gene col 3890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3890); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3890]; `tensor/DDL_lfc|DDL_z.npy` [3890]; `embed/gene_vectors.npy` [3890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3890 or target_col == 3890). Every well: [[CDK18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
