---
symbol: "KLHL9"
type: "gene"
col: 12632
ensembl_id: "ENSG00000198642"
name: "kelch like family member 9"
location: "9p21.3"
module: 16
arm: "+"
pooled_cpm: 26.74
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# KLHL9

*kelch like family member 9* — 9p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.80× (z +12.7, q 2e-34, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.402× (z -28.1, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF22]] (+0.81, fdr 7e-06), [[MSL3P1]] (+0.79, fdr 7e-06), [[AGGF1]] (+0.78, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +12.7 | 2e-34 | 40/45 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +11.5 | 2e-28 | 35/44 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +9.1 | 1e-17 | 29/45 (A-427, SNU-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +9.1 | 2e-17 | 31/45 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.31×** | +8.3 | 9e-15 | 25/44 (KATO III, A498, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +7.4 | 2e-11 | 27/45 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +5.8 | 7e-07 | 21/45 (A-427, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.5 | 3e-06 | 20/43 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.005 | 14/44 (RKO, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.33×** | +3.3 | 0.059 | 6/43 (A498, SK-MEL-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.059 | 8/45 (SNU-423, hTERT-HPNE, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12632.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.402×** | -28.1 | 0e+00 | 43/45 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.449×** | -17.5 | 0e+00 | 35/41 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.533×** | -13.2 | 2e-37 | 35/44 (Panc 03.27, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -10.9 | 1e-25 | 31/45 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -10.8 | 5e-25 | 23/33 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -7.5 | 6e-12 | 23/44 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.727×** | -7.0 | 3e-10 | 20/45 (A-172, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.729×** | -6.3 | 2e-08 | 18/37 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.773×** | -5.6 | 1e-06 | 22/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.798×** | -4.9 | 4e-05 | 19/45 (A-172, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.790×** | -4.9 | 6e-05 | 18/45 (J82, HEC-1-A, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.809×** | -4.6 | 2e-04 | 17/45 (HepG2/C3A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.808×** | -4.5 | 3e-04 | 23/44 (NCI-H23, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.689×** | -4.2 | 9e-04 | 17/40 (Panc 03.27, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.823×** | -4.2 | 9e-04 | 13/44 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.776×** | -4.0 | 0.003 | 8/45 (J82, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.863× | -3.2 | 0.043 | 8/45 (Panc 03.27, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 43.6 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -24.2) |
| [[A549 (line)]] | wt | 37.3 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -17.2) |
| [[KATO III (line)]] | alt | 41.8 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +12.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.1) |
| [[A498 (line)]] | wt | 42.2 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.1) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -18.3) |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -18.0) |
| [[C32 (line)]] | wt | 27.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0681× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 31.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 43.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -20.5) |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0455× (z -21.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.6) |
| [[SW480 (line)]] | alt | 25.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -14.7) |
| [[CHP-212 (line)]] | wt | 37.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -10.6) |
| [[HS-578T (line)]] | alt | 26.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.9) |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -14.1) |
| [[LoVo (line)]] | wt | 43.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -14.9) |
| [[RKO (line)]] | wt | 35.1 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -11.7) |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.3) |
| [[SW48 (line)]] | wt | 32.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -11.1) |
| [[A-427 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -13.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -9.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.1) |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -13.1) |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -14.3) |
| [[J82 (line)]] | alt | 41.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -19.3) |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 25.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.7) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -15.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -13.5) |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF22]] | +0.81 | +0.72 / +0.83 | both halves | 7e-06 |  |
| [[MSL3P1]] | +0.79 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.78 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 914 |
| [[MRFAP1L1]] | +0.75 | +0.61 / +0.79 | both halves | 7e-06 |  |
| [[RTL6]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[PHAX]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.71 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.70 | +0.61 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KLHL9's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | KLHL9 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.63× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |
| [[RBAK]] | C | KLHL9 activity lowers RBAK's level | lines that do not express KLHL9 (3) vs lines expressing it (47) | 2.00× higher at baseline in the lines without KLHL9 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |
| cells under [[Daptomycin (drug)]] 0.5 µM | C | KLHL9 activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.58× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1; cell counts less trustworthy |
| cells under [[Peretinoin (drug)]] 5 µM | C | KLHL9 activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.70× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |
| cells under [[Gallic acid (drug)]] 0.05 µM | C | KLHL9 activity raises the cells' numbers under Gallic acid 0.05 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.63× the cells of the other lines | 0.079 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |
| [[TBL2]] | C | KLHL9 activity lowers TBL2's level | lines that do not express KLHL9 (3) vs lines expressing it (47) | 1.64× higher at baseline in the lines without KLHL9 | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |
| [[ZNF23]] | C | KLHL9 activity lowers ZNF23's level | lines that do not express KLHL9 (3) vs lines expressing it (47) | 1.75× higher at baseline in the lines without KLHL9 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |
| [[PCGF2]] | C | KLHL9 activity strengthens PCGF2's drug response | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9 respond 0.43× as strongly (z diff +1.59); strongest at Homoharringtonine 5 µM: 0.80x vs 0.49x (z diff +5.7) | 0.089 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1; target measured in part of the lines; artifact flags |
| cells under [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | C | KLHL9 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.71× the cells of the other lines | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.0, 10.4); signed map (0.1, -28.0). **Vector** length 102, 23.1% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.8 | +12.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +5.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | -0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -28.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -13.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.1 | -17.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -10.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.3 — chr9:21,329,665-21,335,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1354, FLJ13568 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2J3](https://www.uniprot.org/uniprotkb/Q9P2J3) (Kelch-like protein 9):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex required for mitotic progression and cytokinesis. The BCR(KLHL9-KLHL13) E3 ubiquitin ligase complex mediates the ubiquitination of AURKB and controls the dynamic behavior of AURKB on mitotic chromosomes and thereby coordinates faithful mitotic progression and completion of cytokinesis.

**Summary**, from NCBI Gene [55958](https://www.ncbi.nlm.nih.gov/gene/55958):

> This gene encodes a protein that belongs to the kelch repeat-containing family, and contains an N-terminal BTB/POZ domain, a BACK domain and six C-terminal kelch repeats. The encoded protein is a component of a complex with cullin 3-based E3 ligase, which plays a role in mitosis. This protein complex is a cell cycle regulator, and functions in the organization and integrity of the spindle midzone in anaphase and the completion of cytokinesis. The complex is required for the removal of the …

**Accessions** — [HGNC:18732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18732) · Entrez [55958](https://www.ncbi.nlm.nih.gov/gene/55958) · UniProt [Q9P2J3](https://www.uniprot.org/uniprotkb/Q9P2J3) · Ensembl [ENSG00000198642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198642)

## Data

Gene col 12632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12632); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12632]; `tensor/DDL_lfc|DDL_z.npy` [12632]; `embed/gene_vectors.npy` [12632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12632 or target_col == 12632). Every well: [[KLHL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
