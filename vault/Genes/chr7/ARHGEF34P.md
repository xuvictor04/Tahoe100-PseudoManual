---
symbol: "ARHGEF34P"
type: "gene"
col: 12941
ensembl_id: "ENSG00000204959"
name: "Rho guanine nucleotide exchange factor 34, pseudogene"
location: "7q35"
module: 31
arm: "+"
pooled_cpm: 6.84
n_lines_expressing: 31
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 71
direction_downstream: 61
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ARHGEF34P

*Rho guanine nucleotide exchange factor 34, pseudogene* — 7q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Saquinavir (drug)]] 0.5 µM: 1.40× (z +4.6, q 0.003, up in 10 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.279× (z -17.5, q 0e+00, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF5]] (+0.86, fdr 7e-06), [[B3GNT3]] (+0.69, fdr 7e-06), [[INAVA]] (+0.68, fdr 7e-06); moves opposite to [[CHD1L]] (-0.56, fdr 3e-05), [[VEGFC]] (-0.51, fdr 8e-05), [[PDE3A]] (-0.50, fdr 3e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 71 arrows point to it, the strongest [[SLC6A14]] → it (grade B ⚠); 61 go from it, the strongest it → [[FGD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Saquinavir (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 0.003 | 10/24 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.4 | 0.003 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.011 | 6/27 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.9 | 0.011 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.5 | 0.048 | 2/26 (HCT15, PANC-1) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.048 | 6/25 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.4 | 0.048 | 2/22 (A-427, A498) | top dose only | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.048 | 3/27 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.048 | 5/27 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.54× | +3.1 | 0.10 | 1/16 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.10 | 1/24 (Panc 03.27) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.11 | 4/26 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.279×** | -17.5 | 0e+00 | 25/28 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.414×** | -12.1 | 4e-31 | 23/27 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.420×** | -11.9 | 3e-30 | 23/28 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -11.7 | 1e-29 | 20/25 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -9.6 | 1e-19 | 19/24 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.548×** | -8.2 | 2e-14 | 11/28 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -7.8 | 7e-13 | 17/23 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.579×** | -7.5 | 5e-12 | 14/26 (SW480, SNU-423, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.696×** | -5.0 | 4e-05 | 10/28 (SW480, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.706×** | -4.6 | 2e-04 | 12/25 (Panc 03.27, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -4.4 | 5e-04 | 8/27 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.731×** | -4.3 | 8e-04 | 11/28 (SW480, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -4.0 | 0.003 | 8/27 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.750×** | -4.0 | 0.003 | 5/25 (BT-474, SW480, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.754×** | -3.9 | 0.004 | 6/28 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.618×** | -3.5 | 0.018 | 7/24 (PANC-1, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.028 | 4/28 (H4, J82, …) | top dose only |  |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.788×** | -3.3 | 0.031 | 2/28 (J82, HT-29) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.790×** | -3.2 | 0.034 | 5/28 (SW480, NCI-H1792, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.639×** | -3.2 | 0.036 | 4/27 (A498, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 26.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0881× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.257× (z -14.3) |
| [[SW480 (line)]] | alt | 16.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0467× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.143× (z -15.9) |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.136× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 8.15 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0398× (z -12.6) |
| [[A498 (line)]] | wt | 11.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.209× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0801× (z -14.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 14.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -11.3) |
| [[SW1417 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SW48 (line)]] | wt | 17.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -9.0) |
| [[A-172 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF5]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | same gene group |
| [[B3GNT3]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[INAVA]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GPR35]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[VILL]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SDR16C5]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[LINC03040]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[FAM83B]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD1L]] | -0.56 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[VEGFC]] | -0.51 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[PDE3A]] | -0.50 | -0.56 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 20, C 51. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC6A14]] | B | SLC6A14 activity raises ARHGEF34P's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 3.46× lower at baseline in the lines without SLC6A14 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1 |
| [[ADCY4]] | B | ADCY4 activity raises ARHGEF34P's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.40× lower at baseline in the lines without ADCY4 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[PROM1]] | B | PROM1 activity raises ARHGEF34P's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.56× lower at baseline in the lines without PROM1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[GRAMD2B]] | B | GRAMD2B activity raises ARHGEF34P's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.11× lower at baseline in the lines without GRAMD2B | 0.014 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[LINC02474]] | B | LINC02474 activity raises ARHGEF34P's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 3.32× lower at baseline in the lines without LINC02474 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[DSG3]] | B | DSG3 activity raises ARHGEF34P's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 4.13× lower at baseline in the lines without DSG3 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[FAM83A]] | B | FAM83A activity raises ARHGEF34P's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 2.09× lower at baseline in the lines without FAM83A | 0.023 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[CCDC120]] | B | CCDC120 activity raises ARHGEF34P's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 2.95× lower at baseline in the lines without CCDC120 | 0.028 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[SLC28A3]] | B | SLC28A3 activity raises ARHGEF34P's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.90× lower at baseline in the lines without SLC28A3 | 0.031 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[KRT23]] | B | KRT23 activity raises ARHGEF34P's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.21× lower at baseline in the lines without KRT23 | 0.038 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[GPR87]] | B | GPR87 activity raises ARHGEF34P's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.26× lower at baseline in the lines without GPR87 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[ANXA3]] | B | ANXA3 activity raises ARHGEF34P's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.11× lower at baseline in the lines without ANXA3 | 0.044 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 20, C 41. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD4]] | B | ARHGEF34P activity raises FGD4's level | lines that do not express ARHGEF34P (19) vs lines expressing it (31) | 3.07× lower at baseline in the lines without ARHGEF34P | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A |
| [[EPS8L1]] | B | [[ARHGEF5]], ARHGEF34P activity raises EPS8L1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.90× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[ELMO3]] | B | [[ARHGEF5]], ARHGEF34P activity raises ELMO3's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.23× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[CCDC120]] | B | [[ARHGEF5]], ARHGEF34P activity raises CCDC120's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.36× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[STEAP1]] | B | [[ARHGEF5]], ARHGEF34P activity raises STEAP1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.49× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[FAM83E]] | B | [[ARHGEF5]], ARHGEF34P activity raises FAM83E's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.78× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[IQANK1]] | B | [[ARHGEF5]], ARHGEF34P activity raises IQANK1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.19× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[GRAMD2B]] | B | [[ARHGEF5]], ARHGEF34P activity raises GRAMD2B's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.47× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[ADCY4]] | B | [[ARHGEF5]], ARHGEF34P activity raises ADCY4's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.09× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[ARHGAP27]] | B | [[ARHGEF5]], ARHGEF34P activity raises ARHGAP27's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.36× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[ARHGEF16]] | B | [[ARHGEF5]], ARHGEF34P activity raises ARHGEF16's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.83× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[PDE10A]] | B | [[ARHGEF5]], ARHGEF34P activity lowers PDE10A's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.18× higher at baseline in the lines without ARHGEF5, ARHGEF34P | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.4, 55.4); signed map (57.7, 8.9). **Vector** length 53.6, 10.6% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | -7.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.4 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | -0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.3 | +2.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +1.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | -3.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -1.3 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.0 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.9 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 34, pseudogene |
| Locus type | pseudogene |
| Location | 7q35 — chr7:144,272,445-144,286,966 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:38086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38086) · Entrez [728377](https://www.ncbi.nlm.nih.gov/gene/728377) · Ensembl [ENSG00000204959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204959)

## Data

Gene col 12941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12941); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12941]; `tensor/DDL_lfc|DDL_z.npy` [12941]; `embed/gene_vectors.npy` [12941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12941 or target_col == 12941). Every well: [[ARHGEF34P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF34P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
