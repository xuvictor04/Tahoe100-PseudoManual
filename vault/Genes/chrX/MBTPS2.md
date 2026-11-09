---
symbol: "MBTPS2"
type: "gene"
col: 254
ensembl_id: "ENSG00000012174"
name: "membrane bound transcription factor peptidase, site 2"
location: "Xp22.12"
module: 25
arm: "+"
pooled_cpm: 36.3
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MBTPS2

*membrane bound transcription factor peptidase, site 2* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.93× (z +11.5, q 9e-28, up in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.26× (z +4.1, q 0.006, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 2.47×, A498 2.64×, HS-578T 3.51×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 2.85×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HS-578T 3.77×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.689× (z -9.1, q 4e-17, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MANEA]] (+0.74, fdr 7e-06), [[GUF1]] (+0.73, fdr 7e-06), [[TMEM106B]] (+0.72, fdr 7e-06); moves opposite to [[CSNK1G2]] (-0.69, fdr 1e-05), [[SLC66A2]] (-0.67, fdr 7e-06), [[RBM38]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 254.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A549 2.47×, A498 2.64×, HS-578T 3.51×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 2.85×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HS-578T 3.77×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +11.5 | 9e-28 | 38/45 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.2 | 1e-17 | 25/37 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +6.5 | 1e-08 | 27/42 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.006 | 23/48 (A-427, SW480, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.041 | 13/46 (MIA PaCa-2, A549, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.14× | +3.3 | 0.10 | 18/48 (AsPC-1, LS 180, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -9.1 | 4e-17 | 35/48 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.863× | -8.5 | 8e-15 | 13/48 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.723×** | -5.6 | 4e-06 | 25/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.658×** | -5.2 | 3e-05 | 28/47 (HCT15, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -4.8 | 2e-04 | 21/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.772×** | -4.5 | 7e-04 | 23/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.773×** | -4.5 | 7e-04 | 23/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.780×** | -4.3 | 0.001 | 19/48 (SW1417, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.752×** | -4.3 | 0.001 | 21/48 (HOP62, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.8 | 0.008 | 22/47 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.015 | 20/47 (Panc 03.27, SHP-77, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.672×** | -3.6 | 0.015 | 18/48 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.758×** | -3.4 | 0.027 | 13/48 (NCI-H1792, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.700×** | -3.2 | 0.050 | 17/47 (H4, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -13.4) |
| [[A498 (line)]] | wt | 25.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 47.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0826× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.426× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -8.6) |
| [[SW48 (line)]] | wt | 25.3 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0495× (z -12.9) |
| [[SW480 (line)]] | alt | 46.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.392× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANEA]] | +0.74 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[GUF1]] | +0.73 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[TMEM106B]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.70 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[ALG10B]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.68 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[ALG10]] | +0.68 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[TWF1]] | +0.68 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[SRP9]] | +0.67 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[ERLIN2]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[OCRL]] | +0.67 | +0.52 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK1G2]] | -0.69 | -0.56 / -0.73 | both halves | 1e-05 |  |
| [[SLC66A2]] | -0.67 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[RBM38]] | -0.66 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[BAHD1]] | -0.66 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[ELL]] | -0.65 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[LINC00685]] | -0.65 | -0.42 / -0.72 | both halves | 4e-05 |  |
| [[RABGEF1]] | -0.63 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[CDC34]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.61 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[ATG101]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.60 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[RALGDS]] | -0.60 | -0.46 / -0.67 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity raises MBTPS2's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.87× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.7, -17.9); signed map (-16.2, -39.2). **Vector** length 97.7, 22.3% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +4.0 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.9 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -9.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -5.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -3.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | membrane bound transcription factor peptidase, site 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:21,839,617-21,885,423 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S2P; previously KFSD |
| Reactome | 13 pathways, smallest: ATF6B (ATF6-beta) activates chaperones; CREB3 factors activate genes; Assembly of active LPL and LIPC lipase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [O43462](https://www.uniprot.org/uniprotkb/O43462) (Membrane-bound transcription factor site-2 protease):

> Zinc metalloprotease that mediates intramembrane proteolysis of proteins such as ATF6, ATF6B, SREBF1/SREBP1 and SREBF2/SREBP2. Catalyzes the second step in the proteolytic activation of the sterol regulatory element-binding proteins (SREBPs) SREBF1/SREBP1 and SREBF2/SREBP2: cleaves SREBPs within the first transmembrane segment, thereby releasing the N-terminal segment with a portion of the transmembrane segment attached. Mature N-terminal SREBP fragments shuttle to the nucleus and activate gene …

**Summary**, from NCBI Gene [51360](https://www.ncbi.nlm.nih.gov/gene/51360):

> This gene encodes a intramembrane zinc metalloprotease, which is essential in development. This protease functions in the signal protein activation involved in sterol control of transcription and the ER stress response. Mutations in this gene have been associated with ichthyosis follicularis with atrichia and photophobia (IFAP syndrome); IFAP syndrome has been quantitatively linked to a reduction in cholesterol homeostasis and ER stress response.[provided by RefSeq, Aug 2009]

**Accessions** — [HGNC:15455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15455) · Entrez [51360](https://www.ncbi.nlm.nih.gov/gene/51360) · UniProt [O43462](https://www.uniprot.org/uniprotkb/O43462) · Ensembl [ENSG00000012174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012174)

## Data

Gene col 254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 254); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 254]; `tensor/DDL_lfc|DDL_z.npy` [254]; `embed/gene_vectors.npy` [254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 254 or target_col == 254). Every well: [[MBTPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBTPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
