---
symbol: "NEURL1"
type: "gene"
col: 2903
ensembl_id: "ENSG00000107954"
name: "neuralized E3 ubiquitin protein ligase 1"
location: "10q24.33"
module: 61
arm: "+"
pooled_cpm: 2.61
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# NEURL1

*neuralized E3 ubiquitin protein ligase 1* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.60× (z +15.6, q 0e+00, up in 20 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM: 0.601× (z -4.4, q 0.006, down in 13 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Paclitaxel (drug)]] 0.5 µM in 1 line (SW 1088 0.163×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.128×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.156×; ⚠ toxic; transcription drop); [[Dexamethasone (drug)]] 0.05 µM in 1 line (Hs 766T 0.0807×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.168×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PROSER2-AS1]] (+0.59, fdr 1e-05), [[DENND2C]] (+0.59, fdr 1e-05), [[CELF4]] (+0.59, fdr 4e-05); moves opposite to [[YAP1]] (-0.50, fdr 4e-05), [[EXOSC10]] (-0.50, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[XACT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.60×** | +15.6 | 0e+00 | 20/28 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.90×** | +9.2 | 1e-17 | 18/35 (SW480, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +7.6 | 4e-12 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +7.3 | 6e-11 | 21/41 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +7.0 | 2e-10 | 8/28 (hTERT-HPNE, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +6.7 | 2e-09 | 1/8 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +6.6 | 3e-09 | 19/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +5.8 | 4e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.7 | 1e-04 | 11/32 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +4.5 | 4e-04 | 12/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.68×** | +4.4 | 5e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.001 | 12/39 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 8/39 (A-172, Hs 766T, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.040 | 1/41 (CFPAC-1) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.047 | 12/37 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2903.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Paclitaxel (drug)]] 0.5 µM in 1 line (SW 1088 0.163×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.128×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.156×; ⚠ toxic; transcription drop); [[Dexamethasone (drug)]] 0.05 µM in 1 line (Hs 766T 0.0807×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.168×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.601×** | -4.4 | 0.006 | 13/39 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -3.9 | 0.033 | 11/38 (LoVo, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.8 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.128× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -8.5) |
| [[Hs 766T (line)]] | wt | 8.86 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0807× (z -9.1) |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -9.4) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 1 | — | [[Paclitaxel (drug)]] 0.5 µM 0.163× (z -858.0) |
| [[A-172 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.926 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.949 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.685 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROSER2-AS1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[DENND2C]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CELF4]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[MYO18B]] | +0.59 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[LINC02511]] | +0.58 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[PRR5-ARHGAP8]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[SLC35E4]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[KCND3]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.57 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[WIPF3]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ITGA7]] | +0.56 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[KCNK13]] | +0.56 | +0.39 / +0.63 | both halves | 6e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YAP1]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.50 | -0.29 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XACT]] | B | XACT activity raises NEURL1's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without XACT | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438 |
| [[ERG]] | B | ERG activity raises NEURL1's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.61× lower at baseline in the lines without ERG | 0.055 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |
| [[PLEKHG5]] | B | PLEKHG5 activity lowers NEURL1's level | lines that do not express PLEKHG5 (5) vs lines expressing it (45) | 1.43× higher at baseline in the lines without PLEKHG5 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFRSF25, SLC22A20P, ENSG00000287264; maybe low, not absent; its own permutation p |
| [[CREB3L1]] | B | CREB3L1 activity weakens NEURL1's drug response | lines that do not express CREB3L1 (22) vs lines expressing it (21) | the lines without CREB3L1 respond 3.85× as strongly (z diff -1.64); strongest at Dinaciclib 0.5 µM: 2.49x vs 0.49x (z diff -5.5) | 0.081 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.2, 36.3); signed map (31.4, 20.6). **Vector** length 50.0, 7.12% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +15.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +9.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | neuralized E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,493,705-103,592,546 (+) |
| Ensembl biotype | protein_coding |
| Also known as | h-neu, RNF67, neu-1; previously NEURL |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 15 pathways, smallest: Constitutive Signaling by NOTCH1 HD Domain Mutants; Signaling by NOTCH1 HD Domain Mutants in Cancer; NOTCH2 Activation and Transmission of Signal to the Nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [O76050](https://www.uniprot.org/uniprotkb/O76050) (E3 ubiquitin-protein ligase NEURL1):

> Plays a role in hippocampal-dependent synaptic plasticity, learning and memory. Involved in the formation of spines and functional synaptic contacts by modulating the translational activity of the cytoplasmic polyadenylation element-binding protein CPEB3. Promotes ubiquitination of CPEB3, and hence induces CPEB3-dependent mRNA translation activation of glutamate receptor GRIA1 and GRIA2. Can function as an E3 ubiquitin-protein ligase to activate monoubiquitination of JAG1 (in vitro), thereby …

**Summary**, from NCBI Gene [9148](https://www.ncbi.nlm.nih.gov/gene/9148):

> Predicted to enable translation regulator activity and ubiquitin protein ligase activity. Involved in negative regulation of Notch signaling pathway; negative regulation of cell population proliferation; and positive regulation of apoptotic process. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7761) · Entrez [9148](https://www.ncbi.nlm.nih.gov/gene/9148) · UniProt [O76050](https://www.uniprot.org/uniprotkb/O76050) · Ensembl [ENSG00000107954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107954)

## Data

Gene col 2903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2903); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2903]; `tensor/DDL_lfc|DDL_z.npy` [2903]; `embed/gene_vectors.npy` [2903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2903 or target_col == 2903). Every well: [[NEURL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEURL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
