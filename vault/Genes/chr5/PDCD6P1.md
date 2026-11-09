---
symbol: "PDCD6P1"
type: "gene"
col: 11966
ensembl_id: "ENSG00000188002"
name: "PDCD6 pseudogene 1"
location: "5p15.33"
module: 83
arm: "+"
pooled_cpm: 11.97
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 10
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# PDCD6P1

*PDCD6 pseudogene 1* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.05 µM: 1.33× (z +3.8, q 0.084, up in 9 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 3.10×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.401× (z -13.0, q 5e-36, down in 35 of 43 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.510× (z -9.6, q 1e-19, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSKH1]] (+0.62, fdr 2e-05), [[ZNF26]] (+0.59, fdr 5e-05), [[MLYCD]] (+0.59, fdr 1e-05); moves opposite to [[MAPRE2]] (-0.54, fdr 1e-05), [[ARHGAP32]] (-0.52, fdr 2e-04), [[MAGI3]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SDHAP3]] → it (grade C ⚠); 10 go from it, the strongest it → [[SDHAP3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 3.10×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.084 | 9/39 (J82, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.40 | 6/39 (HCT15, RPMI-7951, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.40 | 7/42 (RKO, HT-29, …) | rises with dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11966.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.401×** | -13.0 | 5e-36 | 35/43 (PANC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.420×** | -11.9 | 4e-30 | 39/42 (MIA PaCa-2, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.595×** | -10.5 | 2e-23 | 25/42 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.493×** | -10.1 | 9e-22 | 30/39 (NCI-H460, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.510×** | -9.6 | 1e-19 | 34/43 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.556×** | -8.4 | 6e-15 | 27/42 (C32, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.567×** | -8.1 | 6e-14 | 27/43 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.589×** | -7.5 | 3e-12 | 27/43 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.629×** | -6.6 | 3e-09 | 21/43 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.639×** | -6.4 | 1e-08 | 19/42 (NCI-H460, C32, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.656×** | -5.8 | 4e-07 | 21/39 (SHP-77, NCI-H460, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.672×** | -5.7 | 7e-07 | 21/42 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.685×** | -5.4 | 3e-06 | 22/43 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.687×** | -5.1 | 2e-05 | 23/41 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.720×** | -4.7 | 1e-04 | 18/40 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -4.1 | 0.001 | 15/43 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -3.5 | 0.011 | 19/42 (C32, COLO 205, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.657×** | -3.1 | 0.041 | 6/42 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0555× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Bestatin (drug)]] 0.05 µM 0.142× (z -8.9) |
| [[C32 (line)]] | wt | 18.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.204× (z -8.8) |
| [[PANC-1 (line)]] | alt | 23.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 12.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0824× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 12.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 32.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 10.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0503× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0937× (z -13.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.229× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSKH1]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ZNF26]] | +0.59 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[MLYCD]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[AGAP5]] | +0.57 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[LINC01909]] | +0.55 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PGS1]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[DPY19L3-DT]] | +0.55 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[PTCD1]] | +0.55 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[FBXO22]] | +0.54 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[UBAP1L]] | +0.54 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[TEX22]] | +0.53 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[PIGG]] | +0.53 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE2]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ARHGAP32]] | -0.52 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[MAGI3]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TUBA1A]] | -0.48 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[ID3]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[MPC2]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[STXBP5L]] | -0.47 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[STK17B]] | -0.46 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[PTPN13]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[PRICKLE2]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[TTLL7]] | -0.46 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[CXADR]] | -0.46 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP3]] | C | SDHAP3 activity raises PDCD6P1's level | lines that do not express SDHAP3 (8) vs lines expressing it (42) | 3.21× lower at baseline in the lines without SDHAP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000291079, PHKA1, C1orf115; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAP3]] | C | PDCD6P1 activity raises SDHAP3's level | lines that do not express PDCD6P1 (4) vs lines expressing it (46) | 5.39× lower at baseline in the lines without PDCD6P1 | 0.004 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent with the target |
| [[MTHFS]] | C | PDCD6P1 activity strengthens MTHFS's drug response | lines that do not express PDCD6P1 (4) vs lines expressing it (44) | the lines without PDCD6P1 respond 0.73× as strongly (z diff +1.95); strongest at Panobinostat 0.05 µM: 0.51x vs 0.33x (z diff +3.5) | 0.022 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Epirubicin (hydrochloride) (drug)]] 0.5 µM | C | [[ENSG00000291055]], PDCD6P1 activity raises the cells' numbers under Epirubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000291055, PDCD6P1 (4) vs lines expressing them (44) | the lines without ENSG00000291055, PDCD6P1: 0.79× the cells of the other lines | 0.037 | ⚠ few lines (4 vs 46); across organs; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent genes |
| [[SLC8A1]] | C | PDCD6P1 activity lowers SLC8A1's level | lines that do not express PDCD6P1 (4) vs lines expressing it (46) | 10.02× higher at baseline in the lines without PDCD6P1 | 0.042 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 5 µM | C | [[ENSG00000291055]], PDCD6P1 activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express ENSG00000291055, PDCD6P1 (4) vs lines expressing them (44) | the lines without ENSG00000291055, PDCD6P1: 0.76× the cells of the other lines | 0.054 | ⚠ few lines (4 vs 46); across organs; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent genes |
| cells under [[Belinostat (drug)]] 5 µM | C | [[ENSG00000291055]], PDCD6P1 activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express ENSG00000291055, PDCD6P1 (4) vs lines expressing them (44) | the lines without ENSG00000291055, PDCD6P1: 0.69× the cells of the other lines | 0.058 | ⚠ few lines (4 vs 46); across organs; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent genes |
| [[DCTN5]] | C | PDCD6P1 activity strengthens DCTN5's drug response | lines that do not express PDCD6P1 (4) vs lines expressing it (45) | the lines without PDCD6P1 respond 0.83× as strongly (z diff +0.84); strongest at Ouabain (Octahydrate) 5 µM: 1.10x vs 1.60x (z diff +3.6) | 0.064 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | [[ENSG00000291055]], PDCD6P1 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000291055, PDCD6P1 (4) vs lines expressing them (44) | the lines without ENSG00000291055, PDCD6P1: 0.75× the cells of the other lines | 0.071 | ⚠ few lines (4 vs 46); across organs; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent genes |
| [[GABRA3]] | C | PDCD6P1 activity lowers GABRA3's level | lines that do not express PDCD6P1 (4) vs lines expressing it (46) | 5.31× higher at baseline in the lines without PDCD6P1 | 0.071 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | C | [[ENSG00000291055]], PDCD6P1 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express ENSG00000291055, PDCD6P1 (4) vs lines expressing them (44) | the lines without ENSG00000291055, PDCD6P1: 0.75× the cells of the other lines | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: NSUN5, KIAA1671, ENSG00000291079; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-7.9, 19.5); signed map (29.5, -20.2). **Vector** length 55.4, 7.80% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | -1.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +1.9 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.6 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.1 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.9 | -11.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | -2.9 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | PDCD6 pseudogene 1 |
| Locus type | pseudogene |
| Location | 5p15.33 — chr5:1,598,920-1,633,984 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55763) · Entrez [728613](https://www.ncbi.nlm.nih.gov/gene/728613) · Ensembl [ENSG00000188002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188002)

## Data

Gene col 11966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11966); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11966]; `tensor/DDL_lfc|DDL_z.npy` [11966]; `embed/gene_vectors.npy` [11966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11966 or target_col == 11966). Every well: [[PDCD6P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD6P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
