---
symbol: "DLD"
type: "gene"
col: 1656
ensembl_id: "ENSG00000091140"
name: "dihydrolipoamide dehydrogenase"
location: "7q31.1"
module: 25
arm: "+"
pooled_cpm: 44.67
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DLD

*dihydrolipoamide dehydrogenase* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.80× (z +10.8, q 1e-24, up in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.74× (z +10.3, q 3e-22, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.703× (z -9.3, q 1e-17, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD23B]] (+0.74, fdr 7e-06), [[API5]] (+0.74, fdr 7e-06), [[ECHS1]] (+0.74, fdr 7e-06); moves opposite to [[RABGEF1]] (-0.68, fdr 7e-06), [[KCNJ14]] (-0.67, fdr 1e-05), [[HIC2]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANKEF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +10.8 | 1e-24 | 40/47 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +10.3 | 3e-22 | 47/48 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +10.2 | 3e-22 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +9.6 | 2e-19 | 32/40 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +8.0 | 1e-13 | 41/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +7.9 | 2e-13 | 43/48 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +7.1 | 1e-10 | 32/48 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +6.1 | 8e-08 | 25/45 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 26/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.5 | 2e-06 | 23/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.5 | 2e-06 | 34/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 6e-06 | 30/48 (C32, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.9 | 4e-05 | 26/47 (LoVo, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.9 | 5e-05 | 24/48 (PANC-1, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 3e-04 | 27/48 (HS-578T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 9e-04 | 22/48 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.005 | 20/48 (C32, NCI-H2030, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.006 | 14/48 (C32, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.009 | 15/48 (C32, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -9.3 | 1e-17 | 41/48 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -4.9 | 2e-04 | 23/48 (SNU-1, A-427, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.699×** | -4.8 | 4e-04 | 30/47 (SNU-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.9 | 0.017 | 23/48 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.769×** | -3.5 | 0.052 | 15/48 (SW 1271, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.12 | 21/48 (SW 1271, AN3 CA, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.845× | -3.1 | 0.14 | 9/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.15 | 15/48 (SW 900, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 70.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 58.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 49.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +13.7) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 38.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 49.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -10.4) |
| [[SW480 (line)]] | alt | 42.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 40.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.478× (z -9.9) |
| [[AN3 CA (line)]] | alt | 76.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.302× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 48.0 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0957× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 61.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -8.5) |
| [[HS-578T (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.358× (z -9.7) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 45.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 57.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.357× (z -11.3) |
| [[SNU-423 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0766× (z -8.5) |
| [[SW48 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -14.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 93.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD23B]] | +0.74 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[API5]] | +0.74 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[ECHS1]] | +0.74 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 491 |
| [[OCRL]] | +0.73 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[MRPL19]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[RBBP9]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[DLAT]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 999 |
| [[ATP5F1A]] | +0.70 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 917 |
| [[EXOC5]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[FAM199X]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[AIFM1]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 | same gene group; pathway: HALLMARK_ADIPOGENESIS; STRING 591 |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | -0.68 | -0.58 / -0.75 | both halves | 7e-06 |  |
| [[KCNJ14]] | -0.67 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[HIC2]] | -0.66 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[TOB2]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[UBE2CP5]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[CATSPERG]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[MIA]] | -0.62 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.62 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[ELL]] | -0.62 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[TTLL3]] | -0.62 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[TRPV1]] | -0.61 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[LINC00685]] | -0.61 | -0.47 / -0.65 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKEF1]] | B | ANKEF1 activity lowers DLD's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without ANKEF1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[TOP2A]] | B | TOP2A activity raises DLD's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises DLD's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.7, -16.0); signed map (-17.0, -42.8). **Vector** length 114, 29.2% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.4 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.2 | -9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dihydrolipoamide dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:107,891,162-107,931,730 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DLDH, E3, OGDC-E3; previously LAD, GCSL |
| Gene groups (HGNC) | Pyruvate dehydrogenase complex subunits; Oxoglutarate dehydrogenase complex subunits; Flavoproteins; Oxoadipate dehydrogenase complex subunits; Branched chain alpha-keto acid dehydrogenase complex subunits; Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, GLYCOLYSIS, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 24 pathways, smallest: OADH complex synthesizes glutaryl-CoA from 2-OA; BCKDH synthesizes BCAA-CoA from KIC, KMVA, KIV; Loss-of-function mutations in DBT cause MSUD2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P09622](https://www.uniprot.org/uniprotkb/P09622) (Dihydrolipoyl dehydrogenase, mitochondrial):

> Lipoamide dehydrogenase is a component of the glycine cleavage system as well as an E3 component of three alpha-ketoacid dehydrogenase complexes (pyruvate-, alpha-ketoglutarate-, and branched-chain amino acid-dehydrogenase complex). The 2-oxoglutarate dehydrogenase complex is mainly active in the mitochondrion. A fraction of the 2-oxoglutarate dehydrogenase complex also localizes in the nucleus and is required for lysine succinylation of histones: associates with KAT2A on chromatin and provides …

**Summary**, from NCBI Gene [1738](https://www.ncbi.nlm.nih.gov/gene/1738):

> This gene encodes a member of the class-I pyridine nucleotide-disulfide oxidoreductase family. The encoded protein has been identified as a moonlighting protein based on its ability to perform mechanistically distinct functions. In homodimeric form, the encoded protein functions as a dehydrogenase and is found in several multi-enzyme complexes that regulate energy metabolism. However, as a monomer, this protein can function as a protease. Mutations in this gene have been identified in patients …

**Accessions** — [HGNC:2898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2898) · Entrez [1738](https://www.ncbi.nlm.nih.gov/gene/1738) · UniProt [P09622](https://www.uniprot.org/uniprotkb/P09622) · Ensembl [ENSG00000091140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091140)

## Data

Gene col 1656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1656); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1656]; `tensor/DDL_lfc|DDL_z.npy` [1656]; `embed/gene_vectors.npy` [1656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1656 or target_col == 1656). Every well: [[DLD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
