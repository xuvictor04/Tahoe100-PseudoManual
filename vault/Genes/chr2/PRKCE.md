---
symbol: "PRKCE"
type: "gene"
col: 10058
ensembl_id: "ENSG00000171132"
name: "protein kinase C epsilon"
location: "2p21"
module: 17
arm: "-"
pooled_cpm: 214.42
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PRKCE

*protein kinase C epsilon* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 1.34× (z +5.6, q 9e-06, up in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +5.5, q 9e-06, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.336× (z -20.1, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.734× (z -5.9, q 3e-07, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL29]] (+0.65, fdr 7e-06), [[SIPA1L1]] (+0.57, fdr 3e-05), [[TEAD4]] (+0.55, fdr 3e-05); moves opposite to [[MMUT]] (-0.55, fdr 3e-05), [[NPHP1]] (-0.52, fdr 5e-05), [[FRG1DP]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.6 | 9e-06 | 33/47 (SW480, AsPC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.5 | 9e-06 | 25/47 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.9 | 1e-04 | 25/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.8 | 2e-04 | 23/47 (LS 180, AsPC-1, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.53×** | +4.2 | 0.003 | 24/45 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.16× | +4.1 | 0.004 | 23/48 (SW480, Hs 766T, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.020 | 23/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.6 | 0.021 | 23/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.024 | 21/47 (SW 900, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.4 | 0.039 | 21/47 (H4, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.040 | 22/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.040 | 24/47 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10058.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.336×** | -20.1 | 0e+00 | 46/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.340×** | -19.8 | 0e+00 | 41/43 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.425×** | -15.1 | 0e+00 | 37/44 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -6.7 | 4e-09 | 37/46 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -6.5 | 1e-08 | 33/46 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.715×** | -6.4 | 1e-08 | 36/47 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.734×** | -5.9 | 3e-07 | 32/47 (C-33 A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.567×** | -5.7 | 1e-06 | 33/48 (LoVo, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.569×** | -5.6 | 1e-06 | 33/46 (H4, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.747×** | -5.6 | 1e-06 | 30/47 (C-33 A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.616×** | -4.8 | 7e-05 | 24/38 (HEC-1-A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.772×** | -4.8 | 9e-05 | 26/47 (A549, LOX-IMVI, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.667×** | -4.0 | 0.002 | 27/47 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.863× | -4.0 | 0.003 | 20/48 (A498, COLO 205, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.681×** | -3.8 | 0.005 | 29/47 (H4, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.874× | -3.7 | 0.008 | 21/48 (COLO 205, A498, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.887× | -3.3 | 0.031 | 6/48 (C-33 A, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 321 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 671 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.397× (z -10.5) |
| [[A549 (line)]] | wt | 376 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -10.5) |
| [[KATO III (line)]] | alt | 175 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 216 | 1 (1 ⚠) | 6 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.92× (z +10.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -20.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 239 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.326× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 266 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 351 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 350 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.461× (z -9.4) |
| [[A-427 (line)]] | wt | 274 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -16.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 195 | 1 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.9) ⚠ cell-cycle shift, explains ~17% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.264× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 183 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.399× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 486 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0326× (z -38.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 240 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -19.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 196 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 313 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -18.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 195 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -12.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 187 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -13.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 280 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 98.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.85× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 181 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -14.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 202 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 90.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +15.6) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.53× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -14.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 134 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -11.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 106 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.39× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 224 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 190 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -11.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -14.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 224 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.8) ⚠ cell-cycle shift, explains ~17% of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -20.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 245 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -18.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 309 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 241 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -19.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 262 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -16.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 244 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 279 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -14.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -9.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 68.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +14.3) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[J82 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 218 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 313 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -14.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL29]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SIPA1L1]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[TEAD4]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[FAM89A]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MEGF11]] | +0.55 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LARGE1]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LONRF3]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[UBASH3B]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[KANK1]] | +0.50 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[IGF2BP3]] | +0.50 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[PBX3]] | +0.50 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MED12L]] | +0.49 | +0.39 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMUT]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[NPHP1]] | -0.52 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[FRG1DP]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DNAL1]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[MRPS31P5-1]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[SCRN3]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[MAPK3]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis |
| [[USP30]] | -0.51 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[ALDH6A1]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZNF17]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TMEM254]] | -0.50 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[EXOC3]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRKCE's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CCDC71L]] | B | CCDC71L activity raises PRKCE's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CCDC71L | 0.075 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[KLHL29]] | B | KLHL29 activity raises PRKCE's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without KLHL29 | 0.085 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (21.7, -8.2); signed map (13.0, 21.3). **Vector** length 119, 39.1% of its response variance represented; |z| ≥ 3 in 1,495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.0 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.7 | +0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | -1.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.3 | -3.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.8 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -2.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -15.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -4.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.6 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C epsilon |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:45,651,345-46,187,990 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCε |
| Gene groups (HGNC) | C2 domain containing protein kinases; Protein kinase C family |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 15 pathways, smallest: Role of phospholipids in phagocytosis; SHC1 events in ERBB2 signaling; Effects of PIP2 hydrolysis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02156](https://www.uniprot.org/uniprotkb/Q02156) (Protein kinase C epsilon type):

> Calcium-independent, phospholipid- and diacylglycerol (DAG)-dependent serine/threonine-protein kinase that plays essential roles in the regulation of multiple cellular processes linked to cytoskeletal proteins, such as cell adhesion, motility, migration and cell cycle, functions in neuron growth and ion channel regulation, and is involved in immune response, cancer cell invasion and regulation of apoptosis. Mediates cell adhesion to the extracellular matrix via integrin-dependent signaling, by …

**Summary**, from NCBI Gene [5581](https://www.ncbi.nlm.nih.gov/gene/5581):

> Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each member of the PKC family has a specific expression profile and is believed to play a distinct role in …

**Accessions** — [HGNC:9401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9401) · Entrez [5581](https://www.ncbi.nlm.nih.gov/gene/5581) · UniProt [Q02156](https://www.uniprot.org/uniprotkb/Q02156) · Ensembl [ENSG00000171132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171132)

## Data

Gene col 10058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10058); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10058]; `tensor/DDL_lfc|DDL_z.npy` [10058]; `embed/gene_vectors.npy` [10058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10058 or target_col == 10058). Every well: [[PRKCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
