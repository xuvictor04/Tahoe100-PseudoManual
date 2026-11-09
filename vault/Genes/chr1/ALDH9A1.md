---
symbol: "ALDH9A1"
type: "gene"
col: 6682
ensembl_id: "ENSG00000143149"
name: "aldehyde dehydrogenase 9 family member A1"
location: "1q24.1"
module: 186
arm: "+"
pooled_cpm: 33.94
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# ALDH9A1

*aldehyde dehydrogenase 9 family member A1* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +12.5, q 2e-33, up in 41 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.59× (z +6.3, q 3e-08, up in 33 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (AN3 CA 0.108×; ⚠ transcription drop); [[Clotrimazole (drug)]] 0.5 µM in 1 line (CHP-212 0.0791×); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.0834×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.392×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISOC1]] (+0.55, fdr 1e-05), [[TLCD4]] (+0.53, fdr 2e-05), [[IMPA1]] (+0.52, fdr 1e-05); moves opposite to [[MEF2B]] (-0.51, fdr 2e-04), [[SMG6]] (-0.49, fdr 2e-05), [[C19orf25]] (-0.48, fdr 3e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.50×** | +12.5 | 2e-33 | 41/44 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.29×** | +10.3 | 2e-22 | 34/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.01×** | +8.8 | 2e-16 | 38/43 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.53×** | +8.2 | 5e-14 | 35/47 (A-172, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.3 | 3e-08 | 33/47 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.8 | 5e-07 | 26/47 (NCI-H2347, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.51×** | +5.1 | 2e-05 | 27/48 (PANC-1, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.37×** | +4.3 | 0.001 | 25/46 (HCT15, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.37×** | +4.3 | 0.001 | 25/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.002 | 21/48 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.35×** | +4.1 | 0.002 | 22/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.72×** | +3.9 | 0.005 | 21/45 (BT-474, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.31×** | +3.7 | 0.009 | 19/46 (BT-474, RPMI-7951, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.5 | 0.016 | 0/48 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.035 | 21/48 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.075 | 20/47 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (AN3 CA 0.108×; ⚠ transcription drop); [[Clotrimazole (drug)]] 0.5 µM in 1 line (CHP-212 0.0791×); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.0834×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.392×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 36.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.3) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 24.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.8) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 2 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0791× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 49.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 30.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.9) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[A-427 (line)]] | wt | 47.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -8.5) |
| [[A549 (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.108× (z -10.0) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HT-29 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW 900 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW480 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A498 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISOC1]] | +0.55 | +0.64 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[TLCD4]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[IMPA1]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[DMXL2]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SCOC]] | +0.51 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NBN]] | +0.50 | +0.62 / +0.32 | both halves | 2e-04 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[BBS2]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ARMT1]] | +0.50 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[C2CD5]] | +0.49 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[ZNF711]] | +0.49 | +0.63 / +0.43 | both halves | 4e-05 |  |
| [[SLC44A1]] | +0.48 | +0.19 / +0.56 | ⚠ one half (not replicated) | 8e-04 | pathway: Metabolism of amino acids and derivatives |
| [[PRKAA1]] | +0.48 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[LANCL1]] | +0.48 | +0.39 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEF2B]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[SMG6]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[C19orf25]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[C1orf159]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MUC20-OT1]] | -0.47 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[KCTD13]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[HIRA]] | -0.46 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[CAMSAP1-DT]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[FBXW7]] | -0.46 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[CCM2]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[MAP3K10]] | -0.45 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MROH1]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity lowers ALDH9A1's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.53× higher at baseline in the lines without ADD3 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.179). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.7, -2.6); signed map (7.0, -36.7). **Vector** length 68.1, 14.1% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.3 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.8 | +1.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 9 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:165,662,216-165,698,562 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E3; previously ALDH7, ALDH4, ALDH9 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, GLYCOLYSIS |
| Reactome | 2 pathways, smallest: Carnitine synthesis; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P49189](https://www.uniprot.org/uniprotkb/P49189) (4-trimethylaminobutyraldehyde dehydrogenase):

> Converts gamma-trimethylaminobutyraldehyde into gamma-butyrobetaine with high efficiency (in vitro). Can catalyze the irreversible oxidation of a broad range of aldehydes to the corresponding acids in an NAD-dependent reaction, but with low efficiency. Catalyzes the oxidation of aldehydes arising from biogenic amines and polyamines.

**Summary**, from NCBI Gene [223](https://www.ncbi.nlm.nih.gov/gene/223):

> This protein belongs to the aldehyde dehydrogenase family of proteins. It has a high activity for oxidation of gamma-aminobutyraldehyde and other amino aldehydes. The enzyme catalyzes the dehydrogenation of gamma-aminobutyraldehyde to gamma-aminobutyric acid (GABA). This isozyme is a tetramer of identical 54-kD subunits. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:412) · Entrez [223](https://www.ncbi.nlm.nih.gov/gene/223) · UniProt [P49189](https://www.uniprot.org/uniprotkb/P49189) · Ensembl [ENSG00000143149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143149)

## Data

Gene col 6682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6682); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6682]; `tensor/DDL_lfc|DDL_z.npy` [6682]; `embed/gene_vectors.npy` [6682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6682 or target_col == 6682). Every well: [[ALDH9A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH9A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
