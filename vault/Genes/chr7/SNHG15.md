---
symbol: "SNHG15"
type: "gene"
col: 13879
ensembl_id: "ENSG00000232956"
name: "small nucleolar RNA host gene 15"
location: "7p13"
module: 33
arm: "+"
pooled_cpm: 20.57
n_lines_expressing: 47
n_dd_up: 30
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SNHG15

*small nucleolar RNA host gene 15* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.50× (z +11.1, q 8e-26, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.523× (z -5.6, q 1e-05, down in 17 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.631× (z -4.0, q 0.012, down in 24 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG17]] (+0.81, fdr 7e-06), [[MRPS26]] (+0.67, fdr 7e-06), [[RIOK1]] (+0.66, fdr 7e-06); moves opposite to [[HADHA]] (-0.62, fdr 1e-05), [[ACTR2]] (-0.61, fdr 1e-05), [[PRKAR1A]] (-0.58, fdr 3e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRFN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.50×** | +11.1 | 8e-26 | 38/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.79×** | +8.7 | 7e-16 | 39/41 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +7.5 | 9e-12 | 31/43 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.79×** | +7.3 | 5e-11 | 28/44 (SHP-77, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.48×** | +7.0 | 3e-10 | 31/42 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.20×** | +6.9 | 3e-10 | 35/44 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.98×** | +6.0 | 1e-07 | 28/43 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.33×** | +5.6 | 2e-06 | 32/44 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.83×** | +5.3 | 6e-06 | 24/44 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.83×** | +5.1 | 2e-05 | 27/44 (LoVo, H4, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +5.1 | 2e-05 | 29/44 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.68×** | +4.6 | 2e-04 | 24/44 (NCI-H460, SHP-77, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.66×** | +4.5 | 4e-04 | 23/44 (Hs 766T, SW1417, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +4.4 | 4e-04 | 12/45 (RKO, LoVo, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **2.47×** | +4.2 | 0.001 | 21/40 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.43×** | +4.1 | 0.001 | 27/43 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.32×** | +3.9 | 0.003 | 21/43 (SW1417, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.92×** | +3.9 | 0.003 | 25/43 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.005 | 23/45 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.008 | 20/44 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +3.6 | 0.008 | 18/43 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.008 | 19/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.16×** | +3.6 | 0.008 | 17/42 (SW1417, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.05×** | +3.3 | 0.019 | 12/43 (SW1417, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.019 | 16/42 (SHP-77, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -5.6 | 1e-05 | 17/29 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.607×** | -4.5 | 0.002 | 22/38 (C-33 A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.631×** | -4.0 | 0.012 | 24/43 (LoVo, A-427, …) | rises with dose | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.679×** | -3.5 | 0.063 | 16/44 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.684×** | -3.4 | 0.065 | 20/44 (A549, SW1417, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -3.3 | 0.081 | 20/44 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.714× | -3.1 | 0.18 | 17/44 (MIA PaCa-2, LS 180, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 28.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.17× (z +8.5) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -12.8) |
| [[LoVo (line)]] | wt | 22.1 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.97× (z +10.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.36× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 24.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.70× (z +9.5) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[PANC-1 (line)]] | alt | 21.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.25× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 42.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 10.3× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 28.4 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.47× (z +9.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +8.9) | — |
| [[A498 (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 7.10 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.6× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.73× (z +8.8) | — |
| [[KATO III (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.66× (z +9.7) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 25.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.60× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.47× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -9.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.72× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.46× (z +9.5) | — |
| [[A-172 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG17]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 | same gene group |
| [[MRPS26]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CTU1]] | +0.66 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RPL22L1]] ⚠ | +0.66 | +0.44 / +0.71 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BRIX1]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[PDCD2L]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NLE1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[WDR43]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NOP16]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ZNF74]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DDX55]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HADHA]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ACTR2]] | -0.61 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.58 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[SERINC3]] | -0.55 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[ITM2B]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[NDUFS1]] | -0.53 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[PRKACA]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[RO60]] | -0.51 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[SCRN1]] | -0.50 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[NEMP1]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[RAB1B]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[GNS]] | -0.50 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRFN4]] | B | LRFN4 activity raises SNHG15's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without LRFN4 | 0.053 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[CENPV]] | B | CENPV activity raises SNHG15's level | lines that do not express CENPV (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without CENPV | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.9, -45.6); signed map (-24.6, -19.0). **Vector** length 90.9, 24.8% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +3.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.6 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 15 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p13 — chr7:44,983,019-44,986,961 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ38860, MYO1GUT, Linc-Myo1g; previously C7orf40 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [285958](https://www.ncbi.nlm.nih.gov/gene/285958):

> This gene represents a snoRNA host gene that produces a short-lived long non-coding RNA. This non-coding RNA is upregulated in tumor cells and may contribute to cell proliferation by acting as a sponge for microRNAs. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:27797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27797) · Entrez [285958](https://www.ncbi.nlm.nih.gov/gene/285958) · Ensembl [ENSG00000232956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232956)

## Data

Gene col 13879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13879); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13879]; `tensor/DDL_lfc|DDL_z.npy` [13879]; `embed/gene_vectors.npy` [13879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13879 or target_col == 13879). Every well: [[SNHG15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
