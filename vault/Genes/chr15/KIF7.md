---
symbol: "KIF7"
type: "gene"
col: 9362
ensembl_id: "ENSG00000166813"
name: "kinesin family member 7"
location: "15q26.1"
module: 1
arm: "+"
pooled_cpm: 11.94
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# KIF7

*kinesin family member 7* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.56× (z +6.7, q 2e-08, up in 23 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 2.80×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.82×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.720× (z -4.9, q 5e-04, down in 19 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.565× (z -4.5, q 0.002, down in 17 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (H4 0.116×, C-33 A 0.240×, NCI-H1792 0.220×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.331×, HOP62 0.392×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (RPMI-7951 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0636×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (AsPC-1 0.0801×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0894×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARAP3]] (+0.60, fdr 1e-05), [[COA7]] (+0.56, fdr 1e-05), [[EIF3J]] (+0.56, fdr 3e-05); moves opposite to [[MXI1]] (-0.54, fdr 2e-05), [[LNX2]] (-0.52, fdr 2e-04), [[SPATA7]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF518B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9362.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 2.80×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 3.82×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.7 | 2e-08 | 23/45 (HCT15, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 8e-04 | 16/46 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.5 | 0.001 | 12/23 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +4.4 | 0.002 | 12/29 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | 1.24× | +3.1 | 0.24 | 12/41 (LoVo, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9362.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (H4 0.116×, C-33 A 0.240×, NCI-H1792 0.220×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.331×, HOP62 0.392×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (RPMI-7951 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0636×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (AsPC-1 0.0801×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0894×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.720×** | -4.9 | 5e-04 | 19/45 (LOX-IMVI, C32, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.565×** | -4.5 | 0.002 | 17/46 (HOP62, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -4.4 | 0.002 | 21/44 (SW 900, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.759×** | -4.1 | 0.005 | 15/45 (AsPC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.763×** | -4.1 | 0.005 | 19/46 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.665× | -3.2 | 0.12 | 10/43 (C32, H4, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | 0.809× | -3.2 | 0.12 | 18/44 (RPMI-7951, SW48, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -3.1 | 0.13 | 10/46 (NCI-H460, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.65 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0675× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0801× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.87 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0878× (z -8.8) |
| [[C-33 A (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.0636× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 4.62 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0894× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A-172 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAP3]] | +0.60 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[COA7]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.56 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[BICD1]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 | STRING 451 |
| [[ZNF518B]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TUBA8]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[MAK16]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[GPATCH4]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[NAA15]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CLPB]] | +0.50 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[DCTD]] | +0.50 | +0.37 / +0.44 | both halves | 7e-05 |  |
| [[RAD54L2]] | +0.50 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXI1]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LNX2]] | -0.52 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[SPATA7]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PAIP2B]] | -0.51 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[NDUFA2]] | -0.50 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[CA5BP1]] | -0.49 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[KDM3A]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CERT1]] | -0.48 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[GAB1]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ATF2]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ARSK]] | -0.48 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[KMT5C]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF518B]] | B | ZNF518B activity raises KIF7's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without ZNF518B | 0.053 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |
| [[EVC]] | B | EVC activity raises KIF7's level | lines that do not express EVC (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without EVC | 0.084 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.8, -30.7); signed map (4.1, -45.9). **Vector** length 65.2, 9.66% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.1 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.2 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,608,789-89,663,086 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JBTS12 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 3 pathways, smallest: Hedgehog 'on' state; Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M1P5](https://www.uniprot.org/uniprotkb/Q2M1P5) (Kinesin-like protein KIF7):

> Essential for hedgehog signaling regulation: acts both as a negative and positive regulator of sonic hedgehog (Shh) and Indian hedgehog (Ihh) pathways, acting downstream of SMO, through both SUFU-dependent and -independent mechanisms. Involved in the regulation of microtubular dynamics. Required for proper organization of the ciliary tip and control of ciliary localization of SUFU-GLI2 complexes (By similarity). Required for localization of GLI3 to cilia in response to Shh. Negatively regulates …

**Summary**, from NCBI Gene [374654](https://www.ncbi.nlm.nih.gov/gene/374654):

> This gene encodes a cilia-associated protein belonging to the kinesin family. This protein plays a role in the sonic hedgehog (SHH) signaling pathway through the regulation of GLI transcription factors. It functions as a negative regulator of the SHH pathway by preventing inappropriate activation of GLI2 in the absence of ligand, and as a positive regulator by preventing the processing of GLI3 into its repressor form. Mutations in this gene have been associated with various ciliopathies. …

**Accessions** — [HGNC:30497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30497) · Entrez [374654](https://www.ncbi.nlm.nih.gov/gene/374654) · UniProt [Q2M1P5](https://www.uniprot.org/uniprotkb/Q2M1P5) · Ensembl [ENSG00000166813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166813)

## Data

Gene col 9362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9362); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9362]; `tensor/DDL_lfc|DDL_z.npy` [9362]; `embed/gene_vectors.npy` [9362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9362 or target_col == 9362). Every well: [[KIF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
