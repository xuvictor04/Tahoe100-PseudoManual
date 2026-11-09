---
symbol: "FAXDC2"
type: "gene"
col: 9926
ensembl_id: "ENSG00000170271"
name: "fatty acid hydroxylase domain containing 2"
location: "5q33.2"
module: 21
arm: "+"
pooled_cpm: 5.75
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# FAXDC2

*fatty acid hydroxylase domain containing 2* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +13.4, q 3e-38, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.648× (z -5.6, q 6e-06, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP27A1]] (+0.62, fdr 1e-05), [[FMO5]] (+0.58, fdr 1e-05), [[ARSL]] (+0.58, fdr 2e-05); moves opposite to [[EEFSEC]] (-0.58, fdr 1e-05), [[PPM1G]] (-0.54, fdr 3e-05), [[UGGT2]] (-0.52, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[WFDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +13.4 | 3e-38 | 24/38 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +9.8 | 2e-20 | 3/12 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.9 | 1e-09 | 3/15 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.5 | 5e-06 | 9/26 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.31×** | +5.0 | 7e-05 | 11/44 (HT-29, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.036 | 11/45 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.036 | 3/47 (SNU-423, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.056 | 5/35 (SNU-423, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.078 | 1/42 (HEC-1-A) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.11 | 5/44 (SHP-77, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -5.6 | 6e-06 | 20/46 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.651×** | -5.6 | 6e-06 | 19/44 (C32, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -5.5 | 6e-06 | 17/45 (RPMI-7951, C32, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.660×** | -5.4 | 9e-06 | 17/46 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -5.3 | 1e-05 | 17/47 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.701×** | -4.5 | 8e-04 | 15/42 (COLO 205, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.727×** | -4.2 | 0.003 | 14/37 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.744×** | -3.9 | 0.008 | 11/39 (AN3 CA, CHP-212, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.737×** | -3.8 | 0.008 | 3/45 (RPMI-7951, LS 180, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -3.8 | 0.009 | 19/45 (RPMI-7951, CHP-212, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.762×** | -3.5 | 0.021 | 13/45 (COLO 205, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.3 | 0.039 | 7/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.075 | 14/44 (AN3 CA, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.793× | -3.0 | 0.10 | 12/45 (HT-29, AN3 CA, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -13.0) |
| [[AN3 CA (line)]] | alt | 36.2 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.0678× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 2.16× (z +11.1) ⚠ position not correctable | [[Homoharringtonine (drug)]] 0.05 µM 0.0937× (z -10.1) |
| [[A-172 (line)]] | wt | 5.18 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0462× (z -12.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 3.50 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0713× (z -11.1) |
| [[C32 (line)]] | wt | 12.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.117× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 5.19 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0781× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.6) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP27A1]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[FMO5]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ARSL]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FCGRT]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MYLK3]] | +0.55 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[MTCP1]] | +0.54 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[SGCD]] | +0.53 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[MYL6B]] | +0.53 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[IL17RE]] | +0.52 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[ACSM3]] | +0.52 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[FAM177B]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SERPINA5]] | +0.51 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PPM1G]] | -0.54 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[UGGT2]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[EDEM3]] | -0.52 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[ABCC10]] | -0.51 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[BMP2K]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[IQCH]] | -0.49 | -0.22 / -0.60 | both halves | 6e-04 |  |
| [[CMSS1]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[BCAP29]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ZBED4]] | -0.46 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ST3GAL3]] | -0.45 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PLGRKT]] | -0.45 | -0.47 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC2]] | B | WFDC2 activity raises FAXDC2's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.40× lower at baseline in the lines without WFDC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[IL17RE]] | B | IL17RE activity raises FAXDC2's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without IL17RE | 0.047 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[TF]] | B | TF activity raises FAXDC2's level | lines that do not express TF (41) vs lines expressing it (9) | 2.26× lower at baseline in the lines without TF | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.444). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, 52.6); signed map (60.7, -1.0). **Vector** length 59.3, 8.13% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.2 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -5.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid hydroxylase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,818,492-154,859,252 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13758; previously C5orf4 |
| Gene groups (HGNC) | Fatty acid hydroxylase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IV6](https://www.uniprot.org/uniprotkb/Q96IV6) (Fatty acid hydroxylase domain-containing protein 2):

> Promotes megakaryocyte differentiation by enhancing ERK phosphorylation and up-regulating RUNX1 expression.

**Summary**, from NCBI Gene [10826](https://www.ncbi.nlm.nih.gov/gene/10826):

> Predicted to enable C-4 methylsterol oxidase activity. Involved in positive regulation of megakaryocyte differentiation and positive regulation of protein phosphorylation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1334) · Entrez [10826](https://www.ncbi.nlm.nih.gov/gene/10826) · UniProt [Q96IV6](https://www.uniprot.org/uniprotkb/Q96IV6) · Ensembl [ENSG00000170271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170271)

## Data

Gene col 9926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9926); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9926]; `tensor/DDL_lfc|DDL_z.npy` [9926]; `embed/gene_vectors.npy` [9926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9926 or target_col == 9926). Every well: [[FAXDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAXDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
