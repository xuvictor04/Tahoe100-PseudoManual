---
symbol: "OSTM1"
type: "gene"
col: 1307
ensembl_id: "ENSG00000081087"
name: "osteoclastogenesis associated transmembrane protein 1"
location: "6q21"
module: 65
arm: "-"
pooled_cpm: 45.46
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# OSTM1

*osteoclastogenesis associated transmembrane protein 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.56× (z +26.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.754× (z -5.6, q 2e-05, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.329×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (SHP-77 0.120×; ⚠ toxic); [[Riluzole hydrochloride (drug)]] 0.5 µM in 1 line (CHP-212 0.0686×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAGC-DT]] (+0.65, fdr 2e-05), [[CHMP3]] (+0.65, fdr 1e-05), [[TUG1]] (+0.64, fdr 1e-05); moves opposite to [[MKRN2]] (-0.65, fdr 3e-05), [[TADA1]] (-0.65, fdr 1e-05), [[HACE1]] (-0.62, fdr 8e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +26.9 | 0e+00 | 45/48 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.13×** | +23.1 | 0e+00 | 44/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +18.8 | 0e+00 | 34/40 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +18.3 | 0e+00 | 44/47 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.42×** | +17.2 | 0e+00 | 45/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +14.4 | 6e-45 | 44/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +13.9 | 4e-42 | 36/44 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +13.7 | 9e-41 | 43/48 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +12.0 | 3e-31 | 38/48 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +11.4 | 2e-28 | 38/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.76×** | +11.4 | 2e-28 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +11.1 | 4e-27 | 38/48 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +10.7 | 3e-25 | 38/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +10.4 | 1e-23 | 40/48 (A498, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.67×** | +10.4 | 1e-23 | 39/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +9.7 | 2e-20 | 33/49 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +9.7 | 2e-20 | 37/48 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 2e-14 | 34/47 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +7.5 | 2e-12 | 34/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 1e-09 | 28/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.329×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (SHP-77 0.120×; ⚠ toxic); [[Riluzole hydrochloride (drug)]] 0.5 µM in 1 line (CHP-212 0.0686×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.754×** | -5.6 | 2e-05 | 23/48 (SNU-1, C-33 A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.717× | -3.6 | 0.11 | 15/43 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 26.7 | 11 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.52× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 40.6 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +24.8) | — |
| [[PANC-1 (line)]] | alt | 135 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.05× (z +15.4) | — |
| [[A-172 (line)]] | wt | 51.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +19.3) | — |
| [[RPMI-7951 (line)]] | alt | 56.5 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.9) | — |
| [[A498 (line)]] | wt | 34.4 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 27.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +13.4) | — |
| [[SW480 (line)]] | alt | 35.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 42.8 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 80.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.3) | — |
| [[C32 (line)]] | wt | 54.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.39× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 30.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +19.8) | — |
| [[HS-578T (line)]] | alt | 50.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.7) | — |
| [[KATO III (line)]] | alt | 42.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.0) | — |
| [[LS 180 (line)]] | wt | 23.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 66.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 60.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 27.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +10.6) | — |
| [[J82 (line)]] | alt | 53.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.0) | — |
| [[LOX-IMVI (line)]] | wt | 42.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.7) | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 55.1 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.69× (z +10.0) | — |
| [[A549 (line)]] | wt | 35.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +12.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.8) | — |
| [[LoVo (line)]] | wt | 40.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[RKO (line)]] | wt | 50.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 62.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +16.0) | — |
| [[C-33 A (line)]] | alt | 96.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.329× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 19.1 | 0 | 1 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0686× (z -8.7) |
| [[COLO 205 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +10.2) | — |
| [[H4 (line)]] | wt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 63.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.120× (z -9.1) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGC-DT]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[CHMP3]] | +0.65 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TUG1]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LIG4]] | +0.63 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[GNPDA1]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.61 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LINC00571]] | +0.61 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[TSGA10]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LEPROT]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PEPD]] | +0.60 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[WSB2]] | +0.60 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[GTF2H1]] | +0.60 | +0.66 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN2]] | -0.65 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TADA1]] | -0.65 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[HACE1]] | -0.62 | -0.68 / -0.37 | both halves | 8e-05 |  |
| [[VDAC3]] | -0.60 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[NFRKB]] | -0.60 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[SCAI]] | -0.59 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[ELP1]] | -0.59 | -0.67 / -0.28 | both halves | 3e-04 |  |
| [[MMS19]] | -0.58 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[ELP2]] | -0.58 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[ATG4C]] | -0.58 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[METTL17]] | -0.57 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[NPRL2]] | -0.57 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OSTM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00571]] | B | LINC00571 activity lowers OSTM1's level | lines that do not express LINC00571 (5) vs lines expressing it (45) | 1.99× higher at baseline in the lines without LINC00571 | 0.065 | ⚠ within organs, on part of the lines; also absent: KIFC3, NDRG1, DELEC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.5, -11.7); signed map (18.8, -27.3). **Vector** length 106, 30.8% of its response variance represented; |z| ≥ 3 in 1,371 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +13.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +9.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.8 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.8 | +11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +10.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +5.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.3 | +11.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | +11.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.2 | -5.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | osteoclastogenesis associated transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:108,029,245-108,165,854 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC019, GL |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WC4](https://www.uniprot.org/uniprotkb/Q86WC4) (Osteopetrosis-associated transmembrane protein 1):

> Required for osteoclast and melanocyte maturation and function.

**Summary**, from NCBI Gene [28962](https://www.ncbi.nlm.nih.gov/gene/28962):

> This gene encodes a protein that may be involved in the degradation of G proteins via the ubiquitin-dependent proteasome pathway. The encoded protein binds to members of subfamily A of the regulator of the G-protein signaling (RGS) family through an N-terminal leucine-rich region. This protein also has a central RING finger-like domain and E3 ubiquitin ligase activity. This protein is highly conserved from flies to humans. Defects in this gene may cause the autosomal recessive, infantile …

**Accessions** — [HGNC:21652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21652) · Entrez [28962](https://www.ncbi.nlm.nih.gov/gene/28962) · UniProt [Q86WC4](https://www.uniprot.org/uniprotkb/Q86WC4) · Ensembl [ENSG00000081087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081087)

## Data

Gene col 1307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1307); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1307]; `tensor/DDL_lfc|DDL_z.npy` [1307]; `embed/gene_vectors.npy` [1307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1307 or target_col == 1307). Every well: [[OSTM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSTM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
