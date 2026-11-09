---
symbol: "PAQR8"
type: "gene"
col: 10025
ensembl_id: "ENSG00000170915"
name: "progestin and adipoQ receptor family member 8"
location: "6p12.2"
module: 27
arm: "+"
pooled_cpm: 2.21
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PAQR8

*progestin and adipoQ receptor family member 8* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.71× (z +7.2, q 4e-10, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +4.6, q 0.001, up in 12 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.288× (z -9.4, q 4e-18, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM139]] (+0.57, fdr 4e-05), [[DNAH6]] (+0.52, fdr 2e-05), [[MROH7]] (+0.50, fdr 6e-05); moves opposite to [[SLC30A6]] (-0.47, fdr 3e-05), [[TRMT2B]] (-0.47, fdr 3e-05), [[ZCCHC17]] (-0.47, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[VSNL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +7.2 | 4e-10 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +4.6 | 0.001 | 12/40 (COLO 205, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.032 | 6/27 (HepG2/C3A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.54× | +3.3 | 0.14 | 6/33 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.54× | +3.0 | 0.24 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.49× | +3.0 | 0.24 | 2/22 (RPMI-7951, COLO 205) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.288×** | -9.4 | 4e-18 | 30/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.327×** | -8.4 | 1e-14 | 26/38 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.383×** | -7.2 | 9e-11 | 24/37 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.377×** | -6.9 | 6e-10 | 22/33 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -6.7 | 2e-09 | 16/20 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.420×** | -6.5 | 7e-09 | 21/37 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.287×** | -4.9 | 7e-05 | 15/26 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -4.2 | 0.002 | 17/31 (LS 180, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.589×** | -4.0 | 0.004 | 13/40 (HT-29, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.599×** | -3.8 | 0.007 | 18/34 (HS-578T, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.601×** | -3.4 | 0.034 | 12/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.607×** | -3.3 | 0.040 | 14/40 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.632×** | -3.3 | 0.050 | 9/37 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.748×** | -3.1 | 0.089 | 15/29 (LS 180, HEC-1-A, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 6.16 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -11.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 3.58 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0280× (z -15.5) |
| [[LoVo (line)]] | wt | 4.83 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0414× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 2.82 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0505× (z -9.2) |
| [[COLO 205 (line)]] | alt | 9.97 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0541× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 2.01 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -10.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0318× (z -10.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.843 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.633 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.574 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM139]] | +0.57 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[DNAH6]] | +0.52 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[MROH7]] | +0.50 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[TMEM232]] | +0.49 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MYB]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[VIL1]] | +0.48 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[LINC02940]] | +0.47 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[PCK1]] | +0.46 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[SMOC2]] | +0.46 | +0.49 / +0.40 | both halves | 4e-05 |  |
| [[LINC01819]] | +0.46 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[LINC00299]] | +0.46 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[LINC00923]] | +0.46 | +0.46 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A6]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TRMT2B]] | -0.47 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ZCCHC17]] | -0.47 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[UBE2M]] | -0.47 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[FLYWCH1]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD39]] | -0.45 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[BABAM1]] | -0.45 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ASB16-AS1]] | -0.44 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[PSMB5]] | -0.44 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ERCC3]] | -0.44 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PHTF1]] | -0.43 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[UFD1]] | -0.43 | -0.47 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSNL1]] | B | VSNL1 activity raises PAQR8's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 1.57× lower at baseline in the lines without VSNL1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[PCK1]] | B | PCK1 activity raises PAQR8's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without PCK1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2 |
| [[LINC00299]] | B | LINC00299 activity raises PAQR8's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without LINC00299 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.453). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.2, 39.9); signed map (56.0, 17.1). **Vector** length 43.5, 5.40% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -8.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -7.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | progestin and adipoQ receptor family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.2 — chr6:52,361,421-52,407,777 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LMPB1, MPRB; previously C6orf33 |
| Gene groups (HGNC) | Progestin and adipoQ receptor family; PAQR family membrane progesterone receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEZ7](https://www.uniprot.org/uniprotkb/Q8TEZ7) (Membrane progestin receptor beta):

> Plasma membrane progesterone (P4) receptor coupled to G proteins. Seems to act through a G(i) mediated pathway. May be involved in oocyte maturation (By similarity). Also binds dehydroepiandrosterone (DHEA), pregnanolone, pregnenolone and allopregnanolone.

**Summary**, from NCBI Gene [85315](https://www.ncbi.nlm.nih.gov/gene/85315):

> Predicted to enable nuclear steroid receptor activity and steroid binding activity. Predicted to be involved in response to steroid hormone. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15708) · Entrez [85315](https://www.ncbi.nlm.nih.gov/gene/85315) · UniProt [Q8TEZ7](https://www.uniprot.org/uniprotkb/Q8TEZ7) · Ensembl [ENSG00000170915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170915)

## Data

Gene col 10025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10025); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10025]; `tensor/DDL_lfc|DDL_z.npy` [10025]; `embed/gene_vectors.npy` [10025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10025 or target_col == 10025). Every well: [[PAQR8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAQR8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
