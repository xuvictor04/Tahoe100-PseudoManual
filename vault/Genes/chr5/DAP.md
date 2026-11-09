---
symbol: "DAP"
type: "gene"
col: 3421
ensembl_id: "ENSG00000112977"
name: "death associated protein"
location: "5p15.2"
module: 42
arm: "+"
pooled_cpm: 118.5
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# DAP

*death associated protein* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.47× (z +6.3, q 2e-07, up in 30 of 41 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 3.26×, SNU-423 3.11×, SNU-1 4.50×, LOX-IMVI 2.67×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LOX-IMVI 3.88×, SNU-423 2.90×, A-172 2.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 3.00×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.529× (z -15.4, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALU]] (+0.73, fdr 7e-06), [[SRPRA]] (+0.72, fdr 7e-06), [[SSR1]] (+0.67, fdr 7e-06); moves opposite to [[TLK2]] (-0.59, fdr 2e-05), [[DYNC1LI1]] (-0.58, fdr 3e-05), [[FDX2]] (-0.55, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3421.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-172 3.26×, SNU-423 3.11×, SNU-1 4.50×, LOX-IMVI 2.67×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LOX-IMVI 3.88×, SNU-423 2.90×, A-172 2.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 3.00×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.3 | 2e-07 | 30/41 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.8 | 2e-06 | 35/49 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +4.7 | 4e-04 | 27/45 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.529×** | -15.4 | 0e+00 | 44/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -10.8 | 6e-25 | 38/49 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -9.5 | 5e-19 | 39/48 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -7.4 | 2e-11 | 40/49 (LoVo, LS 180, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -7.3 | 3e-11 | 42/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -7.1 | 9e-11 | 34/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.745×** | -7.1 | 9e-11 | 35/48 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.663×** | -7.0 | 2e-10 | 36/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -6.8 | 5e-10 | 38/48 (MIA PaCa-2, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.685×** | -6.5 | 6e-09 | 33/48 (AsPC-1, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -6.2 | 2e-08 | 30/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.704×** | -5.8 | 3e-07 | 32/48 (A-427, RKO, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.731×** | -5.4 | 3e-06 | 29/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -5.3 | 5e-06 | 34/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.735×** | -5.3 | 5e-06 | 31/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -4.9 | 4e-05 | 29/48 (BT-474, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.768×** | -4.5 | 2e-04 | 28/48 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.765×** | -4.3 | 4e-04 | 26/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.837× | -4.3 | 4e-04 | 22/48 (AsPC-1, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 209 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -12.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.6) |
| [[HS-578T (line)]] | alt | 142 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 159 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.1) |
| [[A549 (line)]] | wt | 89.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -18.3) |
| [[KATO III (line)]] | alt | 162 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 144 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -9.2) |
| [[HOP62 (line)]] | alt | 155 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.511× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 228 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 80.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.7) |
| [[RKO (line)]] | wt | 80.3 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.236× (z -12.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.517× (z -8.6) |
| [[SNU-423 (line)]] | alt | 96.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 102 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.6) |
| [[A-172 (line)]] | wt | 86.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 92.2 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -12.6) |
| [[A498 (line)]] | wt | 186 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -16.6) |
| [[C32 (line)]] | wt | 56.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -8.7) |
| [[H4 (line)]] | wt | 187 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -12.4) |
| [[HT-29 (line)]] | alt | 232 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 50.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 68.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 131 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.7) |
| [[PANC-1 (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -11.9) |
| [[SW1417 (line)]] | alt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -17.1) |
| [[BT-474 (line)]] | alt | 84.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.324× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 78.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.5) |
| [[Hs 766T (line)]] | wt | 197 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.9) |
| [[J82 (line)]] | alt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -8.9) |
| [[LS 180 (line)]] | wt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.5) |
| [[SHP-77 (line)]] | alt | 121 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.2) |
| [[SNU-1 (line)]] | wt | 63.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -8.9) |
| [[AN3 CA (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 68.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALU]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[SRPRA]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SSR1]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[HDLBP]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[SEC22B]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[COPG1]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.63 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.62 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[P4HB]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TMED3]] | +0.62 | +0.68 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLK2]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[DYNC1LI1]] | -0.58 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[FDX2]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[C1orf131]] | -0.55 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[COIL]] | -0.55 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[RDH14]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[HOXA7]] | -0.55 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[ALKBH4]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[MRPL32]] | -0.53 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[DHX36]] | -0.52 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[RNF8]] | -0.52 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[TBCC]] | -0.52 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DAP's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[YKT6]] | C | YKT6's natural level strengthens DAP's drug response | YKT6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.10; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.8, -30.0); signed map (-55.6, 8.9). **Vector** length 132, 44.3% of its response variance represented; |z| ≥ 3 in 1,256 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.52 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.52 to 9); *IRE1alpha activates chaperones* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.2 | -4.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.4 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -7.3 |

## What is on record

|  |  |
|---|---|
| Name | death associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,679,230-10,761,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAP1 |
| Hallmark sets | APOPTOSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P51397](https://www.uniprot.org/uniprotkb/P51397) (Death-associated protein 1):

> Ribosome-binding protein involved in ribosome hibernation, a process during which ribosomes are stabilized in an inactive state and preserved from proteasomal degradation (By similarity). Acts via its association with eiF5a (EIF5A and EIF5A2) at the polypeptide exit tunnel of the ribosome, preventing mRNA translation (By similarity). Involved in ribosome hibernation in the mature oocyte by preventing mRNA translation, leading to ribosome inactivation (By similarity). Ribosomes, which are …

**Summary**, from NCBI Gene [1611](https://www.ncbi.nlm.nih.gov/gene/1611):

> This gene encodes a basic, proline-rich, 15-kD protein. The protein acts as a positive mediator of programmed cell death that is induced by interferon-gamma. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:2672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2672) · Entrez [1611](https://www.ncbi.nlm.nih.gov/gene/1611) · UniProt [P51397](https://www.uniprot.org/uniprotkb/P51397) · Ensembl [ENSG00000112977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112977)

## Data

Gene col 3421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3421); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3421]; `tensor/DDL_lfc|DDL_z.npy` [3421]; `embed/gene_vectors.npy` [3421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3421 or target_col == 3421). Every well: [[DAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
