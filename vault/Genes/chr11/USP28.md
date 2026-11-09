---
symbol: "USP28"
type: "gene"
col: 528
ensembl_id: "ENSG00000048028"
name: "ubiquitin specific peptidase 28"
location: "11q23.2"
module: 164
arm: "+"
pooled_cpm: 55.87
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# USP28

*ubiquitin specific peptidase 28* — 11q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +10.1, q 3e-21, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.461× (z -18.7, q 0e+00, down in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.830× (z -4.9, q 8e-05, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP37]] (+0.67, fdr 7e-06), [[BNIP3]] (+0.67, fdr 1e-05), [[CABIN1]] (+0.66, fdr 7e-06); moves opposite to [[SFPQ]] (-0.49, fdr 7e-05), [[AVEN]] (-0.48, fdr 4e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PAX6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +10.1 | 3e-21 | 27/48 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +8.6 | 3e-15 | 32/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +8.5 | 4e-15 | 37/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +7.8 | 7e-13 | 31/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +7.3 | 4e-11 | 31/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.8 | 1e-09 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +5.9 | 3e-07 | 26/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +5.7 | 8e-07 | 24/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +4.6 | 3e-04 | 17/47 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +4.4 | 8e-04 | 17/47 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.16× | +3.8 | 0.008 | 13/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.10× | +3.5 | 0.020 | 22/48 (NCI-H2347, HEC-1-A, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.4 | 0.028 | 14/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.042 | 6/47 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.13× | +3.1 | 0.069 | 5/47 (BT-474, HT-29, …) | top dose only | position effect removed |
| [[Fumaric acid (drug)]] 5 µM |  | 1.13× | +3.0 | 0.082 | 5/48 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.082 | 4/48 (NCI-H460, SNU-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.093 | 14/48 (MIA PaCa-2, HCT15, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | 1.12× | +2.9 | 0.095 | 5/47 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.12× | +2.9 | 0.095 | 7/48 (NCI-H1792, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.461×** | -18.7 | 0e+00 | 38/45 (RKO, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -14.5 | 3e-45 | 44/47 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.586×** | -13.4 | 1e-38 | 32/43 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.621×** | -12.4 | 2e-33 | 37/46 (A-427, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -9.1 | 9e-18 | 27/47 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.760×** | -6.9 | 6e-10 | 29/47 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.872× | -5.0 | 4e-05 | 20/48 (A-427, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.830×** | -4.9 | 8e-05 | 21/48 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.711×** | -4.6 | 2e-04 | 16/35 (HepG2/C3A, C32, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.865× | -3.8 | 0.009 | 14/48 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.865× | -3.6 | 0.019 | 10/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.877× | -3.4 | 0.029 | 5/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.3 | 0.040 | 17/48 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.884× | -3.2 | 0.054 | 17/48 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.886× | -3.2 | 0.059 | 4/48 (A-427, C32, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.799×** | -3.1 | 0.079 | 8/48 (HEC-1-A, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.804×** | -3.0 | 0.097 | 9/45 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 68.0 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 39.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 44.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 52.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 69.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -17.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 50.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -24.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 157 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 33.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -13.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 48.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.289× (z -8.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 45.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 62.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -13.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 52.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 90.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.525× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 46.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -15.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 59.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 52.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -15.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 85.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.475× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 78.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -17.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -10.7) ⚠ toxic |
| [[C32 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 61.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 45.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +12.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 48.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.417× (z -8.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 33.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.438× (z -9.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 80.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP37]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 | same gene group; pathway: Deubiquitination; STRING 667 |
| [[BNIP3]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[CABIN1]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MXI1]] | +0.64 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[YEATS2]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PEX3]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[GYS1]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[IPMK]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[PLEKHA2]] | +0.60 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ZNF395]] | +0.60 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[AVEN]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX6]] | B | PAX6 activity raises USP28's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 1.44× lower at baseline in the lines without PAX6 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[HDAC6]] | B | HDAC6 activity lowers USP28's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM216A]] | B | FAM216A activity raises USP28's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without FAM216A | 0.090 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -17.0); signed map (-37.2, 25.1). **Vector** length 108, 26.7% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.6 | +8.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.5 | +3.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.6 | -18.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -13.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -12.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.9 | -5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.2 — chr11:113,797,874-113,875,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1515 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RU2](https://www.uniprot.org/uniprotkb/Q96RU2) (Ubiquitin carboxyl-terminal hydrolase 28):

> Deubiquitinase involved in DNA damage response checkpoint and MYC proto-oncogene stability. Involved in DNA damage induced apoptosis by specifically deubiquitinating proteins of the DNA damage pathway such as CLSPN. Also involved in G2 DNA damage checkpoint, by deubiquitinating CLSPN, and preventing its degradation by the anaphase promoting complex/cyclosome (APC/C). In contrast, it does not deubiquitinate PLK1. Specifically deubiquitinates MYC in the nucleoplasm, leading to prevent MYC …

**Summary**, from NCBI Gene [57646](https://www.ncbi.nlm.nih.gov/gene/57646):

> The protein encoded by this gene is a deubiquitinase involved in the DNA damage pathway and DNA damage-induced apoptosis. Overexpression of this gene is seen in several cancers. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:12625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12625) · Entrez [57646](https://www.ncbi.nlm.nih.gov/gene/57646) · UniProt [Q96RU2](https://www.uniprot.org/uniprotkb/Q96RU2) · Ensembl [ENSG00000048028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048028)

## Data

Gene col 528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 528); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 528]; `tensor/DDL_lfc|DDL_z.npy` [528]; `embed/gene_vectors.npy` [528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 528 or target_col == 528). Every well: [[USP28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
