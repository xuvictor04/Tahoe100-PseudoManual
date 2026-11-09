---
symbol: "RALB"
type: "gene"
col: 6845
ensembl_id: "ENSG00000144118"
name: "RAS like proto-oncogene B"
location: "2q14.2"
module: 78
arm: "+"
pooled_cpm: 73.3
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# RALB

*RAS like proto-oncogene B* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.06× (z +15.4, q 0e+00, up in 36 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.26× (z +5.1, q 6e-05, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (A-427 4.78×, MIA PaCa-2 3.62×, PANC-1 2.75×, KATO III 3.92×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 2.82×, MIA PaCa-2 3.33×, SW480 2.01×, A549 2.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.60×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.696× (z -11.3, q 1e-26, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPM3]] (+0.68, fdr 7e-06), [[CAPN2]] (+0.65, fdr 7e-06), [[MYO5A]] (+0.62, fdr 7e-06); moves opposite to [[GTF2IRD2B]] (-0.63, fdr 2e-05), [[SETDB1]] (-0.59, fdr 1e-05), [[ANKHD1-EIF4EBP3]] (-0.56, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRAPPC6A]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6845.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (A-427 4.78×, MIA PaCa-2 3.62×, PANC-1 2.75×, KATO III 3.92×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (PANC-1 2.82×, MIA PaCa-2 3.33×, SW480 2.01×, A549 2.25×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 2.60×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +15.4 | 0e+00 | 36/40 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +12.2 | 1e-31 | 38/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.1 | 6e-05 | 22/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.25×** | +4.6 | 7e-04 | 22/44 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.014 | 4/48 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | 1.19× | +3.8 | 0.014 | 18/47 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.016 | 18/48 (KATO III, HT-29, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +3.5 | 0.030 | 14/48 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.4 | 0.037 | 17/47 (HT-29, LS 180, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 1.16× | +3.2 | 0.066 | 14/48 (A549, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -11.3 | 1e-26 | 30/48 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.699×** | -11.1 | 4e-26 | 33/48 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.745×** | -6.5 | 2e-08 | 39/48 (A-427, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.761×** | -5.3 | 2e-05 | 29/49 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.856× | -4.7 | 3e-04 | 18/48 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.825×** | -4.2 | 0.002 | 20/49 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.858× | -4.0 | 0.005 | 19/48 (NCI-H23, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.846× | -3.7 | 0.017 | 15/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.844× | -3.6 | 0.021 | 16/47 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.845× | -3.5 | 0.022 | 21/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.852× | -3.5 | 0.023 | 17/49 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.5 | 0.025 | 19/48 (HOP62, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.4 | 0.027 | 19/48 (J82, LS 180, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.852× | -3.4 | 0.031 | 20/47 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.3 | 0.034 | 19/48 (J82, NCI-H2347, …) | top dose only | composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.896× | -3.3 | 0.034 | 17/48 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.856× | -3.2 | 0.047 | 15/48 (NCI-H23, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.872× | -3.0 | 0.072 | 14/47 (RKO, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.875× | -3.0 | 0.072 | 16/49 (NCI-H23, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 82.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.8) |
| [[PANC-1 (line)]] | alt | 56.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +13.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -17.6) |
| [[A-427 (line)]] | wt | 44.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +15.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -14.6) |
| [[HOP62 (line)]] | alt | 87.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -14.2) |
| [[HT-29 (line)]] | alt | 84.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.4) |
| [[A549 (line)]] | wt | 77.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 61.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -14.1) |
| [[KATO III (line)]] | alt | 42.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 87.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -12.6) |
| [[RKO (line)]] | wt | 77.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.244× (z -14.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.4) |
| [[A-172 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -8.9) |
| [[C32 (line)]] | wt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.3) |
| [[H4 (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 67.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 82.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 63.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 68.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 58.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 44.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 68.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.4) |
| [[SNU-423 (line)]] | alt | 63.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.8) |
| [[SW1417 (line)]] | alt | 112 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -10.1) |
| [[SW480 (line)]] | alt | 63.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM3]] | +0.68 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[CAPN2]] | +0.65 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[MYO5A]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ATP13A2]] | +0.62 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[IQGAP1]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ARPC2]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PSMD2]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CAP1]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[BZW1]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CDC42BPB]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PODXL]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IRD2B]] | -0.63 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SETDB1]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ANKHD1-EIF4EBP3]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ANKHD1]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[KANSL1L]] | -0.55 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[KLRK1-AS1]] | -0.55 | -0.57 / -0.24 | both halves | 4e-04 |  |
| [[EIF4EBP3]] | -0.55 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[ZCCHC8]] | -0.54 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[NAPA-AS1]] | -0.54 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[YBEY]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[DYRK1B]] | -0.54 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[TFAP2A-AS1]] | -0.54 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAPPC6A]] | C | TRAPPC6A's natural level strengthens RALB's drug response | TRAPPC6A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.20; direction not clear | 0.093 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.6, 6.9); signed map (-7.8, 39.0). **Vector** length 116, 30.9% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.1 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.8 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -4.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.6 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | RAS like proto-oncogene B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:120,240,064-120,294,710 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 6 pathways, smallest: p38MAPK events; Signalling to RAS; Signalling to ERKs |
| Matched by | ensembl_id |

**Function**, from UniProt [P11234](https://www.uniprot.org/uniprotkb/P11234) (Ras-related protein Ral-B):

> Multifunctional GTPase involved in a variety of cellular processes including gene expression, cell migration, cell proliferation, oncogenic transformation and membrane trafficking. Accomplishes its multiple functions by interacting with distinct downstream effectors. Acts as a GTP sensor for GTP-dependent exocytosis of dense core vesicles (By similarity). Required both to stabilize the assembly of the exocyst complex and to localize functional exocyst complexes to the leading edge of migrating …

**Summary**, from NCBI Gene [5899](https://www.ncbi.nlm.nih.gov/gene/5899):

> This gene encodes a GTP-binding protein that belongs to the small GTPase superfamily and Ras family of proteins. GTP-binding proteins mediate the transmembrane signaling initiated by the occupancy of certain cell surface receptors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9840) · Entrez [5899](https://www.ncbi.nlm.nih.gov/gene/5899) · UniProt [P11234](https://www.uniprot.org/uniprotkb/P11234) · Ensembl [ENSG00000144118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144118)

## Data

Gene col 6845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6845); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6845]; `tensor/DDL_lfc|DDL_z.npy` [6845]; `embed/gene_vectors.npy` [6845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6845 or target_col == 6845). Every well: [[RALB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
