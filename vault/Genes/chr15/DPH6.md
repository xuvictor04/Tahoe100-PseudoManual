---
symbol: "DPH6"
type: "gene"
col: 5516
ensembl_id: "ENSG00000134146"
name: "diphthamine biosynthesis 6"
location: "15q14"
module: 4
arm: "+"
pooled_cpm: 47.35
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 31
n_dd_up_clean: 11
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DPH6

*diphthamine biosynthesis 6* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 2.06× (z +8.0, q 6e-13, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.197× (z -26.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSEN2]] (+0.77, fdr 7e-06), [[DIS3L2]] (+0.75, fdr 7e-06), [[DDX10]] (+0.73, fdr 7e-06); moves opposite to [[KLC4]] (-0.63, fdr 8e-06), [[LASP1]] (-0.60, fdr 1e-05), [[MINDY2]] (-0.59, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TTC28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **2.06×** | +8.0 | 6e-13 | 41/47 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.58×** | +4.5 | 0.002 | 28/47 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.005 | 25/48 (C-33 A, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.8 | 0.020 | 23/48 (HT-29, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.027 | 21/47 (A549, PANC-1, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.048 | 21/48 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.048 | 17/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.057 | 19/48 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.065 | 17/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.075 | 20/48 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.075 | 14/47 (NCI-H2347, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +3.2 | 0.075 | 18/45 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.096 | 11/48 (CFPAC-1, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.197×** | -26.6 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.238×** | -16.6 | 0e+00 | 46/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.289×** | -14.3 | 2e-44 | 43/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.456×** | -12.8 | 1e-35 | 43/48 (CHP-212, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.341×** | -12.0 | 7e-31 | 43/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.378×** | -11.2 | 3e-27 | 42/47 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.405×** | -10.4 | 1e-23 | 37/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.406×** | -10.4 | 2e-23 | 42/47 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.486×** | -8.3 | 5e-15 | 35/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.278×** | -7.7 | 6e-13 | 42/49 (C-33 A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.559×** | -6.7 | 9e-10 | 31/47 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.591×** | -5.8 | 3e-07 | 31/47 (NCI-H23, SNU-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.383×** | -5.8 | 3e-07 | 30/47 (SNU-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -5.7 | 5e-07 | 32/47 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.604×** | -5.5 | 2e-06 | 29/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.4 | 2e-06 | 32/48 (HEC-1-A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -5.1 | 1e-05 | 29/48 (C-33 A, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -4.6 | 1e-04 | 27/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 79.5 | 0 | 14 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0359× (z -20.1) |
| [[A-427 (line)]] | wt | 52.9 | 0 | 12 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -15.6) |
| [[PANC-1 (line)]] | alt | 62.3 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -30.0) |
| [[NCI-H23 (line)]] | alt | 79.1 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.0) |
| [[C-33 A (line)]] | alt | 79.9 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0898× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -13.9) |
| [[CHP-212 (line)]] | wt | 747 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -21.1) |
| [[HEC-1-A (line)]] | alt | 85.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.3) |
| [[MIA PaCa-2 (line)]] | alt | 142 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0437× (z -24.9) |
| [[LoVo (line)]] | wt | 37.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.9) |
| [[SW1417 (line)]] | alt | 36.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.4) |
| [[SW480 (line)]] | alt | 31.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -18.6) |
| [[BT-474 (line)]] | alt | 58.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -17.2) |
| [[C32 (line)]] | wt | 51.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -16.8) |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -17.4) |
| [[J82 (line)]] | alt | 35.9 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 49.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -20.1) |
| [[NCI-H1573 (line)]] | alt | 102 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -25.1) |
| [[RKO (line)]] | wt | 49.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -12.4) |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.8) |
| [[COLO 205 (line)]] | alt | 47.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -13.4) |
| [[LS 180 (line)]] | wt | 45.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 38.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -18.4) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0861× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.194× (z -9.2) |
| [[HT-29 (line)]] | alt | 33.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0575× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.8) |
| [[KATO III (line)]] | alt | 40.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.0) |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.0) |
| [[A498 (line)]] | wt | 31.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -21.2) |
| [[A549 (line)]] | wt | 24.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.1) |
| [[H4 (line)]] | wt | 27.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 63.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 36.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -15.8) |
| [[A-172 (line)]] | wt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.4) |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.9) |
| [[SK-MEL-2 (line)]] | alt | 38.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.6) |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.7) |
| [[SW48 (line)]] | wt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSEN2]] | +0.77 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.75 | +0.65 / +0.81 | both halves | 7e-06 | same gene group |
| [[DDX10]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[NAA15]] | +0.73 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[STX18-AS1]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[METAP1D]] | +0.70 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[MDN1]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[FKTN]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[NAA25]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC4]] | -0.63 | -0.60 / -0.57 | both halves | 8e-06 |  |
| [[LASP1]] | -0.60 | -0.55 / -0.64 | both halves | 1e-05 | same gene group |
| [[MINDY2]] | -0.59 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.58 | -0.41 / -0.59 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity raises DPH6's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.38× lower at baseline in the lines without TTC28 | 0.073 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.4, -35.4); signed map (-8.6, -48.9). **Vector** length 95.3, 31.2% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8); *tRNA processing* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +6.6 | +8.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | -0.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -12.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -8.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | diphthamine biosynthesis 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:35,217,345-35,546,193 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14798; previously ATPBD4 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Diphthamide biosynthesis genes; Ligases |
| Reactome | 2 pathways, smallest: Synthesis of diphthamide-EEF2; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L8W6](https://www.uniprot.org/uniprotkb/Q7L8W6) (Diphthine--ammonia ligase):

> Amidase that may catalyze the last step of diphthamide biosynthesis using ammonium and ATP. Diphthamide biosynthesis consists in the conversion of an L-histidine residue in the translation elongation factor (EEF2) to diphthamide (By similarity).

**Summary**, from NCBI Gene [89978](https://www.ncbi.nlm.nih.gov/gene/89978):

> Enables diphthine-ammonia ligase activity. Predicted to be involved in protein histidyl modification to diphthamide. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30543) · Entrez [89978](https://www.ncbi.nlm.nih.gov/gene/89978) · UniProt [Q7L8W6](https://www.uniprot.org/uniprotkb/Q7L8W6) · Ensembl [ENSG00000134146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134146)

## Data

Gene col 5516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5516); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5516]; `tensor/DDL_lfc|DDL_z.npy` [5516]; `embed/gene_vectors.npy` [5516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5516 or target_col == 5516). Every well: [[DPH6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
