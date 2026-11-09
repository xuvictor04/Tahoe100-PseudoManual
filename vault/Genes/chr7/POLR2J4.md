---
symbol: "POLR2J4"
type: "gene"
col: 13223
ensembl_id: "ENSG00000214783"
name: "SPDYE1 and UBE2D4 antisense RNA 1"
location: "7p13"
module: 24
arm: "+"
pooled_cpm: 66.88
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# POLR2J4

*SPDYE1 and UBE2D4 antisense RNA 1* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.35× (z +17.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.518× (z -12.8, q 8e-35, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.322× (z -12.0, q 1e-30, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INAFM1]] (+0.71, fdr 7e-06), [[ENDOV]] (+0.71, fdr 7e-06), [[ACAD10]] (+0.69, fdr 7e-06); moves opposite to [[COX11]] (-0.69, fdr 7e-06), [[PNPO]] (-0.66, fdr 1e-05), [[ACADM]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UMAD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.35×** | +17.3 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +14.9 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +14.3 | 2e-44 | 46/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 1e-04 | 25/48 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +3.6 | 0.040 | 14/49 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.080 | 14/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.12 | 14/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.16× | +3.0 | 0.17 | 16/48 (BT-474, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -12.8 | 8e-35 | 36/43 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.322×** | -12.0 | 1e-30 | 47/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.552×** | -11.6 | 1e-28 | 40/47 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.581×** | -11.0 | 6e-26 | 40/49 (NCI-H23, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.381×** | -10.2 | 2e-22 | 40/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.591×** | -9.9 | 6e-21 | 36/45 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -7.9 | 2e-13 | 33/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.670×** | -7.8 | 5e-13 | 35/48 (A549, H4, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -5.8 | 4e-07 | 0/49 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.799×** | -4.5 | 3e-04 | 20/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **0.817×** | -4.1 | 0.002 | 20/48 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.835× | -3.6 | 0.013 | 17/48 (A549, LOX-IMVI, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.840× | -3.5 | 0.019 | 19/48 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.841× | -3.5 | 0.019 | 20/48 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.086 | 12/48 (A498, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.4 | 1 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.434× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.453× (z -9.9) |
| [[PANC-1 (line)]] | alt | 74.7 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.225× (z -10.9) |
| [[SW480 (line)]] | alt | 87.6 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.548× (z -8.6) |
| [[A-172 (line)]] | wt | 77.2 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.210× (z -8.9) |
| [[A549 (line)]] | wt | 46.2 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.284× (z -11.8) |
| [[LoVo (line)]] | wt | 81.3 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -18.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 89.5 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 77.0 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.400× (z -10.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.451× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 85.4 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.218× (z -8.6) |
| [[SNU-423 (line)]] | alt | 80.6 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.203× (z -8.8) |
| [[HS-578T (line)]] | alt | 59.1 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.180× (z -9.2) |
| [[KATO III (line)]] | alt | 93.5 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0428× (z -32.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 78.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -21.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 110 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 60.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 67.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -13.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 79.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 50.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 84.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0864× (z -14.4) |
| [[SW48 (line)]] | wt | 78.1 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.99× (z +8.8) | [[TAK-901 (drug)]] 0.05 µM 0.189× (z -12.6) |
| [[A498 (line)]] | wt | 77.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 56.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 62.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.12× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 51.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 70.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 60.0 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.13× (z +9.4) | [[TAK-901 (drug)]] 5 µM 0.111× (z -9.4) |
| [[A-427 (line)]] | wt | 54.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.5) ⚠ cell-cycle shift, explains ~5% of this change |
| [[C32 (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -8.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 76.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.412× (z -8.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0826× (z -17.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 60.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +8.5) | — |
| [[J82 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.347× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H596 (line)]] | alt | 64.3 | 1 | 0 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 5.63× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 96.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +8.5) | — |
| [[SW 1271 (line)]] | alt | 73.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0857× (z -9.4) |
| [[SW 900 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ENDOV]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ACAD10]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[VRK3]] | +0.68 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.66 | +0.66 / +0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PIAS4]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TULP3]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[GON4L]] | +0.65 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.65 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[C19orf81]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[BRI3]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[LSM7]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX11]] | -0.69 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[PNPO]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ACADM]] | -0.62 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.62 | -0.44 / -0.67 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.60 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[RBBP9]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[PTGFRN]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TOP2B]] | -0.58 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[OXCT1]] | -0.57 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[SMG7]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[COPS6]] | -0.57 | -0.65 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers POLR2J4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UMAD1]] | C | POLR2J4's natural level strengthens UMAD1's drug response | POLR2J4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.39; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.3, -14.6); signed map (-18.3, 0.3). **Vector** length 101, 29.4% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +14.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +17.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +4.3 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Resveratrol (drug)]] 5 µM |  | +2.1 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.8 | -12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -10.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -11.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -1.1 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | SPDYE1 and UBE2D4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p13 |
| Also known as | RASA4CP-POLR2J4-UPK3BL3P-RASA4EP |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56874) · Entrez [131554431](https://www.ncbi.nlm.nih.gov/gene/131554431) · Ensembl [ENSG00000214783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214783)

## Data

Gene col 13223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13223); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13223]; `tensor/DDL_lfc|DDL_z.npy` [13223]; `embed/gene_vectors.npy` [13223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13223 or target_col == 13223). Every well: [[POLR2J4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2J4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
