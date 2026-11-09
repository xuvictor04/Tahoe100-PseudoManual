---
symbol: "HLA-A"
type: "gene"
col: 13044
ensembl_id: "ENSG00000206503"
name: "major histocompatibility complex, class I, A"
location: "6p22.1"
module: 70
arm: "+"
pooled_cpm: 307.3
n_lines_expressing: 44
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 10
direction_downstream: 4
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# HLA-A

*major histocompatibility complex, class I, A* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +9.1, q 3e-17, up in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +8.4, q 2e-14, up in 41 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (AsPC-1 3.25×, HOP62 2.79×, RKO 2.70×, NCI-H1573 2.73×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 4.61×, COLO 205 2.56×, NCI-H1573 2.74×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 4.26×, SHP-77 3.85×, SW480 3.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.554× (z -6.4, q 9e-08, down in 39 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-B]] (+0.86, fdr 7e-06), [[HLA-E]] (+0.80, fdr 7e-06), [[B2M]] (+0.80, fdr 7e-06); moves opposite to [[CCT2]] (-0.66, fdr 7e-06), [[USP14]] (-0.65, fdr 1e-05), [[CHCHD6]] (-0.65, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[HLA-F]] → it (grade B ⚠); 4 go from it, the strongest it → [[ICAM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13044.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (AsPC-1 3.25×, HOP62 2.79×, RKO 2.70×, NCI-H1573 2.73×, …); [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 4.61×, COLO 205 2.56×, NCI-H1573 2.74×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 4.26×, SHP-77 3.85×, SW480 3.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.1 | 3e-17 | 40/43 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +8.4 | 2e-14 | 41/43 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.83×** | +6.6 | 8e-09 | 37/38 (LS 180, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.69×** | +5.7 | 2e-06 | 33/42 (AsPC-1, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.60×** | +5.3 | 1e-05 | 38/42 (AsPC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +4.7 | 2e-04 | 29/39 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.002 | 31/44 (SK-MEL-2, SW48, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.44×** | +4.2 | 0.002 | 33/42 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +4.1 | 0.002 | 22/42 (AsPC-1, COLO 205, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.31× | +3.1 | 0.12 | 23/42 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.554×** | -6.4 | 9e-08 | 39/43 (J82, HS-578T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.499×** | -4.1 | 0.011 | 35/42 (A549, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.701×** | -4.0 | 0.012 | 29/42 (HCT15, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.716×** | -3.8 | 0.024 | 31/42 (C32, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.722×** | -3.7 | 0.026 | 35/42 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.714×** | -3.6 | 0.032 | 29/42 (A-172, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.742×** | -3.4 | 0.061 | 26/42 (COLO 205, hTERT-HPNE, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.061 | 24/42 (hTERT-HPNE, A498, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.735×** | -3.3 | 0.064 | 26/42 (COLO 205, C32, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -3.3 | 0.064 | 33/42 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.599× | -3.0 | 0.13 | 25/43 (A-427, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 211 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 227 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.5) | — |
| [[J82 (line)]] | alt | 689 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +8.8) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.347× (z -9.6) |
| [[LS 180 (line)]] | wt | 144 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 184 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 236 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.13× (z +9.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.4) | — |
| [[SW480 (line)]] | alt | 160 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.6) | — |
| [[A-427 (line)]] | wt | 310 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 339 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.6) | — |
| [[RKO (line)]] | wt | 277 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 131 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[COLO 205 (line)]] | alt | 408 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 264 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 394 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.346× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 569 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 247 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 364 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 326 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 354 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 41.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 236 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 938 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 452 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 277 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 613 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 578 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 237 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 471 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 397 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 514 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 708 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 711 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-B]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[HLA-E]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 989 |
| [[B2M]] | +0.80 | +0.76 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999 |
| [[HLA-F]] | +0.73 | +0.65 / +0.76 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 996 |
| [[HLA-C]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 998 |
| [[H2AJ]] | +0.67 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PSME2]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 410 |
| [[HCP5]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PLEKHA4]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TAP1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 984 |
| [[TRIM5]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[CCL5]] | +0.63 | +0.57 / +0.68 | both halves | 9e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 484 |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT2]] | -0.66 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[USP14]] | -0.65 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[PGAM5]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[HERC2]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[CCT3]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[CCT5]] | -0.62 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[CDC123]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[POLR3B]] | -0.62 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[AGPS]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[NOL10]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[RRP1B]] | -0.61 | -0.49 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F]] | B | HLA-F activity raises HLA-A's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 3.01× lower at baseline in the lines without HLA-F | 0.002 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[HLA-B]] | B | HLA-B activity raises HLA-A's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.61× lower at baseline in the lines without HLA-B | 0.008 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[C15orf48]] | B | C15orf48 activity raises HLA-A's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without C15orf48 | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[MAF]] | B | MAF activity raises HLA-A's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without MAF | 0.033 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[GBP4]] | B | GBP4 activity raises HLA-A's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without GBP4 | 0.045 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[HCP5]] | B | HCP5 activity raises HLA-A's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without HCP5 | 0.053 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[ICAM1]] | B | ICAM1 activity raises HLA-A's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without ICAM1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[GBP4]] | B | GBP4 activity weakens HLA-A's drug response | lines that do not express GBP4 (15) vs lines expressing it (29) | the lines without GBP4 respond 1.25× as strongly (z diff -0.96); strongest at Dinaciclib 5 µM: 2.55x vs 1.74x (z diff -3.0) | 0.099 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; target measured in part of the lines; artifact flags |
| [[TENT5A]] | B | TENT5A activity raises HLA-A's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 2.72× lower at baseline in the lines without TENT5A | 0.099 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[HLA-H]] | C | HLA-H activity raises HLA-A's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 4.03× lower at baseline in the lines without HLA-H | 0.036 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICAM1]] | B | HLA-A activity raises ICAM1's level | lines that do not express HLA-A (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without HLA-A | 0.089 | ⚠ within organs, on part of the lines; also absent: PHLDA1, S100A6, HLA-H; its own permutation p |
| [[HSPD1]] | B | HLA-A activity lowers HSPD1's level | lines that do not express HLA-A (6) vs lines expressing it (44) | 1.26× higher at baseline in the lines without HLA-A | 0.096 | ⚠ within organs, on part of the lines; also absent: PHLDA1, S100A6, HLA-H |
| [[S100A6]] | C | HLA-A activity raises S100A6's level | lines that do not express HLA-A (6) vs lines expressing it (44) | 3.38× lower at baseline in the lines without HLA-A | 0.081 | ⚠ within organs, on part of the lines; also absent: PHLDA1, S100A6, HLA-H; co-absent with the target; its own permutation p |
| [[HLA-H]] | C | HLA-A activity raises HLA-H's level | lines that do not express HLA-A (6) vs lines expressing it (44) | 2.80× lower at baseline in the lines without HLA-A | 0.081 | ⚠ within organs, on part of the lines; also absent: PHLDA1, S100A6, HLA-H; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 49.8); signed map (64.2, 27.4). **Vector** length 106, 39.0% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.53 to 19); *complement* (hallmark, mean cos +0.51 to 8); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.3 | +4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +4.7 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.1 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.1 | -3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.0 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I, A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:29,941,260-29,949,572 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 23 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Endosomal/Vacuolar pathway; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters |
| Matched by | ensembl_id |

