---
symbol: "PER3"
type: "gene"
col: 548
ensembl_id: "ENSG00000049246"
name: "period circadian regulator 3"
location: "1p36.23"
module: 14
arm: "+"
pooled_cpm: 38.8
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 41
n_dd_up_clean: 10
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PER3

*period circadian regulator 3* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.92× (z +31.9, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (4 with an alert ⚠); the strongest is [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM: 0.358× (z -16.9, q 0e+00, down in 38 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Megestrol (drug)]] 5 µM: 0.530× (z -14.7, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEF]] (+0.75, fdr 7e-06), [[LINC02968]] (+0.59, fdr 1e-05), [[DBP]] (+0.58, fdr 7e-06); moves opposite to [[OGFOD1]] (-0.54, fdr 3e-05), [[ZDHHC9]] (-0.53, fdr 1e-05), [[SEC14L2]] (-0.53, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BTN2A2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +31.9 | 0e+00 | 40/44 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +11.3 | 5e-27 | 31/44 (A-172, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +9.1 | 1e-17 | 31/45 (COLO 205, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.7 | 2e-12 | 25/44 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +7.6 | 3e-12 | 29/45 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.6 | 5e-09 | 25/45 (HOP62, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.5 | 3e-06 | 25/45 (J82, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 3e-06 | 25/45 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 8e-06 | 25/45 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +5.1 | 2e-05 | 22/45 (HOP62, J82, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | 1.17× | +3.6 | 0.016 | 10/46 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.096 | 14/45 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.1 | 0.096 | 13/45 (NCI-H460, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.358×** | -16.9 | 0e+00 | 38/45 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.530×** | -14.7 | 0e+00 | 37/45 (A498, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -10.4 | 4e-23 | 28/44 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -10.4 | 4e-23 | 30/45 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -7.5 | 1e-11 | 30/45 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.732×** | -7.2 | 5e-11 | 29/45 (HEC-1-A, A-172, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.788×** | -5.5 | 3e-06 | 22/45 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.557×** | -5.0 | 3e-05 | 24/43 (Hs 766T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.741×** | -4.9 | 6e-05 | 21/45 (NCI-H460, CHP-212, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.742×** | -4.9 | 6e-05 | 19/45 (RPMI-7951, C32, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.746×** | -4.8 | 8e-05 | 22/45 (HS-578T, RPMI-7951, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -4.8 | 8e-05 | 19/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -4.6 | 2e-04 | 20/45 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.756×** | -4.6 | 2e-04 | 20/45 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.5 | 3e-04 | 19/45 (RPMI-7951, SW 1088, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.755×** | -4.4 | 3e-04 | 21/45 (HS-578T, RPMI-7951, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 121 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +23.6) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 97.2 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +15.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.161× (z -13.8) ⚠ unreliable plate only · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -13.3) |
| [[A-172 (line)]] | wt | 57.5 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +27.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.173× (z -15.2) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.291× (z -15.1) |
| [[HS-578T (line)]] | alt | 87.1 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +21.1) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.0813× (z -20.1) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.249× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 106 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +22.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.142× (z -14.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.6) |
| [[HOP62 (line)]] | alt | 39.4 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.5) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.239× (z -11.4) ⚠ unreliable plate only · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.3) |
| [[Hs 766T (line)]] | wt | 141 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.124× (z -17.8) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.332× (z -13.3) |
| [[PANC-1 (line)]] | alt | 52.9 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +25.8) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.202× (z -16.7) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.424× (z -12.6) |
| [[H4 (line)]] | wt | 60.1 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +19.5) | [[Megestrol (drug)]] 5 µM 0.212× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 42.8 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +16.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 76.9 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 43.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +22.6) | [[Megestrol (drug)]] 5 µM 0.348× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 34.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0919× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 61.8 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0742× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Megestrol (drug)]] 5 µM 0.392× (z -9.1) |
| [[A-427 (line)]] | wt | 39.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +19.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -8.9) |
| [[A498 (line)]] | wt | 34.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.5) | [[Megestrol (drug)]] 5 µM 0.227× (z -18.3) |
| [[C32 (line)]] | wt | 28.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +16.8) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.155× (z -10.3) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 3 (1 ⚠) | — | [[Cilostazol (drug)]] 0.05 µM 0.0791× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 12.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +22.5) | — |
| [[SNU-423 (line)]] | alt | 73.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +13.8) | [[Megestrol (drug)]] 5 µM 0.377× (z -10.1) |
| [[SW480 (line)]] | alt | 23.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.3) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.358× (z -9.2) ⚠ unreliable plate only · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 26.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +25.2) | — |
| [[C-33 A (line)]] | alt | 37.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +11.6) | [[Roxadustat (drug)]] 0.05 µM 0.192× (z -9.5) |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +14.3) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.187× (z -9.1) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 60.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +16.1) | — |
| [[KATO III (line)]] | alt | 27.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +17.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.284× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 21.2 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.74× (z +9.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.160× (z -9.6) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +16.2) | — |
| [[SW 900 (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.96 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEF]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | STRING 822 |
| [[LINC02968]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DBP]] | +0.58 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Circadian clock; STRING 706 |
| [[PPFIBP2]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[LINC02154]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ANKRD50]] | +0.55 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[RRAD]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ADGRG1]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CGNL1]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MARCKS]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[UAP1L1]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[NDRG4]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGFOD1]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZDHHC9]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SEC14L2]] | -0.53 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[TMEM164]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[UGP2]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[CLASP1]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[STXBP5-AS1]] | -0.51 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[RECQL]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MTRR]] | -0.50 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[GLRX]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RNF4]] | -0.49 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[METTL9]] | -0.48 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PER3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers PER3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTN2A2]] | C | PER3 activity raises BTN2A2's level | lines that do not express PER3 (3) vs lines expressing it (47) | 3.60× lower at baseline in the lines without PER3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: RIPOR3, PPP1R18, SYNPO2; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.3, 1.4); signed map (46.1, 11.7). **Vector** length 120, 32.1% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +31.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +11.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | +0.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +1.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -7.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.7 | -5.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.2 | -4.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | period circadian regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:7,784,291-7,845,177 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PAS domain containing; Period circadian regulator family |
| Reactome | 6 pathways, smallest: Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P56645](https://www.uniprot.org/uniprotkb/P56645) (Period circadian protein homolog 3):

> Originally described as a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, body …

**Summary**, from NCBI Gene [8863](https://www.ncbi.nlm.nih.gov/gene/8863):

> This gene is a member of the Period family of genes and is expressed in a circadian pattern in the suprachiasmatic nucleus, the primary circadian pacemaker in the mammalian brain. Genes in this family encode components of the circadian rhythms of locomotor activity, metabolism, and behavior. This gene is upregulated by CLOCK/ARNTL heterodimers but then represses this upregulation in a feedback loop using PER/CRY heterodimers to interact with CLOCK/ARNTL. Polymorphisms in this gene have been …

**Accessions** — [HGNC:8847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8847) · Entrez [8863](https://www.ncbi.nlm.nih.gov/gene/8863) · UniProt [P56645](https://www.uniprot.org/uniprotkb/P56645) · Ensembl [ENSG00000049246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049246)

## Data

Gene col 548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 548); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 548]; `tensor/DDL_lfc|DDL_z.npy` [548]; `embed/gene_vectors.npy` [548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 548 or target_col == 548). Every well: [[PER3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PER3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
