---
symbol: "PFKFB3"
type: "gene"
col: 9969
ensembl_id: "ENSG00000170525"
name: "6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 3"
location: "10p15.1"
module: 99
arm: "+"
pooled_cpm: 170.32
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# PFKFB3

*6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 3* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.25× (z +8.0, q 8e-13, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.364× (z -19.1, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.706× (z -6.3, q 2e-08, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG1]] (+0.69, fdr 7e-06), [[PGK1]] (+0.67, fdr 1e-05), [[GBE1]] (+0.63, fdr 1e-05); moves opposite to [[ADI1]] (-0.59, fdr 2e-05), [[VBP1]] (-0.51, fdr 5e-05), [[OXCT1]] (-0.50, fdr 4e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC16A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +8.0 | 8e-13 | 34/49 (NCI-H2030, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 1e-04 | 30/48 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 4e-04 | 28/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.4 | 0.001 | 22/48 (A-172, HS-578T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.003 | 28/48 (SW480, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.009 | 24/48 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.017 | 26/48 (NCI-H2030, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.053 | 21/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.053 | 24/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.055 | 21/48 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.056 | 21/48 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.056 | 20/48 (AsPC-1, COLO 205, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.094 | 20/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.364×** | -19.1 | 0e+00 | 44/49 (COLO 205, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.395×** | -16.9 | 0e+00 | 40/44 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.447×** | -14.6 | 0e+00 | 43/47 (C-33 A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.474×** | -13.1 | 8e-37 | 38/45 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.587×** | -9.7 | 4e-20 | 33/47 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -6.3 | 2e-08 | 28/48 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.825×** | -5.2 | 2e-05 | 24/48 (SNU-423, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.757×** | -5.1 | 3e-05 | 27/48 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.769×** | -5.0 | 4e-05 | 28/48 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.839× | -4.7 | 1e-04 | 20/48 (SW1417, SNU-423, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.792×** | -4.4 | 5e-04 | 26/48 (HepG2/C3A, SNU-423, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.848× | -4.4 | 5e-04 | 21/49 (SNU-423, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.4 | 5e-04 | 24/50 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.799×** | -4.3 | 9e-04 | 26/48 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.863× | -4.0 | 0.003 | 20/48 (A549, SW480, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | 0.834× | -3.5 | 0.019 | 16/48 (NCI-H1792, H4, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.059 | 15/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | **0.734×** | -3.1 | 0.065 | 17/46 (C-33 A, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.857× | -2.9 | 0.091 | 14/49 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.808×** | -2.9 | 0.098 | 20/47 (A-427, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 193 | 1 | 8 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.04× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.415× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 286 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.7) |
| [[SNU-423 (line)]] | alt | 259 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -16.0) |
| [[C-33 A (line)]] | alt | 272 | 0 | 8 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -20.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.240× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 212 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.332× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 114 | 5 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.30× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -9.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 197 | 4 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.1× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0984× (z -24.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 323 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -14.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 501 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -14.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 156 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.64× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 131 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.41× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 190 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 242 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.50× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -13.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 263 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.1) |
| [[SW1417 (line)]] | alt | 154 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 162 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.91× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 119 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +32.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.51× (z +18.2) | — |
| [[HCT15 (line)]] | alt | 329 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -14.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 175 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -14.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 135 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.355× (z -12.1) ⚠ toxic |
| [[J82 (line)]] | alt | 202 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 157 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.263× (z -14.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 199 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 151 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 120 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.352× (z -10.8) |
| [[SW480 (line)]] | alt | 128 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.409× (z -11.8) |
| [[C32 (line)]] | wt | 164 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.391× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 132 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -10.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.240× (z -8.9) |
| [[HOP62 (line)]] | alt | 189 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.76× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.47× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 327 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 71.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.220× (z -17.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 72.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 78.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -19.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 117 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -8.8) |
| [[H4 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 136 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.58× (z +10.2) | — |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0662× (z -11.3) |
| [[RKO (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -23.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 87.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0873× (z -9.5) |
| [[AN3 CA (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG1]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[PGK1]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 739 |
| [[GBE1]] | +0.63 | +0.68 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[BNIP3]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ENO2]] | +0.62 | +0.60 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 712 |
| [[SLC2A1]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 767 |
| [[ALDOA]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 610 |
| [[CMIP]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[SLC2A3]] | +0.58 | +0.56 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 736 |
| [[NGLY1]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[FAM162A]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[ENO1]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 682 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADI1]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[VBP1]] | -0.51 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[OXCT1]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[NDUFS1]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[NNT]] | -0.50 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.49 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[MCCC2]] | -0.46 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[ZMPSTE24]] | -0.45 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[CYBRD1]] | -0.45 | -0.35 / -0.24 | both halves | 5e-04 |  |
| [[FAIM]] | -0.45 | -0.38 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A3]] | B | SLC16A3 activity raises PFKFB3's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 1.73× lower at baseline in the lines without SLC16A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[ADM]] | B | ADM activity raises PFKFB3's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without ADM | 0.089 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[IL1RAP]] | B | IL1RAP activity raises PFKFB3's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without IL1RAP | 0.093 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[LINC02649]] | C | LINC02649 activity raises PFKFB3's level | lines that do not express LINC02649 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without LINC02649 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MAP3K8, LINC02656, B4GALT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -15.7); signed map (-37.2, 28.6). **Vector** length 125, 38.5% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.52 to 15); *hypoxia* (control, mean cos +0.54 to 7); *glycolysis* (hallmark, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.6 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.5 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.9 | -14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -19.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -16.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.5 | -9.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.2 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.8 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:6,144,934-6,254,644 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase family; MicroRNA protein coding host genes |
| Hallmark sets | HYPOXIA, ADIPOGENESIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Regulation of glycolysis by fructose 2,6-bisphosphate metabolism; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16875](https://www.uniprot.org/uniprotkb/Q16875) (6-phosphofructo-2-kinase/fructose-2,6-bisphosphatase 3):

> Catalyzes both the synthesis and degradation of fructose 2,6-bisphosphate.

**Summary**, from NCBI Gene [5209](https://www.ncbi.nlm.nih.gov/gene/5209):

> The protein encoded by this gene belongs to a family of bifunctional proteins that are involved in both the synthesis and degradation of fructose-2,6-bisphosphate, a regulatory molecule that controls glycolysis in eukaryotes. The encoded protein has a 6-phosphofructo-2-kinase activity that catalyzes the synthesis of fructose-2,6-bisphosphate (F2,6BP), and a fructose-2,6-biphosphatase activity that catalyzes the degradation of F2,6BP. This protein is required for cell cycle progression and …

**Accessions** — [HGNC:8874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8874) · Entrez [5209](https://www.ncbi.nlm.nih.gov/gene/5209) · UniProt [Q16875](https://www.uniprot.org/uniprotkb/Q16875) · Ensembl [ENSG00000170525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170525)

## Data

Gene col 9969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9969); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9969]; `tensor/DDL_lfc|DDL_z.npy` [9969]; `embed/gene_vectors.npy` [9969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9969 or target_col == 9969). Every well: [[PFKFB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFKFB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
