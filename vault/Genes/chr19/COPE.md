---
symbol: "COPE"
type: "gene"
col: 2641
ensembl_id: "ENSG00000105669"
name: "coat protein complex I subunit epsilon"
location: "19p13.11"
module: 41
arm: "+"
pooled_cpm: 53.33
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# COPE

*coat protein complex I subunit epsilon* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +7.9, q 2e-12, up in 37 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.38× (z +4.2, q 0.003, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 4.75×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 3.48×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 2.73×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.778× (z -4.6, q 0.003, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~66% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (Hs 766T 0.0644×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.287×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.438×; ⚠ cell-cycle shift, explains ~66% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFIP2]] (+0.78, fdr 7e-06), [[POFUT2]] (+0.77, fdr 7e-06), [[ARF4]] (+0.74, fdr 7e-06); moves opposite to [[THAP12]] (-0.62, fdr 1e-05), [[HDAC2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 4.75×; ⚠ cell-cycle shift, explains ~86% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 3.48×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 2.73×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.94×** | +7.9 | 2e-12 | 37/49 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.70×** | +6.6 | 1e-08 | 33/41 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.60×** | +6.0 | 3e-07 | 38/48 (A-172, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.45×** | +4.8 | 2e-04 | 33/48 (A-172, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.42×** | +4.2 | 0.003 | 28/45 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.003 | 33/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.8 | 0.009 | 29/47 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.34×** | +3.8 | 0.009 | 26/48 (A-172, C-33 A, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.046 | 25/48 (SK-MEL-2, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (Hs 766T 0.0644×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.287×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.438×; ⚠ cell-cycle shift, explains ~66% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.778×** | -4.6 | 0.003 | 27/48 (LS 180, HS-578T, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.782× | -3.2 | 0.43 | 25/48 (CFPAC-1, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 73.2 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.75× (z +9.8) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[A-172 (line)]] | wt | 74.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Hs 766T (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0644× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[LS 180 (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.438× (z -10.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H1573 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +9.7) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SNU-1 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFIP2]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[POFUT2]] | +0.77 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[ARF4]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 707 |
| [[KDELR2]] | +0.74 | +0.65 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 634 |
| [[OSBP]] | +0.74 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 418 |
| [[TMED9]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 662 |
| [[SCFD1]] | +0.71 | +0.77 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[MANF]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[HM13]] | +0.71 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 664 |
| [[LYSMD3]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP12]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[HDAC2]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers COPE's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMED9]] | C | TMED9's natural level weakens COPE's drug response | TMED9's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.11; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.1, -36.7); signed map (-51.7, 14.4). **Vector** length 87.5, 24.5% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.7 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.4 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +2.3 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.0 | +2.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.6 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -4.5 | -4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,899,514-18,919,387 (-) |
| Ensembl biotype | protein_coding |
| Also known as | epsilon-COP |
| Gene groups (HGNC) | Coat protein complex I |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O14579](https://www.uniprot.org/uniprotkb/O14579) (Coatomer subunit epsilon):

> The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. The coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. In mammals, the coatomer can only be recruited by membranes associated with ADP-ribosylation …

**Summary**, from NCBI Gene [11316](https://www.ncbi.nlm.nih.gov/gene/11316):

> The product of this gene is an epsilon subunit of coatomer protein complex. Coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles. It is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. Coatomer complex consists of at least the alpha, beta, beta', gamma, delta, epsilon and zeta subunits. Alternatively spliced transcript variants …

**Accessions** — [HGNC:2234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2234) · Entrez [11316](https://www.ncbi.nlm.nih.gov/gene/11316) · UniProt [O14579](https://www.uniprot.org/uniprotkb/O14579) · Ensembl [ENSG00000105669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105669)

## Data

Gene col 2641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2641); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2641]; `tensor/DDL_lfc|DDL_z.npy` [2641]; `embed/gene_vectors.npy` [2641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2641 or target_col == 2641). Every well: [[COPE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
