---
symbol: "NCOA5"
type: "gene"
col: 4488
ensembl_id: "ENSG00000124160"
name: "nuclear receptor coactivator 5"
location: "20q13.12"
module: 51
arm: "+"
pooled_cpm: 49.33
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NCOA5

*nuclear receptor coactivator 5* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.26× (z +5.8, q 3e-06, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 2.04×, NCI-H2030 2.08×, Hs 766T 2.05×, KATO III 1.78×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.65×; ⚠ cell-cycle shift, explains ~13% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.379× (z -24.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2]] (+0.66, fdr 7e-06), [[EPC2]] (+0.66, fdr 7e-06), [[ZNF140]] (+0.62, fdr 1e-05); moves opposite to [[GLUD1]] (-0.60, fdr 9e-06), [[GRB2]] (-0.58, fdr 3e-05), [[HERC3]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 2.04×, NCI-H2030 2.08×, Hs 766T 2.05×, KATO III 1.78×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.65×; ⚠ cell-cycle shift, explains ~13% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.8 | 3e-06 | 25/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.28×** | +4.3 | 0.004 | 26/48 (A-427, Hs 766T, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.042 | 18/48 (SW1417, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4488.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.379×** | -24.2 | 0e+00 | 47/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -14.2 | 4e-43 | 42/48 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.451×** | -14.0 | 3e-42 | 45/49 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.446×** | -13.7 | 1e-40 | 43/49 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.473×** | -12.7 | 6e-35 | 37/44 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.504×** | -11.6 | 3e-29 | 40/47 (NCI-H23, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.553×** | -10.5 | 1e-23 | 43/48 (SW1417, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.568×** | -10.0 | 1e-21 | 43/48 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.553×** | -9.7 | 2e-20 | 35/45 (SW 900, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.585×** | -9.5 | 1e-19 | 41/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.586×** | -9.4 | 2e-19 | 42/48 (NCI-H2030, SW1417, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -8.9 | 3e-17 | 34/49 (SNU-1, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.643×** | -7.8 | 3e-13 | 41/48 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.662×** | -7.3 | 1e-11 | 35/48 (SK-MEL-2, J82, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.672×** | -6.6 | 1e-09 | 31/48 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -6.3 | 8e-09 | 31/48 (BT-474, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -5.6 | 6e-07 | 30/48 (NCI-H2030, SW48, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -4.2 | 8e-04 | 23/48 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.638×** | -4.1 | 9e-04 | 22/48 (NCI-H1792, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.804×** | -3.8 | 0.003 | 19/48 (A-427, J82, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.816×** | -3.4 | 0.015 | 20/48 (NCI-H2030, RKO, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.838× | -2.9 | 0.073 | 14/47 (KATO III, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.4 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -23.9) |
| [[SW1417 (line)]] | alt | 79.9 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 46.3 | 0 | 7 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -18.4) |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 76.8 | 0 | 7 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0956× (z -22.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -18.6) |
| [[NCI-H2030 (line)]] | alt | 56.4 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -22.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -16.1) |
| [[SNU-423 (line)]] | alt | 54.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -13.7) |
| [[C-33 A (line)]] | alt | 95.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -14.4) |
| [[PANC-1 (line)]] | alt | 44.2 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -12.2) |
| [[RKO (line)]] | wt | 61.7 | 0 | 5 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -16.5) |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0996× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -11.8) |
| [[SW480 (line)]] | alt | 59.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -18.6) |
| [[A-172 (line)]] | wt | 46.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -17.5) |
| [[KATO III (line)]] | alt | 72.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 44.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -17.6) |
| [[NCI-H1573 (line)]] | alt | 51.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -10.9) |
| [[SNU-1 (line)]] | wt | 74.4 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -11.7) |
| [[SW 900 (line)]] | alt | 45.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0483× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -15.4) |
| [[A-427 (line)]] | wt | 48.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +9.1) ⚠ cell-cycle shift, explains ~13% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -8.7) |
| [[A549 (line)]] | wt | 41.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.7) |
| [[BT-474 (line)]] | alt | 48.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -12.0) |
| [[C32 (line)]] | wt | 36.3 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -13.9) |
| [[HS-578T (line)]] | alt | 38.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.7) |
| [[LS 180 (line)]] | wt | 41.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 53.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 51.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -18.8) |
| [[AN3 CA (line)]] | alt | 58.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0740× (z -13.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 53.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -18.2) |
| [[COLO 205 (line)]] | alt | 69.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 68.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -13.6) |
| [[Hs 766T (line)]] | wt | 59.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.2) |
| [[HT-29 (line)]] | alt | 52.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.9) |
| [[J82 (line)]] | alt | 61.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -12.5) |
| [[LoVo (line)]] | wt | 39.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 47.3 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -14.1) |
| [[SW48 (line)]] | wt | 49.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -14.8) |
| [[A498 (line)]] | wt | 30.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -12.1) |
| [[CHP-212 (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 38.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -22.9) |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0790× (z -9.2) |
| [[SHP-77 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[EPC2]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZNF140]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[C5orf24]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[EPC1]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RPP14]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[AFG3L1P]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SRSF4]] | +0.59 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ZNF480]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[THADA]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SMARCB1]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLUD1]] | -0.60 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[GRB2]] | -0.58 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[HERC3]] | -0.52 | -0.49 / -0.50 | both halves | 2e-05 |  |
| [[NMRK1]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MYH10]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[LAPTM4A]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SMAP2]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.8, 11.6); signed map (12.2, -31.1). **Vector** length 109, 31.8% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +10.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.1 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +8.6 | +1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.8 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -24.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -14.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.5 | -10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -6.0 | -12.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.5 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor coactivator 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:46,060,991-46,089,962 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA465L10.6, CIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCD5](https://www.uniprot.org/uniprotkb/Q9HCD5) (Nuclear receptor coactivator 5):

> Nuclear receptor coregulator that can have both coactivator and corepressor functions. Interacts with nuclear receptors for steroids (ESR1 and ESR2) independently of the steroid binding domain (AF-2) of the ESR receptors, and with the orphan nuclear receptor NR1D2. Involved in the coactivation of nuclear steroid receptors (ER) as well as the corepression of MYC in response to 17-beta-estradiol (E2).

**Summary**, from NCBI Gene [57727](https://www.ncbi.nlm.nih.gov/gene/57727):

> This gene encodes a coregulator for the alpha and beta estrogen receptors and the orphan nuclear receptor NR1D2. The protein localizes to the nucleus, and is thought to have both coactivator and corepressor functions. Its interaction with nuclear receptors is independent of the AF2 domain on the receptors, which is known to regulate interaction with other coreceptors. Several alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:15909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15909) · Entrez [57727](https://www.ncbi.nlm.nih.gov/gene/57727) · UniProt [Q9HCD5](https://www.uniprot.org/uniprotkb/Q9HCD5) · Ensembl [ENSG00000124160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124160)

## Data

Gene col 4488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4488); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4488]; `tensor/DDL_lfc|DDL_z.npy` [4488]; `embed/gene_vectors.npy` [4488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4488 or target_col == 4488). Every well: [[NCOA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
