---
symbol: "GIPC2"
type: "gene"
col: 6100
ensembl_id: "ENSG00000137960"
name: "GIPC PDZ domain containing family member 2"
location: "1p31.1"
module: 23
arm: "+"
pooled_cpm: 42.36
n_lines_expressing: 49
n_dd_up: 37
n_dd_down: 4
n_dd_up_clean: 31
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# GIPC2

*GIPC PDZ domain containing family member 2* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +22.8, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.681× (z -6.4, q 8e-08, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (KATO III 0.404×, Panc 03.27 0.345×, LS 180 0.405×, LoVo 0.476×); [[Panobinostat (drug)]] 5 µM in 3 lines (Panc 03.27 0.304×, LS 180 0.386×, KATO III 0.446×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 0.241×, SHP-77 0.186×; ⚠ toxic; transcription drop); [[Monocrotaline (drug)]] 5 µM in 1 line (SW48 0.0567×); [[Gemfibrozil (drug)]] 0.5 µM in 1 line (CHP-212 0.0717×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFC1]] (+0.71, fdr 1e-05), [[LSMEM1]] (+0.71, fdr 7e-06), [[NQO1-DT]] (+0.71, fdr 3e-05); moves opposite to [[EHD4]] (-0.64, fdr 7e-05), [[PHC2]] (-0.64, fdr 3e-05), [[PPM1G]] (-0.63, fdr 7e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +22.8 | 0e+00 | 44/47 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +15.5 | 0e+00 | 35/46 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +11.3 | 2e-27 | 42/47 (HS-578T, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +10.6 | 3e-24 | 33/47 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +9.9 | 4e-21 | 39/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +9.4 | 3e-19 | 35/47 (A-172, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.9 | 4e-17 | 31/47 (HOP62, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +8.1 | 3e-14 | 34/45 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +7.6 | 2e-12 | 30/47 (A498, CFPAC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +7.0 | 1e-10 | 34/47 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.9 | 2e-10 | 28/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.48×** | +6.5 | 3e-09 | 32/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.0 | 8e-08 | 25/45 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.9 | 1e-07 | 29/47 (CFPAC-1, C32, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +5.6 | 8e-07 | 28/46 (A-172, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.2 | 7e-06 | 23/47 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 25/48 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6100.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (KATO III 0.404×, Panc 03.27 0.345×, LS 180 0.405×, LoVo 0.476×); [[Panobinostat (drug)]] 5 µM in 3 lines (Panc 03.27 0.304×, LS 180 0.386×, KATO III 0.446×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 0.241×, SHP-77 0.186×; ⚠ toxic; transcription drop); [[Monocrotaline (drug)]] 5 µM in 1 line (SW48 0.0567×); [[Gemfibrozil (drug)]] 0.5 µM in 1 line (CHP-212 0.0717×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -6.4 | 8e-08 | 27/47 (KATO III, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.787×** | -4.0 | 0.012 | 21/47 (Panc 03.27, LS 180, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.788×** | -4.0 | 0.012 | 16/46 (Hs 766T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.807×** | -3.6 | 0.045 | 16/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.824× | -3.3 | 0.13 | 15/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.831× | -3.1 | 0.18 | 11/47 (HT-29, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.4 | 14 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +19.0) | — |
| [[HEC-1-A (line)]] | alt | 51.9 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +13.3) | — |
| [[A498 (line)]] | wt | 59.4 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 27.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +14.7) | — |
| [[HS-578T (line)]] | alt | 55.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +16.5) | — |
| [[NCI-H2030 (line)]] | alt | 49.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.55× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.3) | — |
| [[A-172 (line)]] | wt | 28.5 | 4 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.84× (z +10.8) | — |
| [[A549 (line)]] | wt | 16.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.7) | — |
| [[C32 (line)]] | wt | 34.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +11.9) | — |
| [[SW480 (line)]] | alt | 31.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +14.9) | — |
| [[CFPAC-1 (line)]] | alt | 19.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +14.4) | — |
| [[KATO III (line)]] | alt | 81.9 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.374× (z -11.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.404× (z -10.4) |
| [[LS 180 (line)]] | wt | 87.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.386× (z -10.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 40.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 62.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -15.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 20.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.8) | [[Temsirolimus (drug)]] 0.5 µM 0.183× (z -9.4) |
| [[SNU-423 (line)]] | alt | 45.4 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -11.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 36.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.5) | — |
| [[LoVo (line)]] | wt | 69.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 48.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -11.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -9.8) |
| [[PANC-1 (line)]] | alt | 45.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +14.9) | — |
| [[RKO (line)]] | wt | 26.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 46.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +15.7) | — |
| [[SW 900 (line)]] | alt | 35.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +14.6) | — |
| [[SW48 (line)]] | wt | 12.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.71× (z +10.5) | [[Monocrotaline (drug)]] 5 µM 0.0567× (z -10.9) |
| [[A-427 (line)]] | wt | 34.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.66× (z +16.1) | — |
| [[CHP-212 (line)]] | wt | 39.4 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0717× (z -10.2) |
| [[HCT15 (line)]] | alt | 38.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 95.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 55.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.7) | — |
| [[J82 (line)]] | alt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 79.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFC1]] | +0.71 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LSMEM1]] | +0.71 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[NQO1-DT]] | +0.71 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[KANSL1L]] | +0.69 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[KMT2E-AS1]] | +0.68 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TTC33]] | +0.67 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DNAJB4]] | +0.67 | +0.72 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PSMD7-DT]] | +0.67 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[STX17-DT]] | +0.67 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[RAB21]] | +0.66 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[LINC02955]] | +0.65 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[N4BP2L1]] | +0.65 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[SOX2-OT]] | +0.64 | +0.63 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.64 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[PHC2]] | -0.64 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[PPM1G]] | -0.63 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[GNA12]] | -0.63 | -0.63 / -0.26 | both halves | 4e-04 |  |
| [[GGA1]] | -0.62 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[STUB1]] | -0.60 | -0.40 / -0.21 | both halves | 7e-04 |  |
| [[ZBED4]] | -0.60 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[GPRIN1]] | -0.60 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[STX1A]] | -0.60 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[VPS37C]] | -0.59 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[EEFSEC]] | -0.59 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[WRAP73]] | -0.58 | -0.44 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[TRIM35]] | -0.58 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GIPC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (7.0, 22.6); signed map (24.0, -3.8). **Vector** length 121, 33.1% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.4 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +22.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +4.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.6 | -6.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -8.9 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -8.5 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.7 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.5 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[vincristine (drug)]] 5 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | GIPC PDZ domain containing family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:77,979,542-78,138,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20075, SEMCAP-2 |
| Gene groups (HGNC) | PDZ domain containing; GIPC PDZ domain containing family |
| Matched by | ensembl_id |

UniProt [Q8TF65](https://www.uniprot.org/uniprotkb/Q8TF65) carries no function annotation.

**Summary**, from NCBI Gene [54810](https://www.ncbi.nlm.nih.gov/gene/54810):

> Enables identical protein binding activity. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18177) · Entrez [54810](https://www.ncbi.nlm.nih.gov/gene/54810) · UniProt [Q8TF65](https://www.uniprot.org/uniprotkb/Q8TF65) · Ensembl [ENSG00000137960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137960)

## Data

Gene col 6100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6100); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6100]; `tensor/DDL_lfc|DDL_z.npy` [6100]; `embed/gene_vectors.npy` [6100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6100 or target_col == 6100). Every well: [[GIPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GIPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
