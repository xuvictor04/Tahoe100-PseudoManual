---
symbol: "PAXIP1-AS2"
type: "gene"
col: 13172
ensembl_id: "ENSG00000214106"
name: "PAXIP1 antisense RNA 2"
location: "7q36.2"
module: 68
arm: "+"
pooled_cpm: 10.45
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 25
n_dd_up_clean: 22
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# PAXIP1-AS2

*PAXIP1 antisense RNA 2* — 7q36.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.80× (z +7.6, q 2e-11, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.486× (z -9.7, q 2e-19, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL2]] (+0.71, fdr 1e-05), [[TAPBPL]] (+0.71, fdr 1e-05), [[C7orf31]] (+0.70, fdr 1e-05); moves opposite to [[GNB1L]] (-0.65, fdr 1e-05), [[LPCAT4]] (-0.62, fdr 3e-05), [[TCF3]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02328]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Folic acid (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.80×** | +7.6 | 2e-11 | 25/44 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +5.6 | 5e-06 | 19/47 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +5.5 | 6e-06 | 22/45 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.2 | 4e-05 | 17/44 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +5.0 | 6e-05 | 18/46 (RKO, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.45×** | +4.8 | 1e-04 | 17/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 5e-04 | 16/45 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 0.001 | 12/46 (Hs 766T, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.37×** | +4.3 | 0.001 | 16/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 11/46 (NCI-H23, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.001 | 9/46 (PANC-1, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.002 | 15/45 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 15/46 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.003 | 15/45 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.005 | 11/46 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.005 | 8/46 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.005 | 11/45 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.486×** | -9.7 | 2e-19 | 31/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.468×** | -8.9 | 1e-16 | 31/46 (PANC-1, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.514×** | -8.7 | 5e-16 | 33/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -8.1 | 1e-13 | 29/44 (COLO 205, PANC-1, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.349×** | -7.4 | 2e-11 | 24/44 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.595×** | -7.0 | 3e-10 | 25/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.400×** | -6.4 | 1e-08 | 23/46 (SK-MEL-2, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.632×** | -5.9 | 2e-07 | 22/38 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.640×** | -5.6 | 1e-06 | 20/45 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.660×** | -5.6 | 1e-06 | 20/46 (COLO 205, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.689×** | -5.0 | 3e-05 | 20/46 (CHP-212, H4, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.660×** | -4.9 | 5e-05 | 18/45 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.552×** | -4.2 | 0.001 | 16/43 (HOP62, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.568×** | -4.0 | 0.003 | 17/33 (C-33 A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -3.8 | 0.006 | 15/46 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.760×** | -3.7 | 0.008 | 6/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.618×** | -3.4 | 0.023 | 13/45 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.838× | -3.3 | 0.023 | 11/46 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.695×** | -3.3 | 0.023 | 12/46 (MIA PaCa-2, HT-29, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.621×** | -3.3 | 0.023 | 11/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.633×** | -3.2 | 0.033 | 14/44 (NCI-H1792, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.212× (z -11.5) |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0671× (z -13.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +10.3) ⚠ position not correctable | [[Ixazomib citrate (drug)]] 5 µM 0.0951× (z -13.5) |
| [[A-172 (line)]] | wt | 11.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 13.7 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +8.8) ⚠ position not correctable | [[Auranofin (drug)]] 5 µM 0.163× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 9.15 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0444× (z -10.2) |
| [[HS-578T (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.75× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 7.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +9.9) | — |
| [[J82 (line)]] | alt | 6.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +15.5) | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 1 | — | [[Methyl aminolevulinate (hydrochloride) (drug)]] 0.05 µM 0.0977× (z -8.5) |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | +0.71 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.71 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[C7orf31]] | +0.70 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.69 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[RBM43]] | +0.69 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[FAM111A-DT]] | +0.68 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.67 | +0.75 / +0.41 | both halves | 4e-05 |  |
| [[BAZ2B]] | +0.67 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[IFNAR1]] | +0.66 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[FAM200B]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.66 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZXDA]] | +0.65 | +0.63 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.65 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.62 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[TCF3]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[ZMYND19]] | -0.60 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[WDR5]] | -0.60 | -0.66 / -0.39 | both halves | 6e-05 |  |
| [[GBA2]] | -0.60 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LPCAT1]] | -0.60 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[TPST2]] | -0.59 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ST6GALNAC4]] | -0.59 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[WASF3]] | -0.59 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[IQSEC1]] | -0.58 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[BCR]] | -0.58 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02328]] | B | LINC02328 activity raises PAXIP1-AS2's level | lines that do not express LINC02328 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without LINC02328 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, PDE4B; maybe low, not absent |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises PAXIP1-AS2's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without PLS3-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PAXIP1-AS2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[RBM43]] | C | RBM43 activity raises PAXIP1-AS2's level | lines that do not express RBM43 (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without RBM43 | 0.028 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALPK1, RNASEL, TFAP2A |
| [[NMI]] | C | NMI activity raises PAXIP1-AS2's level | lines that do not express NMI (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without NMI | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NABP1, LGI4, C21orf91 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Folic acid (drug)]] 5 µM | C | PAXIP1-AS2's natural level lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | PAXIP1-AS2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (19.6, 5.8); signed map (20.1, -14.6). **Vector** length 80.3, 15.9% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +3.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +3.1 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.3 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -4.0 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -3.8 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PAXIP1 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q36.2 — chr7:154,928,460-154,952,188 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously PAXIP1OS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48958) · Entrez [100132707](https://www.ncbi.nlm.nih.gov/gene/100132707) · Ensembl [ENSG00000214106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214106)

## Data

Gene col 13172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13172); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13172]; `tensor/DDL_lfc|DDL_z.npy` [13172]; `embed/gene_vectors.npy` [13172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13172 or target_col == 13172). Every well: [[PAXIP1-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAXIP1-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
