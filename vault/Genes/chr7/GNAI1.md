---
symbol: "GNAI1"
type: "gene"
col: 4849
ensembl_id: "ENSG00000127955"
name: "G protein subunit alpha i1"
location: "7q21.11"
module: 182
arm: "+"
pooled_cpm: 61.08
n_lines_expressing: 40
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# GNAI1

*G protein subunit alpha i1* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.01× (z +10.7, q 8e-24, up in 28 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.637× (z -8.1, q 4e-13, down in 24 of 33 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.119×, NCI-H2030 0.184×, SHP-77 0.110×, SW48 0.141×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.276×, A-427 0.310×, NCI-H2030 0.355×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.400×, NCI-H2347 0.496×; ⚠ cell-cycle shift, explains ~45% of this change); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.233×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H2030 0.418×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUBR]] (+0.59, fdr 1e-05), [[RHOBTB1]] (+0.55, fdr 1e-05), [[NTPCR]] (+0.52, fdr 2e-05); moves opposite to [[C13orf46]] (-0.60, fdr 1e-05), [[SLC35C2]] (-0.60, fdr 1e-05), [[SLC30A7]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CD36]] → it (grade B ⚠); 5 go from it, the strongest it → [[ADGRL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.01×** | +10.7 | 8e-24 | 28/39 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +10.3 | 3e-22 | 27/38 (A549, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +9.1 | 2e-17 | 26/38 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +8.9 | 5e-17 | 26/38 (J82, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.5 | 1e-11 | 24/38 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 4e-08 | 22/38 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.1 | 1e-07 | 22/38 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 1e-07 | 22/38 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.9 | 2e-07 | 22/38 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 2e-05 | 20/38 (C32, A-172, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +5.1 | 2e-05 | 18/38 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 3e-04 | 17/38 (LoVo, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.3 | 6e-04 | 16/39 (SW480, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 9e-04 | 20/40 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.002 | 17/39 (C32, RKO, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.003 | 17/37 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.008 | 16/38 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4849.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.119×, NCI-H2030 0.184×, SHP-77 0.110×, SW48 0.141×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.276×, A-427 0.310×, NCI-H2030 0.355×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.400×, NCI-H2347 0.496×; ⚠ cell-cycle shift, explains ~45% of this change); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.233×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H2030 0.418×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.637×** | -8.1 | 4e-13 | 24/33 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.745×** | -5.5 | 1e-05 | 22/37 (NCI-H2030, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.796×** | -4.3 | 0.004 | 17/37 (LS 180, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.861× | -4.0 | 0.010 | 19/38 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **0.818×** | -3.5 | 0.055 | 17/35 (NCI-H2347, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.846× | -3.1 | 0.17 | 10/38 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.799× | -3.0 | 0.18 | 12/38 (HepG2/C3A, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 57.5 | 9 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 235 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -9.7) |
| [[C32 (line)]] | wt | 92.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 15.9× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 65.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[A-427 (line)]] | wt | 205 | 1 | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.82× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -22.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 57.5 | 4 | 0 | [[Trametinib (drug)]] 5 µM 2.79× (z +10.1) | — |
| [[SW48 (line)]] | wt | 145 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.42× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -15.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 75.1 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 127 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.0× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 80.0 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.27× (z +11.6) | — |
| [[A498 (line)]] | wt | 74.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 1.82× (z +10.3) | — |
| [[A549 (line)]] | wt | 75.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.25× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 64.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 54.6 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.80× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 60.5 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.233× (z -12.8) |
| [[RKO (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -17.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 69.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -8.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW 900 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -9.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 9.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 97.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUBR]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RHOBTB1]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[NTPCR]] | +0.52 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TMEM64]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[SLC35D1]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TLE1]] | +0.51 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PITX2]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[ARL6IP5]] | +0.49 | +0.53 / +0.40 | both halves | 5e-05 | pathway: Neuronal System |
| [[ABHD14A]] | +0.49 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[LINC02057]] | +0.49 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[LGR4]] | +0.48 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[TSPAN12]] | +0.48 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C13orf46]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SLC35C2]] | -0.60 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[SLC30A7]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SETX]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PHLDB1]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[TAF1]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[EGR3]] | -0.50 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[GPATCH2L]] | -0.50 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[A3GALT2]] | -0.49 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[MAP3K7]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BLZF2P]] | -0.48 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[PRKAG1]] | -0.48 | -0.54 / -0.36 | both halves | 9e-05 | pathway: Neuronal System |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD36]] | B | CD36 activity raises GNAI1's level | lines that do not express CD36 (25) vs lines expressing it (25) | 2.81× lower at baseline in the lines without CD36 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GNAT3, RPS4Y1, LIN7A; maybe low, not absent |
| [[EPS8]] | B | EPS8 activity raises GNAI1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 2.27× lower at baseline in the lines without EPS8 | 0.082 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[PLEKHA5]] | C | PLEKHA5 activity raises GNAI1's level | lines that do not express PLEKHA5 (4) vs lines expressing it (46) | 4.53× lower at baseline in the lines without PLEKHA5 | 0.070 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |
| [[MBNL2]] | C | MBNL2 activity lowers GNAI1's level | lines that do not express MBNL2 (4) vs lines expressing it (46) | 2.06× higher at baseline in the lines without MBNL2 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM102A, NINJ1, MYD88 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRL3]] | B | GNAI1 activity lowers ADGRL3's level | lines that do not express GNAI1 (10) vs lines expressing it (40) | 1.62× higher at baseline in the lines without GNAI1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: ENSG00000250158, KLF12, ELL2 |
| [[SEMA6A]] | B | GNAI1 activity lowers SEMA6A's level | lines that do not express GNAI1 (10) vs lines expressing it (40) | 1.47× higher at baseline in the lines without GNAI1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: ENSG00000250158, KLF12, ELL2 |
| [[LINC02057]] | B | GNAI1 activity raises LINC02057's level | lines that do not express GNAI1 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without GNAI1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: ENSG00000250158, KLF12, ELL2 |
| [[FOSL1]] | B | GNAI1 activity raises FOSL1's level | lines that do not express GNAI1 (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without GNAI1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: ENSG00000250158, KLF12, ELL2 |
| [[C13orf46]] | B | GNAI1 activity raises C13orf46's level | lines that do not express GNAI1 (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without GNAI1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: ENSG00000250158, KLF12, ELL2 |

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.0, -5.4); signed map (17.8, 23.0). **Vector** length 112, 29.3% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.3 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.7 | -4.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | -0.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | +0.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit alpha i1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:79,768,028-80,226,181 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits alpha, group i |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, CHOLESTEROL_HOMEOSTASIS, APICAL_JUNCTION |
| Reactome | 30 pathways, smallest: Adenylate cyclase inhibitory pathway; ADP signalling through P2Y purinoceptor 12; Adrenaline,noradrenaline inhibits insulin secretion |
| Matched by | ensembl_id |

