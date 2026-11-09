---
symbol: "SNHG26"
type: "gene"
col: 13664
ensembl_id: "ENSG00000228649"
name: "small nucleolar RNA host gene 26"
location: "7p15.3"
module: 1
arm: "+"
pooled_cpm: 12.28
n_lines_expressing: 39
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SNHG26

*small nucleolar RNA host gene 26* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.04× (z +8.8, q 1e-15, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.386× (z -11.7, q 7e-29, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL1]] (+0.69, fdr 1e-05), [[GPATCH4]] (+0.67, fdr 1e-05), [[ABCE1]] (+0.67, fdr 7e-06); moves opposite to [[PIN1]] (-0.66, fdr 6e-05), [[ARL3]] (-0.65, fdr 1e-05), [[MOSPD3]] (-0.63, fdr 6e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[BNC2]] → it (grade B ⚠); 8 go from it, the strongest it → [[LINC01357]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +8.8 | 1e-15 | 23/35 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +8.4 | 2e-14 | 22/35 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.69×** | +6.1 | 2e-07 | 21/34 (A498, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.8 | 2e-04 | 16/35 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.03×** | +4.5 | 6e-04 | 16/33 (Panc 03.27, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.29×** | +4.4 | 0.001 | 12/36 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.96×** | +4.3 | 0.001 | 8/33 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.1 | 0.002 | 13/36 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.003 | 13/34 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.9 | 0.005 | 12/27 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.006 | 15/35 (NCI-H2347, SW480, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.82×** | +3.8 | 0.006 | 14/33 (Panc 03.27, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.8 | 0.006 | 3/17 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.031 | 10/37 (NCI-H1792, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.037 | 12/34 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.044 | 6/35 (SHP-77, SNU-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.051 | 10/36 (A-427, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.1 | 0.058 | 13/36 (HOP62, A-172, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.080 | 7/34 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -11.7 | 7e-29 | 26/36 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.453×** | -9.7 | 7e-20 | 24/36 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -6.9 | 1e-09 | 21/36 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.632×** | -5.4 | 8e-06 | 19/33 (hTERT-HPNE, SNU-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.744×** | -3.6 | 0.033 | 11/35 (NCI-H2030, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **0.753×** | -3.5 | 0.048 | 12/32 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.055 | 12/36 (C-33 A, RKO, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.055 | 8/35 (H4, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.079 | 9/36 (SW 900, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 27.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -9.9) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.156× (z -8.9) |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -10.9) |
| [[RKO (line)]] | wt | 16.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0448× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.0) | — |
| [[A498 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[H4 (line)]] | wt | 14.2 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0762× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 8.66 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -9.8) |
| [[HOP62 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.7) | — |
| [[J82 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.1× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.105× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 8.95 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -10.3) |
| [[A549 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.980 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL1]] | +0.69 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[GPATCH4]] | +0.67 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SLC16A1-AS1]] | +0.67 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ZNF121]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ST7L]] | +0.65 | +0.71 / +0.37 | both halves | 8e-05 |  |
| [[COA7]] | +0.65 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[NCR3LG1]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[HSF2BP]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[MGA]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.63 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ZNF507]] | +0.62 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIN1]] | -0.66 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[ARL3]] | -0.65 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.63 | -0.68 / -0.39 | both halves | 6e-05 |  |
| [[STRN]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.62 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ALDH6A1]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[BAD]] | -0.61 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[APAF1]] | -0.61 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[GNB2]] | -0.61 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[PLEKHH3]] | -0.61 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[CBFA2T2]] | -0.60 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[DHTKD1]] | -0.60 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BNC2]] | B | BNC2 activity raises SNHG26's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.59× lower at baseline in the lines without BNC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[LINC03041]] | B | LINC03041 activity raises SNHG26's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 2.69× lower at baseline in the lines without LINC03041 | 0.003 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[HECW2]] | B | HECW2 activity raises SNHG26's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 2.45× lower at baseline in the lines without HECW2 | 0.010 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041 |
| [[LINC00472]] | B | LINC00472 activity raises SNHG26's level | lines that do not express LINC00472 (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without LINC00472 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000279289, RBMS3, C2orf74-DT |
| [[SLC2A9]] | B | SLC2A9 activity lowers SNHG26's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 3.12× higher at baseline in the lines without SLC2A9 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[MIR130AHG]] | B | MIR130AHG activity raises SNHG26's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without MIR130AHG | 0.063 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1 |
| [[FJX1]] | B | FJX1 activity raises SNHG26's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 2.76× lower at baseline in the lines without FJX1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[CPEB1]] | B | CPEB1 activity raises SNHG26's level | lines that do not express CPEB1 (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without CPEB1 | 0.080 | ⚠ within organs, on part of the lines; also absent: GLIS1, COLEC12, TUB |
| [[HDAC6]] | B | HDAC6 activity raises SNHG26's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CYP46A1]] | B | CYP46A1 activity raises SNHG26's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 2.76× lower at baseline in the lines without CYP46A1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |
| [[FAM171A1]] | C | FAM171A1 activity raises SNHG26's level | lines that do not express FAM171A1 (7) vs lines expressing it (43) | 3.68× lower at baseline in the lines without FAM171A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PORCN, CMTM7, ANXA6; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01357]] | B | SNHG26 activity raises LINC01357's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 2.00× lower at baseline in the lines without SNHG26 | 0.014 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[PIN1]] | B | SNHG26 activity raises PIN1's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without SNHG26 | 0.020 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[FBXO10]] | B | SNHG26 activity raises FBXO10's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without SNHG26 | 0.041 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[ZNF507]] | B | SNHG26 activity raises ZNF507's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without SNHG26 | 0.057 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[P2RX5]] | B | SNHG26 activity raises P2RX5's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without SNHG26 | 0.067 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[CPEB1]] | B | SNHG26 activity raises CPEB1's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without SNHG26 | 0.089 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[BICD1]] | B | SNHG26 activity raises BICD1's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without SNHG26 | 0.098 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[FAM171A1]] | C | SNHG26 activity raises FAM171A1's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 2.86× lower at baseline in the lines without SNHG26 | 0.056 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.3, -36.0); signed map (2.3, -43.3). **Vector** length 82.0, 18.9% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +4.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.5 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -6.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -1.9 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.5 | -5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 26 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p15.3 — chr7:22,854,126-22,872,952 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AC005682.5 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [109729180](https://www.ncbi.nlm.nih.gov/gene/109729180):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:53131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53131) · Entrez [109729180](https://www.ncbi.nlm.nih.gov/gene/109729180) · Ensembl [ENSG00000228649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228649)

## Data

Gene col 13664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13664); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13664]; `tensor/DDL_lfc|DDL_z.npy` [13664]; `embed/gene_vectors.npy` [13664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13664 or target_col == 13664). Every well: [[SNHG26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
