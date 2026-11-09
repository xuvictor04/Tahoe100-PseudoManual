---
symbol: "PPP1R3B-DT"
type: "gene"
col: 14550
ensembl_id: "ENSG00000248538"
name: "PPP1R3B divergent transcript"
location: "8p23.1"
module: 75
arm: "+"
pooled_cpm: 6.48
n_lines_expressing: 45
n_dd_up: 31
n_dd_down: 12
n_dd_up_clean: 23
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# PPP1R3B-DT

*PPP1R3B divergent transcript* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +14.6, q 1e-45, up in 23 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.678× (z -4.5, q 0.004, down in 12 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHAD1]] (+0.58, fdr 1e-05), [[CPVL]] (+0.57, fdr 3e-05), [[PTPN22]] (+0.55, fdr 3e-05); moves opposite to [[ZFYVE21]] (-0.50, fdr 4e-05), [[FBH1]] (-0.49, fdr 3e-05), [[TANGO2]] (-0.46, fdr 1e-04).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[F11-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[MTM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +14.6 | 1e-45 | 23/33 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.14×** | +13.1 | 5e-37 | 28/40 (A498, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +12.0 | 6e-31 | 22/35 (HCT15, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +11.1 | 1e-26 | 3/6 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +11.0 | 6e-26 | 23/41 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +10.5 | 6e-24 | 14/19 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +8.9 | 4e-17 | 21/40 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +8.7 | 2e-16 | 20/38 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +7.8 | 6e-13 | 5/12 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +7.3 | 2e-11 | 22/40 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +7.1 | 4e-11 | 21/36 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +6.7 | 9e-10 | 19/40 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.72×** | +6.4 | 6e-09 | 14/37 (A498, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.3 | 4e-06 | 6/37 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.43×** | +4.2 | 0.001 | 10/35 (A-172, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.006 | 7/40 (SW480, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.020 | 5/39 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.028 | 3/39 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brimonidine (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.044 | 2/36 (LS 180, A-427) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.678×** | -4.5 | 0.004 | 12/36 (COLO 205, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.779×** | -4.3 | 0.004 | 11/38 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[crizotinib (drug)]] 5 µM |  | **0.700×** | -4.2 | 0.004 | 9/40 (RPMI-7951, SNU-1, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.727×** | -3.9 | 0.010 | 11/40 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.729×** | -3.9 | 0.010 | 16/41 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.732×** | -3.8 | 0.010 | 8/41 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.733×** | -3.8 | 0.010 | 6/40 (LoVo, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -3.8 | 0.010 | 7/42 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[Ivermectin (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.024 | 3/42 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.747×** | -3.5 | 0.030 | 13/39 (COLO 205, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.757×** | -3.4 | 0.030 | 12/39 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.613×** | -3.1 | 0.077 | 9/25 (COLO 205, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 68.5 | 0 | 9 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0568× (z -18.4) ⚠ toxic; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.6) |
| [[A-172 (line)]] | wt | 2.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +10.1) | — |
| [[A498 (line)]] | wt | 3.24 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +10.1) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0818× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 5.43 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0890× (z -11.9) |
| [[HCT15 (line)]] | alt | 6.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 5.41 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0805× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~62% of this change |
| [[LS 180 (line)]] | wt | 8.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -9.5) |
| [[SW480 (line)]] | alt | 1.71 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0720× (z -8.5) |
| [[A-427 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHAD1]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CPVL]] | +0.57 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[PTPN22]] | +0.55 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[LINC02343]] | +0.55 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[TCN1]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SMIM2-AS1]] | +0.53 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[CEACAM16-AS1]] | +0.52 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ESR1]] | +0.52 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CARD14]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[PARP8]] | +0.52 | +0.39 / +0.37 | both halves | 7e-05 |  |
| [[GRM7]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[DPP6]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE21]] | -0.50 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[FBH1]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TANGO2]] | -0.46 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[MTM1]] | -0.46 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[RGS12]] | -0.44 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[DIP2A]] | -0.43 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[HEATR5A]] | -0.43 | -0.23 / -0.31 | both halves | 5e-04 |  |
| [[TPRG1L]] | -0.43 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[C9orf78]] | -0.42 | -0.23 / -0.24 | both halves | 5e-04 |  |
| [[CCM2]] | -0.41 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[MOB2]] | -0.41 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F11-AS1]] | B | F11-AS1 activity raises PPP1R3B-DT's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 2.09× lower at baseline in the lines without F11-AS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent |
| [[TCN1]] | B | TCN1 activity raises PPP1R3B-DT's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.41× lower at baseline in the lines without TCN1 | 0.008 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[SMIM2-AS1]] | B | SMIM2-AS1 activity raises PPP1R3B-DT's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 3.17× lower at baseline in the lines without SMIM2-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent |
| [[LRG1]] | B | LRG1 activity raises PPP1R3B-DT's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without LRG1 | 0.065 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[RGS6]] | B | RGS6 activity raises PPP1R3B-DT's level | lines that do not express RGS6 (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without RGS6 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, LIPG, RERG; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTM1]] | B | PPP1R3B-DT activity raises MTM1's level | lines that do not express PPP1R3B-DT (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without PPP1R3B-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: KNDC1; maybe low, not absent; its own permutation p |
| [[FBH1]] | B | PPP1R3B-DT activity lowers FBH1's level | lines that do not express PPP1R3B-DT (5) vs lines expressing it (45) | 1.25× higher at baseline in the lines without PPP1R3B-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: KNDC1; maybe low, not absent; its own permutation p |
| [[HEATR5A]] | B | PPP1R3B-DT activity lowers HEATR5A's level | lines that do not express PPP1R3B-DT (5) vs lines expressing it (45) | 1.17× higher at baseline in the lines without PPP1R3B-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: KNDC1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 57.0); signed map (60.1, -4.6). **Vector** length 52.2, 7.21% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.9 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | +0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | PPP1R3B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p23.1 — chr8:9,151,695-9,425,524 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AC02278.4, RP11-10A14.5, AP000695.2 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56150) · Entrez [102724880](https://www.ncbi.nlm.nih.gov/gene/102724880) · Ensembl [ENSG00000248538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248538)

## Data

Gene col 14550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14550); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14550]; `tensor/DDL_lfc|DDL_z.npy` [14550]; `embed/gene_vectors.npy` [14550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14550 or target_col == 14550). Every well: [[PPP1R3B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R3B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
