---
symbol: "FIGNL1"
type: "gene"
col: 5321
ensembl_id: "ENSG00000132436"
name: "fidgetin like 1"
location: "7p12.2"
module: 6
arm: "+"
pooled_cpm: 19.92
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FIGNL1

*fidgetin like 1* — 7p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.91× (z +16.8, q 0e+00, up in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.69× (z +8.3, q 2e-14, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.516× (z -10.4, q 1e-22, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRIM1]] (+0.74, fdr 7e-06), [[RFC5]] (+0.69, fdr 7e-06), [[TCF19]] (+0.68, fdr 7e-06); moves opposite to [[MAFG]] (-0.60, fdr 2e-05), [[CAB39L]] (-0.60, fdr 2e-05), [[EIF3J-DT]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HLTF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.91×** | +16.8 | 0e+00 | 44/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.73×** | +15.8 | 0e+00 | 40/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.37×** | +13.6 | 7e-40 | 39/45 (LoVo, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +8.3 | 2e-14 | 30/46 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +7.2 | 1e-10 | 28/46 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.10×** | +5.9 | 5e-07 | 22/46 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.22×** | +4.5 | 6e-04 | 15/46 (HT-29, CFPAC-1, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.003 | 17/46 (A-427, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.012 | 13/42 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +3.6 | 0.018 | 15/46 (J82, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.6 | 0.020 | 15/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.17× | +3.5 | 0.021 | 8/46 (HT-29, LS 180, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.25×** | +3.4 | 0.028 | 12/46 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.054 | 6/44 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.072 | 10/42 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.516×** | -10.4 | 1e-22 | 33/46 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -8.4 | 9e-15 | 26/44 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -8.4 | 9e-15 | 30/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -7.8 | 8e-13 | 30/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -6.9 | 5e-10 | 27/45 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.685×** | -5.6 | 2e-06 | 23/44 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Thymol (drug)]] 0.5 µM |  | **0.759×** | -4.2 | 0.002 | 15/42 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.703×** | -4.0 | 0.005 | 16/42 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.846× | -3.7 | 0.012 | 12/46 (HCT15, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.791×** | -3.7 | 0.012 | 16/45 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.797×** | -3.4 | 0.036 | 15/46 (Hs 766T, NCI-H23, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.036 | 10/45 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?) |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **0.803×** | -3.3 | 0.037 | 11/46 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.673×** | -3.1 | 0.069 | 17/38 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.820×** | -3.0 | 0.090 | 15/42 (C32, NCI-H23, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.827×** | -3.0 | 0.090 | 8/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -3.0 | 0.090 | 14/45 (SW480, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 17.5 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -10.3) |
| [[SW480 (line)]] | alt | 45.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -14.9) |
| [[A498 (line)]] | wt | 17.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.12× (z +9.4) ⚠ cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -10.5) |
| [[PANC-1 (line)]] | alt | 19.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.42× (z +10.7) ⚠ cell-cycle shift, explains ~37% of this change | [[Digitoxin (drug)]] 5 µM 0.282× (z -11.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 27.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 41.2 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 22.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.6) |
| [[SW1417 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.08× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 7.19 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0904× (z -8.8) |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.135× (z -9.6) |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -11.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.193× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRIM1]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[RFC5]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 | same gene group; pathway: DNA Double-Strand Break Repair |
| [[TCF19]] | +0.68 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[EME1]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[RNASEH2A]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.66 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[FANCB]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[RFC4]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 | same gene group; pathway: DNA Double-Strand Break Repair |
| [[TUBGCP3]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[C19orf48]] | +0.64 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[EXO1]] | +0.64 | +0.54 / +0.72 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair; STRING 417 |
| [[CDC6]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFG]] | -0.60 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CAB39L]] | -0.60 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[EIF3J-DT]] | -0.57 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[LINC00862]] | -0.57 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[YPEL5]] | -0.56 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ZFTRAF1]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[TBCE-1]] | -0.55 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[CHMP3-AS1]] | -0.54 | -0.34 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLTF]] | B | HLTF activity raises FIGNL1's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without HLTF | 0.049 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.2, -44.1); signed map (-37.8, -42.2). **Vector** length 100, 22.8% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Telomere C-strand (Lagging Strand) Synthesis* (reactome, mean cos +0.52 to 19); *Lagging Strand Synthesis* (reactome, mean cos +0.51 to 16); *Extension of Telomeres* (reactome, mean cos +0.50 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.6 | +13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.4 | +16.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.3 | +15.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +5.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | fidgetin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.2 — chr7:50,444,128-50,450,390 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 11 pathways, smallest: Resolution of D-loop Structures through Holliday Junction Intermediates; Resolution of D-Loop Structures; Meiotic recombination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIW4](https://www.uniprot.org/uniprotkb/Q6PIW4) (Fidgetin-like protein 1):

> ATPase that maintains genome stability by acting as a key regulator of DNA double-strand break (DSB) repair via homologous recombination (HR). Regulates HR by mediating disassembly of RAD51 filaments from DNA and chromatin, thereby preventing DNA damage-independent RAD51 loading and persistent DNA accumulation of RAD51 recombinases. Also regulates HR during meiosis by mediating dissociation of DMC1 filaments from DNA (By similarity). May regulate osteoblast proliferation and differentiation (By …

**Summary**, from NCBI Gene [63979](https://www.ncbi.nlm.nih.gov/gene/63979):

> This gene encodes a member of the AAA ATPase family of proteins. The encoded protein is recruited to sites of DNA damage where it plays a role in DNA double-strand break repair via homologous recombination. This protein has also been shown to localize to the centrosome and inhibit ciliogenesis, and may regulate the proliferation and differentiation of osteoblasts. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:13286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13286) · Entrez [63979](https://www.ncbi.nlm.nih.gov/gene/63979) · UniProt [Q6PIW4](https://www.uniprot.org/uniprotkb/Q6PIW4) · Ensembl [ENSG00000132436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132436)

## Data

Gene col 5321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5321); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5321]; `tensor/DDL_lfc|DDL_z.npy` [5321]; `embed/gene_vectors.npy` [5321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5321 or target_col == 5321). Every well: [[FIGNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIGNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
