---
symbol: "IFIH1"
type: "gene"
col: 3645
ensembl_id: "ENSG00000115267"
name: "interferon induced with helicase C domain 1"
location: "2q24.2"
module: 32
arm: "+"
pooled_cpm: 157.6
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 46
n_dd_up_clean: 23
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 37
direction_downstream: 17
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFIH1

*interferon induced with helicase C domain 1* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +18.5, q 0e+00, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.258× (z -18.1, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.94, fdr 7e-06), [[RIGI]] (+0.92, fdr 7e-06), [[IFIT2]] (+0.92, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[TYMP]] → it (grade B ⚠); 17 go from it, the strongest it → [[HERC6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, none with an alert; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +18.5 | 0e+00 | 37/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.47×** | +16.0 | 0e+00 | 39/45 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.05×** | +14.9 | 0e+00 | 40/45 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.74×** | +13.5 | 4e-39 | 42/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.92×** | +8.4 | 6e-15 | 34/44 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +6.7 | 2e-09 | 31/46 (NCI-H460, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.52×** | +5.8 | 5e-07 | 30/46 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.42×** | +5.7 | 1e-06 | 28/45 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 1e-05 | 29/45 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 2e-05 | 32/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 4e-05 | 26/46 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.9 | 5e-05 | 31/45 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 24/47 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 0.002 | 23/45 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.006 | 29/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.258×** | -18.1 | 0e+00 | 45/45 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.282×** | -16.9 | 0e+00 | 45/45 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.316×** | -15.4 | 0e+00 | 42/45 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.481×** | -13.8 | 3e-41 | 32/46 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.405×** | -12.1 | 2e-31 | 40/45 (NCI-H23, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.557×** | -11.1 | 2e-26 | 35/45 (A549, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.455×** | -10.5 | 5e-24 | 35/46 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.467×** | -10.2 | 2e-22 | 32/46 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.492×** | -9.5 | 1e-19 | 32/45 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.618×** | -9.1 | 5e-18 | 31/46 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.535×** | -7.9 | 1e-13 | 30/45 (SNU-423, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.562×** | -7.7 | 6e-13 | 37/45 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -7.0 | 2e-10 | 32/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -6.7 | 7e-10 | 23/39 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.609×** | -6.6 | 1e-09 | 37/45 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.715×** | -6.3 | 8e-09 | 31/46 (RKO, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 199 | 0 | 20 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.224× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 173 | 0 | 19 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0458× (z -25.0) |
| [[NCI-H2347 (line)]] | alt | 276 | 5 | 14 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +20.5) | [[Tofacitinib (drug)]] 5 µM 0.324× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 268 | 15 (4 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +35.1) | [[Panobinostat (drug)]] 5 µM 0.274× (z -12.5) |
| [[A549 (line)]] | wt | 181 | 0 | 18 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.243× (z -16.7) |
| [[SNU-423 (line)]] | alt | 204 | 1 | 17 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.143× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 221 | 3 | 14 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 4.40× (z +9.5) | [[Tofacitinib (drug)]] 5 µM 0.123× (z -18.9) |
| [[RPMI-7951 (line)]] | alt | 403 | 2 | 15 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.01× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -20.7) |
| [[A498 (line)]] | wt | 266 | 1 | 13 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.18× (z +8.8) | [[Tofacitinib (drug)]] 5 µM 0.408× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 223 | 3 | 11 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +20.9) | [[Tofacitinib (drug)]] 5 µM 0.316× (z -17.5) |
| [[LoVo (line)]] | wt | 201 | 4 | 10 | [[Homoharringtonine (drug)]] 0.5 µM 4.60× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.0998× (z -21.0) |
| [[KATO III (line)]] | alt | 109 | 3 | 10 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.18× (z +11.9) | [[Auranofin (drug)]] 5 µM 0.191× (z -13.7) |
| [[RKO (line)]] | wt | 112 | 0 | 12 | — | [[Belinostat (drug)]] 5 µM 0.0937× (z -15.6) |
| [[NCI-H1792 (line)]] | alt | 196 | 0 | 11 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.308× (z -15.2) |
| [[A-172 (line)]] | wt | 266 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.39× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.194× (z -14.0) |
| [[HS-578T (line)]] | alt | 134 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.72× (z +13.6) | [[Selinexor (drug)]] 5 µM 0.285× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 105 | 3 | 6 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +15.3) | [[Tofacitinib (citrate) (drug)]] 5 µM 0.372× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 130 | 2 | 7 | [[Harringtonine (drug)]] 0.5 µM 4.26× (z +12.5) | [[Selinexor (drug)]] 5 µM 0.333× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 181 | 4 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +16.4) | [[Tofacitinib (drug)]] 5 µM 0.333× (z -12.2) |
| [[COLO 205 (line)]] | alt | 240 | 1 | 7 | [[Harringtonine (drug)]] 5 µM 3.82× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.105× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 98.9 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +30.3) | [[Panobinostat (drug)]] 5 µM 0.311× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 249 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +17.1) | [[Tofacitinib (drug)]] 5 µM 0.464× (z -10.1) |
| [[A-427 (line)]] | wt | 466 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -24.0) |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 7 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.241× (z -12.4) |
| [[J82 (line)]] | alt | 97.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +21.9) | — |
| [[LS 180 (line)]] | wt | 92.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +26.2) | — |
| [[C32 (line)]] | wt | 63.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +20.5) | — |
| [[H4 (line)]] | wt | 126 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +13.7) | [[Ixazomib citrate (drug)]] 5 µM 0.212× (z -9.0) |
| [[HCT15 (line)]] | alt | 100 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +20.6) | [[Panobinostat (drug)]] 5 µM 0.227× (z -10.0) |
| [[SHP-77 (line)]] | alt | 52.9 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.170× (z -10.4) |
| [[CHP-212 (line)]] | wt | 118 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 84.4 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.172× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 84.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +30.6) | — |
| [[PANC-1 (line)]] | alt | 80.6 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.16× (z +17.4) | — |
| [[SW 900 (line)]] | alt | 115 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.255× (z -9.3) |
| [[SW48 (line)]] | wt | 65.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +18.1) | — |
| [[Hs 766T (line)]] | wt | 184 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.301× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 113 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.189× (z -9.1) |
| [[SNU-1 (line)]] | wt | 40.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -9.2) |
| [[SW1417 (line)]] | alt | 184 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -9.6) |
| [[C-33 A (line)]] | alt | 46.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0965× (z -11.1) |
| [[SW 1088 (line)]] | alt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 174 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 972 |
| [[RIGI]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 960 |
| [[IFIT2]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 976 |
| [[IFIT1]] | +0.92 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 982 |
| [[PARP14]] | +0.91 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 879 |
| [[RSAD2]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 954 |
| [[PARP9]] | +0.90 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 888 |
| [[DDX60]] | +0.90 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 987 |
| [[OASL]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 940 |
| [[XAF1]] | +0.89 | +0.78 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 849 |
| [[DHX58]] | +0.88 | +0.78 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999 |
| [[OAS1]] | +0.88 | +0.80 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 939 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 29, C 8. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TYMP]] | B | TYMP activity raises IFIH1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without TYMP | 0.008 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[PLAAT4]] | B | PLAAT4 activity raises IFIH1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.80× lower at baseline in the lines without PLAAT4 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[EPSTI1]] | B | EPSTI1 activity raises IFIH1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.96× lower at baseline in the lines without EPSTI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[CMPK2]] | B | CMPK2 activity raises IFIH1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without CMPK2 | 0.014 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[TRIM34]] | B | TRIM34 activity raises IFIH1's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.82× lower at baseline in the lines without TRIM34 | 0.020 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |
| [[ODF3B]] | B | ODF3B activity raises IFIH1's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without ODF3B | 0.021 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[RSAD2]] | B | RSAD2 activity raises IFIH1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without RSAD2 | 0.024 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[SP110]] | B | SP110 activity raises IFIH1's level | lines that do not express SP110 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without SP110 | 0.031 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises IFIH1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without GBP1 | 0.034 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IL15]] | B | IL15 activity strengthens IFIH1's drug response | lines that do not express IL15 (9) vs lines expressing it (37) | the lines without IL15 respond 0.77× as strongly (z diff +0.72); strongest at Homoharringtonine 5 µM: 1.16x vs 3.51x (z diff +5.3) | 0.034 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[LMO2]] | B | LMO2 activity raises IFIH1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.64× lower at baseline in the lines without LMO2 | 0.038 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises IFIH1's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without PLSCR1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HERC6]] | C | IFIH1 activity raises HERC6's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 3.91× lower at baseline in the lines without IFIH1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ISG15]] | C | IFIH1 activity raises ISG15's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 3.71× lower at baseline in the lines without IFIH1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; co-absent with the target; its own permutation p |
| [[USP18]] | C | IFIH1 activity raises USP18's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 3.47× lower at baseline in the lines without IFIH1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; its own permutation p |
| [[TAP1]] | C | IFIH1 activity raises TAP1's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without IFIH1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; its own permutation p |
| [[NCOA7]] | C | IFIH1 activity raises NCOA7's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without IFIH1 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent |
| [[PSME2]] | C | IFIH1 activity raises PSME2's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 1.52× lower at baseline in the lines without IFIH1 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent |
| [[OAS3]] | C | IFIH1 activity raises OAS3's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 4.53× lower at baseline in the lines without IFIH1 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent |
| [[SP140]] | C | IFIH1 activity raises SP140's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 1.65× lower at baseline in the lines without IFIH1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent |
| [[IFI44]] | C | IFIH1 activity raises IFI44's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 4.97× lower at baseline in the lines without IFIH1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; its own permutation p |
| [[IFIT1]] | C | IFIH1 activity raises IFIT1's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 4.32× lower at baseline in the lines without IFIH1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; its own permutation p |
| [[RIGI]] | C | IFIH1 activity raises RIGI's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 3.85× lower at baseline in the lines without IFIH1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; its own permutation p |
| [[NLRC5]] | C | IFIH1 activity raises NLRC5's level | lines that do not express IFIH1 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without IFIH1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IFI35, ISG15, HERC6; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.926). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.8, 53.2); signed map (64.0, 31.2). **Vector** length 177, 70.5% of its response variance represented; |z| ≥ 3 in 1,941 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon alpha/beta signaling* (reactome, mean cos +0.83 to 27); *Interferon gamma signaling* (reactome, mean cos +0.76 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.83 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.8 | +14.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +13.1 | +13.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +12.7 | +16.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +18.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +8.0 | +8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.1 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.0 | +5.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.7 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +5.5 | +4.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.8 | -13.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.8 | -11.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.8 | -9.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -9.8 | -9.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.5 | -10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.9 | -12.1 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced with helicase C domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:162,267,074-162,318,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MDA-5, Hlcd, MDA5, IDDM19 |
| Gene groups (HGNC) | Caspase recruitment domain containing; RIG-I RNA sensor family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 27 pathways, smallest: NF-kB activation through FADD/RIP-1 pathway mediated by caspase-8 and -10; TRAF3-dependent IRF activation pathway; TRAF6 mediated IRF7 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYX4](https://www.uniprot.org/uniprotkb/Q9BYX4) (Interferon-induced helicase C domain-containing protein 1):

> Innate immune receptor which acts as a cytoplasmic sensor of viral nucleic acids and plays a major role in sensing viral infection and in the activation of a cascade of antiviral responses including the induction of type I interferons and pro-inflammatory cytokines. Its ligands include mRNA lacking 2'-O-methylation at their 5' cap and long double-stranded RNAs (>1 kb in length). Upon ligand binding it associates with mitochondria antiviral signaling protein (MAVS/IPS1) which activates the …

**Summary**, from NCBI Gene [64135](https://www.ncbi.nlm.nih.gov/gene/64135):

> IFIH1 encodes MDA5 which is an intracellular sensor of viral RNA that triggers the innate immune response. Sensing RNA length and secondary structure, MDA5 binds dsRNA oligonucleotides with a modified DExD/H-box helicase core and a C-terminal domain, thus leading to a proinflammatory response that includes interferons. It has been shown that Coronaviruses (CoVs) as well as various other virus families, are capable of evading the MDA5-dependent interferon response, thus impeding the activation …

**Accessions** — [HGNC:18873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18873) · Entrez [64135](https://www.ncbi.nlm.nih.gov/gene/64135) · UniProt [Q9BYX4](https://www.uniprot.org/uniprotkb/Q9BYX4) · Ensembl [ENSG00000115267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115267)

## Data

Gene col 3645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3645); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3645]; `tensor/DDL_lfc|DDL_z.npy` [3645]; `embed/gene_vectors.npy` [3645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3645 or target_col == 3645). Every well: [[IFIH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFIH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
