---
symbol: "PIGC"
type: "gene"
col: 5767
ensembl_id: "ENSG00000135845"
name: "phosphatidylinositol glycan anchor biosynthesis class C"
location: "1q24.3"
module: 114
arm: "+"
pooled_cpm: 17.51
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 29
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# PIGC

*phosphatidylinositol glycan anchor biosynthesis class C* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.71× (z +7.0, q 1e-09, up in 26 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.42× (z +4.7, q 5e-04, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.398× (z -12.6, q 2e-33, down in 38 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.614× (z -6.3, q 2e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF721]] (+0.65, fdr 1e-05), [[STARD7-AS1]] (+0.65, fdr 1e-05), [[DDX59]] (+0.64, fdr 5e-05); moves opposite to [[VPS13A]] (-0.50, fdr 5e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +7.0 | 1e-09 | 26/44 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.35×** | +5.7 | 3e-06 | 28/48 (C32, A498, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.7 | 5e-04 | 21/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.008 | 17/47 (H4, SW 900, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.023 | 13/48 (PANC-1, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.023 | 15/48 (SW480, SHP-77, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.25× | +3.1 | 0.17 | 14/48 (LOX-IMVI, BT-474, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.25× | +3.0 | 0.17 | 9/48 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5767.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.398×** | -12.6 | 2e-33 | 38/46 (HT-29, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.524×** | -12.5 | 3e-33 | 31/47 (NCI-H460, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.416×** | -12.0 | 8e-31 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.533×** | -8.3 | 2e-14 | 31/46 (SHP-77, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.566×** | -7.8 | 9e-13 | 33/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.585×** | -7.1 | 2e-10 | 31/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.603×** | -6.9 | 4e-10 | 35/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.614×** | -6.3 | 2e-08 | 29/48 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.631×** | -6.3 | 2e-08 | 28/48 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.416×** | -6.3 | 2e-08 | 25/48 (A549, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -5.7 | 7e-07 | 25/47 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.663×** | -5.6 | 8e-07 | 25/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.664×** | -5.6 | 9e-07 | 23/48 (AN3 CA, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.666×** | -5.6 | 1e-06 | 26/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.676×** | -5.4 | 3e-06 | 25/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.584×** | -3.9 | 0.003 | 18/45 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.825×** | -3.7 | 0.005 | 11/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.803×** | -3.0 | 0.060 | 4/48 (HT-29, A549, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.735×** | -3.0 | 0.060 | 6/48 (MIA PaCa-2, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 0.05 µM |  | **0.800×** | -2.9 | 0.086 | 11/48 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Procainamide (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -2.9 | 0.090 | 8/47 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.815×** | -2.8 | 0.098 | 4/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | **0.809×** | -2.8 | 0.098 | 19/46 (HepG2/C3A, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.5 | 0 | 10 (10 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.147× (z -15.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[PANC-1 (line)]] | alt | 27.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -10.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 36.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -11.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -10.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.150× (z -9.0) |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -9.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.190× (z -8.6) |
| [[C-33 A (line)]] | alt | 10.00 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0650× (z -10.8) |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0668× (z -12.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -10.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -10.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0834× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0658× (z -15.9) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 12.0 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0667× (z -9.5) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.330× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF721]] | +0.65 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.65 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[DDX59]] | +0.64 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[PPP1R8]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZNF596]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SDHAF4]] | +0.62 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[SPRYD4]] | +0.62 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[MAIP1]] | +0.61 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TMEM222]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SNRNP35]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | +0.61 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[TMEM128]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13A]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.7, 19.6); signed map (27.9, -18.9). **Vector** length 77.9, 15.5% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.5 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +6.8 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.8 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.0 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.6 | -6.9 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:172,370,189-172,444,086 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIG-C, GPI2 |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; Glycosylphosphatidylinositol-N-acetylglucosaminyltransferase complex |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92535](https://www.uniprot.org/uniprotkb/Q92535) (Phosphatidylinositol N-acetylglucosaminyltransferase subunit C):

> Part of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to phosphatidylinositol and participates in the first step of GPI biosynthesis.

**Summary**, from NCBI Gene [5279](https://www.ncbi.nlm.nih.gov/gene/5279):

> This gene encodes an endoplasmic reticulum associated protein that is involved in glycosylphosphatidylinositol (GPI) lipid anchor biosynthesis. The GPI lipid anchor is a glycolipid found on many blood cells and serves to anchor proteins to the cell surface. The encoded protein is one subunit of the GPI N-acetylglucosaminyl (GlcNAc) transferase that transfers GlcNAc to phosphatidylinositol (PI) on the cytoplasmic side of the endoplasmic reticulum. Two alternatively spliced transcripts that …

**Accessions** — [HGNC:8960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8960) · Entrez [5279](https://www.ncbi.nlm.nih.gov/gene/5279) · UniProt [Q92535](https://www.uniprot.org/uniprotkb/Q92535) · Ensembl [ENSG00000135845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135845)

## Data

Gene col 5767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5767); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5767]; `tensor/DDL_lfc|DDL_z.npy` [5767]; `embed/gene_vectors.npy` [5767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5767 or target_col == 5767). Every well: [[PIGC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
