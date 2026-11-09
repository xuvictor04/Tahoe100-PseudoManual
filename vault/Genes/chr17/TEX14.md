---
symbol: "TEX14"
type: "gene"
col: 4254
ensembl_id: "ENSG00000121101"
name: "testis expressed 14, intercellular bridge forming factor"
location: "17q22"
module: 93
arm: "+"
pooled_cpm: 17.0
n_lines_expressing: 47
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# TEX14

*testis expressed 14, intercellular bridge forming factor* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 49.5× (z +22.2, q 0e+00, up in 25 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.1× (z +21.3, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 0.556× (z -5.1, q 2e-04, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00910]] (+0.89, fdr 7e-06), [[CCDC200]] (+0.75, fdr 7e-06), [[TRIM72]] (+0.71, fdr 1e-05); moves opposite to [[TBC1D13]] (-0.62, fdr 1e-05), [[NDUFAF5]] (-0.57, fdr 1e-05), [[ZNF567]] (-0.56, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **49.5×** | +22.2 | 0e+00 | 25/25 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.1×** | +21.3 | 0e+00 | 44/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **54.9×** | +20.6 | 0e+00 | 40/40 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **11.1×** | +20.5 | 0e+00 | 43/45 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **21.8×** | +17.2 | 0e+00 | 33/33 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **9.84×** | +13.0 | 1e-36 | 38/44 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.43×** | +10.5 | 7e-24 | 41/45 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.50×** | +10.3 | 6e-23 | 36/44 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **5.03×** | +9.7 | 1e-20 | 42/44 (SW480, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.99×** | +9.1 | 4e-18 | 35/43 (SW480, BT-474, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **4.28×** | +8.2 | 8e-15 | 38/44 (SW480, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.39×** | +7.4 | 9e-12 | 35/44 (NCI-H460, LoVo, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **7.86×** | +6.5 | 3e-09 | 24/25 (SNU-423, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.79×** | +5.8 | 2e-07 | 33/41 (HCT15, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.79×** | +5.3 | 6e-06 | 29/44 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +4.8 | 6e-05 | 30/45 (HT-29, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.12×** | +4.3 | 7e-04 | 28/44 (A-172, LoVo, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **3.74×** | +4.2 | 0.001 | 29/43 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +3.8 | 0.004 | 25/44 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **3.25×** | +3.7 | 0.005 | 25/42 (LOX-IMVI, RKO, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.84×** | +3.7 | 0.006 | 23/44 (HEC-1-A, HOP62, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.95×** | +3.4 | 0.015 | 18/43 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +3.4 | 0.016 | 23/45 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.556×** | -5.1 | 2e-04 | 30/45 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.501×** | -4.2 | 0.008 | 25/44 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **0.565×** | -3.5 | 0.094 | 18/44 (SW1417, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.673× | -3.3 | 0.12 | 19/45 (SK-MEL-2, LS 180, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 0.571× | -3.2 | 0.15 | 19/44 (SNU-423, SW1417, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.600× | -3.1 | 0.18 | 21/44 (LS 180, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.84 | 13 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 237× (z +20.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 32.3× (z +19.2) | — |
| [[SW480 (line)]] | alt | 8.75 | 10 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.8× (z +20.3) | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.1× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 17.3 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.3× (z +15.6) | — |
| [[BT-474 (line)]] | alt | 17.8 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 13.3 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 13.4 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.1× (z +16.1) | — |
| [[SNU-423 (line)]] | alt | 11.7 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +13.6) | — |
| [[A498 (line)]] | wt | 7.28 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.0× (z +18.6) | — |
| [[CFPAC-1 (line)]] | alt | 22.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 41.4× (z +20.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 47.0× (z +18.2) | — |
| [[SW 900 (line)]] | alt | 18.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 33.3× (z +16.9) | — |
| [[C32 (line)]] | wt | 42.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 67.6× (z +15.2) | — |
| [[LoVo (line)]] | wt | 15.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 109× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 31.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.7× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 13.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +12.9) | — |
| [[A-172 (line)]] | wt | 5.61 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +13.7) | — |
| [[A549 (line)]] | wt | 8.03 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 175× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +13.6) | — |
| [[AN3 CA (line)]] | alt | 51.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 31.8× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 4.69 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.9× (z +14.6) | — |
| [[hTERT-HPNE (line)]] | wt | 8.41 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +11.2) | — |
| [[J82 (line)]] | alt | 15.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 45.4× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.53× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 53.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 6.08 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +14.7) | [[Sunitinib (drug)]] 5 µM 0.0498× (z -11.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 16.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.7× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 66.8× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.30× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 47.8 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.2× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.18× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 11.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 103× (z +19.8) | — |
| [[HCT15 (line)]] | alt | 30.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 19.8× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 51.0× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 7.35× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 56.6 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +13.5) | [[Auranofin (drug)]] 5 µM 0.181× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 13.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +15.9) | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 49.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.5× (z +16.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 33.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 54.8× (z +15.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 22.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +12.1) | — |
| [[H4 (line)]] | wt | 10.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.2× (z +11.1) | — |
| [[RKO (line)]] | wt | 13.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 46.5× (z +16.6) | — |
| [[SW48 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 152× (z +13.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00910]] | +0.89 | +0.83 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CCDC200]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.71 | +0.79 / +0.57 | both halves | 1e-05 |  |
| [[HEXIM1]] | +0.70 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[IQCN]] | +0.68 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[FAM222A]] | +0.68 | +0.82 / +0.65 | both halves | 7e-06 |  |
| [[CLASP1-AS1]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MPDU1]] | +0.67 | +0.76 / +0.44 | both halves | 3e-05 |  |
| [[FOSB]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.65 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.63 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[USP50]] | +0.63 | +0.69 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D13]] | -0.62 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NDUFAF5]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZNF567]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[VPS33B]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PCGF6]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[YTHDF1]] | -0.56 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[FAM24B]] | -0.56 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ASB13]] | -0.56 | -0.48 / -0.46 | both halves | 3e-05 | same gene group |
| [[LRRC42]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MFSD14CP]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[PSMG2]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TEX14's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.9, -26.4); signed map (4.8, 16.3). **Vector** length 111, 33.8% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +20.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +22.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.3 | +8.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.3 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +20.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +10.5 |
|  | [[Artemether (drug)]] 0.05 µM |  | +2.8 | +2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -4.7 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.2 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -5.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 14, intercellular bridge forming factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,556,678-58,692,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CT113, SgK307 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Pseudokinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWB6](https://www.uniprot.org/uniprotkb/Q8IWB6) (Inactive serine/threonine-protein kinase TEX14):

> Required both for the formation of intercellular bridges during meiosis and for kinetochore-microtubule attachment during mitosis. Intercellular bridges are evolutionarily conserved structures that connect differentiating germ cells and are required for spermatogenesis and male fertility. Acts by promoting the conversion of midbodies into intercellular bridges via its interaction with CEP55: interaction with CEP55 inhibits the interaction between CEP55 and PDCD6IP/ALIX and TSG101, blocking cell …

**Summary**, from NCBI Gene [56155](https://www.ncbi.nlm.nih.gov/gene/56155):

> The protein encoded by this gene is necessary for intercellular bridges in germ cells, which are required for spermatogenesis. Three transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:11737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11737) · Entrez [56155](https://www.ncbi.nlm.nih.gov/gene/56155) · UniProt [Q8IWB6](https://www.uniprot.org/uniprotkb/Q8IWB6) · Ensembl [ENSG00000121101](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121101)

## Data

Gene col 4254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4254); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4254]; `tensor/DDL_lfc|DDL_z.npy` [4254]; `embed/gene_vectors.npy` [4254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4254 or target_col == 4254). Every well: [[TEX14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
