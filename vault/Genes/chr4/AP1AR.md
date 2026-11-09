---
symbol: "AP1AR"
type: "gene"
col: 6206
ensembl_id: "ENSG00000138660"
name: "adaptor related protein complex 1 associated regulatory protein"
location: "4q25"
module: 63
arm: "+"
pooled_cpm: 52.88
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# AP1AR

*adaptor related protein complex 1 associated regulatory protein* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +21.3, q 0e+00, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.353×, HT-29 0.434×; ⚠ toxic; cell-cycle shift, explains ~64% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C32 0.0695×); [[Digitoxin (drug)]] 5 µM in 1 line (SW1417 0.326×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.285×); [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0898×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEA1]] (+0.58, fdr 1e-05), [[ZFAND1]] (+0.57, fdr 1e-05), [[ADSS2]] (+0.56, fdr 2e-05); moves opposite to [[MED27]] (-0.50, fdr 3e-05), [[C4orf3]] (-0.47, fdr 6e-05), [[RABGEF1P1]] (-0.47, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC38A1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +21.3 | 0e+00 | 44/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +15.1 | 0e+00 | 43/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +10.6 | 5e-24 | 42/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.7 | 5e-20 | 32/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +8.9 | 5e-17 | 35/48 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.50×** | +8.5 | 2e-15 | 38/48 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.9 | 2e-13 | 34/46 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +7.7 | 9e-13 | 31/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +7.3 | 2e-11 | 30/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.9 | 2e-07 | 19/40 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 1e-05 | 23/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 2e-05 | 20/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 2e-05 | 23/48 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.9 | 4e-05 | 16/48 (SNU-1, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +4.5 | 2e-04 | 21/44 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 16/48 (H4, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +4.1 | 0.001 | 12/48 (A-172, A-427, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.002 | 15/47 (HT-29, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.006 | 13/47 (SNU-1, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.013 | 10/48 (SNU-1, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.5 | 0.013 | 6/48 (Hs 766T, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6206.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.353×, HT-29 0.434×; ⚠ toxic; cell-cycle shift, explains ~64% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C32 0.0695×); [[Digitoxin (drug)]] 5 µM in 1 line (SW1417 0.326×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.285×); [[Brimonidine (drug)]] 0.5 µM in 1 line (NCI-H661 0.0898×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.6 | 0.22 | 16/48 (A-427, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.893× | -3.3 | 0.25 | 11/48 (SW480, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 73.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 35.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 72.4 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.11× (z +11.5) | — |
| [[C32 (line)]] | wt | 23.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +14.3) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0695× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 56.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 43.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.5) | — |
| [[RKO (line)]] | wt | 113 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A549 (line)]] | wt | 30.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +14.8) | — |
| [[COLO 205 (line)]] | alt | 92.3 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.29× (z +9.2) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 68.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 21.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.6) | — |
| [[J82 (line)]] | alt | 37.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.5) | — |
| [[LoVo (line)]] | wt | 74.8 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.14× (z +12.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +17.3) | — |
| [[NCI-H23 (line)]] | alt | 51.4 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.92× (z +9.4) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 55.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 40.3 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.01× (z +9.7) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 46.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.2) | — |
| [[H4 (line)]] | wt | 50.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.434× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~64% of this change |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 42.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.4) | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0898× (z -9.1) |
| [[SW 900 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[SW48 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA1]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZFAND1]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ADSS2]] | +0.56 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[LARS1]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[RSL24D1]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CCDC25]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SBDSP1]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[NARS1]] | +0.51 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[TARS1]] | +0.51 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[XPOT]] | +0.51 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[NIBAN1]] | +0.50 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[CEBPG]] | +0.49 | +0.62 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED27]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[C4orf3]] | -0.47 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[RABGEF1P1]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MARK4]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ST3GAL2]] | -0.46 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[AREL1]] | -0.45 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[KDM2A]] | -0.44 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[LUZP1]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ZNF175]] | -0.44 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[AKAP8L]] | -0.44 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[ABL1]] | -0.43 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[CHMP1A]] | -0.43 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC38A1]] | C | SLC38A1 activity raises AP1AR's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.4, 46.4); signed map (-15.6, 23.2). **Vector** length 108, 27.7% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +10.1 | +15.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.8 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +7.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.0 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.9 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | -3.6 | +1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | -3.5 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 associated regulatory protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:112,231,740-112,273,110 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO0971, 2C18, gamma-BAR; previously C4orf16 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q63HQ0](https://www.uniprot.org/uniprotkb/Q63HQ0) (AP-1 complex-associated regulatory protein):

> Necessary for adaptor protein complex 1 (AP-1)-dependent transport between the trans-Golgi network and endosomes. Regulates the membrane association of AP1G1/gamma1-adaptin, one of the subunits of the AP-1 adaptor complex. The direct interaction with AP1G1/gamma1-adaptin attenuates the release of the AP-1 complex from membranes. Regulates endosomal membrane traffic via association with AP-1 and KIF5B thus linking kinesin-based plus-end-directed microtubular transport to AP-1-dependent membrane …

**Summary**, from NCBI Gene [55435](https://www.ncbi.nlm.nih.gov/gene/55435):

> Enables AP-1 adaptor complex binding activity and kinesin binding activity. Involved in negative regulation of receptor recycling and vesicle targeting, trans-Golgi to endosome. Acts upstream of or within negative regulation of substrate adhesion-dependent cell spreading. Located in Golgi apparatus and transport vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28808) · Entrez [55435](https://www.ncbi.nlm.nih.gov/gene/55435) · UniProt [Q63HQ0](https://www.uniprot.org/uniprotkb/Q63HQ0) · Ensembl [ENSG00000138660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138660)

## Data

Gene col 6206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6206); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6206]; `tensor/DDL_lfc|DDL_z.npy` [6206]; `embed/gene_vectors.npy` [6206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6206 or target_col == 6206). Every well: [[AP1AR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1AR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
