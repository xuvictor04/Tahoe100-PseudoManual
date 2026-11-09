---
symbol: "ATP5MC3"
type: "gene"
col: 7812
ensembl_id: "ENSG00000154518"
name: "ATP synthase membrane subunit c locus 3"
location: "2q31.1"
module: 58
arm: "+"
pooled_cpm: 36.7
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# ATP5MC3

*ATP synthase membrane subunit c locus 3* — 2q31.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.67× (z +8.5, q 1e-14, up in 31 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 5.37×, A549 5.77×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.17×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.316×, KATO III 0.429×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1GALT1C1]] (+0.67, fdr 7e-06), [[ATP5F1A]] (+0.59, fdr 9e-06), [[UQCRC1]] (+0.59, fdr 4e-05, ⚠ UQCRC1 in the vector space only through flagged drug-doses), [[SNRNP25]] (+0.59, fdr 2e-05); moves opposite to [[CIRBP]] (-0.62, fdr 3e-05), [[WDR45]] (-0.58, fdr 1e-04), [[NPIPA1]] (-0.57, fdr 2e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 5.37×, A549 5.77×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 3.17×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.67×** | +8.5 | 1e-14 | 31/38 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.58×** | +7.1 | 3e-10 | 44/46 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.81×** | +5.3 | 2e-05 | 34/46 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.89×** | +5.3 | 2e-05 | 30/43 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.72×** | +4.9 | 1e-04 | 34/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.70×** | +4.8 | 2e-04 | 36/47 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.67×** | +4.6 | 3e-04 | 40/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.64×** | +4.5 | 6e-04 | 33/46 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.6 | 0.023 | 28/46 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.47×** | +3.5 | 0.027 | 31/47 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 1.43× | +3.1 | 0.10 | 25/47 (A498, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.40× | +3.0 | 0.11 | 25/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.316×, KATO III 0.429×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.500× | -3.2 | 0.60 | 24/48 (BT-474, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.0) |
| [[A498 (line)]] | wt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[A549 (line)]] | wt | 34.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[KATO III (line)]] | alt | 42.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 47.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | — |
| [[A-172 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1GALT1C1]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ATP5F1A]] | +0.59 | +0.63 / +0.57 | both halves | 9e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[UQCRC1]] ⚠ | +0.59 | +0.42 / +0.56 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 614; ⚠ in the vector space only through flagged drug-doses |
| [[SNRNP25]] | +0.59 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[UQCR10]] ⚠ | +0.59 | +0.41 / +0.57 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 668; ⚠ in the vector space only through flagged drug-doses |
| [[MRPL12]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 | STRING 558 |
| [[TMEM147]] | +0.58 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[APRT]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZDHHC12]] | +0.58 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[NDUFB6]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 601 |
| [[ATP5MF]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 993 |
| [[NDUFC2]] | +0.56 | +0.37 / +0.53 | both halves | 9e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 622 |
| [[NHP2]] | +0.55 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[RNGTT]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIRBP]] | -0.62 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[WDR45]] | -0.58 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[NPIPA1]] | -0.57 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[CROCC]] | -0.57 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CCDC17]] | -0.57 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ZCWPW1]] | -0.56 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[U2AF1L4]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SPAG5-AS1]] | -0.56 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF547]] | -0.56 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[PPP1R12A-AS2]] | -0.56 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[ZFHX2-AS1]] | -0.55 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[INTS6-AS1]] | -0.55 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ATP5MC3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF547]] | B | ZNF547 activity lowers ATP5MC3's level | lines that do not express ZNF547 (6) vs lines expressing it (44) | 1.43× higher at baseline in the lines without ZNF547 | 0.092 | ⚠ within organs, on part of the lines; also absent: TRAPPC2B, ZNF548, SPACA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-13.2, 6.6); signed map (-37.3, -28.4). **Vector** length 66.6, 18.6% of its response variance represented; |z| ≥ 3 in 607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +2.7 | +4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.6 | +3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +2.1 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.5 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase membrane subunit c locus 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:175,176,258-175,181,710 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP5G3 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P48201](https://www.uniprot.org/uniprotkb/P48201) (ATP synthase F(0) complex subunit C3, mitochondrial):

> Mitochondrial membrane ATP synthase (F(1)F(0) ATP synthase or Complex V) produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. F-type ATPases consist of two structural domains, F(1) - containing the extramembraneous catalytic core and F(0) - containing the membrane proton channel, linked together by a central stalk and a peripheral stalk. During catalysis, ATP synthesis in the catalytic domain …

**Summary**, from NCBI Gene [518](https://www.ncbi.nlm.nih.gov/gene/518):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:843) · Entrez [518](https://www.ncbi.nlm.nih.gov/gene/518) · UniProt [P48201](https://www.uniprot.org/uniprotkb/P48201) · Ensembl [ENSG00000154518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154518)

## Data

Gene col 7812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7812); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7812]; `tensor/DDL_lfc|DDL_z.npy` [7812]; `embed/gene_vectors.npy` [7812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7812 or target_col == 7812). Every well: [[ATP5MC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5MC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
