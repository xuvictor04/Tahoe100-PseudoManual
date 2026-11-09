---
symbol: "CASTOR2"
type: "gene"
col: 15808
ensembl_id: "ENSG00000274070"
name: "cytosolic arginine sensor for mTORC1 subunit 2"
location: "7q11.23"
module: 145
arm: "+"
pooled_cpm: 13.37
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 6
n_dd_up_clean: 29
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# CASTOR2

*cytosolic arginine sensor for mTORC1 subunit 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.82× (z +30.8, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.659× (z -6.8, q 5e-09, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2IP4]] (+0.73, fdr 7e-06), [[AGAP3]] (+0.63, fdr 1e-05), [[PINK1]] (+0.61, fdr 3e-05); moves opposite to [[TRMT5]] (-0.61, fdr 3e-05), [[FASTKD2]] (-0.56, fdr 1e-04), [[THADA]] (-0.56, fdr 3e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LRP10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.82×** | +30.8 | 0e+00 | 45/47 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.80×** | +25.5 | 0e+00 | 46/47 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.78×** | +25.4 | 0e+00 | 46/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.63×** | +24.9 | 0e+00 | 45/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.12×** | +18.5 | 0e+00 | 44/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **3.08×** | +18.3 | 0e+00 | 44/47 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +11.7 | 1e-29 | 15/22 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +11.2 | 2e-27 | 33/46 (C32, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +10.9 | 8e-26 | 23/38 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.12×** | +9.7 | 3e-20 | 35/48 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +9.5 | 7e-20 | 31/47 (SNU-423, C32, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.75×** | +9.1 | 6e-18 | 34/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.8 | 3e-13 | 29/47 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +7.2 | 2e-11 | 23/48 (A498, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +7.0 | 1e-10 | 23/47 (PANC-1, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.9 | 1e-07 | 19/48 (BT-474, HOP62, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.78×** | +4.9 | 3e-05 | 12/45 (A498, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.659×** | -6.8 | 5e-09 | 25/47 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.756×** | -4.6 | 0.001 | 18/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.626×** | -4.0 | 0.011 | 12/45 (A-427, H4, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.802×** | -3.6 | 0.035 | 15/47 (SW1417, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.803×** | -3.6 | 0.035 | 15/47 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.079 | 18/46 (SNU-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.827× | -3.1 | 0.12 | 9/47 (SW 1271, A498, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.1 | 0.12 | 8/48 (PANC-1, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.6 | 7 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.54× (z +12.7) | — |
| [[A-172 (line)]] | wt | 13.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 10.5 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.64× (z +19.7) | — |
| [[C32 (line)]] | wt | 13.0 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.53× (z +14.9) | [[Rosiglitazone (drug)]] 5 µM 0.162× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 9.75 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 15.0 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 4.17× (z +11.5) | [[Pralsetinib (drug)]] 5 µM 0.132× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 26.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 7.48 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +13.0) | — |
| [[KATO III (line)]] | alt | 10.8 | 4 | 0 | [[Belinostat (drug)]] 5 µM 6.43× (z +9.4) | — |
| [[LoVo (line)]] | wt | 12.6 | 4 | 0 | [[Belinostat (drug)]] 5 µM 4.99× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 5.82 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.31× (z +11.4) | — |
| [[A549 (line)]] | wt | 7.37 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.64× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 4.98 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.8× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.06× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 2 (1 ⚠) | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0610× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 11.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +9.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.171× (z -8.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 10.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +9.5) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0955× (z -10.4) |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -11.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 5.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 8.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 6.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.02× (z +8.5) | — |
| [[J82 (line)]] | alt | 6.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 8.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 9.08 | 1 | 0 | [[Belinostat (drug)]] 5 µM 4.96× (z +8.9) | — |
| [[RKO (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 5.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.8) | — |
| [[SW48 (line)]] | wt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IP4]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[AGAP3]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PINK1]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[WIPI2]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[WDTC1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HAGH]] | +0.58 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[UBTD1]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[PTOV1]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[MXD4]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[FBXL20]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NOL4L]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT5]] | -0.61 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[FASTKD2]] | -0.56 | -0.33 / -0.64 | both halves | 1e-04 |  |
| [[THADA]] | -0.56 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[NOL11]] | -0.56 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[DCLRE1A]] | -0.56 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[ARL14EP]] | -0.55 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[ZNF614]] | -0.54 | -0.32 / -0.61 | both halves | 1e-04 |  |
| [[YTHDC2]] | -0.54 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[ZNF678]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[KICS2]] | -0.54 | -0.35 / -0.57 | both halves | 1e-04 | pathway: Amino acids regulate mTORC1; STRING 741 |
| [[POLI]] | -0.54 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[PAK1IP1]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CASTOR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TIMP2]] | C | TIMP2 activity raises CASTOR2's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 1.86× lower at baseline in the lines without TIMP2 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |
| [[KICS2]] | C | KICS2's natural level strengthens CASTOR2's drug response | KICS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.20; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP10]] | C | CASTOR2's natural level weakens LRP10's drug response | CASTOR2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.20; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, -43.6); signed map (-18.1, 13.9). **Vector** length 85.4, 19.2% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +18.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +9.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +7.0 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +9.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -7.3 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic arginine sensor for mTORC1 subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,964,705-75,031,528 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GATSL1, GATSL2 |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NHX0](https://www.uniprot.org/uniprotkb/A6NHX0) (Cytosolic arginine sensor for mTORC1 subunit 2):

> Functions as a negative regulator of the TORC1 signaling pathway through the GATOR complex. As part of homodimers or heterodimers with CASTOR1, directly binds and inhibits the GATOR subcomplex GATOR2 and thereby mTORC1. Does not directly bind arginine, but binding of arginine to CASTOR1 disrupts the interaction of CASTOR2-containing heterodimers with GATOR2 which can in turn activate mTORC1 and the TORC1 signaling pathway.

**Summary**, from NCBI Gene [729438](https://www.ncbi.nlm.nih.gov/gene/729438):

> Enables identical protein binding activity. Involved in cellular response to L-arginine and negative regulation of TORC1 signaling. Located in GATOR2 complex and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37073) · Entrez [729438](https://www.ncbi.nlm.nih.gov/gene/729438) · UniProt [A6NHX0](https://www.uniprot.org/uniprotkb/A6NHX0) · Ensembl [ENSG00000274070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274070)

## Data

Gene col 15808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15808); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15808]; `tensor/DDL_lfc|DDL_z.npy` [15808]; `embed/gene_vectors.npy` [15808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15808 or target_col == 15808). Every well: [[CASTOR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASTOR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
