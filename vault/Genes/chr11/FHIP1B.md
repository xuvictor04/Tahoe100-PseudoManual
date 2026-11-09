---
symbol: "FHIP1B"
type: "gene"
col: 573
ensembl_id: "ENSG00000051009"
name: "FHF complex subunit HOOK interacting protein 1B"
location: "11p15.4"
module: 30
arm: "+"
pooled_cpm: 22.44
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# FHIP1B

*FHF complex subunit HOOK interacting protein 1B* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.77× (z +9.1, q 6e-17, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.439× (z -10.8, q 1e-24, down in 32 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.693× (z -6.8, q 2e-09, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF41]] (+0.68, fdr 3e-05), [[SDHAP1]] (+0.67, fdr 1e-05), [[RNF121]] (+0.66, fdr 2e-05); moves opposite to [[GRIP1]] (-0.62, fdr 2e-05), [[CPSF2]] (-0.61, fdr 9e-05), [[PTPRK]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.77×** | +9.1 | 6e-17 | 41/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.62×** | +8.8 | 4e-16 | 36/45 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +5.1 | 6e-05 | 23/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +4.4 | 0.001 | 22/48 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.8 | 0.014 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.015 | 19/48 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 573.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.439×** | -10.8 | 1e-24 | 32/41 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.449×** | -10.1 | 1e-21 | 26/30 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -6.8 | 2e-09 | 28/47 (LS 180, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -6.2 | 6e-08 | 27/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.624×** | -6.2 | 6e-08 | 34/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -5.5 | 4e-06 | 28/47 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.759×** | -5.1 | 2e-05 | 24/47 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.760×** | -5.1 | 2e-05 | 28/48 (A498, HOP62, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.732×** | -4.1 | 0.002 | 16/48 (A498, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.751×** | -3.8 | 0.008 | 23/48 (SNU-423, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.817×** | -3.8 | 0.008 | 15/48 (CHP-212, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.742×** | -3.6 | 0.013 | 18/34 (BT-474, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.763×** | -3.6 | 0.015 | 19/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.624×** | -3.3 | 0.047 | 12/37 (C-33 A, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.787×** | -3.2 | 0.058 | 17/47 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.1 | 0.058 | 16/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.5 µM |  | **0.719×** | -3.1 | 0.064 | 16/47 (A-427, SW 1088, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -3.0 | 0.083 | 21/48 (SW480, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 37.1 | 2 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 9.51× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -11.0) |
| [[A498 (line)]] | wt | 27.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.406× (z -9.8) |
| [[HOP62 (line)]] | alt | 24.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 25.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -9.9) |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0831× (z -10.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 27.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -18.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 23.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -15.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.346× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 20.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0708× (z -17.6) |
| [[A-172 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -8.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0904× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 9.22 | 0 | 1 | — | [[Verteporfin (drug)]] 0.05 µM 0.0737× (z -8.7) |
| [[Hs 766T (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0980× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF41]] | +0.68 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SDHAP1]] | +0.67 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[RNF121]] | +0.66 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[LRRC42]] | +0.66 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[LCMT1]] | +0.65 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[ESS2]] | +0.65 | +0.53 / +0.49 | both halves | 2e-05 |  |
| [[ELP1]] | +0.65 | +0.66 / +0.37 | both halves | 7e-05 |  |
| [[SDHAP4]] | +0.64 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[NUP160]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[E4F1]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.63 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[SDHAP2]] | +0.63 | +0.69 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIP1]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CPSF2]] | -0.61 | -0.67 / -0.37 | both halves | 9e-05 |  |
| [[PTPRK]] | -0.60 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[LACTB2]] | -0.60 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[GYG1]] | -0.60 | -0.64 / -0.40 | both halves | 4e-05 |  |
| [[PHACTR2]] | -0.60 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[TIA1]] | -0.58 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[NQO1-DT]] | -0.58 | -0.61 / -0.26 | both halves | 3e-04 |  |
| [[RNF6]] | -0.58 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[CACNA2D1]] | -0.57 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[TENM3-AS1]] | -0.57 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[LACC1]] | -0.57 | -0.58 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FHIP1B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00705]] | B | LINC00705 activity raises FHIP1B's level | lines that do not express LINC00705 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without LINC00705 | 0.025 | ⚠ within organs, on part of the lines; also absent: SMAD3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers FHIP1B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.3, -15.2); signed map (-38.5, 0.6). **Vector** length 94.9, 21.1% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +8.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | -1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.6 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -5.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | FHF complex subunit HOOK interacting protein 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,211,345-6,234,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22665, KIAA1759, DKFZP566M1046, FHIP; previously C11orf56, FAM160A2 |
| Gene groups (HGNC) | FHF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N612](https://www.uniprot.org/uniprotkb/Q8N612) (FHF complex subunit HOOK-interacting protein 1B):

> Component of the FTS/Hook/FHIP complex (FHF complex). The FHF complex may function to promote vesicle trafficking and/or fusion via the homotypic vesicular protein sorting complex (the HOPS complex). FHF complex promotes the distribution of AP-4 complex to the perinuclear area of the cell.

**Summary**, from NCBI Gene [84067](https://www.ncbi.nlm.nih.gov/gene/84067):

> The protein encoded by this gene is part of the FTS/Hook/FHIP (FHF) complex, which can interact with members of the homotypic vesicular protein sorting (HOPS) complex. This interaction suggests that the encoded protein is involved in vesicle trafficking. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:25378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25378) · Entrez [84067](https://www.ncbi.nlm.nih.gov/gene/84067) · UniProt [Q8N612](https://www.uniprot.org/uniprotkb/Q8N612) · Ensembl [ENSG00000051009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000051009)

## Data

Gene col 573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 573); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 573]; `tensor/DDL_lfc|DDL_z.npy` [573]; `embed/gene_vectors.npy` [573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 573 or target_col == 573). Every well: [[FHIP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHIP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
