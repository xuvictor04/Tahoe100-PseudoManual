---
symbol: "CREB3"
type: "gene"
col: 2831
ensembl_id: "ENSG00000107175"
name: "cAMP responsive element binding protein 3"
location: "9p13.3"
module: 12
arm: "+"
pooled_cpm: 19.2
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CREB3

*cAMP responsive element binding protein 3* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +12.9, q 5e-35, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.96× (z +8.1, q 2e-13, up in 31 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.626× (z -5.6, q 1e-05, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGB1]] (+0.76, fdr 7e-06), [[STK16]] (+0.72, fdr 7e-06), [[LYSMD3]] (+0.70, fdr 7e-06); moves opposite to [[PRDM10]] (-0.62, fdr 3e-05), [[NUDT3]] (-0.62, fdr 7e-06), [[ZNF718]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[VGLL4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.21×** | +12.9 | 5e-35 | 43/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.31×** | +9.7 | 1e-19 | 41/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +8.1 | 2e-13 | 31/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +7.4 | 1e-11 | 35/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.78×** | +6.9 | 6e-10 | 22/36 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.9 | 6e-10 | 22/30 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.43×** | +4.2 | 0.002 | 20/44 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.9 | 0.007 | 21/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.020 | 20/48 (C-33 A, SNU-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.10 | 13/48 (PANC-1, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2831.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.626×** | -5.6 | 1e-05 | 30/46 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -4.9 | 2e-04 | 27/46 (H4, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -4.9 | 2e-04 | 29/48 (AsPC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -4.5 | 1e-03 | 24/46 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.740×** | -3.6 | 0.033 | 20/46 (SW 900, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.750×** | -3.3 | 0.098 | 21/47 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.774× | -3.1 | 0.16 | 18/48 (LS 180, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +18.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.84× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.61× (z +9.3) | — |
| [[A-172 (line)]] | wt | 23.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +8.8) | — |
| [[A549 (line)]] | wt | 21.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.07× (z +8.9) | — |
| [[H4 (line)]] | wt | 35.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -11.8) |
| [[A498 (line)]] | wt | 46.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 50.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.316× (z -8.9) |
| [[HOP62 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +11.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[STK16]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[LYSMD3]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SNAPIN]] | +0.68 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[GORAB]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[DNAJB2]] | +0.66 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[GZF1]] | +0.65 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ALAS1]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[EXOC8]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.63 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[GFUS]] | +0.63 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[IK]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM10]] | -0.62 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[NUDT3]] | -0.62 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[ZNF718]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SLC41A3]] | -0.61 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[CMTM4]] | -0.61 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[NDC1]] | -0.59 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[PRDM15]] | -0.59 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[NME2]] | -0.58 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[HACD3]] | -0.58 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[TMTC4]] | -0.58 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[NBL1]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VGLL4]] | C | CREB3's natural level weakens VGLL4's drug response | CREB3's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.04; direction clear | 0.087 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.7, 1.0); signed map (-6.5, -21.8). **Vector** length 96.7, 23.4% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.7 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.4 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.0 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.4 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.3 | -4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,732,598-35,736,999 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LZIP, Luman, sLZIP |
| Gene groups (HGNC) | MicroRNA protein coding host genes; CREB3 transcription factor family |
| Reactome | 4 pathways, smallest: CREB3 factors activate genes; Unfolded Protein Response (UPR); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O43889](https://www.uniprot.org/uniprotkb/O43889) (Cyclic AMP-responsive element-binding protein 3):

> Endoplasmic reticulum (ER)-bound sequence-specific transcription factor that directly binds DNA and activates transcription. Plays a role in the unfolded protein response (UPR), promoting cell survival versus ER stress-induced apoptotic cell death. Also involved in cell proliferation, migration and differentiation, tumor suppression and inflammatory gene expression. Acts as a positive regulator of LKN-1/CCL15-induced chemotaxis signaling of leukocyte cell migration. Associates with chromatin to …

**Summary**, from NCBI Gene [10488](https://www.ncbi.nlm.nih.gov/gene/10488):

> This gene encodes a transcription factor that is a member of the leucine zipper family of DNA binding proteins. This protein binds to the cAMP-response element and regulates cell proliferation. The protein interacts with host cell factor C1, which also associates with the herpes simplex virus (HSV) protein VP16 that induces transcription of HSV immediate-early genes. This protein and VP16 both bind to the same site on host cell factor C1. It is thought that the interaction between this protein …

**Accessions** — [HGNC:2347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2347) · Entrez [10488](https://www.ncbi.nlm.nih.gov/gene/10488) · UniProt [O43889](https://www.uniprot.org/uniprotkb/O43889) · Ensembl [ENSG00000107175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107175)

## Data

Gene col 2831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2831); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2831]; `tensor/DDL_lfc|DDL_z.npy` [2831]; `embed/gene_vectors.npy` [2831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2831 or target_col == 2831). Every well: [[CREB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
