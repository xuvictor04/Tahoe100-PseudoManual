---
symbol: "FKBP1B"
type: "gene"
col: 4120
ensembl_id: "ENSG00000119782"
name: "FKBP prolyl isomerase 1B"
location: "2p23.3"
module: 192
arm: "+"
pooled_cpm: 4.74
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# FKBP1B

*FKBP prolyl isomerase 1B* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.50× (z +9.7, q 2e-19, up in 22 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.520× (z -6.9, q 3e-09, down in 21 of 32 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC11]] (+0.64, fdr 1e-05), [[CORO2A]] (+0.62, fdr 2e-05), [[RRAS]] (+0.61, fdr 1e-04); moves opposite to [[ANAPC7]] (-0.54, fdr 5e-05), [[CPSF2]] (-0.54, fdr 9e-05), [[ZFP91]] (-0.54, fdr 3e-04).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MT1F]] → it (grade B ⚠); 6 go from it, the strongest it → [[PLCD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +9.7 | 2e-19 | 22/32 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +8.2 | 1e-13 | 24/33 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +7.7 | 3e-12 | 18/32 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.8 | 1e-09 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +6.3 | 3e-08 | 16/32 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.2 | 4e-08 | 5/21 (A549, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 8e-07 | 12/30 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.4 | 9e-04 | 10/32 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +3.9 | 0.006 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.8 | 0.008 | 6/29 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.009 | 7/27 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.5 | 0.023 | 3/20 (NCI-H1792, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.023 | 11/31 (NCI-H23, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.023 | 1/30 (A-427) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.031 | 7/30 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.038 | 8/32 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.043 | 2/22 (Hs 766T, MIA PaCa-2) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.047 | 6/30 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.053 | 3/33 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.064 | 3/26 (NCI-H2030, NCI-H23, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -6.9 | 3e-09 | 21/32 (SNU-423, KATO III, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.316×** | -6.4 | 6e-08 | 22/29 (KATO III, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.569×** | -6.0 | 5e-07 | 19/30 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.580×** | -5.8 | 1e-06 | 21/32 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.569×** | -5.7 | 1e-06 | 18/31 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.363×** | -5.6 | 2e-06 | 15/25 (Panc 03.27, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -4.4 | 7e-04 | 17/26 (HOP62, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.666×** | -4.3 | 0.001 | 11/32 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -4.0 | 0.004 | 16/32 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.709×** | -3.6 | 0.017 | 12/32 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -3.2 | 0.062 | 8/32 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -3.2 | 0.062 | 11/30 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.21 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0607× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.121× (z -8.7) |
| [[KATO III (line)]] | alt | 17.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -11.3) |
| [[A549 (line)]] | wt | 5.04 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0843× (z -8.8) |
| [[HOP62 (line)]] | alt | 6.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 10.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0714× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0673× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 8.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0627× (z -9.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 3.46 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0407× (z -10.2) |
| [[SW480 (line)]] | alt | 7.44 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.982 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC11]] | +0.64 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[CORO2A]] | +0.62 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[RRAS]] | +0.61 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[KLC3]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ETNK2]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.58 | +0.39 / +0.55 | both halves | 6e-05 | pathway: Cardiac conduction |
| [[MT1F]] | +0.58 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[SLC8B1]] | +0.58 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[SLC66A1L]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TMSB10]] | +0.58 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[DNASE1L1]] | +0.57 | +0.32 / +0.59 | both halves | 2e-04 |  |
| [[MKNK2]] | +0.57 | +0.37 / +0.53 | both halves | 8e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC7]] | -0.54 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[CPSF2]] | -0.54 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[ZFP91]] | -0.54 | -0.29 / -0.56 | both halves | 3e-04 |  |
| [[CRPPA]] | -0.53 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ZNF532]] | -0.53 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[HNRNPL]] | -0.53 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[PSME3IP1]] | -0.52 | -0.18 / -0.55 | ⚠ one half (not replicated) | 1e-03 |  |
| [[TTC6]] | -0.51 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[SLC12A2-DT]] | -0.51 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[ATE1]] | -0.49 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ADGRA3]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[U2AF2]] | -0.49 | -0.21 / -0.49 | both halves | 7e-04 |  |
| [[CDKN2B-AS1]] | -0.49 | -0.23 / -0.45 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1F]] | B | MT1F activity raises FKBP1B's level | lines that do not express MT1F (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without MT1F | 0.027 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[DLK2]] | B | DLK2 activity raises FKBP1B's level | lines that do not express DLK2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without DLK2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ETNK2, CHROMR, DUSP15 |
| [[MFGE8]] | B | MFGE8 activity raises FKBP1B's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without MFGE8 | 0.081 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[ETNK2]] | B | ETNK2 activity raises FKBP1B's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without ETNK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[ENTPD2]] | B | ENTPD2 activity raises FKBP1B's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without ENTPD2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCD1]] | B | FKBP1B activity raises PLCD1's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without FKBP1B | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[TMSB10]] | B | FKBP1B activity raises TMSB10's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.57× lower at baseline in the lines without FKBP1B | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[HDAC11]] | B | FKBP1B activity raises HDAC11's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without FKBP1B | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[TWF2]] | B | FKBP1B activity raises TWF2's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without FKBP1B | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[PROSER2]] | B | FKBP1B activity raises PROSER2's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without FKBP1B | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[MT1F]] | B | FKBP1B activity raises MT1F's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without FKBP1B | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.7, 4.0); signed map (-21.4, 34.0). **Vector** length 53.6, 9.20% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.1 | +8.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.3 | +3.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -5.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,049,701-24,063,681 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OTK4, FKBP12.6, PPIase, FKBP9; previously FKBP1L |
| Gene groups (HGNC) | FKBP prolyl isomerase family |
| Hallmark sets | MYOGENESIS |
| Reactome | 6 pathways, smallest: Ion homeostasis; Stimuli-sensing channels; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P68106](https://www.uniprot.org/uniprotkb/P68106) (Peptidyl-prolyl cis-trans isomerase FKBP1B):

> Has the potential to contribute to the immunosuppressive and toxic effects of FK506 and rapamycin. PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides.

**Summary**, from NCBI Gene [2281](https://www.ncbi.nlm.nih.gov/gene/2281):

> The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds the immunosuppressants FK506 and rapamycin. It is highly similar to the FK506-binding protein 1A. Its physiological role is thought to be in excitation-contraction coupling in cardiac muscle. There are two alternatively spliced transcript …

**Accessions** — [HGNC:3712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3712) · Entrez [2281](https://www.ncbi.nlm.nih.gov/gene/2281) · UniProt [P68106](https://www.uniprot.org/uniprotkb/P68106) · Ensembl [ENSG00000119782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119782)

## Data

Gene col 4120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4120); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4120]; `tensor/DDL_lfc|DDL_z.npy` [4120]; `embed/gene_vectors.npy` [4120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4120 or target_col == 4120). Every well: [[FKBP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
