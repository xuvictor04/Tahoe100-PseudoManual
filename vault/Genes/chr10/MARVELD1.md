---
symbol: "MARVELD1"
type: "gene"
col: 7879
ensembl_id: "ENSG00000155254"
name: "MARVEL domain containing 1"
location: "10q24.2"
module: 98
arm: "+"
pooled_cpm: 7.79
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 29
n_dd_up_clean: 4
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# MARVELD1

*MARVEL domain containing 1* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.88× (z +10.0, q 1e-20, up in 12 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.54× (z +6.0, q 4e-07, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.234× (z -20.1, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53I3]] (+0.58, fdr 3e-05), [[TNS2]] (+0.53, fdr 4e-05), [[PRDX6]] (+0.53, fdr 4e-05); moves opposite to [[PTPRH]] (-0.47, fdr 2e-04), [[DOP1B]] (-0.43, fdr 1e-04), [[HMGA1]] (-0.43, fdr 2e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRABD2B]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Rutin (trihydrate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +10.0 | 1e-20 | 12/15 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +8.8 | 3e-16 | 24/30 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +6.0 | 4e-07 | 23/44 (A498, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +5.0 | 6e-05 | 17/32 (A498, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +4.1 | 0.004 | 13/42 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.8 | 0.013 | 10/21 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ritonavir (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.043 | 12/44 (C32, HEC-1-A, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.043 | 1/43 (PANC-1) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.37× | +3.1 | 0.12 | 8/42 (PANC-1, SW480, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | 1.36× | +3.0 | 0.13 | 6/44 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.0 | 0.13 | 7/44 (NCI-H1573, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.234×** | -20.1 | 0e+00 | 37/39 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.214×** | -15.1 | 0e+00 | 42/43 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.249×** | -13.6 | 6e-40 | 39/43 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.258×** | -13.3 | 4e-38 | 39/43 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.301×** | -11.8 | 7e-30 | 36/37 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.353×** | -9.8 | 9e-21 | 32/41 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.392×** | -9.2 | 4e-18 | 35/43 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.404×** | -8.9 | 5e-17 | 33/42 (SW 900, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.439×** | -8.1 | 5e-14 | 30/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.445×** | -7.9 | 1e-13 | 33/43 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.462×** | -7.6 | 2e-12 | 26/43 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.495×** | -6.5 | 4e-09 | 24/41 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.520×** | -6.4 | 7e-09 | 27/42 (J82, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -6.0 | 6e-08 | 25/39 (HCT15, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.574×** | -5.4 | 2e-06 | 22/42 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.577×** | -5.4 | 3e-06 | 24/39 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.60 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -11.8) |
| [[PANC-1 (line)]] | alt | 7.93 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -15.1) |
| [[HOP62 (line)]] | alt | 8.37 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -14.8) |
| [[HT-29 (line)]] | alt | 5.32 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0354× (z -11.1) |
| [[KATO III (line)]] | alt | 6.95 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0268× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0726× (z -16.5) |
| [[A-172 (line)]] | wt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.6) |
| [[A498 (line)]] | wt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -11.1) |
| [[A549 (line)]] | wt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -11.6) |
| [[HCT15 (line)]] | alt | 9.84 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0640× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 7.28 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -12.1) |
| [[LS 180 (line)]] | wt | 5.48 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0558× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 5.77 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0539× (z -13.0) |
| [[C-33 A (line)]] | alt | 8.34 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0600× (z -10.0) |
| [[C32 (line)]] | wt | 9.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 7.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.2) |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -13.2) |
| [[J82 (line)]] | alt | 5.44 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0603× (z -11.2) |
| [[LoVo (line)]] | wt | 5.79 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0429× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 7.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.121× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 8.11 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0853× (z -8.9) |
| [[SW 900 (line)]] | alt | 6.78 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0415× (z -11.6) |
| [[SW480 (line)]] | alt | 4.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.8) |
| [[A-427 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53I3]] | +0.58 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TNS2]] | +0.53 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[PRDX6]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[MAP3K6]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ADGRG2]] | +0.51 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[LTBR]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[YAP1]] | +0.50 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[RPRD1B]] | +0.50 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[CHST14]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SLC26A2]] | +0.49 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[STOM]] | +0.49 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[UBE2E1]] | +0.48 | +0.44 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRH]] | -0.47 | -0.35 / -0.31 | both halves | 2e-04 |  |
| [[DOP1B]] | -0.43 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[HMGA1]] | -0.43 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[KIAA1217]] | -0.42 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[RPS6KA3]] | -0.42 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[TMOD1]] | -0.42 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[MMP13]] | -0.41 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[ARID5A]] | -0.41 | -0.37 / -0.21 | both halves | 7e-04 |  |
| [[ADAMTS16]] | -0.41 | -0.24 / -0.37 | both halves | 4e-04 |  |
| [[CREB5]] | -0.40 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[RUBCNL]] | -0.40 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[PLCG2]] | -0.40 | -0.28 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRABD2B]] | B | TRABD2B activity raises MARVELD1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without TRABD2B | 0.063 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |
| [[BATF]] | B | BATF activity lowers MARVELD1's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.47× higher at baseline in the lines without BATF | 0.078 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | C | MARVELD1 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express MARVELD1 (4) vs lines expressing it (44) | the lines without MARVELD1: 1.28× the cells of the other lines | 0.075 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: LDHB, GSTP1, E2F7 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.0, 17.4); signed map (21.1, 32.9). **Vector** length 64.3, 12.0% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.8 | +0.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -20.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.3 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | MARVEL domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:97,713,173-97,718,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4415, GB14, FLJ23440, FLJ22343, bA548K23.8; previously MRVLDC1 |
| Gene groups (HGNC) | MARVEL domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSK0](https://www.uniprot.org/uniprotkb/Q9BSK0) (MARVEL domain-containing protein 1):

> Microtubule-associated protein that exhibits cell cycle-dependent localization and can inhibit cell proliferation and migration.

**Summary**, from NCBI Gene [83742](https://www.ncbi.nlm.nih.gov/gene/83742):

> Predicted to be a structural constituent of myelin sheath. Predicted to be involved in myelination. Predicted to be located in cytoskeleton; nucleus; and plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28674) · Entrez [83742](https://www.ncbi.nlm.nih.gov/gene/83742) · UniProt [Q9BSK0](https://www.uniprot.org/uniprotkb/Q9BSK0) · Ensembl [ENSG00000155254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155254)

## Data

Gene col 7879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7879); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7879]; `tensor/DDL_lfc|DDL_z.npy` [7879]; `embed/gene_vectors.npy` [7879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7879 or target_col == 7879). Every well: [[MARVELD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARVELD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
