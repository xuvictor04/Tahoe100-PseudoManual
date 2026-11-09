---
symbol: "MIEF1"
type: "gene"
col: 1930
ensembl_id: "ENSG00000100335"
name: "mitochondrial elongation factor 1"
location: "22q13.1"
module: 119
arm: "+"
pooled_cpm: 26.63
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# MIEF1

*mitochondrial elongation factor 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.75× (z +14.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.568× (z -10.3, q 5e-22, down in 32 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Thymopentin (drug)]] 5 µM: 0.803× (z -3.8, q 0.018, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 0.0543×, PANC-1 0.208×, NCI-H2030 0.151×, RKO 0.216×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.199×, NCI-H2030 0.199×, SHP-77 0.217×, HCT15 0.172×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.179×, A549 0.123×, SW48 0.157×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0853×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM11]] (+0.74, fdr 7e-06), [[NCBP2AS2]] (+0.72, fdr 7e-06), [[ALKBH4]] (+0.72, fdr 9e-06); moves opposite to [[CHP1]] (-0.56, fdr 9e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.75×** | +14.8 | 0e+00 | 46/48 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +14.4 | 2e-44 | 42/46 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +12.6 | 5e-34 | 45/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.15×** | +10.9 | 2e-25 | 38/47 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +8.3 | 8e-15 | 34/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.92×** | +6.2 | 5e-08 | 30/48 (NCI-H2030, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +5.9 | 2e-07 | 28/48 (A549, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 4e-07 | 26/47 (Hs 766T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.5 | 3e-06 | 22/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +5.1 | 2e-05 | 23/48 (PANC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.70×** | +5.0 | 2e-05 | 20/47 (NCI-H1573, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +4.4 | 5e-04 | 18/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 9e-04 | 15/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.18× | +4.2 | 0.001 | 15/48 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.25×** | +4.1 | 0.002 | 21/45 (HOP62, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.004 | 16/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.010 | 10/48 (LS 180, NCI-H1573, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.011 | 8/48 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.4 | 0.019 | 12/48 (HS-578T, A549, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.025 | 9/48 (SK-MEL-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1930.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 0.0543×, PANC-1 0.208×, NCI-H2030 0.151×, RKO 0.216×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.199×, NCI-H2030 0.199×, SHP-77 0.217×, HCT15 0.172×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2030 0.179×, A549 0.123×, SW48 0.157×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0853×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.568×** | -10.3 | 5e-22 | 32/45 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.595×** | -9.1 | 4e-17 | 21/38 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.709×** | -5.8 | 1e-06 | 23/42 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymopentin (drug)]] 5 µM |  | **0.803×** | -3.8 | 0.018 | 16/47 (A-172, RKO, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.3 | 0.12 | 3/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.18× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -15.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.98× (z +9.0) | [[Lonafarnib (drug)]] 5 µM 0.155× (z -9.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 30.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.16× (z +8.9) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.0543× (z -23.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.51× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 30.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -16.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 54.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -12.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0853× (z -9.5) |
| [[BT-474 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -9.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.65× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 28.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.76× (z +12.3) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -8.9) ⚠ cell-cycle shift, explains ~97% of this change |
| [[RKO (line)]] | wt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -14.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11]] | +0.74 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[NCBP2AS2]] | +0.72 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.72 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[BFAR]] | +0.69 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[TRMT10C]] | +0.68 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[YRDC]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[AKAP8]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[POLR3A]] | +0.67 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[C1orf109]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[CTU1]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[RPUSD2]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[METTL13]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHP1]] | -0.56 | -0.36 / -0.61 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.9, -8.8); signed map (-10.9, -10.9). **Vector** length 105, 24.7% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +12.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +14.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +14.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +8.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +5.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.9 | -10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial elongation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,499,432-39,518,132 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20232, MiD51, L0R8F8, D3A; previously SMCR7L |
| Reactome | 3 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [L0R8F8](https://www.uniprot.org/uniprotkb/L0R8F8) (Mitochondrial ribosome and complex I assembly factor AltMIEF1):

> Assembly factor involved in the biogenesis of the mitochondrial-specific ribosomes (mitoribosomes). Specifically associates with intermediates of the mitochondrial ribosome large subunit (mt-LSU) and is required for proper ribosome assembly, possibly preventing premature association of the large and small ribosomal subunits. Thereby, indirectly regulates mitochondrial translation. It is also required for complete assembly of the mitochondrial respiratory chain complex I. May also function in …

**Summary**, from NCBI Gene [54471](https://www.ncbi.nlm.nih.gov/gene/54471):

> Enables identical protein binding activity; mitochondrial large ribosomal subunit binding activity; and purine ribonucleotide binding activity. Involved in several processes, including mitochondrial large ribosomal subunit assembly; mitochondrion organization; and regulation of mitochondrion organization. Located in mitochondrial matrix and mitochondrial outer membrane. Implicated in optic atrophy. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25979) · Entrez [54471](https://www.ncbi.nlm.nih.gov/gene/54471) · UniProt [L0R8F8](https://www.uniprot.org/uniprotkb/L0R8F8) · Ensembl [ENSG00000100335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100335)

## Data

Gene col 1930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1930); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1930]; `tensor/DDL_lfc|DDL_z.npy` [1930]; `embed/gene_vectors.npy` [1930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1930 or target_col == 1930). Every well: [[MIEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
