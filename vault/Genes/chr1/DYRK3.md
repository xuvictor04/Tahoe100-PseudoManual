---
symbol: "DYRK3"
type: "gene"
col: 6753
ensembl_id: "ENSG00000143479"
name: "dual specificity tyrosine phosphorylation regulated kinase 3"
location: "1q32.1"
module: 112
arm: "+"
pooled_cpm: 32.29
n_lines_expressing: 43
n_dd_up: 36
n_dd_down: 3
n_dd_up_clean: 30
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 4
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# DYRK3

*dual specificity tyrosine phosphorylation regulated kinase 3* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.51× (z +24.7, q 0e+00, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.732× (z -4.2, q 0.018, down in 15 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTHD1]] (+0.67, fdr 7e-06), [[LINC02154]] (+0.65, fdr 1e-05), [[C12orf50]] (+0.63, fdr 7e-06); moves opposite to [[BICRA]] (-0.49, fdr 3e-05), [[CLASP1]] (-0.47, fdr 4e-05), [[EHMT1]] (-0.47, fdr 5e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LAMA1]] → it (grade B ⚠); 4 go from it, the strongest it → [[STARD10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.51×** | +24.7 | 0e+00 | 35/40 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +15.1 | 0e+00 | 36/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.88×** | +14.7 | 0e+00 | 38/41 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +13.4 | 7e-39 | 35/40 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +12.9 | 4e-36 | 33/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.88×** | +12.4 | 2e-33 | 37/41 (NCI-H460, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +11.6 | 4e-29 | 34/41 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.09×** | +10.3 | 7e-23 | 34/41 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +10.2 | 1e-22 | 30/40 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +8.7 | 2e-16 | 33/41 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +7.6 | 1e-12 | 30/41 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +7.3 | 1e-11 | 30/41 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +7.1 | 6e-11 | 28/38 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +7.0 | 1e-10 | 30/38 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +6.7 | 8e-10 | 29/41 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.6 | 1e-09 | 21/41 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +5.7 | 5e-07 | 21/41 (LOX-IMVI, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 8e-07 | 25/41 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.732×** | -4.2 | 0.018 | 15/40 (HOP62, AN3 CA, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.770×** | -3.6 | 0.060 | 16/41 (A498, NCI-H460, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.771×** | -3.6 | 0.060 | 14/41 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.793× | -3.2 | 0.19 | 15/41 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.801× | -3.1 | 0.24 | 15/41 (A498, AsPC-1, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.804× | -3.0 | 0.24 | 12/41 (A498, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.5 | 19 (4 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.97× (z +16.9) | — |
| [[A498 (line)]] | wt | 144 | 6 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +26.3) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.402× (z -9.1) |
| [[LoVo (line)]] | wt | 14.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +14.7) | — |
| [[PANC-1 (line)]] | alt | 11.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +15.8) | — |
| [[A-172 (line)]] | wt | 89.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 16.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +13.9) | — |
| [[SNU-423 (line)]] | alt | 77.5 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 21.3 | 4 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.68× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 98.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +17.4) | — |
| [[SW1417 (line)]] | alt | 18.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +12.8) | — |
| [[C32 (line)]] | wt | 16.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 48.9 | 3 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.24× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +18.9) | — |
| [[SW480 (line)]] | alt | 23.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +12.4) | [[Cepharanthine (drug)]] 0.5 µM 0.0268× (z -18.3) |
| [[HS-578T (line)]] | alt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +13.2) | — |
| [[J82 (line)]] | alt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 8.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +11.2) | — |
| [[RKO (line)]] | wt | 69.8 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.35× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 54.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 33.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +15.1) | — |
| [[A-427 (line)]] | wt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -8.9) |
| [[AN3 CA (line)]] | alt | 34.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0707× (z -10.8) |
| [[Hs 766T (line)]] | wt | 45.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +13.7) | — |
| [[SNU-1 (line)]] | wt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.69 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTHD1]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[C12orf50]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ROR1-AS1]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[GDF15]] | +0.58 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LIF]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[LINC01291]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LIF-AS2]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SLAMF7]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GEM]] | +0.55 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CSF2]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICRA]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[CLASP1]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[EHMT1]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ARMC8]] | -0.46 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[CHUK]] | -0.45 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[DROSHA]] | -0.44 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TUBGCP3]] | -0.44 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[CDK5RAP2]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA1]] | B | LAMA1 activity raises DYRK3's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without LAMA1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[CLDN3]] | B | CLDN3 activity lowers DYRK3's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.93× higher at baseline in the lines without CLDN3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[LRRC49]] | B | LRRC49 activity raises DYRK3's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without LRRC49 | 0.025 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[LINC00944]] | B | LINC00944 activity raises DYRK3's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 2.42× lower at baseline in the lines without LINC00944 | 0.032 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[LINC02154]] | B | LINC02154 activity raises DYRK3's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 2.32× lower at baseline in the lines without LINC02154 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530 |
| [[IL1B]] | B | IL1B activity raises DYRK3's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.48× lower at baseline in the lines without IL1B | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[FGFR1]] | B | FGFR1 activity raises DYRK3's level | lines that do not express FGFR1 (8) vs lines expressing it (42) | 2.33× lower at baseline in the lines without FGFR1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SIX4, CPLANE1, QKI |
| [[SSTR2]] | B | SSTR2 activity raises DYRK3's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without SSTR2 | 0.087 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[GLS2]] | B | GLS2 activity lowers DYRK3's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 2.78× higher at baseline in the lines without GLS2 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[ARHGAP30]] | B | ARHGAP30 activity lowers DYRK3's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.82× higher at baseline in the lines without ARHGAP30 | 0.097 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[GPR158]] | B | GPR158 activity raises DYRK3's level | lines that do not express GPR158 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without GPR158 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, P2RX7, LINC02968 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD10]] | B | DYRK3 activity lowers STARD10's level | lines that do not express DYRK3 (7) vs lines expressing it (43) | 3.60× higher at baseline in the lines without DYRK3 | 0.030 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ROBO3, DZIP1L; maybe low, not absent |
| [[FGFR1]] | B | DYRK3 activity raises FGFR1's level | lines that do not express DYRK3 (7) vs lines expressing it (43) | 4.31× lower at baseline in the lines without DYRK3 | 0.084 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ROBO3, DZIP1L; maybe low, not absent |
| [[ZG16B]] | B | DYRK3 activity lowers ZG16B's level | lines that do not express DYRK3 (7) vs lines expressing it (43) | 2.87× higher at baseline in the lines without DYRK3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ROBO3, DZIP1L; maybe low, not absent |
| [[GSDME]] | B | DYRK3 activity raises GSDME's level | lines that do not express DYRK3 (7) vs lines expressing it (43) | 3.54× lower at baseline in the lines without DYRK3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ROBO3, DZIP1L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.1, 21.5); signed map (38.2, 22.2). **Vector** length 94.6, 24.4% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +12.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity tyrosine phosphorylation regulated kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,635,536-206,684,419 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RED, REDK, hYAK3-2 |
| Gene groups (HGNC) | Dual-specificity tyrosine-regulated kinase family |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Matched by | ensembl_id |

