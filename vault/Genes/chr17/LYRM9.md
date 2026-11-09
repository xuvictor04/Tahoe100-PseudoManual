---
symbol: "LYRM9"
type: "gene"
col: 13870
ensembl_id: "ENSG00000232859"
name: "LYR motif containing 9"
location: "17q11.2"
module: 28
arm: "+"
pooled_cpm: 4.92
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# LYRM9

*LYR motif containing 9* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.57× (z +4.5, q 0.004, up in 10 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.220× (z -15.0, q 0e+00, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BPHL]] (+0.62, fdr 1e-05), [[KCTD18]] (+0.59, fdr 7e-06), [[WDR31]] (+0.59, fdr 1e-05); moves opposite to [[SYS1-DBNDD2]] (-0.51, fdr 2e-05), [[LRP8]] (-0.48, fdr 2e-05), [[PRDX1]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RDM1P5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13870.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.57×** | +4.5 | 0.004 | 10/43 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.004 | 12/41 (NCI-H1573, KATO III, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.007 | 11/41 (SW480, SW1417, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.014 | 5/40 (C32, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.022 | 8/42 (KATO III, LS 180, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.026 | 10/42 (BT-474, A498, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.6 | 0.026 | 4/23 (NCI-H2030, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.026 | 6/42 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.42×** | +3.5 | 0.026 | 13/41 (A-172, A498, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +3.5 | 0.026 | 7/26 (C-33 A, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.3 | 0.052 | 4/16 (KATO III, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.062 | 7/43 (SW480, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.067 | 2/30 (SW480, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.10 | 5/41 (A-427, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.220×** | -15.0 | 0e+00 | 38/45 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.301×** | -11.9 | 3e-30 | 36/42 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.310×** | -11.6 | 5e-29 | 36/42 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.332×** | -11.0 | 9e-26 | 36/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.371×** | -9.8 | 9e-21 | 26/33 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.541×** | -8.6 | 7e-16 | 23/36 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.421×** | -8.2 | 1e-14 | 20/28 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.451×** | -7.9 | 2e-13 | 25/41 (HOP62, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.456×** | -7.8 | 4e-13 | 27/41 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.462×** | -7.7 | 1e-12 | 25/43 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.488×** | -7.1 | 6e-11 | 27/44 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.255×** | -7.1 | 6e-11 | 24/32 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.469×** | -7.0 | 1e-10 | 24/38 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.265×** | -6.9 | 2e-10 | 26/37 (MIA PaCa-2, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.571×** | -5.5 | 1e-06 | 19/37 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.424×** | -4.5 | 3e-04 | 12/32 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.559×** | -4.1 | 0.001 | 5/45 (PANC-1, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.771×** | -3.6 | 0.008 | 13/42 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.009 | 13/44 (SHP-77, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | **0.701×** | -3.5 | 0.010 | 8/46 (NCI-H460, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.64 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0435× (z -14.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.111× (z -10.3) |
| [[PANC-1 (line)]] | alt | 4.11 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0824× (z -15.9) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0816× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 9.15 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.111× (z -10.2) |
| [[SW480 (line)]] | alt | 4.88 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -10.3) |
| [[HOP62 (line)]] | alt | 5.54 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0342× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 7.31 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -12.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H23 (line)]] | alt | 9.08 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.0873× (z -10.3) |
| [[A-427 (line)]] | wt | 10.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -11.2) ⚠ toxic |
| [[A549 (line)]] | wt | 6.98 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -13.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[LoVo (line)]] | wt | 3.73 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0518× (z -10.6) ⚠ toxic · without an alert: [[Belinostat (drug)]] 0.5 µM 0.104× (z -8.5) |
| [[A-172 (line)]] | wt | 8.96 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -9.3) ⚠ toxic |
| [[A498 (line)]] | wt | 4.53 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -11.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HCT15 (line)]] | alt | 6.07 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0283× (z -11.2) |
| [[Hs 766T (line)]] | wt | 2.14 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0341× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 4.91 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0803× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 6.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0852× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0573× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 6.55 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0681× (z -10.6) |
| [[RKO (line)]] | wt | 4.42 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.05 µM 0.0523× (z -9.0) |
| [[SNU-423 (line)]] | alt | 4.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0774× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[SW1417 (line)]] | alt | 7.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.118× (z -9.1) |
| [[AN3 CA (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPHL]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[WDR31]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TTC12]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[KLHL12]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[ADAMTS13]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SIRT3]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ERMARD]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[TMEM9B-AS1]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DHFR2]] | +0.55 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[DCP1B]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RAD52]] | +0.54 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYS1-DBNDD2]] | -0.51 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[LRP8]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PRDX1]] | -0.47 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[EHBP1]] | -0.47 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[UTP11]] | -0.47 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[SFXN5]] | -0.46 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[SNRPA]] | -0.46 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[PIP5KL1]] | -0.45 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[ASPH]] | -0.44 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GLA]] | -0.44 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | RDM1P5 activity raises LYRM9's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without RDM1P5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.3, 22.1); signed map (16.9, -41.9). **Vector** length 61.2, 9.69% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +4.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -11.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.2 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | LYR motif containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:27,878,314-27,894,752 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSD24; previously C17orf108 |
| Gene groups (HGNC) | LYR motif containing |
| Matched by | ensembl_id |

UniProt [A8MSI8](https://www.uniprot.org/uniprotkb/A8MSI8) carries no function annotation.

**Summary**, from NCBI Gene [201229](https://www.ncbi.nlm.nih.gov/gene/201229):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27314) · Entrez [201229](https://www.ncbi.nlm.nih.gov/gene/201229) · UniProt [A8MSI8](https://www.uniprot.org/uniprotkb/A8MSI8) · Ensembl [ENSG00000232859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232859)

## Data

Gene col 13870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13870); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13870]; `tensor/DDL_lfc|DDL_z.npy` [13870]; `embed/gene_vectors.npy` [13870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13870 or target_col == 13870). Every well: [[LYRM9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYRM9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
