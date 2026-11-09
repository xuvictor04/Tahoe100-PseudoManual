---
symbol: "SPR"
type: "gene"
col: 3758
ensembl_id: "ENSG00000116096"
name: "sepiapterin reductase"
location: "2p13.2"
module: 7
arm: "+"
pooled_cpm: 9.47
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SPR

*sepiapterin reductase* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.73× (z +11.9, q 6e-30, up in 29 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 2.11× (z +6.4, q 3e-08, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -7.0, q 1e-09, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM217B]] (+0.69, fdr 7e-06), [[PSMA1]] (+0.65, fdr 7e-06), [[CASP6]] (+0.65, fdr 7e-06); moves opposite to [[SUN2]] (-0.54, fdr 3e-05), [[DRAP1]] (-0.53, fdr 3e-04), [[S100A1]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PRAME]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.73×** | +11.9 | 6e-30 | 29/32 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +10.0 | 3e-21 | 13/14 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +7.7 | 3e-12 | 23/31 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.11×** | +6.4 | 3e-08 | 31/43 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.93×** | +6.0 | 3e-07 | 32/46 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +5.5 | 3e-06 | 15/21 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.78×** | +5.2 | 2e-05 | 26/45 (A-172, NCI-H2347, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +4.7 | 2e-04 | 20/35 (NCI-H460, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 21/46 (A-427, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.40×** | +4.3 | 1e-03 | 24/46 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.001 | 22/45 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.006 | 14/46 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.037 | 10/44 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.89× | +3.0 | 0.10 | 5/24 (NCI-H2347, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.580×** | -7.0 | 1e-09 | 28/43 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -5.2 | 5e-05 | 27/46 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -5.1 | 7e-05 | 22/41 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -4.9 | 1e-04 | 25/45 (SNU-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -4.9 | 1e-04 | 24/46 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.393×** | -4.4 | 9e-04 | 19/41 (Panc 03.27, BT-474, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.627×** | -4.2 | 0.002 | 23/46 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -4.0 | 0.004 | 22/45 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -3.9 | 0.007 | 22/46 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.686×** | -3.4 | 0.036 | 18/43 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.4) |
| [[A498 (line)]] | wt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0454× (z -9.3) |
| [[Hs 766T (line)]] | wt | 6.77 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.113× (z -8.5) |
| [[KATO III (line)]] | alt | 21.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 6.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 8.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -10.9) |
| [[A-172 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM217B]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[PSMA1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CASP6]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TYW3]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MTA3]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[BID]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[EPDR1]] | +0.60 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[PSMA4]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SMIM10L1]] | +0.59 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[KEAP1]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PCBD1]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 | STRING 852 |
| [[LRRC61]] | +0.57 | +0.50 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUN2]] | -0.54 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[DRAP1]] | -0.53 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[S100A1]] | -0.52 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[MYL12B]] | -0.49 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[MYADM]] | -0.49 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[TRIOBP]] | -0.48 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[ODF2]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[EFEMP2]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[TBCCD1]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[MYL12A]] | -0.48 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[SEPTIN10]] | -0.48 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ACAP3]] | -0.47 | -0.42 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRAME]] | B | PRAME activity raises SPR's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.27× lower at baseline in the lines without PRAME | 0.034 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[HDAC6]] | B | HDAC6 activity raises SPR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.376). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-18.9, -8.2); signed map (-26.3, -22.8). **Vector** length 71.7, 14.1% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.2 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +5.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.4 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +0.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.5 | -4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.4 | -4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | sepiapterin reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:72,887,382-72,892,158 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR38C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 5 pathways, smallest: Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation; eNOS activation; Metabolism of nitric oxide: NOS3 activation and regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P35270](https://www.uniprot.org/uniprotkb/P35270) (Sepiapterin reductase):

> Catalyzes the final one or two reductions in tetra-hydrobiopterin biosynthesis to form 5,6,7,8-tetrahydrobiopterin.

**Summary**, from NCBI Gene [6697](https://www.ncbi.nlm.nih.gov/gene/6697):

> This gene encodes an aldo-keto reductase that catalyzes the NADPH-dependent reduction of pteridine derivatives and is important in the biosynthesis of tetrahydrobiopterin (BH4). Mutations in this gene result in DOPA-responsive dystonia due to sepiaterin reductase deficiency. A pseudogene has been identified on chromosome 1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11257) · Entrez [6697](https://www.ncbi.nlm.nih.gov/gene/6697) · UniProt [P35270](https://www.uniprot.org/uniprotkb/P35270) · Ensembl [ENSG00000116096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116096)

## Data

Gene col 3758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3758); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3758]; `tensor/DDL_lfc|DDL_z.npy` [3758]; `embed/gene_vectors.npy` [3758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3758 or target_col == 3758). Every well: [[SPR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
