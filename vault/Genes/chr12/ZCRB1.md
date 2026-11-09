---
symbol: "ZCRB1"
type: "gene"
col: 6269
ensembl_id: "ENSG00000139168"
name: "zinc finger CCHC-type and RNA binding motif containing 1"
location: "12q12"
module: 48
arm: "+"
pooled_cpm: 58.15
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ZCRB1

*zinc finger CCHC-type and RNA binding motif containing 1* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.81× (z +8.9, q 3e-16, up in 42 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 4.29×, PANC-1 3.55×, LOX-IMVI 4.51×, NCI-H1792 4.35×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 4.68×, PANC-1 3.85×, MIA PaCa-2 5.53×, HEC-1-A 4.17×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.582× (z -4.8, q 8e-04, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.283×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2B]] (+0.69, fdr 1e-05), [[OGA]] (+0.68, fdr 1e-05), [[ATP5PD]] (+0.67, fdr 7e-06); moves opposite to [[HNRNPAB]] (-0.69, fdr 7e-06), [[ARMC6]] (-0.67, fdr 7e-06), [[PIGW]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM229B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A549 4.29×, PANC-1 3.55×, LOX-IMVI 4.51×, NCI-H1792 4.35×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A549 4.68×, PANC-1 3.85×, MIA PaCa-2 5.53×, HEC-1-A 4.17×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +8.9 | 3e-16 | 42/42 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +8.1 | 1e-13 | 47/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.88×** | +5.7 | 3e-06 | 43/48 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +5.2 | 3e-05 | 36/45 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.30× | +3.3 | 0.11 | 31/48 (J82, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6269.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.283×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -4.8 | 8e-04 | 39/48 (LoVo, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -3.6 | 0.092 | 28/48 (AN3 CA, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -3.5 | 0.092 | 29/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.705× | -3.1 | 0.28 | 27/48 (SW1417, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 58.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +9.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 74.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 77.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 64.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 59.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 53.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +9.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 37.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 65.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 53.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2B]] | +0.69 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[OGA]] | +0.68 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ATP5PD]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[PITPNA-AS1]] | +0.66 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[CWC15]] | +0.66 | +0.54 / +0.71 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 502 |
| [[TOMM7]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.66 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[RAD17]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ATP5MC2]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[CHMP2A]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 | pathway: Early SARS-CoV-2 Infection Events |
| [[FRA10AC1]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.64 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.69 | -0.63 / -0.64 | both halves | 7e-06 | same gene group; STRING 421 |
| [[ARMC6]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[PIGW]] | -0.65 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[GRWD1]] | -0.65 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PSME3]] | -0.63 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[ARSB]] | -0.62 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[SLFNL1-AS1]] | -0.61 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[ABCF2]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.60 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[WDR77]] | -0.60 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[DDX5]] | -0.59 | -0.47 / -0.48 | both halves | 2e-05 | same gene group; pathway: Early SARS-CoV-2 Infection Events |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM229B]] | B | FAM229B activity raises ZCRB1's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without FAM229B | 0.057 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[DNAJC12]] | B | DNAJC12 activity lowers ZCRB1's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.19× higher at baseline in the lines without DNAJC12 | 0.073 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-4.8, -42.1); signed map (-15.2, 6.0). **Vector** length 62.0, 20.1% of its response variance represented; |z| ≥ 3 in 448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.4 | -0.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type and RNA binding motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:42,312,086-42,326,257 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MADP-1, MADP1, RBM36, ZCCHC19, SNRNP31 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; RNA binding motif containing; U11/U12 di-snRNP; MicroRNA protein coding host genes |
| Reactome | 13 pathways, smallest: Replication of the SARS-CoV-1 genome; Replication of the SARS-CoV-2 genome; SARS-CoV-1 Genome Replication and Transcription |
| Matched by | ensembl_id |

UniProt [Q8TBF4](https://www.uniprot.org/uniprotkb/Q8TBF4) carries no function annotation.

**Summary**, from NCBI Gene [85437](https://www.ncbi.nlm.nih.gov/gene/85437):

> Pre-mRNA splicing is catalyzed by the spliceosome. U12-type spliceosome binds U12-type pre-mRNAs and recognizes the 5' splice site and branch-point sequence. U11 and U12 snRNPs are components of U12-type spliceosome and function as a molecular bridge connecting both ends of the intron. The protein encoded by this gene contains a RNA recognition motif. It was identified as one of the protein components of U11/U12 snRNPs. This protein and many other U11/U12 snRNP proteins are highly conserved in …

**Accessions** — [HGNC:29620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29620) · Entrez [85437](https://www.ncbi.nlm.nih.gov/gene/85437) · UniProt [Q8TBF4](https://www.uniprot.org/uniprotkb/Q8TBF4) · Ensembl [ENSG00000139168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139168)

## Data

Gene col 6269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6269); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6269]; `tensor/DDL_lfc|DDL_z.npy` [6269]; `embed/gene_vectors.npy` [6269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6269 or target_col == 6269). Every well: [[ZCRB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCRB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
