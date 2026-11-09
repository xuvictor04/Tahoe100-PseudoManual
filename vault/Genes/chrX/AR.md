---
symbol: "AR"
type: "gene"
col: 9748
ensembl_id: "ENSG00000169083"
name: "androgen receptor"
location: "Xq12"
module: 9
arm: "+"
pooled_cpm: 11.96
n_lines_expressing: 23
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# AR

*androgen receptor* — Xq12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +9.8, q 6e-20, up in 1 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +9.3, q 5e-18, up in 9 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.669× (z -5.0, q 4e-04, down in 10 of 21 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.719× (z -4.1, q 0.013, down in 9 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-423 0.370×, HS-578T 0.378×, NCI-H2030 0.401×; ⚠ cell-cycle shift, explains ~6% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (H4 0.124×, A-172 0.167×, NCI-H460 0.291×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (H4 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENM1]] (+0.58, fdr 1e-05), [[SLITRK5]] (+0.57, fdr 3e-05), [[LINC02506]] (+0.57, fdr 1e-04); moves opposite to [[ZNF710]] (-0.53, fdr 3e-05), [[PIGG]] (-0.50, fdr 3e-05), [[DCTN5]] (-0.48, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +9.8 | 6e-20 | 1/15 (NCI-H661) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +9.3 | 5e-18 | 9/20 (hTERT-HPNE, A549, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +8.6 | 2e-15 | 2/16 (NCI-H1792, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.7 | 2e-12 | 5/19 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.6 | 3e-12 | 13/21 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +6.3 | 3e-08 | 17/21 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.5 | 3e-06 | 9/19 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.35×** | +5.2 | 1e-05 | 14/21 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 1e-05 | 15/20 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-05 | 16/20 (HOP62, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +4.9 | 5e-05 | 11/20 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +4.6 | 2e-04 | 9/19 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **2.01×** | +4.5 | 4e-04 | 13/19 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +4.0 | 0.002 | 13/20 (NCI-H1792, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.003 | 10/19 (RPMI-7951, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.006 | 9/21 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.007 | 7/21 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.014 | 2/19 (Panc 03.27, HS-578T) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.67×** | +3.3 | 0.028 | 6/20 (HS-578T, A-172, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9748.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-423 0.370×, HS-578T 0.378×, NCI-H2030 0.401×; ⚠ cell-cycle shift, explains ~6% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (H4 0.124×, A-172 0.167×, NCI-H460 0.291×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (H4 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -5.0 | 4e-04 | 10/21 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.1 | 0.013 | 9/20 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.765× | -3.2 | 0.28 | 1/20 (NCI-H1573) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.627× | -3.0 | 0.37 | 10/20 (NCI-H2347, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 35.4 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.136× (z -10.6) |
| [[A-172 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -9.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.131× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +8.5) ⚠ position not correctable | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -9.8) ⚠ cell-cycle shift, explains ~6% of this change |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.1) ⚠ cell-cycle shift, explains ~6% of this change |
| [[NCI-H460 (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -11.4) ⚠ cell-cycle shift, explains ~6% of this change |
| [[SW480 (line)]] | alt | 3.37 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.04× (z +10.3) | — |
| [[A-427 (line)]] | wt | 0.995 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.999 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENM1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SLITRK5]] | +0.57 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[LINC02506]] | +0.57 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[BCHE]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SNCA]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[PRKD1]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 | STRING 491 |
| [[EPHA5]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[KLHL13]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[PDGFD]] | +0.53 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MMP16]] | +0.53 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[TRIM6]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[MID1]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF710]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PIGG]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[DCTN5]] | -0.48 | -0.36 / -0.43 | both halves | 1e-04 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 400 |
| [[CRYGS]] | -0.47 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[LINC01128]] | -0.46 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[MAP3K7]] | -0.44 | -0.32 / -0.38 | both halves | 2e-04 | pathway: Deubiquitination |
| [[TBCCD1]] | -0.43 | -0.44 / -0.21 | both halves | 6e-04 |  |
| [[NMNAT1]] | -0.43 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[KDM7A-DT]] | -0.43 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[RABL2A]] | -0.43 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[ARHGAP1]] | -0.43 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[OSMR-DT]] | -0.43 | -0.41 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers AR's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 5.9% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GCNT2]] | B | GCNT2 activity raises AR's level | lines that do not express GCNT2 (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without GCNT2 | 0.073 | ⚠ within organs, on part of the lines; also absent: WBP2NL, LOXL2, CSF3 |
| [[TRERF1]] | B | TRERF1 activity raises AR's level | lines that do not express TRERF1 (6) vs lines expressing it (44) | 3.14× lower at baseline in the lines without TRERF1 | 0.079 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.4, 35.0); signed map (38.6, 37.3). **Vector** length 56.6, 14.9% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[NG25 (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | androgen receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq12 — chrX:67,544,021-67,730,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AIS, NR3C4, SMAX1, HUMARA; previously DHTR, SBMA |
| Gene groups (HGNC) | Nuclear receptor subfamily 3 group C |
| Hallmark sets | BILE_ACID_METABOLISM, ESTROGEN_RESPONSE_EARLY |
| Reactome | 17 pathways, smallest: Activated PKN1 stimulates transcription of AR (androgen receptor) regulated genes KLK2 and KLK3; RUNX2 regulates osteoblast differentiation; RUNX2 regulates bone development |
| Matched by | ensembl_id |

**Function**, from UniProt [P10275](https://www.uniprot.org/uniprotkb/P10275) (Androgen receptor):

> Steroid hormone receptors are ligand-activated transcription factors that regulate eukaryotic gene expression and affect cellular proliferation and differentiation in target tissues. Transcription factor activity is modulated by bound coactivator and corepressor proteins like ZBTB7A that recruits NCOR1 and NCOR2 to the androgen response elements/ARE on target genes, negatively regulating androgen receptor signaling and androgen-induced cell proliferation. Transcription activation is also …

**Summary**, from NCBI Gene [367](https://www.ncbi.nlm.nih.gov/gene/367):

> The androgen receptor gene is more than 90 kb long and codes for a protein that has 3 major functional domains: the N-terminal domain, DNA-binding domain, and androgen-binding domain. The protein functions as a steroid-hormone activated transcription factor. Upon binding the hormone ligand, the receptor dissociates from accessory proteins, translocates into the nucleus, dimerizes, and then stimulates transcription of androgen responsive genes. This gene contains 2 polymorphic trinucleotide …

**Accessions** — [HGNC:644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:644) · Entrez [367](https://www.ncbi.nlm.nih.gov/gene/367) · UniProt [P10275](https://www.uniprot.org/uniprotkb/P10275) · Ensembl [ENSG00000169083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169083)

## Data

Gene col 9748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9748); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9748]; `tensor/DDL_lfc|DDL_z.npy` [9748]; `embed/gene_vectors.npy` [9748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9748 or target_col == 9748). Every well: [[AR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
