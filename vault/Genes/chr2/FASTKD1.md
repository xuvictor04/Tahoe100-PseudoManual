---
symbol: "FASTKD1"
type: "gene"
col: 6170
ensembl_id: "ENSG00000138399"
name: "FASTK mitochondrial RNA regulator 1"
location: "2q31.1"
module: 105
arm: "+"
pooled_cpm: 49.72
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# FASTKD1

*FASTK mitochondrial RNA regulator 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +15.6, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.662× (z -13.9, q 6e-41, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLMN]] (+0.62, fdr 1e-05), [[INTS9]] (+0.62, fdr 1e-05), [[PRDX4]] (+0.56, fdr 1e-05); moves opposite to [[BCL7B]] (-0.59, fdr 1e-05), [[SRSF3]] (-0.54, fdr 1e-05), [[ANXA7]] (-0.53, fdr 3e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +15.6 | 0e+00 | 41/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +10.0 | 6e-21 | 37/48 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.34×** | +6.9 | 1e-09 | 26/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.72×** | +6.8 | 2e-09 | 29/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +6.2 | 8e-08 | 26/48 (A498, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.20× | +6.1 | 9e-08 | 23/48 (AsPC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.9 | 4e-07 | 20/48 (A498, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.27×** | +5.7 | 6e-07 | 23/47 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 6e-06 | 22/48 (LOX-IMVI, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.26×** | +5.2 | 1e-05 | 22/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 1e-05 | 24/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +4.8 | 6e-05 | 20/48 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +4.8 | 7e-05 | 17/48 (LOX-IMVI, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +4.8 | 7e-05 | 23/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.46×** | +4.7 | 8e-05 | 16/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 1e-04 | 18/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 2e-04 | 17/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 8e-04 | 16/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.004 | 9/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.011 | 14/46 (Hs 766T, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.662×** | -13.9 | 6e-41 | 36/47 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -12.0 | 7e-31 | 36/45 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -10.5 | 1e-23 | 28/48 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -10.2 | 5e-22 | 31/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -8.4 | 5e-15 | 34/49 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.716×** | -7.6 | 2e-12 | 30/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -7.5 | 7e-12 | 23/42 (Panc 03.27, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -6.6 | 3e-09 | 28/48 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -6.5 | 4e-09 | 0/49 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.776×** | -6.0 | 9e-08 | 23/47 (PANC-1, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | **0.820×** | -4.7 | 1e-04 | 22/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.814×** | -4.7 | 1e-04 | 20/47 (A-427, SNU-423, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.845× | -4.0 | 0.003 | 14/47 (SNU-423, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.860× | -3.6 | 0.013 | 13/48 (A-427, C-33 A, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.906× | -3.3 | 0.033 | 8/49 (Hs 766T, SW 900, …) | top dose only |  |
| [[Penfluridol (drug)]] 5 µM |  | 0.871× | -3.2 | 0.058 | 14/47 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 102 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.483× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 58.3 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +15.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.373× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 64.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.5) |
| [[A-172 (line)]] | wt | 47.0 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.9) |
| [[LoVo (line)]] | wt | 64.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 54.2 | 0 | 3 | — | [[TAK-901 (drug)]] 5 µM 0.0894× (z -13.2) |
| [[A498 (line)]] | wt | 17.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +12.8) | — |
| [[HCT15 (line)]] | alt | 81.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 53.4 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.51× (z +9.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 56.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 57.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.5) |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.267× (z -9.9) |
| [[SW48 (line)]] | wt | 48.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -12.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 78.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -22.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -17.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 57.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.387× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.2) |
| [[H4 (line)]] | wt | 65.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 44.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 39.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.9) |
| [[J82 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 80.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.1) |
| [[NCI-H661 (line)]] | alt | 45.7 | 0 | 1 | — | [[MK-3903 (drug)]] 0.05 µM 0.0898× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -14.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 46.3 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0719× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 93.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0517× (z -15.1) |
| [[SW 900 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLMN]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[INTS9]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[PRDX4]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FNTB]] | +0.55 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[PRKRIP1]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZNF143]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[TM2D1]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[POM121C]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[POM121]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[KYAT1]] | +0.53 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.53 | +0.40 / +0.54 | both halves | 5e-05 | STRING 465 |
| [[TMEM41A]] | +0.53 | +0.35 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL7B]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ANXA7]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[PLEKHA3]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[MYO1C]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DBNL]] | -0.51 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PNPLA2]] | -0.51 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[NELFE]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[FLII]] | -0.51 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[WDR1]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ACTR3]] | -0.50 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.9, -8.2); signed map (-42.2, -21.2). **Vector** length 114, 28.6% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +10.0 |
|  | [[EX229 (drug)]] 5 µM |  | +5.7 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | +5.5 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.4 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +5.3 | +6.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +5.0 | +5.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.6 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.5 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | FASTK mitochondrial RNA regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,528,508-169,573,875 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21901 |
| Gene groups (HGNC) | FASTK mitochondrial RNA binding family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53R41](https://www.uniprot.org/uniprotkb/Q53R41) (FAST kinase domain-containing protein 1, mitochondrial):

> Involved in the down-regulation of mitochondrial MT-ND3 mRNA levels which leads to decreased respiratory complex I abundance and activity.

**Summary**, from NCBI Gene [79675](https://www.ncbi.nlm.nih.gov/gene/79675):

> Enables RNA binding activity. Involved in mitochondrial RNA metabolic process and regulation of mitochondrial mRNA stability. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26150) · Entrez [79675](https://www.ncbi.nlm.nih.gov/gene/79675) · UniProt [Q53R41](https://www.uniprot.org/uniprotkb/Q53R41) · Ensembl [ENSG00000138399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138399)

## Data

Gene col 6170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6170); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6170]; `tensor/DDL_lfc|DDL_z.npy` [6170]; `embed/gene_vectors.npy` [6170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6170 or target_col == 6170). Every well: [[FASTKD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FASTKD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
