---
symbol: "ELK1"
type: "gene"
col: 4759
ensembl_id: "ENSG00000126767"
name: "ETS transcription factor ELK1"
location: "Xp11.23"
module: 76
arm: "+"
pooled_cpm: 18.46
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# ELK1

*ETS transcription factor ELK1* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.85× (z +16.1, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 0.5 µM: 0.824× (z -4.3, q 0.004, down in 12 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF384]] (+0.57, fdr 1e-05), [[FAAP20]] (+0.57, fdr 3e-05), [[EPN1]] (+0.57, fdr 3e-05); moves opposite to [[DENND1B]] (-0.60, fdr 3e-05), [[KIF21A]] (-0.59, fdr 1e-05), [[CLIP1]] (-0.57, fdr 3e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.85×** | +16.1 | 0e+00 | 44/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.70×** | +14.1 | 9e-43 | 41/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.14×** | +13.3 | 8e-38 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.3 | 8e-23 | 39/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +8.3 | 9e-15 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +7.3 | 3e-11 | 31/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +5.1 | 3e-05 | 18/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.8 | 1e-04 | 18/42 (SW1417, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.30×** | +4.3 | 9e-04 | 16/44 (NCI-H460, NCI-H23, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 17/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.24×** | +3.7 | 0.010 | 12/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +3.6 | 0.013 | 13/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4759.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.5 µM |  | **0.824×** | -4.3 | 0.004 | 12/48 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.777×** | -4.3 | 0.004 | 19/46 (RPMI-7951, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.777×** | -4.2 | 0.004 | 15/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -4.0 | 0.010 | 17/48 (A-427, COLO 205, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.798×** | -3.9 | 0.010 | 15/48 (HOP62, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.854× | -3.8 | 0.012 | 13/48 (HCT15, C32, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.809×** | -3.7 | 0.015 | 11/48 (SW 1271, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.814×** | -3.5 | 0.034 | 14/47 (SNU-423, RKO, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.875× | -3.3 | 0.053 | 14/48 (KATO III, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.878× | -3.3 | 0.063 | 11/48 (SW 1088, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.0 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.12× (z +13.2) | — |
| [[SW480 (line)]] | alt | 28.4 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 17.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +10.9) | — |
| [[A-427 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0840× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 37.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.40× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +8.5) | — |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF384]] | +0.57 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[FAAP20]] | +0.57 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[EPN1]] | +0.57 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[NAB2]] | +0.56 | +0.64 / +0.47 | both halves | 2e-05 | pathway: NGF-stimulated transcription |
| [[CHERP]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[PIK3R2]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 | pathway: ESR-mediated signaling |
| [[ADIPOR1]] | +0.54 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[AGPAT1]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ZNF865]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PIH1D1]] | +0.53 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PMPCA]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DCAF11]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND1B]] | -0.60 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[KIF21A]] | -0.59 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[CLIP1]] | -0.57 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[VRK2]] | -0.54 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[PRPF40A]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CCT6P3]] | -0.49 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[SHTN1]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CASP7]] | -0.47 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[PSMA4]] | -0.47 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DST]] | -0.46 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[LRRFIP2]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[YTHDC2]] | -0.46 | -0.58 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises ELK1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises ELK1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.5, -28.3); signed map (-44.7, 19.9). **Vector** length 71.9, 12.5% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +16.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +14.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.6 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.6 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ETS transcription factor ELK1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:47,635,521-47,650,604 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ETS transcription factor family |
| Reactome | 35 pathways, smallest: ERK/MAPK targets; Estrogen-dependent nuclear events downstream of ESR-membrane signaling; MAPK targets/ Nuclear events mediated by MAP kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P19419](https://www.uniprot.org/uniprotkb/P19419) (ETS domain-containing protein Elk-1):

> Transcription factor that binds to purine-rich DNA sequences. Forms a ternary complex with SRF and the ETS and SRF motifs of the serum response element (SRE) on the promoter region of immediate early genes such as FOS and IER2. Induces target gene transcription upon JNK and MAPK-signaling pathways stimulation.

**Summary**, from NCBI Gene [2002](https://www.ncbi.nlm.nih.gov/gene/2002):

> This gene is a member of the Ets family of transcription factors and of the ternary complex factor (TCF) subfamily. Proteins of the TCF subfamily form a ternary complex by binding to the the serum response factor and the serum response element in the promoter of the c-fos proto-oncogene. The protein encoded by this gene is a nuclear target for the ras-raf-MAPK signaling cascade. This gene produces multiple isoforms by using alternative translational start codons and by alternative splicing. …

**Accessions** — [HGNC:3321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3321) · Entrez [2002](https://www.ncbi.nlm.nih.gov/gene/2002) · UniProt [P19419](https://www.uniprot.org/uniprotkb/P19419) · Ensembl [ENSG00000126767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126767)

## Data

Gene col 4759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4759); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4759]; `tensor/DDL_lfc|DDL_z.npy` [4759]; `embed/gene_vectors.npy` [4759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4759 or target_col == 4759). Every well: [[ELK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
