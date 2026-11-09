---
symbol: "TAF6L"
type: "gene"
col: 8491
ensembl_id: "ENSG00000162227"
name: "TATA-box binding protein associated factor 6 like"
location: "11q12.3"
module: 36
arm: "+"
pooled_cpm: 6.29
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TAF6L

*TATA-box binding protein associated factor 6 like* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.61× (z +7.0, q 2e-09, up in 21 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.590× (z -7.9, q 2e-12, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C2]] (+0.66, fdr 7e-06), [[SMIM7]] (+0.64, fdr 7e-06), [[CCDC12]] (+0.64, fdr 7e-06); moves opposite to [[RO60]] (-0.67, fdr 7e-06), [[CAV2]] (-0.58, fdr 1e-05), [[LEPROT]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +7.0 | 2e-09 | 21/42 (NCI-H1792, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +6.1 | 2e-07 | 15/34 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +6.1 | 2e-07 | 12/35 (HT-29, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.5 | 6e-06 | 16/47 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 1e-04 | 12/47 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 6e-04 | 14/46 (PANC-1, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.20× | +3.9 | 0.007 | 6/46 (LOX-IMVI, PANC-1, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.042 | 7/42 (A-427, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 1.47× | +3.1 | 0.11 | 3/44 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -7.9 | 2e-12 | 21/39 (NCI-H2030, SNU-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.648×** | -6.7 | 5e-09 | 16/40 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -6.5 | 1e-08 | 20/46 (HEC-1-A, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.661×** | -6.4 | 2e-08 | 20/47 (SW480, KATO III, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -5.8 | 7e-07 | 19/43 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.709×** | -5.3 | 9e-06 | 16/30 (SW1417, SW480, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.716×** | -5.2 | 2e-05 | 17/43 (SHP-77, SW 900, …) | rises with dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **0.750×** | -4.5 | 6e-04 | 13/44 (SHP-77, AN3 CA, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.761×** | -4.2 | 0.001 | 10/47 (SW 1271, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.759×** | -4.1 | 0.002 | 11/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.7 | 0.013 | 13/47 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.797×** | -3.5 | 0.020 | 9/46 (SW 900, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 6.13 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0804× (z -8.9) |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0844× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 3.81 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0969× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 6.88 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.113× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 5.07 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[PANC-1 (line)]] | alt | 7.85 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.288× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SHP-77 (line)]] | alt | 7.73 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0981× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 9.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 9.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C2]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SMIM7]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CCDC12]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CLASRP]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[CHST12]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ZFP64]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZBTB3]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 | ⚠ same locus (17.2 kb: neighbours can correlate without regulation) |
| [[PDPR2P]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[E2F6]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[HERC2P2]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[INPP5B]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PPIL2]] | +0.55 | +0.46 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RO60]] | -0.67 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[CAV2]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LEPROT]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[RAP2C]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[HIVEP2]] | -0.51 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[BIRC2]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ACTR2]] | -0.48 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TEAD1]] | -0.47 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[PRKAR1A]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[EEA1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[TAGLN2]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers TAF6L's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.441). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-31.8, -6.8); signed map (-16.8, -20.3). **Vector** length 59.3, 7.88% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +6.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.7 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 6 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,771,357-62,787,342 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAF65A |
| Gene groups (HGNC) | SAGA complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6J9](https://www.uniprot.org/uniprotkb/Q9Y6J9) (TAF6-like RNA polymerase II p300/CBP-associated factor-associated factor 65 kDa subunit 6L):

> Functions as a component of the PCAF complex. The PCAF complex is capable of efficiently acetylating histones in a nucleosomal context. The PCAF complex could be considered as the human version of the yeast SAGA complex (Probable). With TAF5L, acts as an epigenetic regulator essential for somatic reprogramming. Regulates target genes through H3K9ac deposition and MYC recruitment which trigger MYC regulatory network to orchestrate gene expression programs to control embryonic stem cell state. …

**Summary**, from NCBI Gene [10629](https://www.ncbi.nlm.nih.gov/gene/10629):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:17305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17305) · Entrez [10629](https://www.ncbi.nlm.nih.gov/gene/10629) · UniProt [Q9Y6J9](https://www.uniprot.org/uniprotkb/Q9Y6J9) · Ensembl [ENSG00000162227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162227)

## Data

Gene col 8491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8491); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8491]; `tensor/DDL_lfc|DDL_z.npy` [8491]; `embed/gene_vectors.npy` [8491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8491 or target_col == 8491). Every well: [[TAF6L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF6L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
