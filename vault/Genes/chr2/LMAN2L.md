---
symbol: "LMAN2L"
type: "gene"
col: 3609
ensembl_id: "ENSG00000114988"
name: "lectin, mannose binding 2 like"
location: "2q11.2"
module: 64
arm: "+"
pooled_cpm: 20.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# LMAN2L

*lectin, mannose binding 2 like* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.71× (z +8.9, q 4e-16, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.783× (z -4.2, q 0.017, down in 14 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 0.801× (z -3.6, q 0.052, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.117×, SW1417 0.142×, A549 0.231×, NCI-H1792 0.273×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H460 0.321×, RPMI-7951 0.229×, SNU-423 0.301×; ⚠ toxic; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.220×, Panc 03.27 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[vincristine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.138×); [[Roxadustat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.134×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBS1]] (+0.63, fdr 1e-05), [[METTL22]] (+0.60, fdr 7e-06), [[DNAL1]] (+0.60, fdr 7e-06); moves opposite to [[RELL1]] (-0.53, fdr 1e-05), [[TRIM36]] (-0.49, fdr 9e-05), [[KLHL29]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF573]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +8.9 | 4e-16 | 36/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.32×** | +7.5 | 2e-11 | 28/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +6.2 | 9e-08 | 23/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +5.0 | 7e-05 | 22/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.0 | 7e-05 | 3/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.4 | 9e-04 | 20/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.001 | 20/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.30×** | +4.2 | 0.002 | 12/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.002 | 19/48 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.019 | 9/48 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.6 | 0.019 | 11/31 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.23×** | +3.3 | 0.045 | 7/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.21×** | +3.3 | 0.045 | 16/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.075 | 6/48 (LOX-IMVI, HOP62, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +3.1 | 0.076 | 8/48 (NCI-H2030, NCI-H1792, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.076 | 9/48 (SW480, A498, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.084 | 11/47 (A498, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3609.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.117×, SW1417 0.142×, A549 0.231×, NCI-H1792 0.273×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H460 0.321×, RPMI-7951 0.229×, SNU-423 0.301×; ⚠ toxic; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H460 0.220×, Panc 03.27 0.196×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[vincristine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.138×); [[Roxadustat (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.783×** | -4.2 | 0.017 | 14/48 (RPMI-7951, SW 1271, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.801×** | -3.6 | 0.052 | 15/47 (H4, SW480, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.808×** | -3.6 | 0.052 | 17/41 (NCI-H1792, HCT15, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | 0.815× | -3.4 | 0.10 | 15/46 (NCI-H460, RPMI-7951, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.817× | -3.3 | 0.10 | 17/48 (AN3 CA, Panc 03.27, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | 0.693× | -3.3 | 0.10 | 9/48 (Panc 03.27, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.836× | -3.1 | 0.18 | 11/47 (SHP-77, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.270× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~91% of this change |
| [[NCI-H1792 (line)]] | alt | 27.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 19.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[A549 (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.134× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -15.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.138× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.229× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.301× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -12.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 21.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.99× (z +8.5) | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS1]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[METTL22]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[DNAL1]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PPP6C]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[EFCAB7]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ZNF223]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TCTN2]] | +0.57 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[DNAJC7]] | +0.56 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[GFM2]] | +0.56 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[USP30]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NDUFB7]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[TRIM36]] | -0.49 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[KLHL29]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CHD7]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MYO1D]] | -0.47 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[PHLDA2]] | -0.46 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PRKCE]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[CTBP2]] | -0.46 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[OSBPL10]] | -0.46 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF573]] | C | ZNF573 activity raises LMAN2L's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without ZNF573 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-28.9, -5.6); signed map (-12.7, -18.0). **Vector** length 71.7, 11.8% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.0 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +3.0 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.7 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | -3.5 | -3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.9 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | lectin, mannose binding 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,705,929-96,740,064 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564L2423, VIPL |
| Reactome | 7 pathways, smallest: Cargo concentration in the ER; COPII-mediated vesicle transport; ER to Golgi Anterograde Transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0V9](https://www.uniprot.org/uniprotkb/Q9H0V9) (VIP36-like protein):

> May be involved in the regulation of export from the endoplasmic reticulum of a subset of glycoproteins. May function as a regulator of ERGIC-53.

**Summary**, from NCBI Gene [81562](https://www.ncbi.nlm.nih.gov/gene/81562):

> This gene encodes a protein belonging to the L-type lectin group of type 1 membrane proteins, which function in the mammalian early secretory pathway. These proteins contain luminal carbohydrate recognition domains, which display homology to leguminous lectins. Unlike other proteins of the group, which cycle in the early secretory pathway and are predominantly associated with post endoplasmic reticulum membranes, the protein encoded by this gene is a non-cycling resident protein of the ER, …

**Accessions** — [HGNC:19263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19263) · Entrez [81562](https://www.ncbi.nlm.nih.gov/gene/81562) · UniProt [Q9H0V9](https://www.uniprot.org/uniprotkb/Q9H0V9) · Ensembl [ENSG00000114988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114988)

## Data

Gene col 3609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3609); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3609]; `tensor/DDL_lfc|DDL_z.npy` [3609]; `embed/gene_vectors.npy` [3609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3609 or target_col == 3609). Every well: [[LMAN2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMAN2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
