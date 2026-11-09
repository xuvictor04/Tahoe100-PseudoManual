---
symbol: "HSD17B7"
type: "gene"
col: 5284
ensembl_id: "ENSG00000132196"
name: "hydroxysteroid 17-beta dehydrogenase 7"
location: "1q23.3"
module: 86
arm: "+"
pooled_cpm: 9.97
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 18
n_dd_up_clean: 27
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# HSD17B7

*hydroxysteroid 17-beta dehydrogenase 7* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (3 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.24× (z +15.8, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.358× (z -14.2, q 3e-43, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B7P2]] (+0.83, fdr 7e-06), [[MSMO1]] (+0.74, fdr 7e-06), [[HMGCR]] (+0.74, fdr 7e-06); moves opposite to [[ZNF236]] (-0.42, fdr 3e-04), [[VMA21]] (-0.40, fdr 2e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.24×** | +15.8 | 0e+00 | 39/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.77×** | +11.2 | 9e-27 | 39/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +9.1 | 1e-17 | 27/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.98×** | +9.0 | 5e-17 | 33/44 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.76×** | +7.4 | 2e-11 | 23/32 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +7.0 | 3e-10 | 22/47 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | **1.62×** | +6.4 | 1e-08 | 17/47 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +6.1 | 8e-08 | 22/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +6.1 | 8e-08 | 16/47 (RKO, HOP62, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.56×** | +5.9 | 2e-07 | 19/47 (C32, HOP62, …) | top dose only | plate-row cell shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.7 | 7e-07 | 22/47 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.2 | 1e-05 | 17/47 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 4e-05 | 23/45 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +4.9 | 4e-05 | 14/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.40×** | +4.7 | 1e-04 | 14/47 (C32, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 2e-04 | 20/47 (A498, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.358×** | -14.2 | 3e-43 | 37/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.403×** | -12.6 | 6e-34 | 36/47 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.447×** | -11.2 | 1e-26 | 36/45 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -9.8 | 2e-20 | 32/46 (PANC-1, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.501×** | -9.6 | 1e-19 | 23/33 (LS 180, A-172, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -7.2 | 6e-11 | 25/47 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.604×** | -7.0 | 2e-10 | 29/47 (BT-474, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -6.5 | 5e-09 | 22/46 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.651×** | -5.7 | 6e-07 | 15/20 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.658×** | -5.6 | 1e-06 | 20/46 (PANC-1, KATO III, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.671×** | -5.3 | 5e-06 | 19/46 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.684×** | -5.3 | 6e-06 | 22/47 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.749×** | -3.9 | 0.005 | 11/47 (RPMI-7951, C32, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.779×** | -3.5 | 0.021 | 12/45 (A549, HOP62, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.771×** | -3.3 | 0.032 | 14/29 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Everolimus (drug)]] 5 µM |  | **0.725×** | -3.3 | 0.034 | 7/47 (C-33 A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **0.786×** | -3.2 | 0.042 | 8/47 (LS 180, SW 1271, …) | top dose only | position effect removed |
| [[Quinestrol (drug)]] 5 µM |  | 0.850× | -3.2 | 0.044 | 11/48 (KATO III, HOP62, …) | rises with dose | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.853× | -3.1 | 0.052 | 6/48 (SW 1271, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.1 | 1 | 6 (4 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.53× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -11.5) |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0396× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.114× (z -9.4) |
| [[SW480 (line)]] | alt | 9.42 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0998× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.113× (z -14.5) |
| [[HS-578T (line)]] | alt | 11.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0951× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.0622× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0818× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.132× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 14.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.49× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 6.67 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.82× (z +10.9) | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0427× (z -17.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 5.82 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.0685× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.23 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.208× (z -8.7) |
| [[A-427 (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -11.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 5.68 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0610× (z -11.1) |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -8.9) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0906× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[LoVo (line)]] | wt | 6.77 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0690× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 8.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 7.68 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 4.05× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.112× (z -8.7) |
| [[A498 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B7P2]] | +0.83 | +0.75 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MSMO1]] | +0.74 | +0.64 / +0.72 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 998 |
| [[HMGCR]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 849 |
| [[FDPS]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 813 |
| [[MVD]] | +0.71 | +0.64 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 688 |
| [[FDFT1]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 993 |
| [[ACSS2]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[IDI1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 805 |
| [[SCD]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[HMGCS1]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 872 |
| [[SQLE]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 854 |
| [[CYP51A1]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 996 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF236]] | -0.42 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[VMA21]] | -0.40 | -0.44 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.8, -49.2); signed map (-53.4, 32.7). **Vector** length 102, 23.5% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.59 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.59 to 16); *mTORC1 signaling* (hallmark, mean cos +0.51 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +9.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +6.4 | +15.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +9.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.2 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +4.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.0 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.7 | -14.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.4 | -12.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -11.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid 17-beta dehydrogenase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:162,790,702-162,812,823 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRAP, SDR37C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, FATTY_ACID_METABOLISM |
| Reactome | 5 pathways, smallest: Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); Cholesterol biosynthesis via desmosterol (Bloch pathway); Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P56937](https://www.uniprot.org/uniprotkb/P56937) (3-keto-steroid reductase/17-beta-hydroxysteroid dehydrogenase 7):

> Bifunctional enzyme involved in steroid-hormone metabolism and cholesterol biosynthesis. Catalyzes the NADP(H)-dependent reduction of estrogens and androgens and regulates the biological potency of these steroids. Converts estrone (E1) to a more potent estrogen, 17beta-estradiol (E2). Converts dihydrotestosterone (DHT) to its inactive form 5a-androstane-3b,17b-diol. Converts moderately progesterone to 3beta-hydroxypregn-4-ene-20-one, leading to its inactivation. Additionally, participates in …

**Summary**, from NCBI Gene [51478](https://www.ncbi.nlm.nih.gov/gene/51478):

> HSD17B7 encodes an enzyme that functions both as a 17-beta-hydroxysteroid dehydrogenase (EC 1.1.1.62) in the biosynthesis of sex steroids and as a 3-ketosteroid reductase (EC 1.1.1.270) in the biosynthesis of cholesterol (Marijanovic et al., 2003 [PubMed 12829805]).[supplied by OMIM, May 2010]

**Accessions** — [HGNC:5215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5215) · Entrez [51478](https://www.ncbi.nlm.nih.gov/gene/51478) · UniProt [P56937](https://www.uniprot.org/uniprotkb/P56937) · Ensembl [ENSG00000132196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132196)

## Data

Gene col 5284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5284); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5284]; `tensor/DDL_lfc|DDL_z.npy` [5284]; `embed/gene_vectors.npy` [5284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5284 or target_col == 5284). Every well: [[HSD17B7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSD17B7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
