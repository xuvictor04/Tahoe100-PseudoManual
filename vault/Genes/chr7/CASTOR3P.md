---
symbol: "CASTOR3P"
type: "gene"
col: 14198
ensembl_id: "ENSG00000239521"
name: "CASTOR family member 3, pseudogene"
location: "7q22.1"
module: 3
arm: "+"
pooled_cpm: 17.48
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CASTOR3P

*CASTOR family member 3, pseudogene* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +13.5, q 1e-38, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.422× (z -12.3, q 6e-32, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARK4]] (+0.66, fdr 8e-06), [[CSNK1G2]] (+0.64, fdr 7e-06), [[ANKRD13D]] (+0.62, fdr 1e-05); moves opposite to [[HUS1]] (-0.59, fdr 1e-05), [[DDX1]] (-0.57, fdr 1e-05), [[GMFB]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GDAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +13.5 | 1e-38 | 40/47 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +9.6 | 2e-19 | 37/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +9.5 | 3e-19 | 35/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +9.3 | 3e-18 | 34/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +7.5 | 7e-12 | 30/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +6.8 | 1e-09 | 29/47 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.012 | 22/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.012 | 16/48 (C32, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.077 | 16/48 (CFPAC-1, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.422×** | -12.3 | 6e-32 | 35/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.570×** | -11.3 | 4e-27 | 34/47 (hTERT-HPNE, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.441×** | -11.2 | 6e-27 | 21/28 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.482×** | -10.4 | 3e-23 | 30/43 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.458×** | -10.3 | 8e-23 | 27/39 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -7.7 | 1e-12 | 32/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.649×** | -6.1 | 7e-08 | 24/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.667×** | -5.8 | 6e-07 | 27/46 (LS 180, SW48, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.781×** | -5.0 | 4e-05 | 23/48 (HEC-1-A, SW1417, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -5.0 | 4e-05 | 21/46 (C-33 A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.711×** | -4.7 | 2e-04 | 22/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.739×** | -4.3 | 8e-04 | 16/48 (HCT15, SW480, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.567×** | -4.2 | 0.001 | 12/24 (SNU-423, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -4.0 | 0.002 | 19/48 (PANC-1, H4, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **0.755×** | -4.0 | 0.002 | 20/43 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.794×** | -3.3 | 0.033 | 14/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.807×** | -3.0 | 0.059 | 12/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.807×** | -3.0 | 0.059 | 17/47 (PANC-1, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.071 | 15/47 (LoVo, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.0 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0851× (z -22.1) |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -11.7) |
| [[A-427 (line)]] | wt | 25.9 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -14.4) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -12.0) |
| [[A498 (line)]] | wt | 31.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0964× (z -18.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0933× (z -15.4) |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0913× (z -14.7) ⚠ toxic |
| [[C32 (line)]] | wt | 22.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0943× (z -18.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -13.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0874× (z -9.6) |
| [[LS 180 (line)]] | wt | 10.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.0562× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 9.63 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.7) | — |
| [[SW480 (line)]] | alt | 18.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0840× (z -19.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.115× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0592× (z -14.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -13.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -12.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0952× (z -9.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -8.8) |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0520× (z -22.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0993× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARK4]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[CSNK1G2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD13D]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TAF4]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[FOXK2]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TAF5]] | +0.61 | +0.43 / +0.60 | both halves | 4e-05 |  |
| [[SLC27A4]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[NFATC3]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[HIRA]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[GATD1-DT]] | +0.57 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUS1]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[DDX1]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[GMFB]] | -0.57 | -0.36 / -0.64 | both halves | 1e-04 |  |
| [[GDAP1]] | -0.55 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[ZNF772]] | -0.54 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ZNF780A]] | -0.53 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[ZSCAN12]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ARMT1]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[FUNDC1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[NBN]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[GUF1]] | -0.53 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[YTHDC2]] | -0.52 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDAP1]] | B | GDAP1 activity raises CASTOR3P's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without GDAP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers CASTOR3P's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CFL2]] | C | CFL2 activity raises CASTOR3P's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.68× lower at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.7, -4.1); signed map (-42.4, 1.3). **Vector** length 80.9, 16.5% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +13.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.5 | +9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +1.4 | -5.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.3 | +2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.2 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -7.1 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -11.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +0.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | CASTOR family member 3, pseudogene |
| Locus type | pseudogene |
| Location | 7q22.1 — chr7:100,222,597-100,271,983 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | DKFZp686B07267, STAG3OS; previously GATS, CASTOR3 |
| Matched by | ensembl_id |

UniProt [Q8NAP1](https://www.uniprot.org/uniprotkb/Q8NAP1) carries no function annotation.

**Summary**, from NCBI Gene [352954](https://www.ncbi.nlm.nih.gov/gene/352954):

> Predicted to be involved in cellular response to L-arginine and negative regulation of TORC1 signaling. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29954) · Entrez [352954](https://www.ncbi.nlm.nih.gov/gene/352954) · UniProt [Q8NAP1](https://www.uniprot.org/uniprotkb/Q8NAP1) · Ensembl [ENSG00000239521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239521)

## Data

Gene col 14198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14198); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14198]; `tensor/DDL_lfc|DDL_z.npy` [14198]; `embed/gene_vectors.npy` [14198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14198 or target_col == 14198). Every well: [[CASTOR3P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASTOR3P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