**Function**, from UniProt [O43781](https://www.uniprot.org/uniprotkb/O43781) (Dual specificity tyrosine-phosphorylation-regulated kinase 3):

> Dual-specificity protein kinase that promotes disassembly of several types of membraneless organelles during mitosis, such as stress granules, nuclear speckles and pericentriolar material. Dual-specificity tyrosine-regulated kinases (DYRKs) autophosphorylate a critical tyrosine residue in their activation loop and phosphorylate their substrate on serine and threonine residues. Acts as a central dissolvase of membraneless organelles during the G2-to-M transition, after the nuclear-envelope …

**Summary**, from NCBI Gene [8444](https://www.ncbi.nlm.nih.gov/gene/8444):

> This gene product belongs to the DYRK family of dual-specificity protein kinases that catalyze autophosphorylation on serine/threonine and tyrosine residues. The members of this family share structural similarity, however, differ in their substrate specificity, suggesting their involvement in different cellular functions. The encoded protein has been shown to autophosphorylate on tyrosine residue and catalyze phosphorylation of histones H3 and H2B in vitro. Alternatively spliced transcript …

**Accessions** — [HGNC:3094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3094) · Entrez [8444](https://www.ncbi.nlm.nih.gov/gene/8444) · UniProt [O43781](https://www.uniprot.org/uniprotkb/O43781) · Ensembl [ENSG00000143479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143479)

## Data

Gene col 6753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6753); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6753]; `tensor/DDL_lfc|DDL_z.npy` [6753]; `embed/gene_vectors.npy` [6753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6753 or target_col == 6753). Every well: [[DYRK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYRK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
