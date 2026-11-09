---
symbol: "RBM6"
type: "gene"
col: 48
ensembl_id: "ENSG00000004534"
name: "RNA binding motif protein 6"
location: "3p21.31"
module: 58
arm: "+"
pooled_cpm: 223.16
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# RBM6

*RNA binding motif protein 6* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.53× (z +13.8, q 2e-40, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.541× (z -20.0, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.706× (z -11.4, q 9e-28, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (NCI-H2347 0.518×, LOX-IMVI 0.598×, SW48 0.524×, SK-MEL-2 0.627×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 0.0366×, SW480 0.455×, J82 0.373×, NCI-H1573 0.379×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 6 lines (SK-MEL-2 0.434×, HEC-1-A 0.451×, A-172 0.477×, SNU-423 0.543×, …); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.547×, HOP62 0.668×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICOS13]] (+0.62, fdr 2e-05), [[TYW1]] (+0.60, fdr 1e-05), [[ARMH3]] (+0.59, fdr 1e-05); moves opposite to [[SIX4]] (-0.62, fdr 1e-05), [[MKLN1-AS]] (-0.60, fdr 5e-05), [[ZNF436]] (-0.59, fdr 3e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CTXN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 48.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +13.8 | 2e-40 | 40/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +13.1 | 6e-37 | 41/48 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +7.9 | 6e-13 | 27/48 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +7.7 | 2e-12 | 28/48 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +7.3 | 2e-11 | 31/48 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +6.4 | 2e-08 | 24/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +5.9 | 4e-07 | 23/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +5.5 | 3e-06 | 21/47 (NCI-H23, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.2 | 1e-05 | 21/48 (HepG2/C3A, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +4.6 | 2e-04 | 21/47 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 25/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +4.4 | 6e-04 | 23/49 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.13× | +4.0 | 0.003 | 9/49 (SHP-77, AN3 CA, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.12× | +3.5 | 0.017 | 6/48 (HS-578T, SNU-423, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.042 | 3/49 (HT-29, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.097 | 9/48 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 48.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (NCI-H2347 0.518×, LOX-IMVI 0.598×, SW48 0.524×, SK-MEL-2 0.627×, …); [[Dinaciclib (drug)]] 5 µM in 6 lines (SK-MEL-2 0.0366×, SW480 0.455×, J82 0.373×, NCI-H1573 0.379×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 6 lines (SK-MEL-2 0.434×, HEC-1-A 0.451×, A-172 0.477×, SNU-423 0.543×, …); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.547×, HOP62 0.668×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.541×** | -20.0 | 0e+00 | 46/49 (SW48, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -19.0 | 0e+00 | 41/44 (SK-MEL-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.541×** | -18.5 | 0e+00 | 41/45 (SK-MEL-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -11.4 | 9e-28 | 35/48 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -9.0 | 3e-17 | 27/49 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.800×** | -7.0 | 3e-10 | 35/47 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | 0.838× | -5.7 | 7e-07 | 24/48 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.852× | -5.2 | 1e-05 | 19/48 (HS-578T, A-172, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.902× | -4.7 | 1e-04 | 5/48 (NCI-H2347, A498, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.885× | -4.0 | 0.004 | 18/48 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.917× | -4.0 | 0.004 | 1/48 (H4) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.881× | -4.0 | 0.004 | 19/48 (HS-578T, SNU-423, …) | two highest doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.966× | -3.6 | 0.013 | 0/50 | inconsistent across doses | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.907× | -3.2 | 0.064 | 1/47 (SW48) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 48. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 365 | 3 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.57× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 308 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.451× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 244 | 2 | 6 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.90× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -17.2) |
| [[SW48 (line)]] | wt | 329 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.97× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -13.6) |
| [[SW480 (line)]] | alt | 307 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.84× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.455× (z -19.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 167 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.72× (z +9.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.547× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 311 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0366× (z -60.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.434× (z -15.9) |
| [[HS-578T (line)]] | alt | 202 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.62× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -18.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 243 | 3 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.61× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.565× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 206 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -12.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 244 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.543× (z -11.2) |
| [[A549 (line)]] | wt | 175 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.382× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -11.5) |
| [[HOP62 (line)]] | alt | 245 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.571× (z -11.0) |
| [[J82 (line)]] | alt | 261 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -17.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 222 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.85× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 221 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.564× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 189 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.67× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 241 | 1 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.87× (z +11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.520× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.619× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 215 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.69× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -15.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 190 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.565× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 249 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.424× (z -15.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 232 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.95× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -14.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 222 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.12× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 272 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 236 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -21.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 227 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.410× (z -13.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 264 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 1.87× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.505× (z -10.9) |
| [[SNU-1 (line)]] | wt | 244 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.636× (z -8.7) |
| [[SW 900 (line)]] | alt | 169 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.438× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -11.1) |
| [[A498 (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.559× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 262 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 167 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.70× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -13.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 282 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.97× (z +10.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.558× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -12.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 194 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -9.6) |
| [[KATO III (line)]] | alt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.543× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 147 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -16.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 251 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.65× (z +8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.602× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 263 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 277 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -11.5) |
| [[HT-29 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.604× (z -8.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 48), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICOS13]] | +0.62 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TYW1]] | +0.60 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ARMH3]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[LUC7L]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 | STRING 451 |
| [[ANTKMT]] | +0.58 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[MRPL41]] ⚠ | +0.58 | +0.35 / +0.50 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TSEN54]] | +0.58 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[STUB1]] | +0.57 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[WDR70]] | +0.57 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[PTPRA]] | +0.57 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[ATF7]] | +0.57 | +0.62 / +0.32 | both halves | 1e-04 |  |
| [[MEX3D]] | +0.56 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[CELF1]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX4]] | -0.62 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[MKLN1-AS]] | -0.60 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[ZNF436]] | -0.59 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[RNF6]] | -0.58 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[SNX16]] | -0.56 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[ARMT1]] | -0.56 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[THAP2]] | -0.56 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[ZKSCAN8]] | -0.55 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[POLR2M]] | -0.55 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[LGALS8]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ZXDA]] | -0.54 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[STK26]] | -0.53 | -0.52 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTXN1]] | B | CTXN1 activity raises RBM6's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without CTXN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[PI4KAP1-1]] | B | PI4KAP1-1 activity raises RBM6's level | lines that do not express PI4KAP1-1 (26) vs lines expressing it (24) | 1.16× lower at baseline in the lines without PI4KAP1-1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PI4KAP1, ENSG00000260573, LCK |
| [[HDAC6]] | B | HDAC6 activity lowers RBM6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.5, -18.0); signed map (-49.7, -19.0). **Vector** length 120, 37.4% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +9.4 | +13.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.5 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.7 | +7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | -0.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +2.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.9 | -11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.5 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -5.0 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -0.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -1.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,940,007-50,100,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DEF-3, 3G2, NY-LU-12, g16, DEF3 |
| Gene groups (HGNC) | G-patch domain containing; RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P78332](https://www.uniprot.org/uniprotkb/P78332) (RNA-binding protein 6):

> Specifically binds poly(G) RNA homopolymers in vitro.

**Summary**, from NCBI Gene [10180](https://www.ncbi.nlm.nih.gov/gene/10180):

> Enables RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9903) · Entrez [10180](https://www.ncbi.nlm.nih.gov/gene/10180) · UniProt [P78332](https://www.uniprot.org/uniprotkb/P78332) · Ensembl [ENSG00000004534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004534)

## Data

Gene col 48: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 48); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 48, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 48]; `tensor/DDL_lfc|DDL_z.npy` [48]; `embed/gene_vectors.npy` [48]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 48 or target_col == 48). Every well: [[RBM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
