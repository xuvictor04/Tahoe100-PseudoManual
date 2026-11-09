---
symbol: "TTC9C"
type: "gene"
col: 8490
ensembl_id: "ENSG00000162222"
name: "tetratricopeptide repeat domain 9C"
location: "11q12.3"
module: 178
arm: "+"
pooled_cpm: 22.81
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# TTC9C

*tetratricopeptide repeat domain 9C* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +15.0, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.692× (z -6.3, q 2e-07, down in 23 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.819× (z -3.7, q 0.032, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 0.228×, HOP62 0.347×, HS-578T 0.310×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.148×, HCT15 0.205×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.186×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW48 0.0881×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.0867×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB7]] (+0.72, fdr 7e-06), [[ZNHIT1]] (+0.67, fdr 2e-05), [[ZNF224]] (+0.66, fdr 1e-05); moves opposite to [[SFPQ]] (-0.64, fdr 2e-05), [[GALNT10]] (-0.63, fdr 1e-05), [[TMEM185B]] (-0.62, fdr 1e-05).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +15.0 | 0e+00 | 40/47 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +7.4 | 4e-11 | 33/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 5e-09 | 30/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.6 | 5e-09 | 26/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 5e-09 | 29/47 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +5.5 | 3e-06 | 22/48 (A-427, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +5.4 | 5e-06 | 23/48 (PANC-1, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.4 | 5e-06 | 25/48 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[NG25 (drug)]] 5 µM |  | **1.67×** | +5.0 | 4e-05 | 18/46 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.8 | 1e-04 | 20/48 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.29×** | +4.7 | 2e-04 | 21/47 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 3e-04 | 21/48 (NCI-H2030, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.5 | 4e-04 | 18/47 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.004 | 13/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.028 | 7/48 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Cilostazol (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.064 | 4/47 (LoVo, HS-578T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8490.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 0.228×, HOP62 0.347×, HS-578T 0.310×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.148×, HCT15 0.205×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.186×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW48 0.0881×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.0867×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.692×** | -6.3 | 2e-07 | 23/37 (SHP-77, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.783×** | -4.5 | 0.002 | 15/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.9 | 0.017 | 16/47 (AsPC-1, Panc 03.27, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.032 | 14/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.832×** | -3.4 | 0.078 | 17/41 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.086 | 9/47 (KATO III, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -3.3 | 0.088 | 18/48 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.842× | -3.2 | 0.10 | 8/47 (HCT15, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.0) | — |
| [[LoVo (line)]] | wt | 20.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0761× (z -11.2) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0867× (z -10.5) |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.3) | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0881× (z -11.0) |
| [[SW480 (line)]] | alt | 32.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.5) | — |
| [[A-427 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[ZNHIT1]] | +0.67 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ZNF224]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[CACUL1]] | +0.66 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[COG7]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[RELCH]] | +0.65 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[HINFP]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[DCAF5]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[RSBN1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.61 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.64 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[GALNT10]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.61 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[RBBP8]] | -0.60 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[GALNT1]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[WDR1]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[INO80C]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.55 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[THOC6]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TTC9C's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.4, -17.8); signed map (-22.9, 4.0). **Vector** length 86.2, 16.7% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +15.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.2 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 9C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,728,069-62,740,293 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29649 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8N5M4](https://www.uniprot.org/uniprotkb/Q8N5M4) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28432) · Entrez [283237](https://www.ncbi.nlm.nih.gov/gene/283237) · UniProt [Q8N5M4](https://www.uniprot.org/uniprotkb/Q8N5M4) · Ensembl [ENSG00000162222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162222)

## Data

Gene col 8490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8490); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8490]; `tensor/DDL_lfc|DDL_z.npy` [8490]; `embed/gene_vectors.npy` [8490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8490 or target_col == 8490). Every well: [[TTC9C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC9C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