**Function**, from UniProt [P04439](https://www.uniprot.org/uniprotkb/P04439) (HLA class I histocompatibility antigen, A alpha chain):

> Antigen-presenting major histocompatibility complex class I (MHCI) molecule. In complex with B2M/beta 2 microglobulin displays primarily viral and tumor-derived peptides on antigen-presenting cells for recognition by alpha-beta T cell receptor (TCR) on HLA-A-restricted CD8-positive T cells, guiding antigen-specific T cell immune response to eliminate infected or transformed cells. May also present self-peptides derived from the signal sequence of secreted or membrane proteins, although T cells …

**Summary**, from NCBI Gene [3105](https://www.ncbi.nlm.nih.gov/gene/3105):

> HLA-A belongs to the HLA class I heavy chain paralogues. This class I molecule is a heterodimer consisting of a heavy chain and a light chain (beta-2 microglobulin). The heavy chain is anchored in the membrane. Class I molecules play a central role in the immune system by presenting peptides derived from the endoplasmic reticulum lumen so that they can be recognized by cytotoxic T cells. They are expressed in nearly all cells. The heavy chain is approximately 45 kDa and its gene contains 8 …

**Accessions** — [HGNC:4931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4931) · Entrez [3105](https://www.ncbi.nlm.nih.gov/gene/3105) · UniProt [P04439](https://www.uniprot.org/uniprotkb/P04439) · Ensembl [ENSG00000206503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206503)

## Data

Gene col 13044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13044); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13044]; `tensor/DDL_lfc|DDL_z.npy` [13044]; `embed/gene_vectors.npy` [13044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13044 or target_col == 13044). Every well: [[HLA-A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
