---
symbol: "PPIL1"
type: "gene"
col: 5978
ensembl_id: "ENSG00000137168"
name: "peptidylprolyl isomerase like 1"
location: "6p21.2"
module: 1
arm: "+"
pooled_cpm: 8.42
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PPIL1

*peptidylprolyl isomerase like 1* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.04× (z +13.6, q 2e-39, up in 15 of 16 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.23× (z +10.2, q 2e-22, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.548× (z -4.0, q 0.036, down in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0698×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.261×; ⚠ cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HS-578T 0.0769×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP15]] (+0.79, fdr 7e-06), [[ABCE1]] (+0.79, fdr 7e-06), [[ZNF239]] (+0.78, fdr 7e-06); moves opposite to [[AAMDC]] (-0.69, fdr 7e-06), [[TESK2]] (-0.67, fdr 1e-05), [[SEZ6L2]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM169A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.04×** | +13.6 | 2e-39 | 15/16 (SW480, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.79×** | +13.1 | 1e-36 | 26/30 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +10.5 | 1e-23 | 13/20 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +10.2 | 2e-22 | 38/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +8.9 | 1e-16 | 32/43 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +8.7 | 3e-16 | 30/45 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.63×** | +6.2 | 4e-08 | 26/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.65×** | +5.8 | 6e-07 | 20/47 (PANC-1, A549, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.7 | 7e-07 | 16/35 (C-33 A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.57×** | +5.3 | 7e-06 | 17/42 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.2 | 9e-06 | 17/48 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.8 | 7e-05 | 16/46 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 10/44 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.25×** | +4.0 | 0.003 | 19/44 (NCI-H2030, A549, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +3.8 | 0.005 | 8/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.006 | 11/43 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.010 | 7/41 (NCI-H2347, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.016 | 5/35 (NCI-H2030, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.68×** | +3.5 | 0.016 | 8/42 (RPMI-7951, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.028 | 7/46 (NCI-H460, HT-29, …) | inconsistent across doses | position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.033 | 4/45 (CHP-212, HCT15, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.036 | 8/47 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0698×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.261×; ⚠ cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HS-578T 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.548×** | -4.0 | 0.036 | 12/46 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.741×** | -3.7 | 0.070 | 17/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.832× | -3.3 | 0.15 | 17/47 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.767× | -3.3 | 0.15 | 14/47 (HT-29, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.774× | -3.1 | 0.20 | 11/43 (SW48, LOX-IMVI, …) | top dose only | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.779× | -3.0 | 0.21 | 9/46 (HepG2/C3A, HCT15, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.636× | -3.0 | 0.21 | 6/47 (LoVo, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.53 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0698× (z -10.1) |
| [[PANC-1 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP15]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[FARSB]] | +0.78 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[PFAS]] | +0.78 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.77 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[ATIC]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.75 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[MAK16]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[COA7]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[WDR77]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | STRING 596 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAMDC]] | -0.69 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[TESK2]] | -0.67 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[SEZ6L2]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[TPT1]] | -0.66 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[PHF1]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[SIRT2]] | -0.66 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.64 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[RPS11]] | -0.64 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.64 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[RPS20]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[CCNI]] | -0.62 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[ULK1]] | -0.62 | -0.60 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | FAM169A activity raises PPIL1's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.40× lower at baseline in the lines without FAM169A | 0.050 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[IKZF3]] | B | IKZF3 activity raises PPIL1's level | lines that do not express IKZF3 (31) vs lines expressing it (19) | 1.27× lower at baseline in the lines without IKZF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.844). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.9, -35.5); signed map (0.6, -42.8). **Vector** length 77.5, 14.4% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.55 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.7 | +13.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +8.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.3 | +3.5 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.3 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.9 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:36,854,827-36,874,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYPL1 |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases; Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3C6](https://www.uniprot.org/uniprotkb/Q9Y3C6) (Peptidyl-prolyl cis-trans isomerase-like 1):

> Involved in pre-mRNA splicing as component of the spliceosome. PPIases accelerate the folding of proteins. Catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. Catalyzes prolyl peptide bond isomerization in CDC40/PRP17. Plays an important role in embryonic brain development; this function is independent of its isomerase activity.

**Summary**, from NCBI Gene [51645](https://www.ncbi.nlm.nih.gov/gene/51645):

> This gene is a member of the cyclophilin family of peptidylprolyl isomerases (PPIases). The cyclophilins are a highly conserved, ubiquitous family, members of which play an important role in protein folding, immunosuppression by cyclosporin A, and infection of HIV-1 virions. Based on similarity to other PPIases, this protein could accelerate the folding of proteins and might catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9260) · Entrez [51645](https://www.ncbi.nlm.nih.gov/gene/51645) · UniProt [Q9Y3C6](https://www.uniprot.org/uniprotkb/Q9Y3C6) · Ensembl [ENSG00000137168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137168)

## Data

Gene col 5978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5978); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5978]; `tensor/DDL_lfc|DDL_z.npy` [5978]; `embed/gene_vectors.npy` [5978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5978 or target_col == 5978). Every well: [[PPIL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
