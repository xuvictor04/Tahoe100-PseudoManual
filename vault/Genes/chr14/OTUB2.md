---
symbol: "OTUB2"
type: "gene"
col: 1597
ensembl_id: "ENSG00000089723"
name: "OTU deubiquitinase, ubiquitin aldehyde binding 2"
location: "14q32.12"
module: 34
arm: "+"
pooled_cpm: 5.85
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# OTUB2

*OTU deubiquitinase, ubiquitin aldehyde binding 2* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +6.8, q 6e-09, up in 19 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.400× (z -10.9, q 1e-24, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WNT7B]] (+0.69, fdr 7e-06), [[WSCD1]] (+0.63, fdr 7e-06), [[RAC2]] (+0.60, fdr 1e-05); moves opposite to [[ZMYND11]] (-0.56, fdr 2e-05), [[NNMT]] (-0.53, fdr 3e-05), [[CEBPD]] (-0.49, fdr 4e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TTC19]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.8 | 6e-09 | 19/44 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 3e-04 | 15/42 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.002 | 9/36 (HEC-1-A, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.1 | 0.005 | 0/10 | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.30× | +3.2 | 0.16 | 7/43 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.22 | 2/42 (CFPAC-1, NCI-H2030) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.400×** | -10.9 | 1e-24 | 28/42 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -10.0 | 7e-21 | 31/44 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -8.9 | 9e-17 | 20/35 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -6.3 | 3e-08 | 20/43 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -5.5 | 4e-06 | 18/43 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -5.2 | 2e-05 | 16/36 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -5.0 | 5e-05 | 18/43 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -5.0 | 5e-05 | 15/34 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.679×** | -4.8 | 1e-04 | 16/44 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.517×** | -4.2 | 0.001 | 9/40 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.700×** | -4.1 | 0.002 | 12/41 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.714×** | -4.1 | 0.002 | 13/45 (COLO 205, SW 900, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.727×** | -3.8 | 0.007 | 15/28 (HOP62, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.801×** | -3.7 | 0.007 | 9/44 (SW 900, PANC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.727×** | -3.6 | 0.011 | 8/44 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.794×** | -3.5 | 0.014 | 12/44 (COLO 205, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.753×** | -3.5 | 0.016 | 12/42 (C32, SW 900, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 33.0 | 0 | 6 | — | [[Cobimetinib (drug)]] 5 µM 0.0128× (z -20.3) |
| [[PANC-1 (line)]] | alt | 9.53 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -10.6) |
| [[A549 (line)]] | wt | 7.73 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.3) |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.1000× (z -14.6) |
| [[HOP62 (line)]] | alt | 4.28 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0756× (z -9.6) ⚠ toxic · without an alert: [[(S)-Crizotinib (drug)]] 5 µM 0.0996× (z -8.6) |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 7.25 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 3.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 4.90 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0989× (z -9.0) |
| [[SW480 (line)]] | alt | 3.15 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0780× (z -11.6) |
| [[A-172 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT7B]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[WSCD1]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[RAC2]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SHB]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ARL4C]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[EPHB6]] | +0.60 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[CIB1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ITGA2]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[FAM107B]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LYPD3]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.56 | +0.60 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NNMT]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CEBPD]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DNAH5]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[THOC7]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[STXBP5]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[ATXN7]] | -0.47 | -0.44 / -0.42 | both halves | 4e-05 | pathway: Deubiquitination |
| [[HOPX]] | -0.47 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[CFLAR]] | -0.47 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[SORBS2]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC19]] | C | OTUB2's natural level weakens TTC19's drug response | OTUB2's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.36; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, -0.3); signed map (1.3, 46.5). **Vector** length 71.6, 11.6% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.1 | +1.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.9 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase, ubiquitin aldehyde binding 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:94,026,340-94,048,930 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21916, MGC3102; previously C14orf137 |
| Gene groups (HGNC) | OTU domain containing |
| Reactome | 2 pathways, smallest: Ovarian tumor domain proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DC9](https://www.uniprot.org/uniprotkb/Q96DC9) (Ubiquitin thioesterase OTUB2):

> Hydrolase that can remove conjugated ubiquitin from proteins in vitro and may therefore play an important regulatory role at the level of protein turnover by preventing degradation. Mediates deubiquitination of 'Lys-11'-,'Lys-48'- and 'Lys-63'-linked polyubiquitin chains, with a preference for 'Lys-63'-linked polyubiquitin chains.

**Summary**, from NCBI Gene [78990](https://www.ncbi.nlm.nih.gov/gene/78990):

> This gene encodes one of several deubiquitylating enzymes. Ubiquitin modification of proteins is needed for their stability and function; to reverse the process, deubiquityling enzymes remove ubiquitin. This protein contains an OTU domain and binds Ubal (ubiquitin aldehyde); an active cysteine protease site is present in the OTU domain. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:20351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20351) · Entrez [78990](https://www.ncbi.nlm.nih.gov/gene/78990) · UniProt [Q96DC9](https://www.uniprot.org/uniprotkb/Q96DC9) · Ensembl [ENSG00000089723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089723)

## Data

Gene col 1597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1597); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1597]; `tensor/DDL_lfc|DDL_z.npy` [1597]; `embed/gene_vectors.npy` [1597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1597 or target_col == 1597). Every well: [[OTUB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
