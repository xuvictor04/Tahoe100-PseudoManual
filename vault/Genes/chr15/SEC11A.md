---
symbol: "SEC11A"
type: "gene"
col: 6438
ensembl_id: "ENSG00000140612"
name: "SEC11 homolog A, signal peptidase complex subunit"
location: "15q25.2"
module: 168
arm: "+"
pooled_cpm: 91.12
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# SEC11A

*SEC11 homolog A, signal peptidase complex subunit* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.70× (z +9.1, q 7e-17, up in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.67× (z +8.8, q 4e-16, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.748× (z -7.1, q 9e-10, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX1]] (+0.81, fdr 7e-06), [[DHRS1]] (+0.78, fdr 7e-06), [[SDHAP1]] (+0.75, fdr 7e-06); moves opposite to [[ZXDB]] (-0.72, fdr 7e-06), [[ERCC6L2]] (-0.72, fdr 7e-06), [[ZC3H11A]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KRT86]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +9.1 | 7e-17 | 41/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +8.8 | 4e-16 | 41/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +7.0 | 4e-10 | 41/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.45×** | +6.3 | 4e-08 | 37/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.43×** | +6.2 | 8e-08 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.7 | 1e-06 | 31/47 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +5.6 | 2e-06 | 35/49 (KATO III, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 34/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +4.5 | 4e-04 | 28/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.002 | 27/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.29×** | +4.1 | 0.002 | 23/45 (LoVo, KATO III, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.33×** | +4.0 | 0.003 | 24/49 (NCI-H460, A549, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +4.0 | 0.003 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.6 | 0.011 | 19/38 (SW480, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.018 | 23/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.031 | 8/49 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.040 | 7/49 (NCI-H2030, C32, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.069 | 17/48 (SHP-77, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.748×** | -7.1 | 9e-10 | 35/48 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.787×** | -4.1 | 0.011 | 26/48 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.794×** | -3.8 | 0.026 | 25/48 (AN3 CA, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.086 | 21/48 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.832× | -3.2 | 0.15 | 16/48 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.823× | -3.2 | 0.15 | 19/47 (A-427, A549, …) | inconsistent across doses |  |
| [[Finasteride (drug)]] 5 µM |  | 0.831× | -3.1 | 0.18 | 13/48 (KATO III, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.6 | 7 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.41× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.07× (z +8.5) | — |
| [[SW480 (line)]] | alt | 85.9 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.82× (z +9.4) | — |
| [[LoVo (line)]] | wt | 94.6 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.63× (z +10.5) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 75.7 | 2 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.41× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.634× (z -8.6) |
| [[KATO III (line)]] | alt | 77.6 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 80.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 1088 (line)]] | alt | 86.2 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0779× (z -9.2) |
| [[A549 (line)]] | wt | 132 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[COLO 205 (line)]] | alt | 85.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 80.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -8.6) |
| [[J82 (line)]] | alt | 97.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 85.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.67× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.71× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 75.1 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX1]] | +0.81 | +0.85 / +0.68 | both halves | 7e-06 |  |
| [[DHRS1]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.75 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.75 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.74 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[KCTD7]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[RAP1A]] | +0.71 | +0.77 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDB]] | -0.72 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.72 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[ZC3H11A]] | -0.71 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[MED1]] | -0.70 | -0.68 / -0.69 | both halves | 7e-06 | pathway: Respiratory Syncytial Virus Infection Pathway |
| [[RPL7L1]] | -0.70 | -0.76 / -0.58 | both halves | 7e-06 |  |
| [[TASOR]] | -0.69 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[SRCAP]] | -0.68 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[MIS12]] | -0.68 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[LZIC]] | -0.67 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[ZNF614]] | -0.67 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[ICE2]] | -0.66 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[DCAF8]] | -0.66 | -0.60 / -0.57 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT86]] | B | KRT86 activity raises SEC11A's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 1.20× lower at baseline in the lines without KRT86 | 0.040 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.3, -14.3); signed map (-38.2, -1.4). **Vector** length 112, 34.0% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.2 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.4 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.1 | -7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.7 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.8 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | SEC11 homolog A, signal peptidase complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:84,669,538-84,716,460 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPC18, sid2895, SPCS4A; previously SEC11L1 |
| Hallmark sets | PANCREAS_BETA_CELLS, UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 22 pathways, smallest: Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP); Synthesis, secretion, and deacylation of Ghrelin; Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1) |
| Matched by | ensembl_id |

**Function**, from UniProt [P67812](https://www.uniprot.org/uniprotkb/P67812) (Signal peptidase complex catalytic subunit SEC11A):

> Catalytic component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum. Specifically cleaves N-terminal signal peptides that contain a hydrophobic alpha-helix (h-region) shorter than 18-20 amino acids.

**Summary**, from NCBI Gene [23478](https://www.ncbi.nlm.nih.gov/gene/23478):

> This gene encodes a member of the peptidase S26B family. The encoded protein is an 18kDa subunit of the signal peptidase complex and has been linked to cell migration and invasion, gastric cancer and lymph node metastasis. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 8. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:17718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17718) · Entrez [23478](https://www.ncbi.nlm.nih.gov/gene/23478) · UniProt [P67812](https://www.uniprot.org/uniprotkb/P67812) · Ensembl [ENSG00000140612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140612)

## Data

Gene col 6438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6438); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6438]; `tensor/DDL_lfc|DDL_z.npy` [6438]; `embed/gene_vectors.npy` [6438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6438 or target_col == 6438). Every well: [[SEC11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
