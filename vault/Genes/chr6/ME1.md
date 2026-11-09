---
symbol: "ME1"
type: "gene"
col: 806
ensembl_id: "ENSG00000065833"
name: "malic enzyme 1"
location: "6q14.2"
module: 117
arm: "+"
pooled_cpm: 88.54
n_lines_expressing: 39
n_dd_up: 45
n_dd_down: 7
n_dd_up_clean: 37
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# ME1

*malic enzyme 1* — 6q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (8 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 4.96× (z +22.6, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.657× (z -7.4, q 1e-10, down in 22 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIR]] (+0.70, fdr 7e-06), [[SLC7A11]] (+0.69, fdr 7e-06), [[GCLM]] (+0.69, fdr 7e-06); moves opposite to [[MCRIP1]] (-0.56, fdr 1e-05), [[MTMR14]] (-0.53, fdr 2e-05), [[TAF5]] (-0.52, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[TRIM16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **4.96×** | +22.6 | 0e+00 | 36/37 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.38×** | +21.3 | 0e+00 | 35/36 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +21.2 | 0e+00 | 28/37 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.25×** | +20.6 | 0e+00 | 36/37 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.20×** | +20.3 | 0e+00 | 36/37 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +15.8 | 0e+00 | 29/37 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +15.1 | 0e+00 | 30/37 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.04×** | +12.5 | 9e-34 | 33/37 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +11.9 | 4e-31 | 30/36 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.63×** | +10.6 | 3e-24 | 32/35 (NCI-H2347, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.35×** | +9.5 | 7e-20 | 33/38 (COLO 205, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +8.7 | 1e-16 | 21/33 (NCI-H1792, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +8.5 | 8e-16 | 22/36 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.2 | 3e-11 | 16/33 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +6.9 | 2e-10 | 23/36 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.44×** | +6.4 | 7e-09 | 25/37 (BT-474, HT-29, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +6.1 | 5e-08 | 21/37 (A498, KATO III, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **2.01×** | +5.7 | 4e-07 | 25/36 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.98×** | +5.6 | 6e-07 | 23/36 (NCI-H460, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 8e-07 | 19/37 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 4e-06 | 22/36 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.657×** | -7.4 | 1e-10 | 22/37 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.697×** | -6.3 | 7e-08 | 22/37 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.719×** | -5.8 | 1e-06 | 21/37 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.822×** | -4.9 | 1e-04 | 21/38 (C32, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -4.9 | 1e-04 | 22/36 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.788×** | -4.2 | 0.003 | 19/37 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.821×** | -3.3 | 0.071 | 18/39 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.836× | -3.2 | 0.11 | 13/36 (SW480, C32, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.840× | -3.1 | 0.14 | 13/36 (C32, LS 180, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 344 | 4 | 11 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 5.42× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.140× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 170 | 14 (3 ⚠) | 1 | [[Bortezomib (drug)]] 0.05 µM 4.05× (z +15.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -8.8) |
| [[C32 (line)]] | wt | 155 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -22.4) |
| [[PANC-1 (line)]] | alt | 110 | 8 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +20.9) | [[Digitoxin (drug)]] 5 µM 0.371× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.1) |
| [[BT-474 (line)]] | alt | 55.5 | 11 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.51× (z +16.2) | — |
| [[HOP62 (line)]] | alt | 32.1 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +25.1) | — |
| [[NCI-H2347 (line)]] | alt | 38.7 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +18.5) | — |
| [[HEC-1-A (line)]] | alt | 91.1 | 10 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.53× (z +25.3) | — |
| [[HT-29 (line)]] | alt | 180 | 5 (1 ⚠) | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.50× (z +21.3) | [[Panobinostat (drug)]] 5 µM 0.163× (z -18.2) |
| [[SW48 (line)]] | wt | 160 | 6 (1 ⚠) | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.20× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.340× (z -10.0) |
| [[A549 (line)]] | wt | 79.9 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +20.0) | — |
| [[KATO III (line)]] | alt | 197 | 4 | 5 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.21× (z +14.1) | [[Belinostat (drug)]] 5 µM 0.163× (z -17.8) |
| [[LS 180 (line)]] | wt | 218 | 4 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.54× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 42.1 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +23.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 25.9 | 6 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.65× (z +11.3) | [[Belinostat (drug)]] 5 µM 0.231× (z -10.9) |
| [[COLO 205 (line)]] | alt | 42.3 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 27.6× (z +18.1) | — |
| [[NCI-H1792 (line)]] | alt | 132 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.38× (z +12.2) | — |
| [[SW480 (line)]] | alt | 70.9 | 5 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 3.67× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.495× (z -8.7) |
| [[A498 (line)]] | wt | 85.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.93× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.490× (z -11.5) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 45.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 144 | 5 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 5.27× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 27.1 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.62× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 5 | 0 | [[Auranofin (drug)]] 5 µM 7.61× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 42.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +17.8) | — |
| [[SW1417 (line)]] | alt | 56.9 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.75× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.6) ⚠ cell-cycle shift, explains ~9% of this change |
| [[HS-578T (line)]] | alt | 75.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 91.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.04× (z +13.1) | — |
| [[SHP-77 (line)]] | alt | 96.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 70.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +15.1) | — |
| [[J82 (line)]] | alt | 71.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -11.2) ⚠ cell-cycle shift, explains ~9% of this change |
| [[NCI-H23 (line)]] | alt | 26.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.4) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -11.6) |
| [[AN3 CA (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.60 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 19.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIR]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[SLC7A11]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 455 |
| [[GCLM]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 538 |
| [[TRIM16L]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TRIM16]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CYP4F11]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[VEGFD]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[IDE]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GSR]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 608 |
| [[TRIM16L-1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PSMD11]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 | pathway: Cellular response to chemical stress |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCRIP1]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MTMR14]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TAF5]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ARHGAP1]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[UHRF2]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[STC1]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[FAM110A]] | -0.48 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SP4]] | -0.48 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[B3GAT3]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[PPOX]] | -0.47 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[SHPK]] | -0.47 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[RASA2]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ME1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers ME1's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.1% of all compounds | 0.042 | ⚠ off-target possible; 4 compounds |
| [[VEGFD]] | B | VEGFD activity raises ME1's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 2.72× lower at baseline in the lines without VEGFD | 0.056 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[HTATIP2]] | B | HTATIP2 activity raises ME1's level | lines that do not express HTATIP2 (7) vs lines expressing it (43) | 4.81× lower at baseline in the lines without HTATIP2 | 0.077 | ⚠ within organs, on part of the lines; also absent: C3orf52, TBILA, ITPR3 |
| [[HDAC6]] | B | HDAC6 activity raises ME1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01564]] | B | LINC01564 activity raises ME1's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 2.20× lower at baseline in the lines without LINC01564 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM16]] | B | ME1 activity raises TRIM16's level | lines that do not express ME1 (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without ME1 | 0.098 | ⚠ within organs, on part of the lines |
| [[PSMD1]] | C | ME1 activity weakens PSMD1's drug response | lines that do not express ME1 (11) vs lines expressing it (38) | the lines without ME1 respond 0.92× as strongly (z diff -0.87); strongest at Ixazomib citrate 0.5 µM: 4.24x vs 4.34x (z diff -2.4) | 0.065 | ⚠ within organs, on part of the lines; target measured in part of the lines; rests on the correction; artifact flags |
| [[PSMD11]] | C | ME1 activity weakens PSMD11's drug response | lines that do not express ME1 (11) vs lines expressing it (38) | the lines without ME1 respond 0.82× as strongly (z diff +0.02); strongest at Ixazomib citrate 0.5 µM: 3.72x vs 3.82x (z diff -2.3) | 0.089 | ⚠ within organs, on part of the lines; target measured in part of the lines; both ways; rests on the correction; artifact flags |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.4, 48.5); signed map (50.9, -10.2). **Vector** length 146, 47.6% of its response variance represented; |z| ≥ 3 in 1,441 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NFE2L2 regulating anti-oxidant/detoxification enzymes* (reactome, mean cos +0.60 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.9 | +22.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.1 | +21.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.3 | +20.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.1 | +20.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.8 | +10.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.5 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.0 | +9.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.5 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.2 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.6 | -3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | malic enzyme 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.2 — chr6:83,210,402-83,431,051 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Malic enzyme family |
| Hallmark sets | FATTY_ACID_METABOLISM, COMPLEMENT, GLYCOLYSIS, ADIPOGENESIS, MTORC1_SIGNALING |
| Reactome | 12 pathways, smallest: NFE2L2 regulating TCA cycle genes; Regulation of pyruvate metabolism; Pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P48163](https://www.uniprot.org/uniprotkb/P48163) (NADP-dependent malic enzyme):

> Catalyzes the oxidative decarboxylation of (S)-malate in the presence of NADP(+) and divalent metal ions, and decarboxylation of oxaloacetate.

**Summary**, from NCBI Gene [4199](https://www.ncbi.nlm.nih.gov/gene/4199):

> This gene encodes a cytosolic, NADP-dependent enzyme that generates NADPH for fatty acid biosynthesis. The activity of this enzyme, the reversible oxidative decarboxylation of malate, links the glycolytic and citric acid cycles. The regulation of expression for this gene is complex. Increased expression can result from elevated levels of thyroid hormones or by higher proportions of carbohydrates in the diet. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6983) · Entrez [4199](https://www.ncbi.nlm.nih.gov/gene/4199) · UniProt [P48163](https://www.uniprot.org/uniprotkb/P48163) · Ensembl [ENSG00000065833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065833)

## Data

Gene col 806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 806); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 806]; `tensor/DDL_lfc|DDL_z.npy` [806]; `embed/gene_vectors.npy` [806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 806 or target_col == 806). Every well: [[ME1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ME1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
