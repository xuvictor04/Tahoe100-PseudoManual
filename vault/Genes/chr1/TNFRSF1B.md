---
symbol: "TNFRSF1B"
type: "gene"
col: 382
ensembl_id: "ENSG00000028137"
name: "TNF receptor superfamily member 1B"
location: "1p36.22"
module: 14
arm: "+"
pooled_cpm: 14.93
n_lines_expressing: 33
n_dd_up: 16
n_dd_down: 26
n_dd_up_clean: 12
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNFRSF1B

*TNF receptor superfamily member 1B* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.28× (z +20.1, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.252× (z -8.6, q 4e-15, down in 20 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSTR2]] (+0.61, fdr 1e-05), [[TRIM15]] (+0.60, fdr 1e-05), [[PPP4R4]] (+0.59, fdr 4e-05); moves opposite to [[EIF3F]] (-0.58, fdr 4e-05), [[C1D]] (-0.51, fdr 4e-05), [[CSDE1]] (-0.50, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GBP4]] → it (grade B ⚠); 8 go from it, the strongest it → [[IER3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.28×** | +20.1 | 0e+00 | 29/30 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.22×** | +14.0 | 8e-42 | 24/29 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.07×** | +13.4 | 1e-38 | 25/31 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.69×** | +11.8 | 4e-30 | 20/30 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.67×** | +11.7 | 8e-30 | 24/29 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.26×** | +9.8 | 2e-20 | 23/31 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +7.8 | 5e-13 | 16/30 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.49×** | +5.7 | 9e-07 | 13/31 (AsPC-1, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 9e-06 | 14/30 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +5.2 | 9e-06 | 12/31 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +4.3 | 8e-04 | 12/30 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +3.7 | 0.012 | 8/29 (SK-MEL-2, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.35×** | +3.6 | 0.015 | 7/27 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.21×** | +3.2 | 0.053 | 8/30 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.058 | 6/30 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.252×** | -8.6 | 4e-15 | 20/31 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.518×** | -7.9 | 1e-12 | 18/29 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.537×** | -7.4 | 2e-11 | 17/30 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.365×** | -6.3 | 4e-08 | 18/28 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.591×** | -6.3 | 4e-08 | 17/29 (PANC-1, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.597×** | -5.7 | 1e-06 | 13/21 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.622×** | -5.4 | 6e-06 | 15/29 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.731×** | -5.3 | 8e-06 | 15/31 (NCI-H460, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.647×** | -5.2 | 1e-05 | 18/24 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.436×** | -5.2 | 1e-05 | 14/26 (COLO 205, A549, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.648×** | -5.2 | 1e-05 | 11/30 (A549, CFPAC-1, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.677×** | -4.7 | 1e-04 | 14/30 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.685×** | -4.5 | 3e-04 | 10/30 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.688×** | -4.3 | 7e-04 | 13/29 (SK-MEL-2, SW480, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.728×** | -3.8 | 0.005 | 6/30 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.800×** | -3.8 | 0.006 | 8/31 (KATO III, A549, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.009 | 11/31 (COLO 205, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 40.3 | 2 | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.28× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.6) |
| [[SW480 (line)]] | alt | 66.4 | 1 | 8 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.75× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -23.2) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.284× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 26.2 | 5 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.37× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -12.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 16.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.3 | 4 | 2 | [[Harringtonine (drug)]] 0.5 µM 6.15× (z +13.1) | [[Bortezomib (drug)]] 0.05 µM 0.234× (z -9.9) |
| [[COLO 205 (line)]] | alt | 64.2 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.42× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.149× (z -12.6) |
| [[J82 (line)]] | alt | 11.7 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.45× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0796× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 12.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +16.9) | — |
| [[HOP62 (line)]] | alt | 4.05 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 9.57× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 7.36 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +13.2) | — |
| [[NCI-H460 (line)]] | wt | 7.23 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.15× (z +8.6) | [[Selinexor (drug)]] 5 µM 0.196× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.29× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.391× (z -8.5) |
| [[A549 (line)]] | wt | 17.2 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.65× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0544× (z -14.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 15.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.25× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 10.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.7× (z +11.8) | — |
| [[KATO III (line)]] | alt | 33.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.89× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0265× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSTR2]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TRIM15]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PPP4R4]] | +0.59 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[CD82]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[IFNAR2]] | +0.58 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[TNFRSF9]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 640 |
| [[DTX2]] | +0.58 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[VDR]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[CD40]] | +0.55 | +0.44 / +0.64 | both halves | 3e-05 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 777 |
| [[CYP2J2]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[IL1A]] | +0.55 | +0.43 / +0.65 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 770 |
| [[SLFN11]] | +0.54 | +0.32 / +0.55 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3F]] | -0.58 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[C1D]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CSDE1]] | -0.50 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[PPIP5K2]] | -0.49 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SPAG16]] | -0.48 | -0.32 / -0.43 | both halves | 2e-04 | same gene group |
| [[ANXA2R-OT1]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[GHITM]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[UBQLN1]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[NNT]] | -0.47 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[PSMC2]] | -0.46 | -0.40 / -0.40 | both halves | 5e-05 | pathway: TNFR2 non-canonical NF-kB pathway; STRING 400 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | GBP4 activity raises TNFRSF1B's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without GBP4 | 0.009 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[NEURL3]] | B | NEURL3 activity raises TNFRSF1B's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without NEURL3 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[CFB]] | B | CFB activity raises TNFRSF1B's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without CFB | 0.084 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[GBP5]] | B | GBP5 activity raises TNFRSF1B's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.54× lower at baseline in the lines without GBP5 | 0.094 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[SLC43A3]] | B | SLC43A3 activity raises TNFRSF1B's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without SLC43A3 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[C15orf48]] | C | C15orf48 activity raises TNFRSF1B's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 2.53× lower at baseline in the lines without C15orf48 | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IER3]] | B | TNFRSF1B activity raises IER3's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without TNFRSF1B | 0.019 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[GBP4]] | B | TNFRSF1B activity raises GBP4's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without TNFRSF1B | 0.045 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[DTX2]] | B | TNFRSF1B activity raises DTX2's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without TNFRSF1B | 0.055 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[SDC4]] | B | TNFRSF1B activity raises SDC4's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 2.11× lower at baseline in the lines without TNFRSF1B | 0.067 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | B | TNFRSF1B activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express TNFRSF1B (17) vs lines expressing it (31) | the lines without TNFRSF1B: 0.83× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[BTG1]] | B | TNFRSF1B activity raises BTG1's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without TNFRSF1B | 0.090 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[HLA-F]] | B | TNFRSF1B activity raises HLA-F's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without TNFRSF1B | 0.099 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |
| [[C15orf48]] | C | TNFRSF1B activity raises C15orf48's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 3.83× lower at baseline in the lines without TNFRSF1B | 0.013 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.7, 2.3); signed map (42.6, 13.3). **Vector** length 102, 27.7% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +20.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +11.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +14.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +13.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.1 | -8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:12,166,991-12,209,228 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TNFBR, TNFR80, TNF-R75, TNF-R-II, p75, CD120b; previously TNFR2 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily; MicroRNA protein coding host genes |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING |
| Reactome | 8 pathways, smallest: TNFs bind their physiological receptors; Interleukin-10 signaling; TNFR2 non-canonical NF-kB pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P20333](https://www.uniprot.org/uniprotkb/P20333) (Tumor necrosis factor receptor superfamily member 1B):

> Receptor for TNF/TNFSF2 and LTA/TNFSF1, which activates the tumor necrosis factor-mediated (TNF) signaling pathway upon ligand-binding. Has high affinity for TNFSF2/TNF and approximately 5-fold lower affinity for LTA/TNFSF1. The TNF signaling pathway acts as a master regulator of the immune system, which either (1) promotes cell survival and inflammation by activating the canonical NF-kappa-B pathway or (2) trigger programmed cell death (apoptosis and necroptosis). TNF/TNFSF2 and …

**Summary**, from NCBI Gene [7133](https://www.ncbi.nlm.nih.gov/gene/7133):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This protein and TNF-receptor 1 form a heterocomplex that mediates the recruitment of two anti-apoptotic proteins, c-IAP1 and c-IAP2, which possess E3 ubiquitin ligase activity. The function of IAPs in TNF-receptor signalling is unknown, however, c-IAP1 is thought to potentiate TNF-induced apoptosis by the ubiquitination and degradation of TNF-receptor-associated factor 2, which mediates anti-apoptotic signals. …

**Accessions** — [HGNC:11917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11917) · Entrez [7133](https://www.ncbi.nlm.nih.gov/gene/7133) · UniProt [P20333](https://www.uniprot.org/uniprotkb/P20333) · Ensembl [ENSG00000028137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000028137)

## Data

Gene col 382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 382); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 382]; `tensor/DDL_lfc|DDL_z.npy` [382]; `embed/gene_vectors.npy` [382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 382 or target_col == 382). Every well: [[TNFRSF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
