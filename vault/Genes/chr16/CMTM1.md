---
symbol: "CMTM1"
type: "gene"
col: 1590
ensembl_id: "ENSG00000089505"
name: "CKLF like MARVEL transmembrane domain containing 1"
location: "16q21"
module: 6
arm: "+"
pooled_cpm: 11.99
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CMTM1

*CKLF like MARVEL transmembrane domain containing 1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.15× (z +13.7, q 3e-40, up in 15 of 19 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +5.9, q 3e-07, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.300× (z -21.2, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CKLF]] (+0.71, fdr 7e-06, ⚠ same locus), [[AP3M2]] (+0.67, fdr 1e-05), [[BRI3BP]] (+0.59, fdr 1e-05), [[RNF168]] (+0.59, fdr 1e-05); moves opposite to [[MMP25-AS1]] (-0.54, fdr 1e-04), [[TBC1D22B]] (-0.52, fdr 5e-05), [[CLIP1]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.15×** | +13.7 | 3e-40 | 15/19 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.63×** | +12.0 | 7e-31 | 27/33 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.74×** | +6.9 | 1e-09 | 27/46 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.70×** | +6.1 | 2e-07 | 14/26 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.9 | 3e-07 | 22/46 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.54×** | +5.4 | 8e-06 | 21/46 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.53×** | +5.3 | 9e-06 | 25/47 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +4.9 | 6e-05 | 20/47 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.47×** | +4.6 | 3e-04 | 18/46 (LoVo, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.6 | 3e-04 | 18/39 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.86×** | +4.1 | 0.003 | 11/45 (NCI-H2030, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.011 | 14/44 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.017 | 13/47 (NCI-H2030, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.32×** | +3.4 | 0.027 | 14/47 (A498, HT-29, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.4 | 0.029 | 11/44 (NCI-H460, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.300×** | -21.2 | 0e+00 | 42/44 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -9.2 | 9e-18 | 27/43 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.330×** | -7.2 | 9e-11 | 30/47 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.352×** | -6.8 | 1e-09 | 27/42 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.587×** | -6.6 | 4e-09 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.600×** | -6.1 | 8e-08 | 28/46 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.623×** | -6.0 | 1e-07 | 26/47 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.671×** | -4.7 | 2e-04 | 21/44 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.694×** | -4.6 | 3e-04 | 16/47 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -4.4 | 7e-04 | 19/44 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.762×** | -4.2 | 0.001 | 20/46 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.737×** | -4.1 | 0.002 | 17/47 (COLO 205, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.713×** | -4.1 | 0.002 | 18/45 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -3.7 | 0.010 | 17/46 (AN3 CA, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.579×** | -3.6 | 0.014 | 10/46 (AsPC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.761×** | -3.4 | 0.021 | 16/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.8 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.7) |
| [[SW480 (line)]] | alt | 23.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.0796× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0219× (z -21.2) |
| [[NCI-H460 (line)]] | wt | 9.11 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.0) |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 25.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.8) |
| [[HOP62 (line)]] | alt | 9.27 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 5.18 | 0 | 2 | — | [[Bendamustine (drug)]] 5 µM 0.0659× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 21.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -13.3) |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0969× (z -9.5) |
| [[A549 (line)]] | wt | 5.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -10.8) |
| [[BT-474 (line)]] | alt | 6.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -19.6) |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.4) |
| [[KATO III (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -19.3) |
| [[LoVo (line)]] | wt | 6.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.2) |
| [[LS 180 (line)]] | wt | 5.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.2) |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.3) |
| [[RKO (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 9.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.3) |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0816× (z -8.9) |
| [[SW48 (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.7) |
| [[A-172 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CKLF]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | STRING 440; ⚠ same locus (0.1 kb, same strand: neighbours can correlate without regulation) |
| [[AP3M2]] | +0.67 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[BRI3BP]] | +0.59 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[RNF168]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[FANCB]] | +0.59 | +0.65 / +0.37 | both halves | 7e-05 |  |
| [[RTTN]] | +0.58 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[DSCC1]] | +0.58 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[CDCA7]] | +0.57 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[HPCAL1]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CENPK]] | +0.57 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[ERI1]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[RFC5]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[GGCT]] | +0.56 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP25-AS1]] | -0.54 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[TBC1D22B]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CLIP1]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[C11orf71]] | -0.51 | -0.55 / -0.22 | both halves | 6e-04 |  |
| [[LINC02951]] | -0.51 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[PEF1]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[CIRBP]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[MYL5]] | -0.50 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[HOMEZ]] | -0.48 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[U2AF1L4]] | -0.48 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[CLIP3]] | -0.48 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[SMDT1]] | -0.48 | -0.51 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CMTM1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[VSIG1]] | B | VSIG1 activity strengthens CMTM1's drug response | lines that do not express VSIG1 (33) vs lines expressing it (14) | the lines without VSIG1 respond 0.68× as strongly (z diff +0.97); strongest at Harringtonine 5 µM: 0.59x vs 0.37x (z diff +2.5) | 0.090 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-30.2, -44.3); signed map (-41.3, -10.3). **Vector** length 80.6, 15.6% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.0 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +4.0 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.6 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -21.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.7 | -6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -9.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | CKLF like MARVEL transmembrane domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:66,566,393-66,579,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CKLFH1a, CKLFH; previously CKLFSF1 |
| Gene groups (HGNC) | CKLF like MARVEL transmembrane domain containing |
| Matched by | ensembl_id |

UniProt [Q8IZ96](https://www.uniprot.org/uniprotkb/Q8IZ96) carries no function annotation.

**Summary**, from NCBI Gene [113540](https://www.ncbi.nlm.nih.gov/gene/113540):

> This gene belongs to the chemokine-like factor gene superfamily, a novel family that is similar to the chemokine and the transmembrane 4 superfamilies of signaling molecules. The protein encoded by this gene may play an important role in testicular development. Alternatively spliced transcript variants encoding different isoforms have been identified. Naturally occurring read-through transcription occurs between this locus and the neighboring locus CKLF (chemokine-like factor).[provided by …

**Accessions** — [HGNC:19172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19172) · Entrez [113540](https://www.ncbi.nlm.nih.gov/gene/113540) · UniProt [Q8IZ96](https://www.uniprot.org/uniprotkb/Q8IZ96) · Ensembl [ENSG00000089505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089505)

## Data

Gene col 1590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1590); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1590]; `tensor/DDL_lfc|DDL_z.npy` [1590]; `embed/gene_vectors.npy` [1590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1590 or target_col == 1590). Every well: [[CMTM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMTM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
