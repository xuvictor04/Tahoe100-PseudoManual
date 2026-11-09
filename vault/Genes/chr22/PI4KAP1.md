---
symbol: "PI4KAP1"
type: "gene"
col: 15826
ensembl_id: "ENSG00000274602"
name: "phosphatidylinositol 4-kinase alpha pseudogene 1"
location: "22q11.21"
module: 88
arm: "-"
pooled_cpm: 2.71
n_lines_expressing: 26
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# PI4KAP1

*phosphatidylinositol 4-kinase alpha pseudogene 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.11× (z +10.8, q 1e-24, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.72× (z +5.4, q 2e-05, up in 9 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Tranilast (drug)]] 0.05 µM in 1 line (SNU-423 0.0628×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.120×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PI4KAP2]] (+0.85, fdr 7e-06), [[PI4KAP1-1]] (+0.74, fdr 7e-06, ⚠ same locus), [[HIC2]] (+0.64, fdr 1e-05), [[LLGL2]] (+0.61, fdr 2e-05); moves opposite to [[UFL1-AS1]] (-0.61, fdr 1e-04), [[MCTS1]] (-0.61, fdr 8e-05), [[LEKR1]] (-0.60, fdr 1e-04).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PI4KAP1-1]] → it (grade C ⚠); 2 go from it, the strongest it → [[HIC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +10.8 | 1e-24 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +5.8 | 2e-06 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +5.4 | 2e-05 | 9/22 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.6 | 8e-04 | 2/12 (BT-474, KATO III) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 9e-04 | 8/22 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +4.4 | 1e-03 | 9/22 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.0 | 0.006 | 5/17 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.010 | 7/22 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.4 | 0.033 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.033 | 2/17 (NCI-H2030, BT-474) | top dose only |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.096 | 5/18 (BT-474, SW480, …) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.36× | +3.0 | 0.11 | 2/17 (BT-474, SNU-423) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 1.36× | +3.0 | 0.11 | 4/22 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Tranilast (drug)]] 0.05 µM in 1 line (SNU-423 0.0628×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.120×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 5 µM |  | 0.806× | -3.1 | 0.94 | 4/23 (SW48, CHP-212, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.16 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 6.17 | 0 | 1 | — | [[Tranilast (drug)]] 0.05 µM 0.0628× (z -10.5) |
| [[SW480 (line)]] | alt | 6.38 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4KAP2]] | +0.85 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[PI4KAP1-1]] | +0.74 | +0.79 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[HIC2]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LLGL2]] | +0.61 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ATAT1]] | +0.60 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[VRK3]] | +0.59 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[PI4KA]] | +0.57 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[FAM118A]] | +0.57 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[SLC66A2]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SEMA6C]] | +0.56 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[CBFA2T2]] | +0.56 | +0.62 / +0.21 | both halves | 6e-04 |  |
| [[COX6A1]] | +0.56 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[KYAT1]] | +0.56 | +0.55 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFL1-AS1]] | -0.61 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[MCTS1]] | -0.61 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[LEKR1]] | -0.60 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[ARMT1]] | -0.60 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[RGS5]] | -0.60 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.60 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[TASOR]] | -0.59 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[CLHC1]] | -0.59 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[HNRNPU]] | -0.57 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[OTUD4]] | -0.57 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[IQCH-AS1]] | -0.57 | -0.55 / -0.26 | both halves | 3e-04 |  |
| [[ALG10B]] | -0.56 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PI4KAP1-1]] | C | PI4KAP1-1 activity raises PI4KAP1's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 3.77× lower at baseline in the lines without PI4KAP1-1 | 7e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIC2]] | B | PI4KAP1 activity raises HIC2's level | lines that do not express PI4KAP1 (24) vs lines expressing it (26) | 1.39× lower at baseline in the lines without PI4KAP1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1-1, ENSG00000260573, LCK; maybe low, not absent |
| [[PI4KAP1-1]] | C | PI4KAP1 activity raises PI4KAP1-1's level | lines that do not express PI4KAP1 (24) vs lines expressing it (26) | 5.86× lower at baseline in the lines without PI4KAP1 | 5e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1-1, ENSG00000260573, LCK; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-5.9, 0.8); signed map (-32.9, 13.9). **Vector** length 24.2, 2.72% of its response variance represented; |z| ≥ 3 in 470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.2 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.2 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.1 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.0 | +10.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.6 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.5 | +1.6 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +0.5 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -1.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol 4-kinase alpha pseudogene 1 |
| Locus type | pseudogene |
| Location | 22q11.21 — chr22:18,534,005-18,548,798 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

UniProt [Q8N8J0](https://www.uniprot.org/uniprotkb/Q8N8J0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33576) · Entrez [728233](https://www.ncbi.nlm.nih.gov/gene/728233) · UniProt [Q8N8J0](https://www.uniprot.org/uniprotkb/Q8N8J0) · Ensembl [ENSG00000274602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274602)

## Data

Gene col 15826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15826); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15826]; `tensor/DDL_lfc|DDL_z.npy` [15826]; `embed/gene_vectors.npy` [15826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15826 or target_col == 15826). Every well: [[PI4KAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI4KAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
