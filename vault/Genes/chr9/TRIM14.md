---
symbol: "TRIM14"
type: "gene"
col: 2805
ensembl_id: "ENSG00000106785"
name: "tripartite motif containing 14"
location: "9q22.33"
module: 32
arm: "+"
pooled_cpm: 53.08
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 40
n_dd_up_clean: 14
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 44
direction_downstream: 34
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# TRIM14

*tripartite motif containing 14* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.38× (z +4.4, q 0.006, up in 25 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 1.38× (z +4.2, q 0.007, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.381× (z -18.4, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPT1]] (+0.92, fdr 7e-06), [[OAS3]] (+0.91, fdr 7e-06), [[PARP9]] (+0.90, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 34 go from it, the strongest it → [[TDRD7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.4 | 0.006 | 25/45 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.007 | 21/46 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.1 | 0.007 | 20/39 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +3.9 | 0.012 | 25/47 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.012 | 22/46 (A498, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.012 | 24/46 (NCI-H2347, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.022 | 23/47 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.026 | 24/46 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.026 | 18/47 (NCI-H2347, SW 1088, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.052 | 23/47 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.052 | 22/47 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.052 | 11/47 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.065 | 20/47 (J82, COLO 205, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.072 | 13/44 (A-427, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.089 | 15/47 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.094 | 12/47 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.096 | 15/47 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 4 with an alert ⚠; shown: the 15 strongest. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.381×** | -18.4 | 0e+00 | 44/46 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.490×** | -13.6 | 2e-39 | 33/47 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.562×** | -11.0 | 1e-25 | 36/47 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.453×** | -10.7 | 2e-24 | 37/47 (NCI-H23, A549, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.455×** | -10.6 | 3e-24 | 40/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.476×** | -10.0 | 1e-21 | 35/47 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.604×** | -9.6 | 9e-20 | 36/47 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.476×** | -9.4 | 2e-19 | 41/47 (MIA PaCa-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.510×** | -9.1 | 7e-18 | 36/47 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.514×** | -9.0 | 2e-17 | 37/47 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.520×** | -8.8 | 8e-17 | 32/47 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -8.4 | 1e-15 | 34/47 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.530×** | -8.2 | 1e-14 | 35/47 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -7.6 | 1e-12 | 34/47 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.606×** | -6.7 | 6e-10 | 28/46 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 153 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0754× (z -27.0) |
| [[A549 (line)]] | wt | 113 | 0 | 18 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0612× (z -32.9) |
| [[NCI-H23 (line)]] | alt | 67.1 | 0 | 14 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -13.1) |
| [[A-172 (line)]] | wt | 158 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -17.3) |
| [[C-33 A (line)]] | alt | 115 | 0 | 13 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.259× (z -15.6) |
| [[LoVo (line)]] | wt | 62.1 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 12 | — | [[Tofacitinib (drug)]] 5 µM 0.240× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 12 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.280× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 40.6 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.6) |
| [[A498 (line)]] | wt | 103 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.3) |
| [[SNU-423 (line)]] | alt | 48.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 56.2 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.330× (z -12.7) |
| [[COLO 205 (line)]] | alt | 104 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 47.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.4) |
| [[J82 (line)]] | alt | 47.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.49× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 25.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.8) |
| [[SHP-77 (line)]] | alt | 51.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -12.9) |
| [[BT-474 (line)]] | alt | 63.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -20.0) |
| [[CFPAC-1 (line)]] | alt | 44.0 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.360× (z -12.6) |
| [[CHP-212 (line)]] | wt | 62.4 | 0 | 3 | — | [[Tofacitinib (drug)]] 0.5 µM 0.114× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 46.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -17.4) |
| [[HepG2_C3A (line)]] | wt | 50.0 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.285× (z -10.4) |
| [[Hs 766T (line)]] | wt | 47.5 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.400× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 54.4 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.341× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 76.9 | 0 | 3 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.321× (z -9.7) |
| [[PANC-1 (line)]] | alt | 29.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -25.8) |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -13.6) |
| [[SNU-1 (line)]] | wt | 50.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.0) |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 45.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.8) |
| [[SW1417 (line)]] | alt | 60.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.1) |
| [[SW48 (line)]] | wt | 36.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.4) |
| [[SW480 (line)]] | alt | 26.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -13.2) |
| [[A-427 (line)]] | wt | 22.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.409× (z -9.0) |
| [[HOP62 (line)]] | alt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.8) |
| [[KATO III (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.5) |
| [[LS 180 (line)]] | wt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +11.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPT1]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS3]] | +0.91 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 467 |
| [[PARP9]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SAMHD1]] | +0.88 | +0.80 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 423 |
| [[OAS2]] | +0.88 | +0.79 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 454 |
| [[EIF2AK2]] | +0.87 | +0.79 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[CMPK2]] | +0.87 | +0.80 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[MX1]] | +0.86 | +0.76 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PARP12]] | +0.86 | +0.80 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PLSCR1]] | +0.86 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 557 |
| [[STAT1]] | +0.85 | +0.78 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 662 |
| [[OAS1]] | +0.84 | +0.81 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 474 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 25, C 19. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises TRIM14's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.05× lower at baseline in the lines without OAS2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[CMPK2]] | B | CMPK2 activity raises TRIM14's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without CMPK2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[PLSCR1]] | B | PLSCR1 activity raises TRIM14's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without PLSCR1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises TRIM14's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without OAS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises TRIM14's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without PARP9 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity strengthens TRIM14's drug response | lines that do not express OAS2 (13) vs lines expressing it (34) | the lines without OAS2 respond 0.42× as strongly (z diff +2.21); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.68x vs 0.37x (z diff +3.5) | 0.014 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[OAS3]] | B | OAS3 activity raises TRIM14's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without OAS3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[SAMD9]] | B | SAMD9 activity raises TRIM14's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without SAMD9 | 0.020 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[IFI6]] | B | IFI6 activity raises TRIM14's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.98× lower at baseline in the lines without IFI6 | 0.029 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity strengthens TRIM14's drug response | lines that do not express PLSCR1 (8) vs lines expressing it (39) | the lines without PLSCR1 respond 0.29× as strongly (z diff +2.91); strongest at Selinexor 5 µM: 0.85x vs 0.56x (z diff +4.7) | 0.033 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFI6]] | B | IFI6 activity strengthens TRIM14's drug response | lines that do not express IFI6 (13) vs lines expressing it (34) | the lines without IFI6 respond 0.32× as strongly (z diff +2.98); strongest at Selinexor 5 µM: 0.79x vs 0.54x (z diff +4.3) | 0.033 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[BATF2]] | B | BATF2 activity raises TRIM14's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without BATF2 | 0.034 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 0, C 34. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TDRD7]] | C | TRIM14's natural level strengthens TDRD7's drug response | TRIM14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.66; direction not clear | 3e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | TRIM14's natural level strengthens TRIM25's drug response | TRIM14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.72; direction not clear | 9e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | TRIM14's natural level strengthens USP18's drug response | TRIM14's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.63; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | TRIM14's natural level strengthens HELZ2's drug response | TRIM14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.82; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | TRIM14's natural level strengthens PML's drug response | TRIM14's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.61; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PNPT1]] | C | TRIM14's natural level strengthens PNPT1's drug response | TRIM14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.82; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | TRIM14's natural level strengthens PARP12's drug response | TRIM14's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.68; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[UBE2L6]] | C | TRIM14's natural level strengthens UBE2L6's drug response | TRIM14's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.33; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFI35]] | C | TRIM14's natural level strengthens IFI35's drug response | TRIM14's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.60; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | TRIM14's natural level strengthens ADAR's drug response | TRIM14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.68; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OAS3]] | C | TRIM14's natural level strengthens OAS3's drug response | TRIM14's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.72; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HERC6]] | C | TRIM14's natural level strengthens HERC6's drug response | TRIM14's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.60; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 54.7); signed map (65.3, 32.7). **Vector** length 133, 47.3% of its response variance represented; |z| ≥ 3 in 1,490 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.79 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.77 to 27); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.77 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.3 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | -4.4 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.3 | +3.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +4.2 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.4 | -13.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.8 | -11.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.5 | -10.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.5 | -10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.2 | -9.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.6 | -10.0 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:98,069,275-98,119,222 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0129 |
| Gene groups (HGNC) | Tripartite motif family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14142](https://www.uniprot.org/uniprotkb/Q14142) (Tripartite motif-containing protein 14):

> Plays an essential role in the innate immune defense against viruses and bacteria. Promotes the 'Lys-48'-linked ubiquitination and subsequent degradation of hepatitis C virus NS5A leading to the inhibition of viral replication. Also plays a role in the inhibition of ebolavirus infection by enhancing IFN-beta and NF-kappa-B activation after binding to the viral protein NP. Facilitates the type I IFN response by interacting with MAVS at the outer mitochondria membrane and thereby recruiting …

**Summary**, from NCBI Gene [9830](https://www.ncbi.nlm.nih.gov/gene/9830):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic bodies and its function has not been determined. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:16283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16283) · Entrez [9830](https://www.ncbi.nlm.nih.gov/gene/9830) · UniProt [Q14142](https://www.uniprot.org/uniprotkb/Q14142) · Ensembl [ENSG00000106785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106785)

## Data

Gene col 2805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2805); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2805]; `tensor/DDL_lfc|DDL_z.npy` [2805]; `embed/gene_vectors.npy` [2805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2805 or target_col == 2805). Every well: [[TRIM14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
