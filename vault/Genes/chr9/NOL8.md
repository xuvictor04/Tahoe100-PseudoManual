---
symbol: "NOL8"
type: "gene"
col: 12509
ensembl_id: "ENSG00000198000"
name: "nucleolar protein 8"
location: "9q22.31"
module: 11
arm: "+"
pooled_cpm: 66.85
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NOL8

*nucleolar protein 8* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.78× (z +30.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.784× (z -7.2, q 4e-10, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-1 0.139×, SW48 0.242×, NCI-H460 0.415×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.138×, RKO 0.280×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.578×, RKO 0.537×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL7L1]] (+0.83, fdr 7e-06), [[REXO4]] (+0.80, fdr 7e-06), [[ESF1]] (+0.76, fdr 7e-06); moves opposite to [[NPTN]] (-0.66, fdr 7e-06), [[TWSG1]] (-0.64, fdr 9e-06), [[UBTD1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRABP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +30.1 | 0e+00 | 48/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.49×** | +27.3 | 0e+00 | 48/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +17.6 | 0e+00 | 48/48 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +13.6 | 3e-40 | 45/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +10.7 | 9e-25 | 41/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +9.1 | 1e-17 | 35/47 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +8.5 | 2e-15 | 35/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +7.4 | 8e-12 | 38/48 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +7.3 | 2e-11 | 26/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +7.1 | 6e-11 | 27/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +7.0 | 1e-10 | 30/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +6.7 | 1e-09 | 34/49 (LoVo, RKO, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +5.9 | 1e-07 | 29/48 (NCI-H1792, J82, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.4 | 2e-06 | 26/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +5.4 | 3e-06 | 26/48 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +5.2 | 8e-06 | 29/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +4.7 | 9e-05 | 23/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12509.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-1 0.139×, SW48 0.242×, NCI-H460 0.415×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.138×, RKO 0.280×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 0.578×, RKO 0.537×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -7.2 | 4e-10 | 27/48 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.852× | -4.7 | 9e-04 | 22/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.836× | -3.9 | 0.017 | 22/48 (Hs 766T, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.1 | 0.30 | 10/48 (C-33 A, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +23.6) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 60.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +21.2) | — |
| [[RKO (line)]] | wt | 117 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 59.9 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +17.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 104 | 5 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.45× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 42.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +21.4) | — |
| [[SW480 (line)]] | alt | 101 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +13.5) | — |
| [[A-427 (line)]] | wt | 51.4 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +12.9) | — |
| [[A498 (line)]] | wt | 111 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.7) |
| [[COLO 205 (line)]] | alt | 66.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 53.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.1) | — |
| [[J82 (line)]] | alt | 113 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +22.5) | — |
| [[LoVo (line)]] | wt | 61.9 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 48.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +16.4) | — |
| [[SNU-423 (line)]] | alt | 87.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +18.6) | — |
| [[C32 (line)]] | wt | 51.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.5) | — |
| [[HEC-1-A (line)]] | alt | 76.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 36.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 46.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 51.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +11.7) | [[Lonafarnib (drug)]] 5 µM 0.0928× (z -9.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 81.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +18.2) | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +19.5) | — |
| [[NCI-H23 (line)]] | alt | 77.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +21.7) | — |
| [[Panc 03.27 (line)]] | alt | 64.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.40× (z +15.3) | [[Lonafarnib (drug)]] 5 µM 0.194× (z -8.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 66.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +16.0) | — |
| [[SK-MEL-2 (line)]] | alt | 65.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.6) | — |
| [[A549 (line)]] | wt | 62.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +17.0) | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +12.3) | — |
| [[H4 (line)]] | wt | 45.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 70.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 84.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 61.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 29.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.2) | — |
| [[PANC-1 (line)]] | alt | 70.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 67.0 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 69.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SW 900 (line)]] | alt | 32.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +12.5) | — |
| [[SW48 (line)]] | wt | 75.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 74.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 89.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL7L1]] | +0.83 | +0.84 / +0.81 | both halves | 7e-06 |  |
| [[REXO4]] | +0.80 | +0.82 / +0.84 | both halves | 7e-06 |  |
| [[ESF1]] | +0.76 | +0.86 / +0.71 | both halves | 7e-06 | STRING 517 |
| [[CEBPZ]] | +0.74 | +0.83 / +0.71 | both halves | 7e-06 | STRING 543 |
| [[UTP14A]] | +0.74 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.73 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[RAD50]] | +0.72 | +0.82 / +0.63 | both halves | 7e-06 |  |
| [[ICE2]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.71 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[LDAH]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.70 | +0.85 / +0.58 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.66 | -0.72 / -0.59 | both halves | 7e-06 |  |
| [[TWSG1]] | -0.64 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[UBTD1]] | -0.64 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[BSG]] | -0.63 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[TMED4]] | -0.62 | -0.67 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRABP2]] | B | CRABP2 activity weakens NOL8's drug response | lines that do not express CRABP2 (24) vs lines expressing it (24) | the lines without CRABP2 respond 1.17× as strongly (z diff -0.82); strongest at Homoharringtonine 0.05 µM: 1.76x vs 1.40x (z diff -1.9) | 0.071 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.4, 1.0); signed map (-1.4, -21.6). **Vector** length 128, 38.2% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.4 | +27.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.2 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +30.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +5.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -5.1 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:92,297,358-92,325,636 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20736, Nop132; previously C9orf34 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76FK4](https://www.uniprot.org/uniprotkb/Q76FK4) (Nucleolar protein 8):

> Plays an essential role in the survival of diffuse-type gastric cancer cells. Acts as a nucleolar anchoring protein for DDX47. May be involved in regulation of gene expression at the post-transcriptional level or in ribosome biogenesis in cancer cells.

**Summary**, from NCBI Gene [55035](https://www.ncbi.nlm.nih.gov/gene/55035):

> NOL8 binds Ras-related GTP-binding proteins (see MIM 608267) and plays a role in cell growth (Sekiguchi et al., 2004 [PubMed 14660641]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23387) · Entrez [55035](https://www.ncbi.nlm.nih.gov/gene/55035) · UniProt [Q76FK4](https://www.uniprot.org/uniprotkb/Q76FK4) · Ensembl [ENSG00000198000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198000)

## Data

Gene col 12509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12509); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12509]; `tensor/DDL_lfc|DDL_z.npy` [12509]; `embed/gene_vectors.npy` [12509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12509 or target_col == 12509). Every well: [[NOL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
