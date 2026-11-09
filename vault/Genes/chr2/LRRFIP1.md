---
symbol: "LRRFIP1"
type: "gene"
col: 4578
ensembl_id: "ENSG00000124831"
name: "LRR binding FLII interacting protein 1"
location: "2q37.3"
module: 136
arm: "+"
pooled_cpm: 560.6
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# LRRFIP1

*LRR binding FLII interacting protein 1* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.33× (z +7.6, q 2e-11, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.381× (z -37.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB]] (+0.74, fdr 7e-06), [[RTN4]] (+0.71, fdr 7e-06), [[FLNB-AS1]] (+0.66, fdr 7e-06); moves opposite to [[ZNF362]] (-0.61, fdr 2e-04), [[C5orf15]] (-0.60, fdr 8e-05), [[NFYC]] (-0.60, fdr 4e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[STAC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +7.6 | 2e-11 | 34/47 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +7.3 | 9e-11 | 31/47 (NCI-H460, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +6.9 | 9e-10 | 22/49 (HepG2/C3A, CHP-212, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +5.8 | 1e-06 | 27/47 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +5.7 | 1e-06 | 26/48 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +5.3 | 1e-05 | 25/48 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +5.3 | 1e-05 | 26/48 (HT-29, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.9 | 7e-05 | 26/45 (SW1417, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.8 | 8e-05 | 23/48 (SW1417, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +4.7 | 1e-04 | 29/48 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.12× | +4.6 | 2e-04 | 9/48 (RKO, LS 180, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +4.5 | 3e-04 | 22/47 (COLO 205, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.15× | +3.8 | 0.007 | 19/47 (COLO 205, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.10× | +3.7 | 0.008 | 0/48 | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.018 | 19/49 (NCI-H1573, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.018 | 22/48 (LS 180, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.4 | 0.019 | 13/48 (KATO III, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.027 | 11/48 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.037 | 9/48 (RKO, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.381×** | -37.6 | 0e+00 | 48/48 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -23.7 | 0e+00 | 44/49 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -20.4 | 0e+00 | 47/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -20.2 | 0e+00 | 43/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.572×** | -14.8 | 0e+00 | 45/48 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.578×** | -14.5 | 0e+00 | 42/47 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -13.4 | 3e-39 | 48/49 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.715×** | -13.1 | 3e-37 | 39/48 (RKO, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -9.5 | 2e-19 | 34/50 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.724×** | -8.9 | 4e-17 | 38/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.734×** | -8.5 | 8e-16 | 37/48 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.739×** | -8.3 | 4e-15 | 33/48 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -8.3 | 5e-15 | 28/48 (A-172, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.759×** | -7.6 | 1e-12 | 30/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.783×** | -6.7 | 6e-10 | 30/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.781×** | -6.3 | 1e-08 | 31/48 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.637×** | -5.7 | 3e-07 | 34/48 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.816×** | -5.6 | 6e-07 | 27/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.827×** | -5.2 | 5e-06 | 23/48 (KATO III, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 680 | 2 | 24 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.90× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -32.5) |
| [[HOP62 (line)]] | alt | 848 | 7 (1 ⚠) | 13 (5 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.87× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -32.1) |
| [[A-172 (line)]] | wt | 871 | 2 | 17 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.77× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -27.2) |
| [[H4 (line)]] | wt | 905 | 2 | 15 (8 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.98× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -26.7) |
| [[RPMI-7951 (line)]] | alt | 925 | 4 (1 ⚠) | 13 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.37× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -33.4) |
| [[NCI-H460 (line)]] | wt | 619 | 5 (1 ⚠) | 11 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.32× (z +17.7) | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -26.7) |
| [[KATO III (line)]] | alt | 609 | 1 | 14 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.65× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -35.4) |
| [[HEC-1-A (line)]] | alt | 621 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -27.1) |
| [[HS-578T (line)]] | alt | 623 | 1 | 13 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.83× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -30.0) |
| [[LS 180 (line)]] | wt | 663 | 4 | 10 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -23.5) |
| [[AsPC-1 (line)]] | alt | 907 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 660 | 3 (1 ⚠) | 9 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.65× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -31.1) |
| [[PANC-1 (line)]] | alt | 690 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -27.5) |
| [[MIA PaCa-2 (line)]] | alt | 663 | 1 | 10 (3 ⚠) | [[Auranofin (drug)]] 5 µM 1.73× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -34.4) |
| [[SK-MEL-2 (line)]] | alt | 471 | 1 | 10 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.52× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -21.1) |
| [[A549 (line)]] | wt | 626 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -27.0) |
| [[CFPAC-1 (line)]] | alt | 746 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -29.1) |
| [[Hs 766T (line)]] | wt | 791 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -24.0) |
| [[NCI-H1792 (line)]] | alt | 1,084 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -27.4) |
| [[SNU-423 (line)]] | alt | 881 | 1 | 9 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.63× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -30.5) |
| [[A498 (line)]] | wt | 332 | 4 (2 ⚠) | 4 | [[Ixazomib citrate (drug)]] 5 µM 1.92× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -11.6) |
| [[BT-474 (line)]] | alt | 616 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -18.2) |
| [[LOX-IMVI (line)]] | wt | 502 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -30.4) |
| [[RKO (line)]] | wt | 331 | 1 | 7 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.72× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -17.4) |
| [[HT-29 (line)]] | alt | 489 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 536 | 2 | 5 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.51× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -31.7) |
| [[SW1417 (line)]] | alt | 301 | 6 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.588× (z -13.2) |
| [[SW48 (line)]] | wt | 442 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -18.4) |
| [[SW480 (line)]] | alt | 366 | 4 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -17.6) |
| [[C32 (line)]] | wt | 270 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.5) |
| [[COLO 205 (line)]] | alt | 408 | 4 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.07× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -18.2) |
| [[HepG2_C3A (line)]] | wt | 423 | 3 (1 ⚠) | 3 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.75× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 575 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -23.6) |
| [[CHP-212 (line)]] | wt | 527 | 1 | 4 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.74× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -13.6) |
| [[A-427 (line)]] | wt | 258 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.88× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -20.6) |
| [[J82 (line)]] | alt | 336 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -21.7) |
| [[SW 1088 (line)]] | alt | 875 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.4) |
| [[HCT15 (line)]] | alt | 476 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -22.2) |
| [[NCI-H2030 (line)]] | alt | 315 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -25.7) |
| [[NCI-H23 (line)]] | alt | 538 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -44.0) |
| [[SW 1271 (line)]] | alt | 769 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.8) |
| [[SW 900 (line)]] | alt | 440 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -16.3) |
| [[AN3 CA (line)]] | alt | 389 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.9) |
| [[SNU-1 (line)]] | wt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.0) |
| [[C-33 A (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 590 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 540 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 257 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | +0.74 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[RTN4]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[FLNB-AS1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[GIPR]] | +0.65 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[MYO9B]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[CAST]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CLTCL1]] | +0.62 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[SLC35E4]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MPP3]] | +0.61 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[RTN2]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TMEM184B]] | +0.60 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[PAQR5]] | +0.60 | +0.61 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF362]] | -0.61 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[C5orf15]] | -0.60 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[NFYC]] | -0.60 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[JADE2]] | -0.60 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[RBM33]] | -0.60 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[RAF1]] | -0.60 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CASD1]] | -0.59 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[HOTAIR]] | -0.58 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[RPRD2]] | -0.57 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[POMK]] | -0.57 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SAFB]] | -0.57 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[FAM111A-DT]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAC]] | B | STAC activity raises LRRFIP1's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.49× lower at baseline in the lines without STAC | 0.011 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[SERPINB1]] | B | SERPINB1 activity raises LRRFIP1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without SERPINB1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[S100A16]] | B | S100A16 activity raises LRRFIP1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without S100A16 | 0.025 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[TOP2A]] | B | TOP2A activity raises LRRFIP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYO1E]] | B | MYO1E activity raises LRRFIP1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without MYO1E | 0.038 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[LINC00887]] | B | LINC00887 activity raises LRRFIP1's level | lines that do not express LINC00887 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without LINC00887 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02036, STAMBPL1, CFAP45; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers LRRFIP1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LANCL3]] | B | LANCL3 activity raises LRRFIP1's level | lines that do not express LANCL3 (21) vs lines expressing it (29) | 1.40× lower at baseline in the lines without LANCL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: PLAT, HTR1F, ENSG00000289153 |
| [[P4HTM]] | C | P4HTM activity raises LRRFIP1's level | lines that do not express P4HTM (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without P4HTM | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, RNASEL; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.2, 5.1); signed map (-5.4, 44.4). **Vector** length 142, 57.3% of its response variance represented; |z| ≥ 3 in 2,204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.7 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.3 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.3 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +9.3 | -8.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +9.2 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.6 | +6.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +7.2 | +7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.0 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.8 | -13.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.6 | -13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -20.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.7 | -6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.6 | -6.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.9 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -5.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | LRR binding FLII interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,627,587-237,813,682 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLAP-1, FLIIAP1, TRIP, GCF-2, HUFI-1, GCF2 |
| Reactome | 8 pathways, smallest: LRR FLII-interacting protein 1 (LRRFIP1) activates type I IFN production; Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32MZ4](https://www.uniprot.org/uniprotkb/Q32MZ4) (Leucine-rich repeat flightless-interacting protein 1):

> Transcriptional repressor which preferentially binds to the GC-rich consensus sequence (5'-AGCCCCCGGCG-3') and may regulate expression of TNF, EGFR and PDGFA. May control smooth muscle cells proliferation following artery injury through PDGFA repression. May also bind double-stranded RNA. Positively regulates Toll-like receptor (TLR) signaling in response to agonist probably by competing with the negative FLII regulator for MYD88-binding.

**Summary**, from NCBI Gene [9208](https://www.ncbi.nlm.nih.gov/gene/9208):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and protein homodimerization activity. Involved in negative regulation of transcription by RNA polymerase II. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6702) · Entrez [9208](https://www.ncbi.nlm.nih.gov/gene/9208) · UniProt [Q32MZ4](https://www.uniprot.org/uniprotkb/Q32MZ4) · Ensembl [ENSG00000124831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124831)

## Data

Gene col 4578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4578); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4578]; `tensor/DDL_lfc|DDL_z.npy` [4578]; `embed/gene_vectors.npy` [4578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4578 or target_col == 4578). Every well: [[LRRFIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRFIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
