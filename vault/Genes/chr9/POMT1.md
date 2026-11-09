---
symbol: "POMT1"
type: "gene"
col: 5104
ensembl_id: "ENSG00000130714"
name: "protein O-mannosyltransferase 1"
location: "9q34.13"
module: 207
arm: "+"
pooled_cpm: 16.77
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# POMT1

*protein O-mannosyltransferase 1* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.23× (z +5.2, q 1e-04, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.568× (z -9.5, q 8e-19, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLE1]] (+0.61, fdr 1e-05), [[HDAC10]] (+0.59, fdr 1e-05), [[TRMU]] (+0.57, fdr 1e-05); moves opposite to [[STK3]] (-0.51, fdr 3e-05), [[AIG1]] (-0.49, fdr 2e-04), [[EID1]] (-0.48, fdr 6e-05).
> It sits in the **+** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FGD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.2 | 1e-04 | 16/45 (HT-29, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.20×** | +4.6 | 0.001 | 20/47 (CFPAC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -9.5 | 8e-19 | 30/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.581×** | -9.5 | 8e-19 | 30/46 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.588×** | -9.3 | 3e-18 | 31/46 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.632×** | -8.0 | 2e-13 | 25/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.654×** | -7.4 | 1e-11 | 29/46 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.666×** | -7.1 | 1e-10 | 28/46 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.674×** | -6.9 | 5e-10 | 29/46 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.691×** | -6.4 | 8e-09 | 20/39 (HEC-1-A, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.688×** | -6.3 | 2e-08 | 24/45 (C32, AN3 CA, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -5.5 | 2e-06 | 23/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -5.3 | 8e-06 | 18/47 (Hs 766T, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.766×** | -4.6 | 2e-04 | 18/45 (J82, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.770×** | -4.6 | 2e-04 | 16/47 (HEC-1-A, C-33 A, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.759×** | -4.4 | 4e-04 | 18/34 (A549, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -4.4 | 5e-04 | 16/47 (C32, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -4.2 | 8e-04 | 15/47 (AN3 CA, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.787×** | -4.2 | 0.001 | 15/46 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.802×** | -3.7 | 0.007 | 17/46 (C-33 A, CHP-212, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.828×** | -3.3 | 0.029 | 6/47 (NCI-H661, COLO 205, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.829×** | -3.3 | 0.030 | 8/46 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.880× | -3.1 | 0.042 | 9/47 (MIA PaCa-2, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 2 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0712× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.203× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.280× (z -10.1) |
| [[A-172 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.105× (z -9.5) |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0917× (z -10.3) |
| [[KATO III (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -9.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLE1]] | +0.61 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HDAC10]] | +0.59 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TRMU]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[VDAC1P8]] | +0.55 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ZFYVE21]] | +0.55 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[TMEM94]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[TIAL1]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[CUL7]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ITGAE]] | +0.52 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[MED24]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[IKZF4]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[SUOX]] | +0.50 | +0.34 / +0.55 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK3]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[AIG1]] | -0.49 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[EID1]] | -0.48 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[RASAL2]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[C11orf96]] | -0.48 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[ADNP2]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SKIL]] | -0.47 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[SEMA3C]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ATP7A]] | -0.47 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[RAB31]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[NFE2L2]] | -0.46 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[RANBP6]] | -0.45 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD1]] | B | FGD1 activity raises POMT1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without FGD1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-4.8, -20.9); signed map (-26.3, -0.3). **Vector** length 65.4, 10.2% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.8 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | -0.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.1 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -9.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein O-mannosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:131,502,789-131,523,806 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LGMD2K |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases |
| Reactome | 18 pathways, smallest: Defective POMT1 causes MDDGA1, MDDGB1 and MDDGC1; Defective POMT2 causes MDDGA2, MDDGB2 and MDDGC2; DAG1 core M1 glycosylations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6A1](https://www.uniprot.org/uniprotkb/Q9Y6A1) (Protein O-mannosyl-transferase 1):

> Transfers mannosyl residues to the hydroxyl group of serine or threonine residues. Coexpression of both POMT1 and POMT2 is necessary for enzyme activity, expression of either POMT1 or POMT2 alone is insufficient. Essentially dedicated to O-mannosylation of alpha-DAG1 and few other proteins but not of cadherins and protocaherins.

**Summary**, from NCBI Gene [10585](https://www.ncbi.nlm.nih.gov/gene/10585):

> The protein encoded by this gene is an O-mannosyltransferase that requires interaction with the product of the POMT2 gene for enzymatic function. The encoded protein is found in the membrane of the endoplasmic reticulum. Defects in this gene are a cause of Walker-Warburg syndrome (WWS) and limb-girdle muscular dystrophy type 2K (LGMD2K). Several transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:9202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9202) · Entrez [10585](https://www.ncbi.nlm.nih.gov/gene/10585) · UniProt [Q9Y6A1](https://www.uniprot.org/uniprotkb/Q9Y6A1) · Ensembl [ENSG00000130714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130714)

## Data

Gene col 5104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5104); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5104]; `tensor/DDL_lfc|DDL_z.npy` [5104]; `embed/gene_vectors.npy` [5104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5104 or target_col == 5104). Every well: [[POMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
