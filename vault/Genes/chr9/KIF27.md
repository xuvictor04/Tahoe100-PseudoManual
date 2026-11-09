---
symbol: "KIF27"
type: "gene"
col: 9070
ensembl_id: "ENSG00000165115"
name: "kinesin family member 27"
location: "9q21.32"
module: 23
arm: "+"
pooled_cpm: 22.1
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# KIF27

*kinesin family member 27* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +12.2, q 2e-31, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.413× (z -6.6, q 3e-08, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (45 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 55 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2-AS1]] (+0.67, fdr 7e-04), [[ANKRD17-DT]] (+0.66, fdr 3e-04), [[RFX3-DT]] (+0.66, fdr 0.003, ⚠ one half only (not replicated)), [[ZCWPW1]] (+0.65, fdr 4e-05); moves opposite to [[ARRB2]] (-0.59, fdr 0.002, ⚠ one half only (not replicated)), [[CDK18]] (-0.58, fdr 4e-04), [[YIF1B]] (-0.58, fdr 1.00, ⚠ one half only (not replicated)), [[STARD3NL]] (-0.58, fdr 1e-04), [[GPR160]] (-0.57, fdr 6e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +12.2 | 2e-31 | 39/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 9e-05 | 27/46 (HOP62, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +4.6 | 9e-04 | 26/46 (A549, RKO, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.007 | 19/46 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.007 | 20/47 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.014 | 15/46 (A549, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.014 | 11/46 (NCI-H1792, LOX-IMVI, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.031 | 18/46 (NCI-H1792, NCI-H2347, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.075 | 16/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.080 | 13/47 (A549, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.26×** | +3.2 | 0.080 | 17/44 (HT-29, A-172, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.13 | 8/47 (A-172, LoVo, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.413×** | -6.6 | 3e-08 | 32/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -6.4 | 4e-08 | 34/46 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.681×** | -5.5 | 6e-06 | 24/46 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -5.5 | 6e-06 | 26/46 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.682×** | -5.4 | 6e-06 | 24/47 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -5.4 | 8e-06 | 22/46 (SW480, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -4.6 | 4e-04 | 23/46 (C-33 A, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -4.4 | 8e-04 | 16/47 (LS 180, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.766×** | -3.6 | 0.017 | 17/46 (LoVo, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.776×** | -3.6 | 0.018 | 17/46 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.781×** | -3.5 | 0.023 | 20/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.726×** | -3.3 | 0.054 | 9/47 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.791×** | -3.1 | 0.091 | 15/38 (HCT15, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.807×** | -3.1 | 0.091 | 15/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.2 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.326× (z -10.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Pemetrexed (drug)]] 5 µM 0.109× (z -8.9) |
| [[RKO (line)]] | wt | 17.7 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0961× (z -13.4) |
| [[A-427 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.101× (z -9.2) ⚠ cell-cycle shift, explains ~5% of this change |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0775× (z -8.5) |
| [[KATO III (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0883× (z -10.9) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0506× (z -9.4) ⚠ toxic |
| [[SW480 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.398× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 46 of them with an alert (⚠; 46 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | +0.67 | +0.80 / +0.21 | both halves | 7e-04 |  |
| [[ANKRD17-DT]] | +0.66 | +0.75 / +0.27 | both halves | 3e-04 |  |
| [[RFX3-DT]] | +0.66 | +0.77 / +0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[ST7L]] | +0.66 | +0.78 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZCWPW1]] | +0.65 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[BICRAL]] | +0.65 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[DPY19L1P1]] | +0.63 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | +0.62 | +0.67 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[TMEM9B-AS1]] | +0.62 | +0.65 / +0.37 | both halves | 9e-05 |  |
| [[DNMT3A]] | +0.62 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[RXYLT1]] | +0.62 | +0.74 / +0.21 | both halves | 7e-04 |  |
| [[ERCC6L2]] | +0.62 | +0.65 / +0.24 | both halves | 4e-04 |  |
| [[ZNF337-AS1]] | +0.61 | +0.69 / +0.26 | both halves | 4e-04 |  |
| [[HSPBAP1]] | +0.61 | +0.67 / +0.37 | both halves | 7e-05 |  |
| [[PPP3CB-AS1]] | +0.60 | +0.60 / +0.21 | both halves | 7e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARRB2]] | -0.59 | -0.50 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[CDK18]] | -0.58 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[YIF1B]] | -0.58 | -0.60 / +0.01 | ⚠ one half (not replicated) | 1.00 |  |
| [[STARD3NL]] | -0.58 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[RAB3A]] | -0.58 | -0.40 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[GPR160]] | -0.57 | -0.59 / -0.21 | both halves | 6e-04 |  |
| [[RASAL1]] | -0.57 | -0.59 / -0.24 | both halves | 4e-04 |  |
| [[MPP1]] | -0.56 | -0.39 / -0.22 | both halves | 6e-04 |  |
| [[FCHO1]] | -0.56 | -0.52 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[GIPR]] | -0.55 | -0.58 / -0.20 | both halves | 7e-04 |  |
| [[MGST3]] | -0.55 | -0.57 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[TMEM9]] | -0.55 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[MATCAP1]] | -0.55 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[MBOAT2]] | -0.54 | -0.59 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | KIF27's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | KIF27's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.361 over the table, 0.035 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | KIF27's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | KIF27's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.390 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | KIF27's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | KIF27's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.457 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.3, 17.3); signed map (25.4, -8.9). **Vector** length 73.4, 14.0% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +3.0 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.4 | -0.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.2 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,834,099-83,921,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434D0917 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VH2](https://www.uniprot.org/uniprotkb/Q86VH2) (Kinesin-like protein KIF27):

> Plays an essential role in motile ciliogenesis.

**Summary**, from NCBI Gene [55582](https://www.ncbi.nlm.nih.gov/gene/55582):

> This gene is a member of the KIF27 (kinesin 4) sub-family of the mammalian kinesin family. The gene is an ortholog of the Drosophila Cos2 gene, which plays an important role in the Hedgehog signaling pathway. The encoded protein contains an N-terminal motor domain which includes nucleotide-binding and microtubule-interacting regions, a stalk domain containing a predicted coiled coil motif and a C-terminal tail domain. Alternatively spliced transcript variants have been observed for this gene. …

**Accessions** — [HGNC:18632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18632) · Entrez [55582](https://www.ncbi.nlm.nih.gov/gene/55582) · UniProt [Q86VH2](https://www.uniprot.org/uniprotkb/Q86VH2) · Ensembl [ENSG00000165115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165115)

## Data

Gene col 9070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9070); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9070]; `tensor/DDL_lfc|DDL_z.npy` [9070]; `embed/gene_vectors.npy` [9070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9070 or target_col == 9070). Every well: [[KIF27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
