---
symbol: "SCAP"
type: "gene"
col: 3572
ensembl_id: "ENSG00000114650"
name: "SREBF chaperone"
location: "3p21.31"
module: 33
arm: "+"
pooled_cpm: 25.23
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SCAP

*SREBF chaperone* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.95× (z +12.5, q 3e-33, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.690× (z -7.0, q 2e-09, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGES2]] (+0.70, fdr 1e-05), [[FXN]] (+0.69, fdr 7e-06), [[ASB13]] (+0.68, fdr 7e-06); moves opposite to [[MRPS6]] (-0.62, fdr 7e-06), [[KRBOX5]] (-0.61, fdr 2e-05), [[LINC00310]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RNFT2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3572.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +12.5 | 3e-33 | 41/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +11.9 | 2e-30 | 43/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +10.0 | 2e-21 | 39/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +9.5 | 4e-19 | 41/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +9.1 | 7e-18 | 30/46 (RKO, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +7.9 | 3e-13 | 32/47 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.8 | 7e-10 | 29/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +6.2 | 3e-08 | 25/48 (NCI-H2347, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.7 | 6e-07 | 25/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **1.26×** | +4.2 | 0.002 | 18/46 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.008 | 11/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.011 | 10/48 (HepG2/C3A, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.036 | 11/47 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.2 | 0.066 | 10/48 (NCI-H2347, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -7.0 | 2e-09 | 27/47 (SW480, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -6.4 | 4e-08 | 25/48 (SNU-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.785×** | -4.6 | 1e-03 | 20/46 (KATO III, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.089 | 15/48 (SW 1271, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.3 | 0.11 | 13/47 (CHP-212, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 24.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.10× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 42.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -12.4) |
| [[A-427 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0904× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0963× (z -9.6) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0595× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 39.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.423× (z -10.1) |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGES2]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[FXN]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ASB13]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.66 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[EXOSC5]] | +0.65 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[COG2]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[LSM12]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.65 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MRPL4]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[HEATR3]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS6]] | -0.62 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[KRBOX5]] | -0.61 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[LINC00310]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CFAP53]] | -0.58 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C6orf62]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[NPHS1]] | -0.57 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[LRIF1]] | -0.57 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[BOLA1]] | -0.56 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ZNF341-AS1]] | -0.56 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[OFD1]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NOTCH2NLB]] | -0.54 | -0.53 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNFT2]] | C | RNFT2 activity raises SCAP's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without RNFT2 | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |
| [[TSEN2]] | C | TSEN2 activity raises SCAP's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.2, -40.5); signed map (-9.0, -52.9). **Vector** length 92.7, 20.0% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +9.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +11.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +6.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.1 | -1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SREBF chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:47,413,681-47,477,126 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0199 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 7 pathways, smallest: Maturation of DENV proteins; Regulation of cholesterol biosynthesis by SREBP (SREBF); Dengue Virus Genome Translation and Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12770](https://www.uniprot.org/uniprotkb/Q12770) (Sterol regulatory element-binding protein cleavage-activating protein):

> Escort protein required for cholesterol as well as lipid homeostasis (By similarity). Regulates export of the SCAP-SREBP complex from the endoplasmic reticulum to the Golgi upon low cholesterol, thereby regulating the processing of sterol regulatory element-binding proteins (SREBPs) SREBF1/SREBP1 and SREBF2/SREBP2. At high sterol concentrations, formation of a ternary complex with INSIG (INSIG1 or INSIG2) leads to mask the ER export signal in SCAP, promoting retention of the complex in the …

**Summary**, from NCBI Gene [22937](https://www.ncbi.nlm.nih.gov/gene/22937):

> This gene encodes a protein with a sterol sensing domain (SSD) and seven WD domains. In the presence of cholesterol, this protein binds to sterol regulatory element binding proteins (SREBPs) and mediates their transport from the ER to the Golgi. The SREBPs are then proteolytically cleaved and regulate sterol biosynthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:30634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30634) · Entrez [22937](https://www.ncbi.nlm.nih.gov/gene/22937) · UniProt [Q12770](https://www.uniprot.org/uniprotkb/Q12770) · Ensembl [ENSG00000114650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114650)

## Data

Gene col 3572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3572); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3572]; `tensor/DDL_lfc|DDL_z.npy` [3572]; `embed/gene_vectors.npy` [3572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3572 or target_col == 3572). Every well: [[SCAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
