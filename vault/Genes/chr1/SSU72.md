---
symbol: "SSU72"
type: "gene"
col: 8297
ensembl_id: "ENSG00000160075"
name: "SSU72 homolog, RNA polymerase II CTD phosphatase"
location: "1p36.33"
module: 3
arm: "-"
pooled_cpm: 36.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SSU72

*SSU72 homolog, RNA polymerase II CTD phosphatase* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +16.3, q 0e+00, up in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.41× (z +12.0, q 4e-31, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.672× (z -7.5, q 5e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.77, fdr 7e-06), [[ZNF460]] (+0.72, fdr 7e-06), [[SF3B4]] (+0.72, fdr 7e-06); moves opposite to [[LAMTOR5]] (-0.68, fdr 4e-05), [[CAMLG]] (-0.67, fdr 1e-05), [[TMEM191A-1]] (-0.66, fdr 7e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +16.3 | 0e+00 | 41/46 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +15.0 | 0e+00 | 38/39 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +14.2 | 1e-43 | 36/43 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.41×** | +12.0 | 4e-31 | 45/48 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +9.8 | 1e-20 | 39/48 (SW480, HCT15, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +7.5 | 5e-12 | 0/48 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +7.1 | 7e-11 | 33/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +6.2 | 3e-08 | 29/45 (HEC-1-A, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.7 | 1e-06 | 26/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Eplerenone (drug)]] 0.05 µM |  | **1.29×** | +4.4 | 7e-04 | 20/47 (PANC-1, A498, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.8 | 0.007 | 16/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.009 | 16/48 (KATO III, HT-29, …) | two highest doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.017 | 16/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.4 | 0.030 | 18/45 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.069 | 7/48 (SK-MEL-2, SW 1088, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.087 | 11/47 (LoVo, HCT15, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8297.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.672×** | -7.5 | 5e-11 | 33/48 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.696×** | -6.8 | 3e-09 | 34/48 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.723×** | -6.1 | 2e-07 | 33/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.742×** | -5.6 | 3e-06 | 32/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Adenine (drug)]] 5 µM |  | **0.820×** | -5.3 | 1e-05 | 21/48 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.821×** | -5.2 | 1e-05 | 25/48 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.788×** | -4.5 | 6e-04 | 22/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.867× | -3.8 | 0.009 | 17/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Eplerenone (drug)]] 5 µM |  | **0.811×** | -3.8 | 0.009 | 15/48 (SW 1088, NCI-H1573, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.875× | -3.6 | 0.021 | 15/48 (SNU-423, RKO, …) | top dose only | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.878× | -3.5 | 0.026 | 7/48 (NCI-H1792, SW480, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **0.832×** | -3.5 | 0.026 | 18/47 (A549, SHP-77, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.031 | 15/47 (SNU-1, SW 900, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 44.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.30× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -13.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 30.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 36.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +12.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 53.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +12.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 44.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 51.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +14.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 23.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.0) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.428× (z -8.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[C32 (line)]] | wt | 20.9 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.166× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.06× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 54.8 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.7) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 39.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.1× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +8.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +11.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.99× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 35.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.05× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.77 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.72 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TUG1]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[COG8]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[NRAS]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[MCM3AP]] | +0.69 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[MFN2]] | +0.68 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[PSME3]] | +0.68 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SRSF1]] | +0.68 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[ABCF2]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5]] | -0.68 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[CAMLG]] | -0.67 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | -0.66 | -0.38 / -0.67 | both halves | 7e-05 |  |
| [[IFI27L2]] | -0.66 | -0.39 / -0.71 | both halves | 6e-05 |  |
| [[VPS37D]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.64 | -0.36 / -0.69 | both halves | 1e-04 |  |
| [[CNNM4]] | -0.63 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[LIN7B]] | -0.63 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ING2]] | -0.62 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[RPL18]] ⚠ | -0.61 | -0.32 / -0.66 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J]] ⚠ | -0.61 | -0.28 / -0.62 | both halves | 3e-04 | pathway: RNA polymerase II transcribes snRNA genes; STRING 558; ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | -0.61 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[SPATA7]] | -0.61 | -0.41 / -0.68 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SSU72's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SSU72's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.7, -25.2); signed map (-13.4, -35.3). **Vector** length 106, 25.2% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dengue Virus-Host Interactions* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.5 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -7.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | SSU72 homolog, RNA polymerase II CTD phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,541,673-1,574,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC182 |
| Gene groups (HGNC) | Serine/threonine phosphatases |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP77](https://www.uniprot.org/uniprotkb/Q9NP77) (RNA polymerase II subunit A C-terminal domain phosphatase SSU72):

> Protein phosphatase that catalyzes the dephosphorylation of the C-terminal domain of RNA polymerase II. Plays a role in RNA processing and termination. Plays a role in pre-mRNA polyadenylation via its interaction with SYMPK.

**Summary**, from NCBI Gene [29101](https://www.ncbi.nlm.nih.gov/gene/29101):

> Enables RNA polymerase II CTD heptapeptide repeat phosphatase activity. Involved in co-transcriptional mRNA 3'-end processing, cleavage and polyadenylation pathway. Predicted to be located in cytoplasm and nucleus. Predicted to be part of mRNA cleavage and polyadenylation specificity factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25016) · Entrez [29101](https://www.ncbi.nlm.nih.gov/gene/29101) · UniProt [Q9NP77](https://www.uniprot.org/uniprotkb/Q9NP77) · Ensembl [ENSG00000160075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160075)

## Data

Gene col 8297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8297); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8297]; `tensor/DDL_lfc|DDL_z.npy` [8297]; `embed/gene_vectors.npy` [8297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8297 or target_col == 8297). Every well: [[SSU72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSU72.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
