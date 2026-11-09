---
symbol: "PDPR2P"
type: "gene"
col: 13195
ensembl_id: "ENSG00000214331"
name: "pyruvate dehydrogenase phosphatase regulatory subunit 2, pseudogene"
location: "16q23.1"
module: 40
arm: "+"
pooled_cpm: 9.3
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# PDPR2P

*pyruvate dehydrogenase phosphatase regulatory subunit 2, pseudogene* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 2.11× (z +5.4, q 4e-05, up in 18 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.462× (z -10.6, q 1e-23, down in 26 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.528× (z -8.5, q 8e-15, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYPOP]] (+0.68, fdr 1e-05), [[SDHAP1]] (+0.68, fdr 1e-05), [[CCZ1B]] (+0.66, fdr 1e-05); moves opposite to [[RIPK2-DT]] (-0.63, fdr 3e-05), [[CYREN]] (-0.63, fdr 1e-05), [[RAP2C]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +5.4 | 4e-05 | 18/43 (RPMI-7951, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.015 | 15/48 (NCI-H1792, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.462×** | -10.6 | 1e-23 | 26/32 (HOP62, SNU-423, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.528×** | -8.5 | 8e-15 | 29/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.545×** | -7.7 | 2e-12 | 21/26 (NCI-H1792, HOP62, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.672×** | -7.7 | 3e-12 | 28/47 (HOP62, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.576×** | -7.6 | 4e-12 | 31/46 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -7.4 | 9e-12 | 24/44 (RPMI-7951, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -7.4 | 1e-11 | 26/44 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.656×** | -5.8 | 5e-07 | 21/47 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.651×** | -5.7 | 9e-07 | 15/18 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.503×** | -4.9 | 4e-05 | 17/45 (SHP-77, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.779×** | -4.8 | 7e-05 | 13/47 (NCI-H2347, HOP62, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.526×** | -4.6 | 2e-04 | 13/44 (SK-MEL-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.742×** | -4.1 | 0.002 | 14/46 (SNU-1, CHP-212, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.775×** | -3.4 | 0.031 | 13/44 (A-172, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.777×** | -3.3 | 0.033 | 16/45 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.037 | 15/45 (A-172, C32, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.850× | -3.1 | 0.062 | 7/47 (NCI-H1573, SW 1271, …) | top dose only |  |
| [[Busulfan (drug)]] 5 µM |  | 0.852× | -3.1 | 0.063 | 12/48 (SW48, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.75 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0589× (z -16.1) |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.42 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0477× (z -11.1) |
| [[SNU-423 (line)]] | alt | 9.23 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -9.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 9.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -9.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[CFPAC-1 (line)]] | alt | 5.09 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HS-578T (line)]] | alt | 9.01 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.135× (z -9.1) |
| [[J82 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 8.06 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 6.24 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0631× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H2347 (line)]] | alt | 5.85 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 6.29 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0727× (z -9.0) |
| [[SW480 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[A-427 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYPOP]] | +0.68 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CCZ1B]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.66 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[E4F1]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PDPR]] | +0.65 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ANKS3]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[NCK1]] | +0.64 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[BRAT1]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TFB2M]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | -0.63 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[CYREN]] | -0.63 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[RAP2C]] | -0.62 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[TIA1]] | -0.61 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[DZIP3]] | -0.60 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[LEKR1]] | -0.60 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[ZNF655]] | -0.60 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[CUBN]] | -0.59 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[TASOR]] | -0.59 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[HNRNPK]] | -0.59 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[CACNA2D1]] | -0.58 | -0.57 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PDPR2P's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-0.2, -14.8); signed map (-37.4, 0.8). **Vector** length 64.2, 9.72% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | -0.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.9 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase phosphatase regulatory subunit 2, pseudogene |
| Locus type | pseudogene |
| Location | 16q23.1 — chr16:74,332,567-74,360,859 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27556) · Entrez [283922](https://www.ncbi.nlm.nih.gov/gene/283922) · Ensembl [ENSG00000214331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214331)

## Data

Gene col 13195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13195); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13195]; `tensor/DDL_lfc|DDL_z.npy` [13195]; `embed/gene_vectors.npy` [13195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13195 or target_col == 13195). Every well: [[PDPR2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDPR2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
