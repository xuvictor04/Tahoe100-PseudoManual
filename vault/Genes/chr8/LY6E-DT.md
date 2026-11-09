---
symbol: "LY6E-DT"
type: "gene"
col: 14493
ensembl_id: "ENSG00000247317"
name: "LY6E divergent transcript"
location: "8q24.3"
module: 32
arm: "+"
pooled_cpm: 4.69
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 31
n_dd_up_clean: 12
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LY6E-DT

*LY6E divergent transcript* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.15× (z +5.9, q 3e-06, up in 2 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 5 µM: 1.57× (z +3.8, q 0.021, up in 11 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.271× (z -10.4, q 2e-22, down in 33 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO39]] (+0.69, fdr 1e-05), [[TRIM34]] (+0.64, fdr 1e-05), [[CCDC194]] (+0.64, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 5 go from it, the strongest it → [[APOBEC3F]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +5.9 | 3e-06 | 2/9 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +4.0 | 0.017 | 2/17 (J82, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.021 | 11/41 (NCI-H23, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.46×** | +3.8 | 0.021 | 8/40 (AsPC-1, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.032 | 10/40 (Hs 766T, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.032 | 10/38 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.032 | 7/40 (C32, NCI-H2347, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.032 | 11/30 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.032 | 11/35 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.044 | 13/40 (A-427, Hs 766T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.044 | 13/36 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.045 | 5/40 (SW480, SNU-423, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.046 | 8/40 (NCI-H23, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +3.3 | 0.046 | 1/14 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.065 | 9/40 (NCI-H23, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.271×** | -10.4 | 2e-22 | 33/41 (BT-474, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.333×** | -8.7 | 9e-16 | 28/39 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.369×** | -7.9 | 6e-13 | 25/38 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.425×** | -6.8 | 2e-09 | 22/29 (BT-474, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.419×** | -6.6 | 4e-09 | 24/36 (A498, BT-474, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.578×** | -6.1 | 8e-08 | 24/33 (A498, BT-474, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.448×** | -6.1 | 8e-08 | 21/26 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.478×** | -5.8 | 4e-07 | 21/38 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.480×** | -5.8 | 4e-07 | 24/40 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -5.5 | 2e-06 | 17/31 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.513×** | -5.0 | 3e-05 | 20/36 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.551×** | -4.7 | 1e-04 | 20/38 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.553×** | -4.7 | 1e-04 | 18/41 (BT-474, AsPC-1, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.584×** | -4.2 | 9e-04 | 18/39 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.538×** | -4.1 | 0.001 | 15/40 (SW 900, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.003 | 16/40 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.008 | 16/40 (CFPAC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.620×** | -3.6 | 0.009 | 13/39 (Panc 03.27, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.636×** | -3.4 | 0.018 | 12/38 (COLO 205, J82, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.652×** | -3.4 | 0.021 | 14/40 (MIA PaCa-2, BT-474, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.659×** | -3.3 | 0.027 | 13/37 (A498, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -15.8) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.166× (z -8.5) |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0448× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0662× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 19.8 | 0 | 5 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 9.73 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0675× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0780× (z -9.1) |
| [[A-427 (line)]] | wt | 6.75 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0586× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0803× (z -10.1) |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -10.4) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0613× (z -9.9) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.2) ⚠ cell-cycle shift, explains ~55% of this change |
| [[AsPC-1 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0465× (z -10.3) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 7.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0786× (z -8.8) |
| [[COLO 205 (line)]] | alt | 5.89 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0350× (z -8.8) |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0537× (z -9.5) |
| [[Hs 766T (line)]] | wt | 6.22 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0361× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 6.39 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0697× (z -8.8) |
| [[PANC-1 (line)]] | alt | 2.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0380× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 5.68 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0468× (z -9.1) |
| [[SW1417 (line)]] | alt | 5.97 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0707× (z -9.3) |
| [[SW480 (line)]] | alt | 1.75 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0672× (z -8.9) |
| [[A549 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO39]] | +0.69 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[TRIM34]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CCDC194]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[IFI44L]] | +0.62 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[IFIT3]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TRANK1]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[IFIT1]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[IFIT2]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[RSAD2]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SAMHD1]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[NRIR]] | +0.61 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[OAS2]] | +0.61 | +0.43 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers LY6E-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[IFI44L]] | B | IFI44L activity raises LY6E-DT's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.69× lower at baseline in the lines without IFI44L | 0.069 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[SERPINB9P1]] | B | SERPINB9P1 activity raises LY6E-DT's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without SERPINB9P1 | 0.084 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9 |
| [[FBXO39]] | B | FBXO39 activity raises LY6E-DT's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without FBXO39 | 0.090 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[BST2]] | B | BST2 activity raises LY6E-DT's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without BST2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[MAP2K2]] | B | MAP2K2 activity lowers LY6E-DT's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOBEC3F]] | B | LY6E-DT activity raises APOBEC3F's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without LY6E-DT | 0.014 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |
| [[PARP12]] | B | LY6E-DT activity raises PARP12's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 2.88× lower at baseline in the lines without LY6E-DT | 0.017 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |
| [[LY6E]] | B | LY6E-DT activity raises LY6E's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 3.25× lower at baseline in the lines without LY6E-DT | 0.041 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |
| [[ZNF630]] | B | LY6E-DT activity raises ZNF630's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without LY6E-DT | 0.044 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |
| [[UNC93B1]] | B | LY6E-DT activity raises UNC93B1's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without LY6E-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 56.4); signed map (66.7, 31.2). **Vector** length 67.8, 12.7% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.51 to 56); *interferon gamma response* (hallmark, mean cos +0.51 to 60); *interferon* (control, mean cos +0.57 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.0 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +3.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.5 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.4 | +3.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -5.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | LY6E divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.3 — chr8:142,981,738-143,018,447 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LOC100133669 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53728) · Entrez [100133669](https://www.ncbi.nlm.nih.gov/gene/100133669) · Ensembl [ENSG00000247317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247317)

## Data

Gene col 14493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14493); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14493]; `tensor/DDL_lfc|DDL_z.npy` [14493]; `embed/gene_vectors.npy` [14493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14493 or target_col == 14493). Every well: [[LY6E-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LY6E-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
