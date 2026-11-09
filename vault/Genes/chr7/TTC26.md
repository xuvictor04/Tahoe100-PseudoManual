---
symbol: "TTC26"
type: "gene"
col: 2691
ensembl_id: "ENSG00000105948"
name: "intraflagellar transport 56"
location: "7q34"
module: 17
arm: "+"
pooled_cpm: 31.08
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TTC26

*intraflagellar transport 56* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.67× (z +22.7, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.520× (z -21.4, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPHP1]] (+0.79, fdr 7e-06), [[THOC1]] (+0.73, fdr 7e-06), [[MRPS31P4]] (+0.72, fdr 1e-05); moves opposite to [[SAXO1]] (-0.64, fdr 2e-04), [[RNF217-AS1]] (-0.60, fdr 4e-04), [[SIAH2-AS1]] (-0.58, fdr 9e-04, ⚠ not reproduced), [[SAP30L-AS1]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.67×** | +22.7 | 0e+00 | 46/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.49×** | +21.2 | 0e+00 | 47/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +19.2 | 0e+00 | 35/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +16.5 | 0e+00 | 43/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +11.0 | 2e-26 | 26/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +9.0 | 2e-17 | 27/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +8.2 | 3e-14 | 24/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +7.5 | 4e-12 | 25/47 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +6.1 | 8e-08 | 22/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.29×** | +5.9 | 2e-07 | 20/47 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +5.7 | 5e-07 | 20/47 (LoVo, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.7 | 5e-07 | 19/47 (RKO, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +5.2 | 9e-06 | 22/47 (RKO, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.9 | 3e-05 | 16/47 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +4.6 | 1e-04 | 13/46 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +4.3 | 8e-04 | 10/47 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.9 | 0.003 | 12/47 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 13/47 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.025 | 10/47 (A498, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.520×** | -21.4 | 0e+00 | 35/47 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -14.3 | 7e-44 | 38/47 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.528×** | -13.6 | 7e-40 | 38/46 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.590×** | -12.2 | 6e-32 | 34/47 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -7.7 | 2e-12 | 29/47 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -5.5 | 3e-06 | 20/47 (A498, COLO 205, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -5.2 | 2e-05 | 21/47 (PANC-1, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.831×** | -4.3 | 0.001 | 13/47 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.835× | -4.1 | 0.002 | 18/46 (SNU-423, LS 180, …) | rises with dose | low cells (technical?) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.842× | -4.0 | 0.004 | 15/47 (C-33 A, SW1417, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.831×** | -3.9 | 0.005 | 14/46 (NCI-H661, HEC-1-A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -3.8 | 0.007 | 2/47 (HepG2/C3A, NCI-H661) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.755×** | -3.4 | 0.031 | 10/42 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.037 | 6/46 (A-427, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 5 µM |  | 0.856× | -3.3 | 0.037 | 6/47 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.868× | -3.2 | 0.044 | 8/47 (HepG2/C3A, SW 1271, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.906× | -3.2 | 0.047 | 6/47 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | 0.863× | -3.1 | 0.055 | 8/47 (CHP-212, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.912× | -3.0 | 0.082 | 7/47 (HOP62, HS-578T, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.784×** | -2.9 | 0.090 | 15/47 (SHP-77, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +37.5) | — |
| [[SW480 (line)]] | alt | 38.3 | 4 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.45× (z +14.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.4) |
| [[C32 (line)]] | wt | 70.7 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -19.9) |
| [[A498 (line)]] | wt | 43.2 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +12.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 29.5 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.32× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.263× (z -11.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.9) |
| [[LoVo (line)]] | wt | 18.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.66× (z +15.1) | — |
| [[PANC-1 (line)]] | alt | 34.0 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +15.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.319× (z -13.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -13.1) |
| [[HT-29 (line)]] | alt | 14.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 66.4 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -10.3) |
| [[RKO (line)]] | wt | 33.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +8.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -17.7) |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -13.0) |
| [[HOP62 (line)]] | alt | 37.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +18.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.402× (z -8.6) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 25.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.7) | — |
| [[KATO III (line)]] | alt | 22.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.20× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -12.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 11.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 33.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.89× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.5) |
| [[A-172 (line)]] | wt | 26.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.213× (z -10.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -10.3) |
| [[A-427 (line)]] | wt | 32.5 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -21.7) |
| [[A549 (line)]] | wt | 37.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.149× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.06× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +16.3) | — |
| [[CFPAC-1 (line)]] | alt | 31.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.3) |
| [[H4 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -11.7) ⚠ toxic |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0963× (z -13.4) ⚠ toxic |
| [[HS-578T (line)]] | alt | 46.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 37.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -10.8) |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.0) |
| [[SW 900 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +9.9) | — |
| [[SW48 (line)]] | wt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 7.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP1]] | +0.79 | +0.68 / +0.73 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[THOC1]] | +0.73 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.72 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.71 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[DHX57]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[CINP]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ZNF45]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TBC1D19]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[GPATCH11]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TMEM67]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAXO1]] | -0.64 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[RNF217-AS1]] | -0.60 | -0.25 / -0.62 | both halves | 4e-04 |  |
| [[SIAH2-AS1]] | -0.58 | -0.18 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[SAP30L-AS1]] | -0.58 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[PXDNL]] | -0.57 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[LINC00880]] | -0.56 | -0.21 / -0.47 | both halves | 6e-04 |  |
| [[EPM2A]] | -0.56 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[ATP11C]] | -0.55 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[C2orf88]] | -0.55 | -0.12 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[PRDM10]] | -0.55 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LINC00393]] | -0.54 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[CPEB2-DT]] | -0.54 | -0.09 / -0.56 | ⚠ one half (not replicated) | 0.003 |  |
| [[GATA2-AS1]] | -0.54 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity raises TTC26's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without DYNC2H1 | 0.010 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[ZNF569]] | B | ZNF569 activity raises TTC26's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without ZNF569 | 0.028 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[TOP2A]] | B | TOP2A activity raises TTC26's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MICB]] | B | MICB activity raises TTC26's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without MICB | 0.093 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[TBC1D19]] | C | TBC1D19 activity raises TTC26's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[CCDC113]] | C | CCDC113 activity raises TTC26's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 2.23× lower at baseline in the lines without CCDC113 | 0.0997 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.2, -2.0); signed map (-21.5, -15.4). **Vector** length 110, 27.8% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +21.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +22.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +16.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +11.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +4.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.0 | -21.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -11.7 | -14.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -10.4 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.5 | -12.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.6 | -13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 56 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,133,744-139,191,986 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12571, dyf-13, DYF13; previously TTC26 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [A0AVF1](https://www.uniprot.org/uniprotkb/A0AVF1) (Intraflagellar transport protein 56):

> Component of the intraflagellar transport (IFT) complex B required for transport of proteins in the motile cilium. Required for transport of specific ciliary cargo proteins related to motility, while it is neither required for IFT complex B assembly or motion nor for cilium assembly. Required for efficient coupling between the accumulation of GLI2 and GLI3 at the ciliary tips and their dissociation from the negative regulator SUFU. Plays a key role in maintaining the integrity of the IFT …

**Summary**, from NCBI Gene [79989](https://www.ncbi.nlm.nih.gov/gene/79989):

> Predicted to enable intraciliary transport particle B binding activity. Involved in cilium assembly. Located in cilium. Part of intraciliary transport particle A. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21882) · Entrez [79989](https://www.ncbi.nlm.nih.gov/gene/79989) · UniProt [A0AVF1](https://www.uniprot.org/uniprotkb/A0AVF1) · Ensembl [ENSG00000105948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105948)

## Data

Gene col 2691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2691); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2691]; `tensor/DDL_lfc|DDL_z.npy` [2691]; `embed/gene_vectors.npy` [2691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2691 or target_col == 2691). Every well: [[TTC26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
