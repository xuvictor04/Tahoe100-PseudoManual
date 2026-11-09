---
symbol: "RAB4A"
type: "gene"
col: 9602
ensembl_id: "ENSG00000168118"
name: "RAB4A, member RAS oncogene family"
location: "1q42.13"
module: 57
arm: "+"
pooled_cpm: 33.97
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# RAB4A

*RAB4A, member RAS oncogene family* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.85× (z +11.2, q 2e-26, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.55× (z +8.0, q 2e-13, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.625× (z -12.1, q 5e-31, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CROT]] (+0.71, fdr 7e-06), [[TMEM185A]] (+0.70, fdr 7e-06), [[STX7]] (+0.69, fdr 9e-06); moves opposite to [[MPDU1]] (-0.64, fdr 1e-05), [[MZF1-AS1]] (-0.64, fdr 6e-05), [[LETM2]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SYBU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +11.2 | 2e-26 | 34/44 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +9.5 | 9e-19 | 27/38 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +8.0 | 2e-13 | 36/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +6.6 | 6e-09 | 25/42 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +6.5 | 1e-08 | 31/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.9 | 4e-07 | 24/48 (CFPAC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.8 | 5e-07 | 30/47 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +5.0 | 4e-05 | 18/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +4.8 | 1e-04 | 22/45 (LS 180, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.3 | 0.001 | 25/45 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.001 | 20/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.0 | 0.003 | 19/46 (A498, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 16/48 (AN3 CA, C32, …) | all doses, stronger at high dose |  |
| [[OTS514 (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.004 | 16/44 (MIA PaCa-2, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.004 | 12/47 (LS 180, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.012 | 20/46 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.016 | 14/47 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.041 | 10/44 (SNU-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.063 | 7/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.063 | 9/46 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.625×** | -12.1 | 5e-31 | 36/47 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -7.9 | 1e-12 | 31/48 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.773×** | -4.7 | 5e-04 | 24/47 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.772×** | -4.5 | 8e-04 | 20/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.789×** | -4.3 | 0.002 | 21/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -4.2 | 0.002 | 18/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -3.6 | 0.031 | 14/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -11.3) |
| [[A-172 (line)]] | wt | 36.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -18.7) |
| [[HOP62 (line)]] | alt | 28.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.1) |
| [[PANC-1 (line)]] | alt | 42.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -9.6) |
| [[C32 (line)]] | wt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.3) |
| [[Hs 766T (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.455× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.3) |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.2) |
| [[SW480 (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROT]] | +0.71 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[STX7]] | +0.69 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ATP5F1C]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.68 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[SLC9A6]] | +0.67 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[PLA2G12A]] | +0.66 | +0.56 / +0.51 | both halves | 1e-05 | pathway: Phospholipid metabolism |
| [[MYPOP]] | +0.66 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[PAPSS1]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SDHB]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TMOD2]] | +0.64 | +0.45 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPDU1]] | -0.64 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.64 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[LETM2]] | -0.63 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[ACTR3-AS1]] | -0.63 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | -0.63 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[C6orf62]] | -0.62 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.61 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[HOMER1]] | -0.60 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[KRBOX5]] | -0.59 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[BOLA1]] | -0.59 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MEPCE]] | -0.58 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYBU]] | B | SYBU activity raises RAB4A's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without SYBU | 0.096 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.9, -7.3); signed map (-33.9, -13.1). **Vector** length 91.6, 20.6% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.3 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB4A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:229,271,062-229,305,894 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRES-1/RAB4; previously RAB4 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 13 pathways, smallest: MET receptor recycling; TBC/RABGAPs; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P20338](https://www.uniprot.org/uniprotkb/P20338) (Ras-related protein Rab-4A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB4A is involved in protein transport. Also plays a role in vesicular traffic. Mediates VEGFR2 endosomal trafficking …

**Summary**, from NCBI Gene [5867](https://www.ncbi.nlm.nih.gov/gene/5867):

> This gene is a member of the largest group in the Ras superfamily of small GTPases, which regulate membrane trafficking. The encoded protein is associated with early endosomes and is involved in their sorting and recycling. The protein also plays a role in regulating the recycling of receptors from endosomes to the plasma membrane. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:9781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9781) · Entrez [5867](https://www.ncbi.nlm.nih.gov/gene/5867) · UniProt [P20338](https://www.uniprot.org/uniprotkb/P20338) · Ensembl [ENSG00000168118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168118)

## Data

Gene col 9602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9602); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9602]; `tensor/DDL_lfc|DDL_z.npy` [9602]; `embed/gene_vectors.npy` [9602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9602 or target_col == 9602). Every well: [[RAB4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
