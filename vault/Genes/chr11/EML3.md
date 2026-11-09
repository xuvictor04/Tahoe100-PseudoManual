---
symbol: "EML3"
type: "gene"
col: 7379
ensembl_id: "ENSG00000149499"
name: "EMAP like 3"
location: "11q12.3"
module: 2
arm: "+"
pooled_cpm: 9.02
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# EML3

*EMAP like 3* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.69× (z +7.9, q 1e-12, up in 7 of 18 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.623× (z -7.5, q 5e-11, down in 23 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAH]] (+0.65, fdr 1e-05), [[NBEAL2]] (+0.63, fdr 1e-05), [[MAPK12]] (+0.61, fdr 1e-05); moves opposite to [[SNRPB2]] (-0.54, fdr 2e-05), [[TRIP11]] (-0.51, fdr 5e-05), [[NIPBL]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FKBP10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.9 | 1e-12 | 7/18 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.7 | 8e-09 | 15/31 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +5.4 | 1e-05 | 10/23 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.38×** | +4.9 | 2e-04 | 14/40 (SW1417, AsPC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.6 | 0.040 | 6/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.25 | 5/41 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -7.5 | 5e-11 | 23/43 (LOX-IMVI, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -4.9 | 3e-04 | 15/46 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.735×** | -4.7 | 5e-04 | 16/46 (HEC-1-A, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.814×** | -4.6 | 5e-04 | 20/46 (COLO 205, RKO, …) | all doses, flat | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.748×** | -4.6 | 5e-04 | 14/47 (HEC-1-A, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -4.2 | 0.003 | 10/46 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.603×** | -4.2 | 0.003 | 13/46 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -3.7 | 0.015 | 8/48 (A-427, SW 900, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -3.6 | 0.020 | 17/46 (A-172, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 11.7 | 0 | 2 | — | [[Allantoin (drug)]] 0.5 µM 0.101× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 5.59 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0948× (z -9.6) |
| [[RKO (line)]] | wt | 13.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 5.10 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.101× (z -11.6) |
| [[COLO 205 (line)]] | alt | 8.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -12.0) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HEC-1-A (line)]] | alt | 7.93 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.166× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.136× (z -10.8) |
| [[HT-29 (line)]] | alt | 8.85 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.300× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 8.32 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0849× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 9.26 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0597× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.13 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0700× (z -8.5) |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0713× (z -10.1) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAH]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 | same gene group |
| [[MAPK12]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TCF3]] | +0.60 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[AKT1]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ABCA2]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[PLXND1]] | +0.58 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[KAT2A]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 | STRING 479 |
| [[PEX5]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PCGF2]] | +0.55 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.55 | +0.54 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB2]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TRIP11]] | -0.51 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[NIPBL]] | -0.49 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[PPCS]] | -0.48 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[MPLKIP]] | -0.48 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[FAM200A]] | -0.48 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[H3-3B]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CKMT2-AS1]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SNW1]] | -0.47 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[REST]] | -0.47 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[GOLGB1]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PIGBOS1]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP10]] | B | FKBP10 activity raises EML3's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without FKBP10 | 0.040 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[DLG4]] | C | DLG4 activity raises EML3's level | lines that do not express DLG4 (3) vs lines expressing it (46) | 1.37× lower at baseline in the lines without DLG4 | 0.091 | ⚠ few lines (3 vs 46); within organs, on part of the lines; also absent: CHST14, NECAB2, DMXL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.8, -24.6); signed map (-44.6, -9.9). **Vector** length 57.7, 7.38% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | +2.4 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | EMAP like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,602,218-62,612,775 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35827, ELP95 |
| Gene groups (HGNC) | WD repeat domain containing; EMAP like |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32P44](https://www.uniprot.org/uniprotkb/Q32P44) (Echinoderm microtubule-associated protein-like 3):

> Regulates mitotic spindle assembly, microtubule (MT)-kinetochore attachment and chromosome separation via recruitment of HAUS augmin-like complex and TUBG1 to the existing MTs and promoting MT-based MT nucleation. Required for proper alignnment of chromosomes during metaphase.

**Summary**, from NCBI Gene [256364](https://www.ncbi.nlm.nih.gov/gene/256364):

> Predicted to enable microtubule binding activity. Involved in mitotic metaphase chromosome alignment and regulation of mitotic spindle assembly. Located in several cellular components, including midbody; mitotic spindle microtubule; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26666) · Entrez [256364](https://www.ncbi.nlm.nih.gov/gene/256364) · UniProt [Q32P44](https://www.uniprot.org/uniprotkb/Q32P44) · Ensembl [ENSG00000149499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149499)

## Data

Gene col 7379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7379); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7379]; `tensor/DDL_lfc|DDL_z.npy` [7379]; `embed/gene_vectors.npy` [7379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7379 or target_col == 7379). Every well: [[EML3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EML3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
