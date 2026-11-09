---
symbol: "PRKDC"
type: "gene"
col: 14836
ensembl_id: "ENSG00000253729"
name: "protein kinase, DNA-activated, catalytic subunit"
location: "8q11.21"
module: 4
arm: "+"
pooled_cpm: 320.0
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# PRKDC

*protein kinase, DNA-activated, catalytic subunit* — 8q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +18.4, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.29× (z +4.2, q 0.002, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.771× (z -6.3, q 1e-07, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AN3 CA 0.354×, SK-MEL-2 0.436×, A-427 0.518×, J82 0.592×, …); [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.562×, A498 0.573×, LS 180 0.468×; ⚠ cell-cycle shift, explains ~60% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.343×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTHFD1]] (+0.86, fdr 7e-06), [[NUP155]] (+0.83, fdr 7e-06), [[IPO5]] (+0.82, fdr 7e-06); moves opposite to [[TERF2IP]] (-0.79, fdr 7e-06), [[ZMYM5]] (-0.78, fdr 7e-06), [[SAT2]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.92×** | +18.4 | 0e+00 | 49/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.90×** | +17.6 | 0e+00 | 43/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.36×** | +13.6 | 1e-39 | 44/45 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.91×** | +11.1 | 2e-26 | 44/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.78×** | +9.9 | 5e-21 | 44/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.72×** | +9.3 | 1e-18 | 41/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +7.6 | 3e-12 | 43/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.45×** | +6.1 | 6e-08 | 34/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.29×** | +4.2 | 0.002 | 28/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 29/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.27×** | +4.1 | 0.002 | 32/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +4.0 | 0.003 | 25/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.006 | 25/48 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.006 | 21/48 (NCI-H1792, A-172, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.006 | 27/48 (RKO, HEC-1-A, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.006 | 32/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.006 | 32/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.006 | 26/49 (NCI-H1792, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.013 | 26/48 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.015 | 31/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.031 | 29/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.031 | 26/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 1.20× | +3.1 | 0.043 | 18/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.047 | 8/48 (RKO, SW 900, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.073 | 22/48 (HOP62, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14836.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (AN3 CA 0.354×, SK-MEL-2 0.436×, A-427 0.518×, J82 0.592×, …); [[Selinexor (drug)]] 5 µM in 3 lines (A-427 0.562×, A498 0.573×, LS 180 0.468×; ⚠ cell-cycle shift, explains ~60% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.343×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.771×** | -6.3 | 1e-07 | 32/48 (AN3 CA, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.824×** | -4.7 | 7e-04 | 23/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.755× | -3.4 | 0.13 | 27/48 (AN3 CA, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | 0.827× | -3.3 | 0.16 | 24/48 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.835× | -3.1 | 0.17 | 21/49 (SW1417, C32, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.827× | -3.1 | 0.17 | 22/49 (Hs 766T, H4, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.837× | -3.1 | 0.17 | 20/49 (A498, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 146 | 11 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.71× (z +21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 2.61× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 379 | 8 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 193 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[C32 (line)]] | wt | 304 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HS-578T (line)]] | alt | 296 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 462 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SNU-423 (line)]] | alt | 221 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A549 (line)]] | wt | 270 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[CFPAC-1 (line)]] | alt | 92.0 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[H4 (line)]] | wt | 189 | 5 (5 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.01× (z +11.1) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.476× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HOP62 (line)]] | alt | 321 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 208 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +12.0) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[NCI-H1573 (line)]] | alt | 101 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[RPMI-7951 (line)]] | alt | 267 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AsPC-1 (line)]] | alt | 127 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 211 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 215 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.604× (z -9.1) |
| [[SW 900 (line)]] | alt | 167 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW480 (line)]] | alt | 361 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[A-427 (line)]] | wt | 442 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.05× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -12.9) |
| [[A498 (line)]] | wt | 440 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.13× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Selinexor (drug)]] 5 µM 0.573× (z -11.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2347 (line)]] | alt | 212 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Panc 03.27 (line)]] | alt | 227 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW1417 (line)]] | alt | 191 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 183 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 237 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 226 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 521 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 306 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -14.2) |
| [[SNU-1 (line)]] | wt | 313 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.6) |
| [[AN3 CA (line)]] | alt | 447 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -15.5) |
| [[COLO 205 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LS 180 (line)]] | wt | 257 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.468× (z -9.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2030 (line)]] | alt | 443 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 773 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.602× (z -9.8) |
| [[SW48 (line)]] | wt | 498 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.467× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 278 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HCT15 (line)]] | alt | 361 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 565 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -12.2) |
| [[KATO III (line)]] | alt | 251 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SHP-77 (line)]] | alt | 773 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.69× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 1271 (line)]] | alt | 313 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 648 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 316 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 670 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 531 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD1]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[NUP155]] | +0.83 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[IPO5]] | +0.82 | +0.83 / +0.84 | both halves | 7e-06 |  |
| [[XRCC5]] | +0.79 | +0.78 / +0.84 | both halves | 7e-06 | pathway: Cytosolic sensors of pathogen-associated DNA; STRING 999 |
| [[TFDP1]] | +0.77 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.76 | +0.78 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PAICS]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[POLA1]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[ATIC]] | +0.75 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[RBBP7]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[IPO7]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[LRPPRC]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.79 | -0.73 / -0.75 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.78 | -0.74 / -0.73 | both halves | 7e-06 |  |
| [[SAT2]] | -0.74 | -0.78 / -0.74 | both halves | 7e-06 |  |
| [[TMEM106A]] | -0.72 | -0.69 / -0.70 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.71 | -0.68 / -0.78 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.70 | -0.62 / -0.72 | both halves | 7e-06 |  |
| [[ZFYVE1]] | -0.69 | -0.69 / -0.69 | both halves | 7e-06 |  |
| [[APBA3]] | -0.68 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[HOTAIRM1]] | -0.68 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.68 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.67 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[EIF3J-DT]] | -0.67 | -0.55 / -0.72 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity lowers PRKDC's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.58× higher at baseline in the lines without MPZL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[FBXO32]] | B | FBXO32 activity lowers PRKDC's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.63× higher at baseline in the lines without FBXO32 | 0.033 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[VAMP5]] | B | VAMP5 activity lowers PRKDC's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.63× higher at baseline in the lines without VAMP5 | 0.033 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.3, -32.0); signed map (-19.4, -45.2). **Vector** length 162, 66.7% of its response variance represented; |z| ≥ 3 in 1,521 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.57 to 21); *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8); *Folding of actin by CCT/TriC* (reactome, mean cos +0.63 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.4 | +4.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +5.3 | +3.8 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.9 | +4.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.3 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.0 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.9 | -6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -8.6 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.4 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -7.7 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -6.6 | -3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -5.7 | -2.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -5.1 | -2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.8 | -2.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -4.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase, DNA-activated, catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.21 — chr8:47,773,111-47,960,178 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DNPK1, p350, DNAPK, XRCC7, DNA-PKcs, DNAPKc, DNA-PKC, p460; previously HYRC, HYRC1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Phosphatidylinositol 3-kinase-related kinase family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 9 pathways, smallest: IRF3-mediated induction of type I IFN; STING mediated induction of host immune responses; Nonhomologous End-Joining (NHEJ) |
| Matched by | ensembl_id |

**Function**, from UniProt [P78527](https://www.uniprot.org/uniprotkb/P78527) (DNA-dependent protein kinase catalytic subunit):

> Serine/threonine-protein kinase that acts as a molecular sensor for DNA damage. Involved in DNA non-homologous end joining (NHEJ) required for double-strand break (DSB) repair and V(D)J recombination. Must be bound to DNA to express its catalytic properties. Promotes processing of hairpin DNA structures in V(D)J recombination by activation of the hairpin endonuclease artemis (DCLRE1C). Recruited by XRCC5 and XRCC6 to DNA ends and is required to (1) protect and align broken ends of DNA, thereby …

**Summary**, from NCBI Gene [5591](https://www.ncbi.nlm.nih.gov/gene/5591):

> This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:9413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9413) · Entrez [5591](https://www.ncbi.nlm.nih.gov/gene/5591) · UniProt [P78527](https://www.uniprot.org/uniprotkb/P78527) · Ensembl [ENSG00000253729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253729)

## Data

Gene col 14836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14836); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14836]; `tensor/DDL_lfc|DDL_z.npy` [14836]; `embed/gene_vectors.npy` [14836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14836 or target_col == 14836). Every well: [[PRKDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
