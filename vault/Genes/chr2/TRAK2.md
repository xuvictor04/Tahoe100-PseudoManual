---
symbol: "TRAK2"
type: "gene"
col: 3747
ensembl_id: "ENSG00000115993"
name: "trafficking kinesin protein 2"
location: "2q33.1"
module: 65
arm: "+"
pooled_cpm: 48.76
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# TRAK2

*trafficking kinesin protein 2* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.27× (z +5.6, q 1e-05, up in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.39× (z +5.4, q 1e-05, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.607× (z -8.3, q 6e-14, down in 35 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.563× (z -5.0, q 1e-04, down in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.518×, A498 0.507×, HS-578T 0.456×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.294×, HS-578T 0.382×; ⚠ cell-cycle shift, explains ~13% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.323×, PANC-1 0.372×; ⚠ cell-cycle shift, explains ~49% of this change); [[Ciclopirox (drug)]] 0.05 µM in 1 line (AN3 CA 0.0497×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC16]] (+0.60, fdr 4e-05), [[ZDHHC6]] (+0.54, fdr 4e-05), [[ELMOD2]] (+0.54, fdr 1e-04); moves opposite to [[POU2F1]] (-0.53, fdr 7e-05), [[PHLPP1]] (-0.51, fdr 5e-05), [[ARID2]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.27×** | +5.6 | 1e-05 | 23/48 (C32, SW480, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.4 | 1e-05 | 21/38 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +5.4 | 1e-05 | 26/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 0.001 | 23/47 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.3 | 0.002 | 24/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.005 | 21/47 (SNU-423, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.009 | 22/48 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +3.8 | 0.009 | 21/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.012 | 19/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.5 | 0.023 | 19/45 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.3 | 0.053 | 14/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.068 | 16/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.096 | 16/48 (CFPAC-1, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.096 | 19/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 10 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.518×, A498 0.507×, HS-578T 0.456×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.294×, HS-578T 0.382×; ⚠ cell-cycle shift, explains ~13% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.323×, PANC-1 0.372×; ⚠ cell-cycle shift, explains ~49% of this change); [[Ciclopirox (drug)]] 0.05 µM in 1 line (AN3 CA 0.0497×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.607×** | -8.3 | 6e-14 | 35/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.673×** | -6.6 | 1e-08 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -5.0 | 1e-04 | 24/49 (A-427, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.769×** | -4.3 | 0.003 | 23/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.862× | -3.5 | 0.049 | 22/48 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.827× | -3.2 | 0.14 | 22/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.4 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.287× (z -13.1) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A498 (line)]] | wt | 87.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 64.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 66.3 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[PANC-1 (line)]] | alt | 45.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -11.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[AsPC-1 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.9) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HOP62 (line)]] | alt | 64.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.2) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A549 (line)]] | wt | 53.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0497× (z -12.4) |
| [[HT-29 (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.365× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.111× (z -8.7) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -15.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.71× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC16]] | +0.60 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ZDHHC6]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ELMOD2]] | +0.54 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[DPY19L4]] | +0.52 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[KCTD21]] | +0.49 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[DYNC1LI2]] | +0.48 | +0.27 / +0.53 | both halves | 3e-04 |  |
| [[DTD1]] | +0.47 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[ARL1]] | +0.47 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[BBS7]] | +0.46 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RUSF1]] | +0.45 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[YKT6]] | +0.45 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[FAM114A2]] | +0.45 | +0.32 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POU2F1]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[PHLPP1]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ARID2]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ENDOG]] | -0.47 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[CCNL1]] | -0.47 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[MEIS2]] | -0.46 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[IP6K2]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[LRIG3-DT]] | -0.45 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[MYLIP]] | -0.45 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[BCL2L14]] | -0.44 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[TLE4]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[USP6NL]] | -0.43 | -0.39 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | TRAK2's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | TRAK2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.0780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.3, -52.9); signed map (-34.7, -32.2). **Vector** length 97.8, 23.3% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.6 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.7 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.9 | -1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -1.9 | -8.3 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Furosemide (drug)]] 5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | trafficking kinesin protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,377,207-201,451,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CALS-C, KIAA0549, GRIF-1, OIP98, MILT2; previously ALS2CR3 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: RHOT1 GTPase cycle; RHOT2 GTPase cycle; Miro GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O60296](https://www.uniprot.org/uniprotkb/O60296) (Trafficking kinesin-binding protein 2):

> May regulate endosome-to-lysosome trafficking of membrane cargo, including EGFR.

**Summary**, from NCBI Gene [66008](https://www.ncbi.nlm.nih.gov/gene/66008):

> Predicted to enable GABA receptor binding activity and myosin binding activity. Predicted to be involved in several processes, including mitochondrion distribution; protein targeting; and vesicle transport along microtubule. Predicted to be located in cytoplasm and plasma membrane. Predicted to be active in cytoplasmic vesicle; dendrite; and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13206) · Entrez [66008](https://www.ncbi.nlm.nih.gov/gene/66008) · UniProt [O60296](https://www.uniprot.org/uniprotkb/O60296) · Ensembl [ENSG00000115993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115993)

## Data

Gene col 3747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3747); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3747]; `tensor/DDL_lfc|DDL_z.npy` [3747]; `embed/gene_vectors.npy` [3747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3747 or target_col == 3747). Every well: [[TRAK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
