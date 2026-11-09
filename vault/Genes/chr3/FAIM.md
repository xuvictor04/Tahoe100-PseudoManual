---
symbol: "FAIM"
type: "gene"
col: 8145
ensembl_id: "ENSG00000158234"
name: "Fas apoptotic inhibitory molecule"
location: "3q22.3"
module: 137
arm: "+"
pooled_cpm: 7.84
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# FAIM

*Fas apoptotic inhibitory molecule* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +11.7, q 9e-29, up in 13 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.60× (z +6.1, q 1e-07, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.233× (z -18.8, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C6]] (+0.75, fdr 1e-05), [[DHRS4]] (+0.75, fdr 1e-05), [[SLC25A21]] (+0.75, fdr 3e-05); moves opposite to [[DNAAF3]] (-0.73, fdr 2e-05), [[PIBF1]] (-0.67, fdr 3e-05), [[COX6A1]] (-0.66, fdr 5e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[FAM169A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +11.7 | 9e-29 | 13/14 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +8.6 | 2e-15 | 24/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +8.3 | 1e-14 | 24/46 (Panc 03.27, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +7.0 | 3e-10 | 12/21 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.1 | 1e-07 | 19/46 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 7e-05 | 12/47 (KATO III, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 1e-04 | 12/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.4 | 7e-04 | 16/36 (SW1417, A-172, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +4.3 | 9e-04 | 15/47 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.006 | 11/46 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.8 | 0.008 | 8/33 (SNU-423, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.008 | 6/46 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 12/42 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.011 | 11/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.019 | 11/40 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.061 | 9/45 (NCI-H2347, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.061 | 13/40 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.233×** | -18.8 | 0e+00 | 46/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.240×** | -18.4 | 0e+00 | 41/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.272×** | -16.8 | 0e+00 | 42/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.482×** | -9.4 | 6e-19 | 31/42 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.493×** | -9.1 | 7e-18 | 33/47 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.507×** | -8.8 | 1e-16 | 31/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.626×** | -8.6 | 7e-16 | 26/43 (NCI-H460, MIA PaCa-2, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.556×** | -7.6 | 2e-12 | 25/42 (NCI-H23, J82, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -5.9 | 3e-07 | 24/44 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.423×** | -5.8 | 3e-07 | 24/46 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.437×** | -5.6 | 1e-06 | 22/40 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -5.5 | 2e-06 | 24/46 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.694×** | -4.7 | 1e-04 | 20/46 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -4.1 | 0.002 | 16/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.733×** | -4.0 | 0.002 | 16/46 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.592×** | -3.5 | 0.014 | 12/37 (SW1417, SHP-77, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.788×** | -3.0 | 0.090 | 10/40 (HepG2/C3A, A549, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **0.796×** | -3.0 | 0.091 | 11/43 (HOP62, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.36 | 1 (1 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -10.2) |
| [[SW48 (line)]] | wt | 15.2 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0428× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0489× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0744× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 5.59 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -10.4) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0965× (z -16.7) |
| [[A-427 (line)]] | wt | 15.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -11.0) |
| [[LoVo (line)]] | wt | 8.64 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0731× (z -13.0) |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -12.1) |
| [[A-172 (line)]] | wt | 5.67 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0544× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 9.46 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -8.7) |
| [[J82 (line)]] | alt | 7.66 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0788× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 7.33 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0454× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 4.35 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0284× (z -12.2) |
| [[LS 180 (line)]] | wt | 8.20 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.131× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 6.26 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -8.7) |
| [[SNU-423 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.107× (z -9.9) ⚠ toxic |
| [[A498 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C6]] | +0.75 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[DHRS4]] | +0.75 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SLC25A21]] | +0.75 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[PRDM11]] | +0.74 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[IDNK]] | +0.73 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.73 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[KLHL42]] | +0.72 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[PBLD]] | +0.71 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[FAM169A]] | +0.71 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[FBXW4]] | +0.71 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RXYLT1]] | +0.69 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[ZMYND11]] | +0.69 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.73 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PIBF1]] | -0.67 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.66 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[SLC27A1]] | -0.65 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[GNAI2]] | -0.65 | -0.58 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ABCB9]] | -0.64 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[EFHC1]] | -0.64 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[RAB3A]] | -0.64 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[YIF1B]] | -0.64 | -0.54 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[NXPH4]] | -0.63 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[FCHO1]] | -0.63 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[RFX2]] | -0.63 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[SH3GL1]] | -0.63 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[RNF24]] | -0.63 | -0.62 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | FAM169A activity raises FAIM's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.80× lower at baseline in the lines without FAM169A | 0.008 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[TOP2A]] | B | TOP2A activity lowers FAIM's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYO1E]] | B | MYO1E activity lowers FAIM's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.65× higher at baseline in the lines without MYO1E | 0.046 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity lowers FAIM's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.71× higher at baseline in the lines without NDRG1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[MRAS]] | B | MRAS activity raises FAIM's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without MRAS | 0.057 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[LIMCH1]] | B | LIMCH1 activity lowers FAIM's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.22× higher at baseline in the lines without LIMCH1 | 0.077 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[FAXC]] | B | FAXC activity raises FAIM's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.29× lower at baseline in the lines without FAXC | 0.079 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[EEPD1]] | B | EEPD1 activity raises FAIM's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.45× lower at baseline in the lines without EEPD1 | 0.088 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[STOX1]] | B | STOX1 activity raises FAIM's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without STOX1 | 0.094 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[SLC16A9]] | B | SLC16A9 activity raises FAIM's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without SLC16A9 | 0.098 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[CIB1]], [[SEMA4B]], [[SLC2A1]] | C | CIB1, SEMA4B, SLC2A1 activity lowers FAIM's level | lines that do not express CIB1, SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 1.66× higher at baseline in the lines without CIB1, SEMA4B, SLC2A1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.892). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.9, 8.1); signed map (23.9, -27.3). **Vector** length 80.9, 15.3% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.2 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.3 | -18.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -9.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -9.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -18.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -16.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -5.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | Fas apoptotic inhibitory molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,608,606-138,633,376 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10582, FAIM1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVQ4](https://www.uniprot.org/uniprotkb/Q9NVQ4) (Fas apoptotic inhibitory molecule 1):

> Plays a role as an inducible effector molecule that mediates Fas resistance produced by surface Ig engagement in B cells.

**Summary**, from NCBI Gene [55179](https://www.ncbi.nlm.nih.gov/gene/55179):

> The protein encoded by this gene protects against death receptor-triggered apoptosis and regulates B-cell signaling and differentiation. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:18703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18703) · Entrez [55179](https://www.ncbi.nlm.nih.gov/gene/55179) · UniProt [Q9NVQ4](https://www.uniprot.org/uniprotkb/Q9NVQ4) · Ensembl [ENSG00000158234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158234)

## Data

Gene col 8145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8145); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8145]; `tensor/DDL_lfc|DDL_z.npy` [8145]; `embed/gene_vectors.npy` [8145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8145 or target_col == 8145). Every well: [[FAIM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAIM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
