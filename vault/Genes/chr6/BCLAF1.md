---
symbol: "BCLAF1"
type: "gene"
col: 389
ensembl_id: "ENSG00000029363"
name: "BCL2 associated transcription factor 1"
location: "6q23.3"
module: 3
arm: "-"
pooled_cpm: 220.94
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# BCLAF1

*BCL2 associated transcription factor 1* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.31× (z +36.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.451× (z -17.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUBP1]] (+0.72, fdr 7e-06), [[EIF1B-AS1]] (+0.72, fdr 1e-05), [[HNRNPH3]] (+0.70, fdr 1e-05); moves opposite to [[MPG]] (-0.70, fdr 1e-05), [[TMEM184B]] (-0.69, fdr 1e-05), [[TPST2]] (-0.69, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.31×** | +36.6 | 0e+00 | 48/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.20×** | +25.2 | 0e+00 | 48/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.52×** | +19.2 | 0e+00 | 48/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.10×** | +18.4 | 0e+00 | 48/49 (COLO 205, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.98×** | +14.8 | 0e+00 | 48/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.21×** | +13.2 | 1e-37 | 48/48 (COLO 205, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.84×** | +13.2 | 1e-37 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +12.4 | 3e-33 | 40/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +11.5 | 9e-29 | 44/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +10.0 | 1e-21 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.58×** | +9.9 | 2e-21 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +9.5 | 8e-20 | 39/45 (A549, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.47×** | +8.4 | 2e-15 | 38/49 (RKO, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +7.8 | 2e-13 | 35/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.4 | 7e-09 | 33/38 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +5.4 | 3e-06 | 30/48 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.001 | 24/48 (LS 180, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -17.2 | 0e+00 | 47/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -13.3 | 4e-38 | 45/48 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.545×** | -13.1 | 3e-37 | 44/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.560×** | -12.6 | 5e-34 | 45/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.631×** | -10.0 | 2e-21 | 45/48 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.548×** | -6.8 | 9e-10 | 42/49 (A-427, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -4.0 | 0.004 | 0/50 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.887× | -3.7 | 0.016 | 9/48 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.895× | -3.4 | 0.043 | 4/48 (A-427, NCI-H661, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.902× | -3.2 | 0.089 | 3/48 (C-33 A, AsPC-1, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.868× | -3.1 | 0.11 | 8/49 (COLO 205, SW1417, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.869× | -3.0 | 0.11 | 16/48 (C-33 A, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 228 | 14 (8 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +31.0) | [[Belinostat (drug)]] 5 µM 0.376× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 213 | 13 (5 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +28.0) | [[Belinostat (drug)]] 5 µM 0.411× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 198 | 15 (8 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +24.5) | [[Belinostat (drug)]] 5 µM 0.506× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 153 | 13 (7 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +28.3) | [[Belinostat (drug)]] 5 µM 0.334× (z -15.6) |
| [[LS 180 (line)]] | wt | 255 | 11 (5 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +22.8) | [[Belinostat (drug)]] 5 µM 0.467× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 240 | 10 (6 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +23.2) | [[Belinostat (drug)]] 5 µM 0.373× (z -13.6) |
| [[SW480 (line)]] | alt | 326 | 15 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +24.9) | — |
| [[LoVo (line)]] | wt | 263 | 11 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +31.4) | [[Belinostat (drug)]] 5 µM 0.462× (z -12.9) |
| [[HT-29 (line)]] | alt | 236 | 9 (4 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +24.8) | [[Belinostat (drug)]] 5 µM 0.384× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 194 | 11 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +26.2) | [[Panobinostat (drug)]] 0.5 µM 0.503× (z -8.9) |
| [[COLO 205 (line)]] | alt | 574 | 8 (3 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +34.1) | [[Belinostat (drug)]] 5 µM 0.382× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 225 | 8 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +29.6) | [[Belinostat (drug)]] 5 µM 0.423× (z -13.7) |
| [[KATO III (line)]] | alt | 278 | 8 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +27.7) | [[Belinostat (drug)]] 5 µM 0.343× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 228 | 11 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +24.1) | [[Belinostat (drug)]] 5 µM 0.469× (z -9.7) |
| [[SW 900 (line)]] | alt | 246 | 7 (3 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +18.4) | [[Belinostat (drug)]] 5 µM 0.416× (z -12.8) |
| [[A549 (line)]] | wt | 163 | 8 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +30.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -9.7) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.524× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 184 | 10 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +29.5) | [[Belinostat (drug)]] 5 µM 0.496× (z -8.9) |
| [[BT-474 (line)]] | alt | 218 | 10 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +25.5) | [[Belinostat (drug)]] 0.5 µM 0.560× (z -8.7) |
| [[HOP62 (line)]] | alt | 165 | 7 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +26.2) | [[Belinostat (drug)]] 5 µM 0.353× (z -13.2) |
| [[RKO (line)]] | wt | 210 | 10 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +21.1) | [[Belinostat (drug)]] 5 µM 0.497× (z -9.0) |
| [[SW48 (line)]] | wt | 269 | 9 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.2) | [[Belinostat (drug)]] 5 µM 0.364× (z -11.4) |
| [[C32 (line)]] | wt | 173 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +28.0) | [[Belinostat (drug)]] 5 µM 0.354× (z -11.9) |
| [[J82 (line)]] | alt | 181 | 6 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +20.9) | [[Belinostat (drug)]] 5 µM 0.420× (z -12.5) |
| [[SW1417 (line)]] | alt | 259 | 8 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +22.5) | [[Belinostat (drug)]] 5 µM 0.531× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 154 | 5 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +27.5) | [[Belinostat (drug)]] 5 µM 0.343× (z -12.6) |
| [[A-172 (line)]] | wt | 130 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +24.5) | [[Belinostat (drug)]] 5 µM 0.441× (z -9.7) |
| [[A-427 (line)]] | wt | 205 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +17.4) | — |
| [[A498 (line)]] | wt | 174 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.453× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 142 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +19.1) | [[Belinostat (drug)]] 5 µM 0.417× (z -11.0) |
| [[HCT15 (line)]] | alt | 323 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +18.7) | [[Belinostat (drug)]] 5 µM 0.361× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 249 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +19.8) | — |
| [[RPMI-7951 (line)]] | alt | 226 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +22.5) | [[Belinostat (drug)]] 5 µM 0.472× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 157 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +18.6) | [[Belinostat (drug)]] 5 µM 0.436× (z -12.3) |
| [[Hs 766T (line)]] | wt | 166 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +23.4) | [[Belinostat (drug)]] 5 µM 0.470× (z -9.5) |
| [[HS-578T (line)]] | alt | 197 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +22.0) | — |
| [[NCI-H2030 (line)]] | alt | 289 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 161 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +17.5) | [[Belinostat (drug)]] 5 µM 0.528× (z -8.6) |
| [[SNU-423 (line)]] | alt | 269 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +25.5) | [[Belinostat (drug)]] 5 µM 0.438× (z -11.4) |
| [[H4 (line)]] | wt | 179 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +17.1) | [[Belinostat (drug)]] 5 µM 0.337× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 175 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +22.5) | — |
| [[SNU-1 (line)]] | wt | 231 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +18.1) | — |
| [[SHP-77 (line)]] | alt | 279 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +17.7) | — |
| [[C-33 A (line)]] | alt | 285 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.480× (z -8.8) |
| [[CHP-212 (line)]] | wt | 268 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.7) ⚠ cell-cycle shift, explains ~81% of this change |
| [[AN3 CA (line)]] | alt | 279 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.7) | — |
| [[SW 1271 (line)]] | alt | 285 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +10.9) | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | +0.72 | +0.64 / +0.64 | both halves | 7e-06 | STRING 433 |
| [[EIF1B-AS1]] | +0.72 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[HNRNPH3]] | +0.70 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 | STRING 459 |
| [[RBM39]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 | STRING 750 |
| [[HNRNPM]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 | STRING 548 |
| [[SRSF10]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 | STRING 732 |
| [[YWHAE]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ATRX]] | +0.67 | +0.63 / +0.54 | both halves | 1e-05 | STRING 769 |
| [[LEKR1]] | +0.67 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZNF644]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 | STRING 557 |
| [[HNRNPL]] | +0.66 | +0.47 / +0.62 | both halves | 2e-05 | STRING 529 |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.70 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.69 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TPST2]] | -0.69 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.69 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CORO7]] | -0.67 | -0.64 / -0.46 | both halves | 3e-05 |  |
| [[CDC34]] | -0.66 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[MAP3K9]] | -0.66 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.65 | -0.49 / -0.55 | both halves | 2e-05 |  |
| [[GUK1]] | -0.65 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[DNAJC5]] | -0.65 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[HEBP1]] | -0.64 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[RGS10]] | -0.64 | -0.58 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises BCLAF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CTSO]] | B | CTSO activity strengthens BCLAF1's drug response | lines that do not express CTSO (8) vs lines expressing it (41) | the lines without CTSO respond 0.95× as strongly (z diff +0.51); strongest at Panobinostat 0.5 µM: 0.73x vs 0.53x (z diff +4.1) | 0.045 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT; target measured in part of the lines; both ways; artifact flags |
| [[FAM111A]] | C | FAM111A activity weakens BCLAF1's drug response | lines that do not express FAM111A (3) vs lines expressing it (46) | the lines without FAM111A respond 0.80× as strongly (z diff +0.23); strongest at Harringtonine 5 µM: 2.01x vs 2.53x (z diff -3.6) | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent; target measured in part of the lines; both ways; rests on the correction; artifact flags |
| [[SPIRE1]] | C | SPIRE1 activity lowers BCLAF1's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 1.63× higher at baseline in the lines without SPIRE1 | 0.083 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23 |
| [[CLTCL1]] | C | CLTCL1 activity lowers BCLAF1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.56× higher at baseline in the lines without CLTCL1 | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.8, 1.7); signed map (14.5, -37.7). **Vector** length 108, 43.9% of its response variance represented; |z| ≥ 3 in 1,424 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA 3'-end processing* (reactome, mean cos +0.60 to 12); *mRNA Polyadenylation* (reactome, mean cos +0.61 to 11); *mRNA Splicing - Major Pathway* (reactome, mean cos +0.60 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +10.1 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +9.7 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +25.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +36.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -9.1 | -10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.0 | -17.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.4 | -0.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.6 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.5 | -12.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.9 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.4 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -6.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 associated transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:136,256,627-136,289,851 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0164, BTF |
| Gene groups (HGNC) | WTAP complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYF8](https://www.uniprot.org/uniprotkb/Q9NYF8) (Bcl-2-associated transcription factor 1):

> Death-promoting transcriptional repressor. May be involved in cyclin-D1/CCND1 mRNA stability through the SNARP complex which associates with both the 3'end of the CCND1 gene and its mRNA.

**Summary**, from NCBI Gene [9774](https://www.ncbi.nlm.nih.gov/gene/9774):

> This gene encodes a transcriptional repressor that interacts with several members of the BCL2 family of proteins. Overexpression of this protein induces apoptosis, which can be suppressed by co-expression of BCL2 proteins. The protein localizes to dot-like structures throughout the nucleus, and redistributes to a zone near the nuclear envelope in cells undergoing apoptosis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16863) · Entrez [9774](https://www.ncbi.nlm.nih.gov/gene/9774) · UniProt [Q9NYF8](https://www.uniprot.org/uniprotkb/Q9NYF8) · Ensembl [ENSG00000029363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000029363)

## Data

Gene col 389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 389); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 389]; `tensor/DDL_lfc|DDL_z.npy` [389]; `embed/gene_vectors.npy` [389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 389 or target_col == 389). Every well: [[BCLAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCLAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
