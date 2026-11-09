---
symbol: "PLRG1"
type: "gene"
col: 10133
ensembl_id: "ENSG00000171566"
name: "pleiotropic regulator 1"
location: "4q31.3"
module: 17
arm: "+"
pooled_cpm: 29.98
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PLRG1

*pleiotropic regulator 1* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.75× (z +11.4, q 2e-27, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.763× (z -7.8, q 5e-12, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 0.287×, AsPC-1 0.353×, SW48 0.296×); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.112×, LoVo 0.375×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 0.322×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT9]] (+0.68, fdr 7e-06), [[HARS2]] (+0.66, fdr 7e-06), [[ADH5]] (+0.66, fdr 1e-05); moves opposite to [[HIC2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CXCR4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +11.4 | 2e-27 | 46/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +10.3 | 2e-22 | 40/48 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.3 | 3e-18 | 33/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +9.1 | 2e-17 | 36/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +9.0 | 2e-17 | 37/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +8.8 | 2e-16 | 36/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +8.6 | 6e-16 | 32/48 (LoVo, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +8.4 | 4e-15 | 36/48 (HOP62, C32, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +7.8 | 4e-13 | 27/48 (NCI-H1573, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +7.8 | 4e-13 | 37/48 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +7.0 | 1e-10 | 29/47 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +7.0 | 1e-10 | 35/48 (SNU-423, SW 900, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.42×** | +6.8 | 3e-10 | 21/37 (A498, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.8 | 5e-10 | 26/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.88×** | +6.7 | 7e-10 | 27/48 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +6.5 | 3e-09 | 27/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 6e-06 | 21/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10133.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-1 0.287×, AsPC-1 0.353×, SW48 0.296×); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.112×, LoVo 0.375×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 0.322×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -7.8 | 5e-12 | 30/48 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.822×** | -4.0 | 0.020 | 14/48 (RKO, RPMI-7951, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.6 | 0.066 | 15/48 (NCI-H2347, BT-474, …) | two highest doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.837× | -3.4 | 0.088 | 13/48 (A-427, HCT15, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.862× | -3.0 | 0.29 | 12/46 (SHP-77, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 30.4 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.38× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 28.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.0) | — |
| [[A498 (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.171× (z -10.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.6) |
| [[SW48 (line)]] | wt | 35.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -10.1) |
| [[A-172 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT9]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[HARS2]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ADH5]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.64 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[PYROXD1]] | +0.64 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.63 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[VPS50]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[COPS2]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DLD]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[RPP30]] | +0.61 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[HAX1]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TARS1]] | +0.60 | +0.59 / +0.57 | both halves | 8e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIC2]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCR4]] | B | CXCR4 activity lowers PLRG1's level | lines that do not express CXCR4 (22) vs lines expressing it (28) | 1.19× higher at baseline in the lines without CXCR4 | 0.035 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, LMO2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.0, 1.6); signed map (-23.1, -18.1). **Vector** length 89.2, 19.1% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.1 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +8.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +11.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +6.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | pleiotropic regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:154,535,005-154,550,400 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRL1, Prp46, PRPF46, Cwc1, TANGO4 |
| Gene groups (HGNC) | WD repeat domain containing; NineTeen complex; NTC associated proteins; Spliceosomal C complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O43660](https://www.uniprot.org/uniprotkb/O43660) (Pleiotropic regulator 1):

> Involved in pre-mRNA splicing as component of the spliceosome. Component of the PRP19-CDC5L complex that forms an integral part of the spliceosome and is required for activating pre-mRNA splicing. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [5356](https://www.ncbi.nlm.nih.gov/gene/5356):

> This gene encodes a core component of the cell division cycle 5-like (CDC5L) complex. The CDC5L complex is part of the spliceosome and is required for pre-mRNA splicing. The encoded protein plays a critical role in alternative splice site selection. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:9089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9089) · Entrez [5356](https://www.ncbi.nlm.nih.gov/gene/5356) · UniProt [O43660](https://www.uniprot.org/uniprotkb/O43660) · Ensembl [ENSG00000171566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171566)

## Data

Gene col 10133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10133); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10133]; `tensor/DDL_lfc|DDL_z.npy` [10133]; `embed/gene_vectors.npy` [10133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10133 or target_col == 10133). Every well: [[PLRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
