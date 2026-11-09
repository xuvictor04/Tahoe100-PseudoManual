---
symbol: "QTRT1"
type: "gene"
col: 13096
ensembl_id: "ENSG00000213339"
name: "queuine tRNA-ribosyltransferase catalytic subunit 1"
location: "19p13.3"
module: 1
arm: "+"
pooled_cpm: 7.54
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 10
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# QTRT1

*queuine tRNA-ribosyltransferase catalytic subunit 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +16.5, q 0e+00, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.710× (z -7.9, q 1e-12, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC5A6]] (+0.81, fdr 7e-06), [[DUS3L]] (+0.76, fdr 7e-06), [[MCCC2]] (+0.76, fdr 7e-06); moves opposite to [[CARHSP1]] (-0.65, fdr 2e-05), [[COX6A1]] (-0.64, fdr 2e-05), [[YIF1B]] (-0.62, fdr 7e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +16.5 | 0e+00 | 35/44 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +16.3 | 0e+00 | 14/15 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +13.9 | 7e-42 | 25/32 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +12.0 | 8e-31 | 20/23 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +8.5 | 2e-15 | 20/48 (A-172, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.5 | 2e-15 | 25/43 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +8.3 | 6e-15 | 25/47 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +8.1 | 4e-14 | 22/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.4 | 9e-12 | 22/42 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +7.0 | 1e-10 | 16/46 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.5 | 6e-09 | 20/46 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.9 | 2e-07 | 14/40 (SK-MEL-2, LS 180, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +5.8 | 4e-07 | 14/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +5.4 | 3e-06 | 13/45 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.9 | 4e-05 | 12/45 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.5 | 2e-04 | 13/48 (A-427, A549, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.22×** | +4.5 | 2e-04 | 7/47 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.008 | 6/47 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.008 | 10/46 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.008 | 2/39 (AsPC-1, NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.011 | 2/44 (LoVo, HEC-1-A) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.013 | 1/48 (NCI-H460) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.710×** | -7.9 | 1e-12 | 24/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -7.7 | 3e-12 | 24/47 (SW 900, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.655×** | -6.9 | 9e-10 | 21/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.678×** | -6.3 | 3e-08 | 22/47 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.723×** | -5.3 | 1e-05 | 14/47 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.778×** | -4.1 | 0.004 | 11/46 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Erlotinib (drug)]] 5 µM |  | **0.790×** | -3.7 | 0.017 | 10/46 (BT-474, NCI-H23, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -3.6 | 0.027 | 9/48 (SNU-1, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.672×** | -3.4 | 0.043 | 10/44 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.814×** | -3.4 | 0.043 | 5/46 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.830× | -3.0 | 0.12 | 5/46 (H4, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.37 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +19.6) | — |
| [[SK-MEL-2 (line)]] | alt | 8.87 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0572× (z -12.0) |
| [[A549 (line)]] | wt | 6.45 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.101× (z -9.5) ⚠ toxic |
| [[BT-474 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.117× (z -9.2) |
| [[HCT15 (line)]] | alt | 9.71 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0974× (z -8.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.231× (z -9.2) |
| [[J82 (line)]] | alt | 6.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +16.0) | — |
| [[KATO III (line)]] | alt | 3.95 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0942× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 8.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 6.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 5.00 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0730× (z -9.5) |
| [[SW480 (line)]] | alt | 8.98 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A6]] | +0.81 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[DUS3L]] | +0.76 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[MCCC2]] | +0.76 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ITPA]] | +0.71 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[VPS52]] | +0.70 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[WDR74]] | +0.68 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GTF3C6]] | +0.68 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[SNX5]] | +0.67 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SMYD5]] | +0.67 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[UTP20]] | +0.67 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.66 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[DHX37]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARHSP1]] | -0.65 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.64 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.62 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[PCMT1]] | -0.62 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[CBL]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NDRG1]] | -0.61 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[PEDS1]] | -0.61 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[DNAAF3]] | -0.61 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[OAZ1]] | -0.60 | -0.17 / -0.67 | ⚠ one half (not replicated) | 0.001 |  |
| [[PDCD10]] | -0.59 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[PJA2]] | -0.59 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[RASSF7]] | -0.58 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[ANAPC11]] | -0.57 | -0.55 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers QTRT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RALGPS2]] | B | RALGPS2 activity lowers QTRT1's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.36× higher at baseline in the lines without RALGPS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises QTRT1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises QTRT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC9B2]] | C | SLC9B2 activity raises QTRT1's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.58× lower at baseline in the lines without SLC9B2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | QTRT1's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | QTRT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.56 | 0.530 over the table, 0.0997 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.586). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.1, 6.3); signed map (21.2, -31.6). **Vector** length 71.9, 11.6% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +16.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | queuine tRNA-ribosyltransferase catalytic subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:10,701,430-10,713,437 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TGT |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXR0](https://www.uniprot.org/uniprotkb/Q9BXR0) (Queuine tRNA-ribosyltransferase catalytic subunit 1):

> Catalytic subunit of the queuine tRNA-ribosyltransferase (TGT) that catalyzes the base-exchange of a guanine (G) residue with queuine (Q) at position 34 (anticodon wobble position) in tRNAs with GU(N) anticodons (tRNA-Asp, -Asn, -His and -Tyr), resulting in the hypermodified nucleoside queuosine (7-(((4,5-cis-dihydroxy-2-cyclopenten-1-yl)amino)methyl)-7-deazaguanosine). Catalysis occurs through a double-displacement mechanism. The nucleophile active site attacks the C1' of nucleotide 34 to …

**Summary**, from NCBI Gene [81890](https://www.ncbi.nlm.nih.gov/gene/81890):

> This gene encodes the catalytic subunit of tRNA-guanine transglycosylase. tRNA-guanine transglycosylase is a heterodimeric enzyme complex that plays a critical role in tRNA modification by synthesizing the 7-deazaguanosine queuosine, which is found in tRNAs that code for asparagine, aspartic acid, histidine and tyrosine. A pseudogene of this gene is located on the long arm of chromosome X. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:23797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23797) · Entrez [81890](https://www.ncbi.nlm.nih.gov/gene/81890) · UniProt [Q9BXR0](https://www.uniprot.org/uniprotkb/Q9BXR0) · Ensembl [ENSG00000213339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213339)

## Data

Gene col 13096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13096); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13096]; `tensor/DDL_lfc|DDL_z.npy` [13096]; `embed/gene_vectors.npy` [13096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13096 or target_col == 13096). Every well: [[QTRT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QTRT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
