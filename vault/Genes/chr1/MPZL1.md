---
symbol: "MPZL1"
type: "gene"
col: 12500
ensembl_id: "ENSG00000197965"
name: "myelin protein zero like 1"
location: "1q24.2"
module: 77
arm: "+"
pooled_cpm: 122.61
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# MPZL1

*myelin protein zero like 1* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.70× (z +14.7, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.474× (z -28.9, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNA12]] (+0.68, fdr 1e-05), [[ATP7B]] (+0.67, fdr 1e-05), [[PACC1]] (+0.66, fdr 4e-05); moves opposite to [[DCAF8]] (-0.67, fdr 1e-05), [[ZC3H4]] (-0.65, fdr 1e-05), [[C11orf58]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +14.7 | 0e+00 | 37/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +11.7 | 3e-29 | 31/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +10.7 | 3e-24 | 31/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +9.7 | 4e-20 | 31/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +9.5 | 1e-19 | 28/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +8.1 | 7e-14 | 30/45 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +8.0 | 1e-13 | 34/49 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +7.7 | 7e-13 | 31/48 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +7.6 | 2e-12 | 29/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +7.6 | 2e-12 | 32/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +5.6 | 1e-06 | 18/48 (PANC-1, RKO, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.23×** | +5.5 | 2e-06 | 25/47 (LoVo, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.13× | +4.8 | 8e-05 | 20/49 (COLO 205, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 6e-04 | 16/49 (C32, RPMI-7951, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.1 | 0.002 | 14/38 (LOX-IMVI, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.7 | 0.007 | 9/48 (CHP-212, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.011 | 14/48 (MIA PaCa-2, NCI-H460, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.012 | 17/49 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.474×** | -28.9 | 0e+00 | 38/48 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -9.5 | 9e-19 | 28/48 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.765×** | -7.2 | 1e-10 | 27/48 (A-172, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.781×** | -6.6 | 5e-09 | 24/44 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.811×** | -5.8 | 6e-07 | 23/49 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.824×** | -5.4 | 6e-06 | 23/48 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.695×** | -5.3 | 1e-05 | 24/49 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.837× | -4.6 | 3e-04 | 21/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.767×** | -3.9 | 0.007 | 17/50 (NCI-H2030, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.7 | 0.012 | 19/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.915× | -3.5 | 0.026 | 11/48 (J82, NCI-H2030, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.885× | -3.4 | 0.031 | 12/49 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.888× | -3.3 | 0.042 | 13/48 (RPMI-7951, J82, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.807×** | -3.1 | 0.076 | 10/49 (C32, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 138 | 2 | 6 (4 ⚠) | [[Belinostat (drug)]] 5 µM 1.88× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -16.4) |
| [[A-172 (line)]] | wt | 234 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -32.7) |
| [[PANC-1 (line)]] | alt | 60.6 | 3 | 3 | [[Belinostat (drug)]] 5 µM 2.58× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -24.1) |
| [[A498 (line)]] | wt | 351 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -30.6) |
| [[NCI-H1573 (line)]] | alt | 127 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.6) |
| [[NCI-H2030 (line)]] | alt | 210 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -35.2) |
| [[CFPAC-1 (line)]] | alt | 83.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.32× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 165 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -24.1) |
| [[J82 (line)]] | alt | 227 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -20.8) |
| [[LoVo (line)]] | wt | 95.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.02× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~16% of this change | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 80.5 | 1 | 2 | [[Belinostat (drug)]] 5 µM 2.16× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.5) |
| [[RKO (line)]] | wt | 90.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -18.0) |
| [[SW480 (line)]] | alt | 70.2 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.03× (z +10.4) | — |
| [[A549 (line)]] | wt | 148 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 78.4 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.70× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 60.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.9) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.5) |
| [[HOP62 (line)]] | alt | 167 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -19.3) |
| [[NCI-H460 (line)]] | wt | 163 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -23.7) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.3) |
| [[SW1417 (line)]] | alt | 85.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -15.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 88.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -26.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 57.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.3) |
| [[H4 (line)]] | wt | 80.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.438× (z -10.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 64.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.0) |
| [[Hs 766T (line)]] | wt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -27.6) |
| [[NCI-H23 (line)]] | alt | 78.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.2) |
| [[SHP-77 (line)]] | alt | 80.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 85.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -25.3) |
| [[SNU-1 (line)]] | wt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.4) |
| [[AN3 CA (line)]] | alt | 118 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNA12]] | +0.68 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ATP7B]] | +0.67 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[PACC1]] | +0.66 | +0.71 / +0.43 | both halves | 4e-05 |  |
| [[WASF3]] | +0.66 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[RGS10]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.65 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ANO10]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[ECI2]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.62 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[HYKK]] | +0.61 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[PALS2]] | +0.61 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[WDFY2]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF8]] | -0.67 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.65 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.64 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[MED12]] | -0.64 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[RBM23]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[GTF2H1]] | -0.63 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.63 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[SRRM2]] | -0.62 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PMF1]] | -0.61 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[WARS2-AS1]] | -0.60 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[CHMP3]] | -0.60 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPH2]] | -0.60 | -0.62 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MPZL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers MPZL1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.2, 2.4); signed map (-41.0, -3.5). **Vector** length 135, 39.8% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.6 | +14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +9.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.3 | +8.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.3 | +7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +7.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.9 | -28.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.0 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.4 | -5.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | myelin protein zero like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:167,721,192-167,791,919 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PZR, FLJ21047 |
| Gene groups (HGNC) | V-set domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [O95297](https://www.uniprot.org/uniprotkb/O95297) (Myelin protein zero-like protein 1):

> Cell surface receptor, which is involved in signal transduction processes. Recruits PTPN11/SHP-2 to the cell membrane and is a putative substrate of PTPN11/SHP-2. Is a major receptor for concanavalin-A (ConA) and is involved in cellular signaling induced by ConA, which probably includes Src family tyrosine-protein kinases. Isoform 3 seems to have a dominant negative role; it blocks tyrosine phosphorylation of MPZL1 induced by ConA. Isoform 1, but not isoform 2 and isoform 3, may be involved in …

**Summary**, from NCBI Gene [9019](https://www.ncbi.nlm.nih.gov/gene/9019):

> Enables identical protein binding activity. Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway and cell-cell signaling. Predicted to act upstream of or within positive regulation of cell migration. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7226) · Entrez [9019](https://www.ncbi.nlm.nih.gov/gene/9019) · UniProt [O95297](https://www.uniprot.org/uniprotkb/O95297) · Ensembl [ENSG00000197965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197965)

## Data

Gene col 12500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12500); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12500]; `tensor/DDL_lfc|DDL_z.npy` [12500]; `embed/gene_vectors.npy` [12500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12500 or target_col == 12500). Every well: [[MPZL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPZL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
