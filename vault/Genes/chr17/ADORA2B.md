---
symbol: "ADORA2B"
type: "gene"
col: 9951
ensembl_id: "ENSG00000170425"
name: "adenosine A2b receptor"
location: "17p12"
module: 5
arm: "+"
pooled_cpm: 24.13
n_lines_expressing: 44
n_dd_up: 1
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ADORA2B

*adenosine A2b receptor* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.26× (z +3.8, q 0.072, up in 17 of 42 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 3.03×; ⚠ cell-cycle shift, explains ~15% of this change).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.440× (z -19.2, q 0e+00, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRR7-AS1]] (+0.54, fdr 3e-04), [[EVA1A-AS]] (+0.50, fdr 3e-05), [[TBRG4]] (+0.49, fdr 2e-05); moves opposite to [[ABI1]] (-0.51, fdr 3e-04), [[NCOA1]] (-0.50, fdr 1e-05), [[PIK3CA]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[UBASH3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 3.03×; ⚠ cell-cycle shift, explains ~15% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.072 | 17/42 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.46 | 3/42 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | 1.41× | +3.0 | 0.46 | 5/41 (A-172, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.440×** | -19.2 | 0e+00 | 37/41 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.427×** | -14.1 | 2e-42 | 36/42 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.396×** | -13.8 | 7e-41 | 37/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.453×** | -13.1 | 6e-37 | 33/42 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.482×** | -12.1 | 2e-31 | 31/42 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.548×** | -8.9 | 4e-17 | 18/25 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.585×** | -7.9 | 2e-13 | 22/39 (RPMI-7951, SW 1271, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.621×** | -7.8 | 3e-13 | 23/40 (H4, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -6.9 | 4e-10 | 22/41 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.666×** | -6.7 | 1e-09 | 21/35 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -6.7 | 1e-09 | 20/41 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.689×** | -6.1 | 4e-08 | 22/42 (SW 900, A-172, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.750×** | -5.6 | 9e-07 | 19/42 (SW480, HepG2/C3A, …) | two highest doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -5.6 | 1e-06 | 8/42 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -5.4 | 2e-06 | 25/41 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.797×** | -5.3 | 5e-06 | 18/42 (A498, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.767×** | -4.6 | 1e-04 | 17/42 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.778×** | -4.1 | 0.001 | 8/42 (SW480, RKO, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.780×** | -4.1 | 0.001 | 15/42 (SW480, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0605× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.221× (z -17.1) |
| [[PANC-1 (line)]] | alt | 30.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -17.3) |
| [[SW 900 (line)]] | alt | 90.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.7) |
| [[LoVo (line)]] | wt | 35.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.332× (z -9.1) |
| [[LS 180 (line)]] | wt | 47.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -17.3) |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.212× (z -10.2) |
| [[A-172 (line)]] | wt | 17.4 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0961× (z -12.7) |
| [[COLO 205 (line)]] | alt | 57.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.8) |
| [[J82 (line)]] | alt | 44.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.9) |
| [[SW480 (line)]] | alt | 28.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -11.1) |
| [[A498 (line)]] | wt | 33.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -10.4) |
| [[H4 (line)]] | wt | 27.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0767× (z -11.8) |
| [[SNU-423 (line)]] | alt | 88.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.3) |
| [[SW48 (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.158× (z -8.9) |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -8.8) |
| [[C32 (line)]] | wt | 9.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.8) |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 9.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -8.7) |
| [[HS-578T (line)]] | alt | 26.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.259× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.5) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -12.5) |
| [[RKO (line)]] | wt | 35.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -10.0) |
| [[A-427 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR7-AS1]] | +0.54 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[EVA1A-AS]] | +0.50 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TBRG4]] | +0.49 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TSR1]] | +0.49 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[SLC25A19]] | +0.48 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[NAT10]] | +0.48 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[EARS2]] | +0.47 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PTRH2]] | +0.47 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[BUD23]] | +0.47 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[LINC03009-1]] | +0.47 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[LIMD1]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[OTUB2]] | +0.47 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABI1]] | -0.51 | -0.28 / -0.58 | both halves | 3e-04 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[NCOA1]] | -0.50 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PIK3CA]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ITSN2]] | -0.48 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[SNX15]] | -0.48 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[RAB13]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[LRRFIP2]] | -0.46 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[YPEL2]] | -0.46 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ZBTB10]] | -0.46 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[UBXN1]] | -0.45 | -0.46 / -0.43 | both halves | 4e-05 |  |
| [[WDR48]] | -0.45 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[OPTN]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBASH3B]] | B | ADORA2B activity raises UBASH3B's level | lines that do not express ADORA2B (6) vs lines expressing it (44) | 2.52× lower at baseline in the lines without ADORA2B | 0.060 | ⚠ within organs, on part of the lines; also absent: SGK2, FOSL1, PAQR5; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.432). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.2, -37.1); signed map (-21.0, -0.8). **Vector** length 84.4, 17.9% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +3.5 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -19.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | adenosine A2b receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,945,130-15,975,746 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Adenosine receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, GLYCOLYSIS, HYPOXIA |
| Reactome | 13 pathways, smallest: Adenosine P1 receptors; Nucleotide-like (purinergic) receptors; Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P29275](https://www.uniprot.org/uniprotkb/P29275) (Adenosine receptor A2b):

> Receptor for adenosine. The activity of this receptor is mediated by G proteins which activate adenylyl cyclase.

**Summary**, from NCBI Gene [136](https://www.ncbi.nlm.nih.gov/gene/136):

> This gene encodes an adenosine receptor that is a member of the G protein-coupled receptor superfamily. This integral membrane protein stimulates adenylate cyclase activity in the presence of adenosine. This protein also interacts with netrin-1, which is involved in axon elongation. The gene is located near the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:264) · Entrez [136](https://www.ncbi.nlm.nih.gov/gene/136) · UniProt [P29275](https://www.uniprot.org/uniprotkb/P29275) · Ensembl [ENSG00000170425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170425)

## Data

Gene col 9951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9951); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9951]; `tensor/DDL_lfc|DDL_z.npy` [9951]; `embed/gene_vectors.npy` [9951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9951 or target_col == 9951). Every well: [[ADORA2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADORA2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
