---
symbol: "GTPBP2"
type: "gene"
col: 10256
ensembl_id: "ENSG00000172432"
name: "GTP binding protein 2"
location: "6p21.1"
module: 63
arm: "+"
pooled_cpm: 46.15
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 29
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# GTPBP2

*GTP binding protein 2* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.26× (z +9.8, q 5e-20, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.526× (z -10.9, q 4e-25, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.623× (z -8.1, q 1e-13, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF2]] (+0.68, fdr 7e-06), [[AAK1]] (+0.64, fdr 7e-06), [[TRIB3]] (+0.64, fdr 7e-06); moves opposite to [[MAP3K1]] (-0.60, fdr 1e-05), [[DOP1A]] (-0.55, fdr 1e-05), [[TAPT1]] (-0.50, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.26×** | +9.8 | 5e-20 | 37/48 (LoVo, RKO, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.03×** | +8.6 | 3e-15 | 42/47 (LoVo, HEC-1-A, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.48×** | +6.6 | 6e-09 | 31/48 (SW480, BT-474, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.62×** | +5.8 | 8e-07 | 33/47 (NCI-H460, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.9 | 1e-04 | 24/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.32×** | +4.8 | 2e-04 | 32/48 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 2e-04 | 29/48 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +4.2 | 0.002 | 28/47 (NCI-H460, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +3.9 | 0.006 | 26/48 (COLO 205, BT-474, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.006 | 28/47 (BT-474, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.35×** | +3.6 | 0.018 | 23/48 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.020 | 21/49 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.021 | 22/47 (SW480, RKO, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.4 | 0.026 | 23/48 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.056 | 23/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.056 | 21/49 (SHP-77, LoVo, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.061 | 20/48 (BT-474, RKO, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.063 | 18/47 (COLO 205, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.526×** | -10.9 | 4e-25 | 44/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.464×** | -8.9 | 2e-16 | 37/48 (NCI-H23, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -8.1 | 1e-13 | 38/48 (NCI-H1792, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.537×** | -7.2 | 8e-11 | 42/47 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.555×** | -7.1 | 1e-10 | 39/47 (H4, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.543×** | -6.8 | 1e-09 | 27/42 (HepG2/C3A, RPMI-7951, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.600×** | -6.2 | 6e-08 | 34/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.612×** | -5.9 | 2e-07 | 33/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.641×** | -5.4 | 5e-06 | 27/47 (NCI-H23, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **0.645×** | -5.3 | 7e-06 | 36/47 (LoVo, BT-474, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.438×** | -5.1 | 1e-05 | 36/46 (SNU-1, H4, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -5.1 | 2e-05 | 30/47 (Hs 766T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.662×** | -5.0 | 3e-05 | 31/48 (NCI-H1573, HT-29, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.655×** | -4.9 | 4e-05 | 31/49 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.667×** | -4.9 | 4e-05 | 30/48 (HT-29, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.787×** | -4.1 | 0.001 | 27/48 (SNU-423, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -3.8 | 0.004 | 25/47 (hTERT-HPNE, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.7 | 0.006 | 26/48 (BT-474, A-427, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.747×** | -3.3 | 0.022 | 17/47 (SNU-423, LoVo, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -3.2 | 0.029 | 21/48 (H4, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.831×** | -3.2 | 0.033 | 20/48 (RKO, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 56.2 | 2 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 5.22× (z +14.9) | [[Digitoxin (drug)]] 5 µM 0.295× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.2) |
| [[BT-474 (line)]] | alt | 75.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.217× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 47.7 | 2 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.54× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HT-29 (line)]] | alt | 95.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 46.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 57.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 91.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.437× (z -8.8) |
| [[RKO (line)]] | wt | 81.2 | 1 | 2 | [[Auranofin (drug)]] 5 µM 4.86× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 57.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW480 (line)]] | alt | 29.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 2.16× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[5-Azacytidine (drug)]] 5 µM 2.76× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A-172 (line)]] | wt | 53.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.86× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.1) |
| [[A498 (line)]] | wt | 33.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.3) |
| [[H4 (line)]] | wt | 84.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.255× (z -8.7) |
| [[Hs 766T (line)]] | wt | 25.9 | 0 | 2 (1 ⚠) | — | [[Futibatinib (drug)]] 5 µM 0.0720× (z -8.8) |
| [[KATO III (line)]] | alt | 82.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H460 (line)]] | wt | 31.4 | 1 | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.48× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[PANC-1 (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[RPMI-7951 (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.3) ⚠ cell-cycle shift, explains ~62% of this change |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0928× (z -8.6) |
| [[COLO 205 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HCT15 (line)]] | alt | 64.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 60.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0718× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HS-578T (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0846× (z -9.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 56.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SHP-77 (line)]] | alt | 35.6 | 0 | 1 | — | [[ULK-101 (drug)]] 5 µM 0.0823× (z -9.2) |
| [[SW 900 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -11.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF2]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[AAK1]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TRIB3]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PABPC1L]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[HSPA9]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[AARS1]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[CEBPG]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[MAP1B]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[XPOT]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MICALL1]] | +0.60 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[NIT1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[STK40]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K1]] | -0.60 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[DOP1A]] | -0.55 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[TAPT1]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.50 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[SSH2]] | -0.50 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[S100A4]] | -0.48 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[LCOR]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP12]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[DEPDC7]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF608]] | -0.47 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[KAT2B]] | -0.46 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[FCHSD2]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GTPBP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF165]] | B | ZNF165 activity raises GTPBP2's level | lines that do not express ZNF165 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without ZNF165 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ENSG00000224621, ESRP2, CNKSR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, 44.7); signed map (-10.6, 24.7). **Vector** length 124, 40.8% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.53 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.53 to 9); *unfolded protein response* (hallmark, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.2 | +9.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +9.8 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.9 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.2 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.8 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -5.9 | -10.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.8 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.2 | -8.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -7.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Ixazomib (drug)]] 5 µM |  | -2.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,605,316-43,629,264 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Translational GTPases |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX10](https://www.uniprot.org/uniprotkb/Q9BX10) (GTP-binding protein 2):

> Involved in the rescue of ribosome stalling due to the presence of non-functional tRNA (By similarity). Has very low GTP-binding activity.

**Summary**, from NCBI Gene [54676](https://www.ncbi.nlm.nih.gov/gene/54676):

> GTP-binding proteins, or G proteins, constitute a superfamily capable of binding GTP or GDP. G proteins are activated by binding GTP and are inactivated by hydrolyzing GTP to GDP. This general mechanism enables G proteins to perform a wide range of biologic activities.[supplied by OMIM, Jan 2003]

**Accessions** — [HGNC:4670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4670) · Entrez [54676](https://www.ncbi.nlm.nih.gov/gene/54676) · UniProt [Q9BX10](https://www.uniprot.org/uniprotkb/Q9BX10) · Ensembl [ENSG00000172432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172432)

## Data

Gene col 10256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10256); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10256]; `tensor/DDL_lfc|DDL_z.npy` [10256]; `embed/gene_vectors.npy` [10256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10256 or target_col == 10256). Every well: [[GTPBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTPBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
