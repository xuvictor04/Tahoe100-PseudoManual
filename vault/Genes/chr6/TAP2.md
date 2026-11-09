---
symbol: "TAP2"
type: "gene"
col: 12841
ensembl_id: "ENSG00000204267"
name: "transporter 2, ATP binding cassette subfamily B member"
location: "6p21.32"
module: 32
arm: "+"
pooled_cpm: 39.5
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 14
n_dd_up_clean: 25
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TAP2

*transporter 2, ATP binding cassette subfamily B member* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +13.6, q 4e-39, up in 35 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +12.5, q 2e-33, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.525× (z -15.8, q 0e+00, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP12]] (+0.82, fdr 7e-06), [[TRIM14]] (+0.81, fdr 7e-06), [[PARP9]] (+0.79, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[JAK2]] → it (grade B ⚠); 7 go from it, the strongest it → [[IFIT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.20×** | +13.6 | 4e-39 | 35/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +12.5 | 2e-33 | 37/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.05×** | +11.9 | 2e-30 | 24/36 (LOX-IMVI, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +9.9 | 1e-20 | 35/46 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +9.6 | 6e-20 | 32/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +8.5 | 1e-15 | 30/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.64×** | +8.5 | 1e-15 | 39/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +8.1 | 4e-14 | 31/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.66×** | +8.0 | 6e-14 | 25/41 (J82, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 6e-09 | 28/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +6.3 | 1e-08 | 30/46 (PANC-1, SW 900, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +6.3 | 2e-08 | 30/47 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +6.1 | 5e-08 | 27/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.90×** | +5.8 | 3e-07 | 35/46 (CFPAC-1, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +5.6 | 7e-07 | 27/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +5.6 | 1e-06 | 25/47 (NCI-H23, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +4.9 | 3e-05 | 21/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 4e-05 | 24/47 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 2e-04 | 22/47 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 4e-04 | 21/48 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 7e-04 | 21/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 19/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.001 | 16/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.001 | 17/47 (CFPAC-1, A498, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12841.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.525×** | -15.8 | 0e+00 | 33/47 (RKO, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.650×** | -10.6 | 1e-23 | 33/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.596×** | -8.9 | 7e-17 | 30/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.696×** | -8.9 | 9e-17 | 28/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.627×** | -8.1 | 8e-14 | 30/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.633×** | -7.9 | 3e-13 | 25/48 (LoVo, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.760×** | -6.7 | 1e-09 | 26/48 (COLO 205, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -6.1 | 7e-08 | 6/48 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -5.9 | 3e-07 | 27/48 (NCI-H23, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.584×** | -4.9 | 7e-05 | 25/46 (NCI-H2347, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.758×** | -4.8 | 8e-05 | 24/48 (C-33 A, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.768×** | -4.6 | 2e-04 | 22/48 (BT-474, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.768×** | -4.6 | 2e-04 | 23/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.761×** | -4.6 | 2e-04 | 22/47 (AN3 CA, A-172, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.05 µM |  | **0.798×** | -3.9 | 0.003 | 22/48 (CHP-212, LoVo, …) | all doses, stronger at high dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.856× | -3.8 | 0.005 | 13/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.884× | -3.0 | 0.085 | 7/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 70.3 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -21.5) |
| [[PANC-1 (line)]] | alt | 46.2 | 5 (3 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 3.03× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.7) |
| [[RKO (line)]] | wt | 68.4 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -28.5) |
| [[SW480 (line)]] | alt | 20.5 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 61.7 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.291× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.230× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 63.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 65.1 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.421× (z -12.4) |
| [[A498 (line)]] | wt | 54.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -17.0) |
| [[A549 (line)]] | wt | 35.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.0) |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.147× (z -12.3) |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -11.9) |
| [[COLO 205 (line)]] | alt | 39.6 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.250× (z -11.8) |
| [[HOP62 (line)]] | alt | 11.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.79× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 42.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.27× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -22.5) |
| [[NCI-H1792 (line)]] | alt | 26.9 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.0) |
| [[A-172 (line)]] | wt | 67.9 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.352× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 37.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +11.8) | [[Tofacitinib (drug)]] 5 µM 0.383× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 34.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 28.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 43.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.6) |
| [[H4 (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.6) |
| [[Hs 766T (line)]] | wt | 55.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 64.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.5) |
| [[HT-29 (line)]] | alt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.5) | — |
| [[KATO III (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 52.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 56.7 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.444× (z -8.5) |
| [[SW48 (line)]] | wt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.0) |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP12]] | +0.82 | +0.76 / +0.87 | both halves | 7e-06 |  |
| [[TRIM14]] | +0.81 | +0.77 / +0.87 | both halves | 7e-06 |  |
| [[PARP9]] | +0.79 | +0.70 / +0.84 | both halves | 7e-06 |  |
| [[SLC15A3]] | +0.78 | +0.61 / +0.83 | both halves | 7e-06 |  |
| [[IFI35]] | +0.78 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[OAS3]] | +0.77 | +0.66 / +0.84 | both halves | 7e-06 |  |
| [[GBP1]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 | STRING 465 |
| [[ADAR]] | +0.77 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[RNF213]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[APOL6]] | +0.76 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[TAP1]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999; ⚠ same locus (6.5 kb, same strand: neighbours can correlate without regulation) |
| [[DDX60L]] | +0.74 | +0.58 / +0.81 | both halves | 7e-06 |  |
| [[PML]] | +0.73 | +0.68 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAK2]] | B | JAK2 activity raises TAP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | B | MAP2K1 activity lowers TAP2's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds |
| [[SAMD9]] | B | SAMD9 activity raises TAP2's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without SAMD9 | 0.066 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[SP110]] | B | SP110 activity raises TAP2's level | lines that do not express SP110 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without SP110 | 0.091 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[ISG15]] | C | ISG15 activity raises TAP2's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without ISG15 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |
| [[SAMHD1]] | C | SAMHD1 activity raises TAP2's level | lines that do not express SAMHD1 (3) vs lines expressing it (47) | 1.90× lower at baseline in the lines without SAMHD1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM2, IL27RA, SLC38A1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT5]] | C | TAP2's natural level strengthens IFIT5's drug response | TAP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.05; direction clear | 0.022 | ⚠ tissue can mimic it; precision caveat |
| [[PSMB8]] | C | TAP2's natural level strengthens PSMB8's drug response | TAP2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.14; direction not clear | 0.024 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PHF11]] | C | TAP2's natural level strengthens PHF11's drug response | TAP2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.09; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | TAP2's natural level strengthens TDRD7's drug response | TAP2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.01; direction clear | 0.043 | ⚠ tissue can mimic it; precision caveat |
| [[PARP12]] | C | TAP2's natural level strengthens PARP12's drug response | TAP2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.12; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | TAP2's natural level strengthens CMTR1's drug response | TAP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.10; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB9]] | C | TAP2's natural level strengthens PSMB9's drug response | TAP2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.09; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 55.0); signed map (64.4, 33.3). **Vector** length 136, 43.4% of its response variance represented; |z| ≥ 3 in 1,386 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.63 to 56); *interferon gamma response* (hallmark, mean cos +0.65 to 60); *interferon* (control, mean cos +0.66 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.7 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +12.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.3 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.0 | +6.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.5 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.3 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.0 | +4.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -8.6 | -10.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.6 | -8.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.2 | -8.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.1 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -15.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -6.5 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | transporter 2, ATP binding cassette subfamily B member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,821,833-32,838,739 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSF2, RING11, D6S217E; previously ABCB3 |
| Gene groups (HGNC) | ATP binding cassette subfamily B |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 5 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; ER-Phagosome pathway; Antigen processing-Cross presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03519](https://www.uniprot.org/uniprotkb/Q03519) (Antigen peptide transporter 2):

> ABC transporter associated with antigen processing. In complex with TAP1 mediates unidirectional translocation of peptide antigens from cytosol to endoplasmic reticulum (ER) for loading onto MHC class I (MHCI) molecules. Uses the chemical energy of ATP to export peptides against the concentration gradient. During the transport cycle alternates between 'inward-facing' state with peptide binding site facing the cytosol to 'outward-facing' state with peptide binding site facing the ER lumen. …

**Summary**, from NCBI Gene [6891](https://www.ncbi.nlm.nih.gov/gene/6891):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily are involved in multidrug resistance. This gene is located 7 kb telomeric to gene family member …

**Accessions** — [HGNC:44](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44) · Entrez [6891](https://www.ncbi.nlm.nih.gov/gene/6891) · UniProt [Q03519](https://www.uniprot.org/uniprotkb/Q03519) · Ensembl [ENSG00000204267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204267)

## Data

Gene col 12841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12841); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12841]; `tensor/DDL_lfc|DDL_z.npy` [12841]; `embed/gene_vectors.npy` [12841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12841 or target_col == 12841). Every well: [[TAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