**Function**, from UniProt [P63096](https://www.uniprot.org/uniprotkb/P63096) (Guanine nucleotide-binding protein G(i) subunit alpha-1):

> Guanine nucleotide-binding proteins (G proteins) function as transducers downstream of G protein-coupled receptors (GPCRs) in numerous signaling cascades. The alpha chain contains the guanine nucleotide binding site and alternates between an active, GTP-bound state and an inactive, GDP-bound state. Signaling by an activated GPCR promotes GDP release and GTP binding. The alpha subunit has a low GTPase activity that converts bound GTP to GDP, thereby terminating the signal. Both GDP release and …

**Summary**, from NCBI Gene [2770](https://www.ncbi.nlm.nih.gov/gene/2770):

> Guanine nucleotide binding proteins are heterotrimeric signal-transducing molecules consisting of alpha, beta, and gamma subunits. The alpha subunit binds guanine nucleotide, can hydrolyze GTP, and can interact with other proteins. The protein encoded by this gene represents the alpha subunit of an inhibitory complex. The encoded protein is part of a complex that responds to beta-adrenergic signals by inhibiting adenylate cyclase. Two transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:4384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4384) · Entrez [2770](https://www.ncbi.nlm.nih.gov/gene/2770) · UniProt [P63096](https://www.uniprot.org/uniprotkb/P63096) · Ensembl [ENSG00000127955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127955)

## Data

Gene col 4849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4849); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4849]; `tensor/DDL_lfc|DDL_z.npy` [4849]; `embed/gene_vectors.npy` [4849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4849 or target_col == 4849). Every well: [[GNAI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
