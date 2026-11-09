---
symbol: "RAD51C"
type: "gene"
col: 2940
ensembl_id: "ENSG00000108384"
name: "RAD51 paralog C"
location: "17q22"
module: 62
arm: "+"
pooled_cpm: 14.44
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# RAD51C

*RAD51 paralog C* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.57× (z +12.7, q 3e-34, up in 42 of 46 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.91× (z +8.2, q 2e-14, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.637× (z -6.1, q 6e-07, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGME1]] (+0.62, fdr 1e-05), [[DDB2]] (+0.60, fdr 1e-05), [[PCNA]] (+0.57, fdr 1e-05); moves opposite to [[CRELD1]] (-0.41, fdr 1e-04), [[ELOVL5]] (-0.40, fdr 2e-04), [[TPST2]] (-0.40, fdr 2e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.57×** | +12.7 | 3e-34 | 42/46 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.35×** | +11.5 | 4e-28 | 41/46 (BT-474, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.17×** | +10.4 | 5e-23 | 40/45 (HOP62, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.95×** | +9.0 | 3e-17 | 26/37 (A498, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +8.2 | 2e-14 | 30/46 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.87×** | +7.9 | 2e-13 | 15/23 (CFPAC-1, A498, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.52×** | +7.9 | 2e-13 | 24/46 (A498, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.88×** | +7.9 | 3e-13 | 18/30 (A498, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +7.5 | 3e-12 | 31/45 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.71×** | +7.2 | 4e-11 | 31/46 (A498, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.73×** | +7.0 | 2e-10 | 28/43 (A498, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.73×** | +7.0 | 2e-10 | 27/41 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.67×** | +6.9 | 2e-10 | 28/45 (A498, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.62×** | +6.1 | 4e-08 | 25/45 (A498, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +5.4 | 2e-06 | 18/46 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +5.3 | 3e-06 | 19/45 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 2e-05 | 23/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 19/46 (BT-474, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.5 | 2e-04 | 21/44 (NCI-H460, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.4 | 3e-04 | 16/46 (A498, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +4.1 | 0.001 | 11/46 (A498, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.002 | 16/46 (A498, A-172, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.004 | 16/45 (RKO, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +3.4 | 0.017 | 11/46 (SW480, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.026 | 9/45 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.043 | 5/46 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Lapatinib ditosylate (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.052 | 7/46 (Hs 766T, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -6.1 | 6e-07 | 24/45 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.680×** | -5.2 | 4e-05 | 21/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -5.1 | 8e-05 | 23/45 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.656×** | -4.1 | 0.006 | 11/46 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.745×** | -3.8 | 0.018 | 17/45 (HEC-1-A, LOX-IMVI, …) | all doses, flat |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.758×** | -3.6 | 0.035 | 8/46 (J82, SW 1088, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.038 | 14/45 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.782×** | -3.4 | 0.057 | 19/44 (PANC-1, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.638×** | -3.2 | 0.089 | 14/32 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.0 | 8 (7 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +15.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.49× (z +10.6) | — |
| [[LoVo (line)]] | wt | 9.67 | 3 (3 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +10.0) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[LS 180 (line)]] | wt | 12.4 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +10.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H460 (line)]] | wt | 12.5 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +14.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[PANC-1 (line)]] | alt | 9.60 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -12.0) |
| [[A549 (line)]] | wt | 12.9 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +11.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HEC-1-A (line)]] | alt | 35.2 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -10.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.382× (z -8.6) |
| [[C32 (line)]] | wt | 15.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +9.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HOP62 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +9.0) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.114× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGME1]] | +0.62 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[DDB2]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 442 |
| [[PCNA]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 751 |
| [[ACTA2]] | +0.56 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SMC1B]] | +0.53 | +0.62 / +0.50 | both halves | 1e-05 | pathway: Meiosis |
| [[MDM2]] | +0.52 | +0.45 / +0.50 | both halves | 3e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[ZNF79]] | +0.51 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[XPC]] | +0.51 | +0.51 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[PPP4R3A]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[CHD9]] | +0.50 | +0.37 / +0.59 | both halves | 9e-05 |  |
| [[PTCHD4]] | +0.49 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[FAS]] | +0.49 | +0.50 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRELD1]] | -0.41 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ELOVL5]] | -0.40 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[TPST2]] | -0.40 | -0.56 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RAD51C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises RAD51C's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FDXR]] | B | FDXR activity raises RAD51C's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without FDXR | 0.085 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-57.6, 10.6); signed map (40.7, -24.7). **Vector** length 74.4, 14.5% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.4 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.9 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +7.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +3.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.2 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.2 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | RAD51 paralog C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,692,573-58,735,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAD51L2, FANCO |
| Gene groups (HGNC) | FA complementation groups; RAD51 paralogs |
| Hallmark sets | P53_PATHWAY, E2F_TARGETS |
| Reactome | 24 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [O43502](https://www.uniprot.org/uniprotkb/O43502) (DNA repair protein RAD51 homolog 3):

> Essential for the homologous recombination (HR) pathway of DNA repair. Involved in the homologous recombination repair (HRR) pathway of double-stranded DNA breaks arising during DNA replication or induced by DNA-damaging agents. Part of the RAD51 paralog protein complexes BCDX2 and CX3 which act at different stages of the BRCA1-BRCA2-dependent HR pathway. Upon DNA damage, BCDX2 seems to act downstream of BRCA2 recruitment and upstream of RAD51 recruitment; CX3 seems to act downstream of RAD51 …

**Summary**, from NCBI Gene [5889](https://www.ncbi.nlm.nih.gov/gene/5889):

> This gene is a member of the RAD51 family. RAD51 family members are highly similar to bacterial RecA and Saccharomyces cerevisiae Rad51 and are known to be involved in the homologous recombination and repair of DNA. This protein can interact with other RAD51 paralogs and is reported to be important for Holliday junction resolution. Mutations in this gene are associated with Fanconi anemia-like syndrome. This gene is one of four localized to a region of chromosome 17q23 where amplification …

**Accessions** — [HGNC:9820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9820) · Entrez [5889](https://www.ncbi.nlm.nih.gov/gene/5889) · UniProt [O43502](https://www.uniprot.org/uniprotkb/O43502) · Ensembl [ENSG00000108384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108384)

## Data

Gene col 2940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2940); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2940]; `tensor/DDL_lfc|DDL_z.npy` [2940]; `embed/gene_vectors.npy` [2940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2940 or target_col == 2940). Every well: [[RAD51C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD51C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
