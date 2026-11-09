---
symbol: "NDC1"
type: "gene"
col: 668
ensembl_id: "ENSG00000058804"
name: "NDC1 transmembrane nucleoporin"
location: "1p32.3"
module: 186
arm: "+"
pooled_cpm: 57.44
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# NDC1

*NDC1 transmembrane nucleoporin* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.00× (z +8.4, q 4e-14, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -17.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENT4A]] (+0.75, fdr 7e-06), [[RNF4]] (+0.75, fdr 7e-06), [[RPA1]] (+0.74, fdr 7e-06); moves opposite to [[TFE3]] (-0.66, fdr 8e-06), [[BCL10]] (-0.65, fdr 7e-06), [[CHMP4A]] (-0.64, fdr 1e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LAMB3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FNTB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +8.4 | 4e-14 | 38/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.74×** | +8.1 | 2e-13 | 32/47 (LoVo, J82, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +7.1 | 2e-10 | 33/49 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.58×** | +6.6 | 5e-09 | 29/48 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.52×** | +6.1 | 1e-07 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.50×** | +5.9 | 3e-07 | 30/48 (HOP62, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 5e-07 | 32/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +5.8 | 6e-07 | 29/48 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +5.6 | 1e-06 | 36/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.28×** | +5.1 | 2e-05 | 24/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.009 | 19/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.30×** | +3.7 | 0.011 | 22/48 (A-427, LS 180, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.011 | 17/48 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.033 | 15/48 (LOX-IMVI, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.081 | 16/48 (KATO III, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.098 | 19/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -17.3 | 0e+00 | 46/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -11.3 | 2e-27 | 44/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -9.3 | 2e-18 | 38/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.655×** | -6.1 | 1e-07 | 29/47 (NCI-H23, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -5.8 | 7e-07 | 28/42 (C-33 A, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -5.0 | 7e-05 | 26/44 (SNU-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.802×** | -4.5 | 5e-04 | 24/48 (HCT15, HOP62, …) | rises with dose | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **0.749×** | -4.2 | 0.002 | 26/48 (J82, SW48, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.003 | 27/48 (C-33 A, KATO III, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.830×** | -3.8 | 0.008 | 20/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.013 | 23/48 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.788×** | -3.4 | 0.027 | 17/48 (A549, C32, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.792×** | -3.4 | 0.033 | 20/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.795×** | -3.3 | 0.036 | 16/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.803×** | -3.2 | 0.057 | 20/48 (HOP62, SW 1088, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.809×** | -3.1 | 0.077 | 17/48 (HOP62, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 84.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -13.9) |
| [[HOP62 (line)]] | alt | 51.9 | 3 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.70× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.3) |
| [[LS 180 (line)]] | wt | 58.2 | 2 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -9.9) |
| [[PANC-1 (line)]] | alt | 75.5 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.33× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -18.0) |
| [[A-427 (line)]] | wt | 73.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.8) ⚠ cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.9) |
| [[C32 (line)]] | wt | 64.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -8.7) |
| [[J82 (line)]] | alt | 63.2 | 1 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.51× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -19.1) |
| [[KATO III (line)]] | alt | 42.4 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.94× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.9) |
| [[LoVo (line)]] | wt | 43.0 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 74.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -11.4) |
| [[SW480 (line)]] | alt | 67.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -15.0) |
| [[A-172 (line)]] | wt | 30.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -14.3) |
| [[AN3 CA (line)]] | alt | 93.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.7) |
| [[H4 (line)]] | wt | 79.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0453× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.4) |
| [[HCT15 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 92.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0490× (z -22.7) |
| [[NCI-H23 (line)]] | alt | 83.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0838× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.7) |
| [[SW1417 (line)]] | alt | 61.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.2) |
| [[SW48 (line)]] | wt | 105 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.2) |
| [[C-33 A (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -16.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 0.5 µM 0.0796× (z -8.9) |
| [[Hs 766T (line)]] | wt | 58.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.1) |
| [[HS-578T (line)]] | alt | 69.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 71.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -12.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 66.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.3) |
| [[SNU-423 (line)]] | alt | 37.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.3) |
| [[A549 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENT4A]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[RNF4]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[RPA1]] | +0.74 | +0.84 / +0.69 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[SNRPA1]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PMS2P3-1]] | +0.71 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[PPIH]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SNHG30]] | +0.70 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[SNRNP40]] | +0.70 | +0.73 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[POC1A]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PDE7A]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[WHAMMP1]] | +0.67 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[RFC4]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFE3]] | -0.66 | -0.67 / -0.58 | both halves | 8e-06 |  |
| [[BCL10]] | -0.65 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[CHMP4A]] | -0.64 | -0.74 / -0.53 | both halves | 1e-05 | pathway: HCMV Infection |
| [[TUT7]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ZNF554]] | -0.61 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[ZNF674]] | -0.61 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[GOLGB1]] | -0.60 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[AFF4]] | -0.60 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[SLC22A1]] | -0.60 | -0.70 / -0.55 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.60 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[CREB3]] | -0.59 | -0.63 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB3]] | B | LAMB3 activity lowers NDC1's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.24× higher at baseline in the lines without LAMB3 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[NT5M]] | B | NT5M activity raises NDC1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without NT5M | 0.079 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[DSCC1]] | C | DSCC1 activity raises NDC1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without DSCC1 | 0.050 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[OIP5]] | C | OIP5's natural level strengthens NDC1's drug response | OIP5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.03; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FNTB]] | C | NDC1's natural level strengthens FNTB's drug response | NDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.13; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.9, -15.1); signed map (-39.2, -13.3). **Vector** length 138, 45.7% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +7.6 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.8 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +5.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.9 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.6 | -11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -12.4 | -17.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.3 | -9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | NDC1 transmembrane nucleoporin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:53,765,478-53,838,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10407, NET3; previously TMEM48 |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 73 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTX1](https://www.uniprot.org/uniprotkb/Q9BTX1) (Nucleoporin NDC1):

> Component of the nuclear pore complex (NPC), which plays a key role in de novo assembly and insertion of NPC in the nuclear envelope. Required for NPC and nuclear envelope assembly, possibly by forming a link between the nuclear envelope membrane and soluble nucleoporins, thereby anchoring the NPC in the membrane.

**Summary**, from NCBI Gene [55706](https://www.ncbi.nlm.nih.gov/gene/55706):

> A structural constituent of nuclear pore. Involved in nuclear pore complex assembly and nuclear pore localization. Located in nuclear membrane. Part of nuclear pore. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25525) · Entrez [55706](https://www.ncbi.nlm.nih.gov/gene/55706) · UniProt [Q9BTX1](https://www.uniprot.org/uniprotkb/Q9BTX1) · Ensembl [ENSG00000058804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058804)

## Data

Gene col 668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 668); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 668]; `tensor/DDL_lfc|DDL_z.npy` [668]; `embed/gene_vectors.npy` [668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 668 or target_col == 668). Every well: [[NDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
