---
symbol: "BLOC1S1"
type: "gene"
col: 5704
ensembl_id: "ENSG00000135441"
name: "biogenesis of lysosomal organelles complex 1 subunit 1"
location: "12q13.2"
module: 48
arm: "+"
pooled_cpm: 11.55
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# BLOC1S1

*biogenesis of lysosomal organelles complex 1 subunit 1* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.69× (z +9.9, q 3e-20, up in 34 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 5.40×, LS 180 6.21×, NCI-H1573 9.84×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.07×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.635× (z -4.9, q 6e-04, down in 29 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (Panc 03.27 0.192×, SW480 0.260×, KATO III 0.264×, A-427 0.349×); [[Darinaparsin (drug)]] 0.05 µM in 1 line (Hs 766T 0.0730×); [[Selinexor (drug)]] 5 µM in 1 line (SW1417 0.260×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC12]] (+0.66, fdr 7e-06), [[NDUFB1]] (+0.65, fdr 1e-05), [[RPA3]] (+0.64, fdr 1e-05); moves opposite to [[DDX21]] (-0.52, fdr 3e-05), [[ZNF587B]] (-0.50, fdr 1e-04), [[LINC01355]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRDX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5704.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 5.40×, LS 180 6.21×, NCI-H1573 9.84×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.07×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +9.9 | 3e-20 | 34/35 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +9.0 | 8e-17 | 18/20 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.17×** | +5.9 | 8e-07 | 28/38 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +5.8 | 8e-07 | 20/25 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | 1.54× | +3.1 | 0.20 | 17/38 (A-172, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5704.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (Panc 03.27 0.192×, SW480 0.260×, KATO III 0.264×, A-427 0.349×); [[Darinaparsin (drug)]] 0.05 µM in 1 line (Hs 766T 0.0730×); [[Selinexor (drug)]] 5 µM in 1 line (SW1417 0.260×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.635×** | -4.9 | 6e-04 | 29/45 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -4.2 | 0.008 | 21/44 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.642× | -3.4 | 0.15 | 22/46 (AN3 CA, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.658× | -3.2 | 0.21 | 17/47 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.439× | -3.1 | 0.21 | 16/43 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.652× | -3.1 | 0.21 | 18/47 (SW48, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.7) |
| [[Hs 766T (line)]] | wt | 5.18 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.05 µM 0.0730× (z -9.6) |
| [[KATO III (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.4) |
| [[LS 180 (line)]] | wt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 6.83 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.84× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.4) |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.260× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -10.8) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 12 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC12]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NDUFB1]] | +0.65 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[RPA3]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[NDUFB11]] ⚠ | +0.63 | +0.55 / +0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DCTN3]] | +0.62 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[ARF5]] | +0.60 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[CENPW]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[HINT2]] | +0.60 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[NDUFA11]] ⚠ | +0.59 | +0.53 / +0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J]] ⚠ | +0.58 | +0.35 / +0.70 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR2]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 | STRING 597 |
| [[COMMD4]] | +0.58 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[CUTA]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NPC2]] | +0.57 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[NUDT1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX21]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ZNF587B]] | -0.50 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[LINC01355]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ZNF783]] ⚠ | -0.49 | -0.48 / -0.29 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[SRP72]] | -0.48 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[NOLC1]] | -0.47 | -0.34 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDX2]] | B | PRDX2 activity lowers BLOC1S1's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without PRDX2 | 0.087 | ⚠ within organs, on part of the lines; also absent: RAB20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.8, -20.5); signed map (-37.3, 10.3). **Vector** length 45.1, 7.33% of its response variance represented; |z| ≥ 3 in 538 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +0.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +0.8 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | biogenesis of lysosomal organelles complex 1 subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,716,038-55,720,087 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BLOS1, BORCS1; previously GCN5L1 |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 1 subunits; BLOC-1 related complex subunits; Acyltransferases |
| Reactome | 5 pathways, smallest: Lysosome Vesicle Biogenesis; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [P78537](https://www.uniprot.org/uniprotkb/P78537) (Biogenesis of lysosome-related organelles complex 1 subunit 1):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes. In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension. As part of the BORC complex may …

**Summary**, from NCBI Gene [2647](https://www.ncbi.nlm.nih.gov/gene/2647):

> BLOC1S1 is a component of the ubiquitously expressed BLOC1 multisubunit protein complex. BLOC1 is required for normal biogenesis of specialized organelles of the endosomal-lysosomal system, such as melanosomes and platelet dense granules (Starcevic and Dell'Angelica, 2004 [PubMed 15102850]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:4200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4200) · Entrez [2647](https://www.ncbi.nlm.nih.gov/gene/2647) · UniProt [P78537](https://www.uniprot.org/uniprotkb/P78537) · Ensembl [ENSG00000135441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135441)

## Data

Gene col 5704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5704); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5704]; `tensor/DDL_lfc|DDL_z.npy` [5704]; `embed/gene_vectors.npy` [5704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5704 or target_col == 5704). Every well: [[BLOC1S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BLOC1S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
