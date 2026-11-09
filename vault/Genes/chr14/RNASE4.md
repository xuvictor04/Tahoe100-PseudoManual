---
symbol: "RNASE4"
type: "gene"
col: 15142
ensembl_id: "ENSG00000258818"
name: "ribonuclease A family member 4"
location: "14q11.2"
module: 1
arm: "-"
pooled_cpm: 16.42
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 44
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 17
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RNASE4

*ribonuclease A family member 4* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.24× (z +6.4, q 7e-08, up in 27 of 44 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.71×, HOP62 1.49×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.108× (z -27.1, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANG]] (+0.88, fdr 7e-06, ⚠ same locus), [[RAB40C]] (+0.70, fdr 7e-06), [[EFNA3]] (+0.70, fdr 7e-06), [[MOSPD3]] (+0.69, fdr 7e-06); moves opposite to [[GNL3L]] (-0.74, fdr 7e-06), [[ANAPC7]] (-0.70, fdr 7e-06), [[PRMT3]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA5]] → it (grade B ⚠); 17 go from it, the strongest it → cells under [[AT7519 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15142.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.71×, HOP62 1.49×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +6.4 | 7e-08 | 27/44 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.44× | +3.1 | 0.47 | 15/44 (KATO III, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.108×** | -27.1 | 0e+00 | 43/44 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.0894×** | -20.7 | 0e+00 | 43/43 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.108×** | -18.3 | 0e+00 | 42/44 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.207×** | -13.5 | 2e-39 | 42/44 (A549, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.223×** | -12.9 | 7e-36 | 43/44 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.240×** | -12.2 | 2e-32 | 42/44 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.266×** | -11.4 | 6e-28 | 44/44 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.277×** | -11.0 | 2e-26 | 41/42 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.288×** | -10.7 | 1e-24 | 38/44 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.296×** | -10.4 | 1e-23 | 37/44 (A549, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.293×** | -10.1 | 2e-22 | 31/40 (A549, C32, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.342×** | -9.2 | 2e-18 | 40/44 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.349×** | -9.0 | 9e-18 | 40/44 (A549, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.510×** | -8.1 | 2e-14 | 33/43 (NCI-H1792, CFPAC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.377×** | -8.0 | 3e-14 | 29/40 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.391×** | -8.0 | 3e-14 | 38/44 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.414×** | -7.6 | 1e-12 | 37/44 (C32, HepG2/C3A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.397×** | -7.5 | 2e-12 | 32/43 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.455×** | -6.7 | 5e-10 | 31/44 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.623×** | -5.7 | 3e-07 | 29/44 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.271×** | -5.6 | 5e-07 | 31/43 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.529×** | -5.4 | 1e-06 | 30/43 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.292×** | -5.3 | 3e-06 | 29/44 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.97 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 39.6 | 0 | 16 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0345× (z -18.9) |
| [[H4 (line)]] | wt | 27.2 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0474× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0434× (z -26.3) |
| [[C32 (line)]] | wt | 38.8 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0463× (z -25.5) |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0492× (z -26.4) |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0472× (z -25.9) |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0339× (z -26.3) |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 1 (1 ⚠) | 10 (6 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +9.3) ⚠ position not correctable | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -11.4) |
| [[A549 (line)]] | wt | 36.5 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0317× (z -31.6) |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0420× (z -25.6) |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0291× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0491× (z -15.5) |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -19.8) |
| [[A-172 (line)]] | wt | 15.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0314× (z -25.7) |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0483× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0691× (z -18.0) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0929× (z -18.7) |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0711× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -14.4) |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -15.1) |
| [[A498 (line)]] | wt | 11.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0284× (z -19.7) |
| [[J82 (line)]] | alt | 6.44 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 58.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -25.4) |
| [[NCI-H2347 (line)]] | alt | 7.01 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.6) |
| [[PANC-1 (line)]] | alt | 9.76 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0974× (z -12.7) |
| [[SW480 (line)]] | alt | 4.24 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -16.8) |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0816× (z -13.4) |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0224× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 9.50 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0437× (z -13.5) |
| [[LS 180 (line)]] | wt | 9.43 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -17.5) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0308× (z -13.5) |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0486× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 4.41 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0420× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.7) |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0720× (z -10.3) |
| [[RKO (line)]] | wt | 8.30 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0707× (z -9.7) |
| [[SHP-77 (line)]] | alt | 5.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -8.6) |
| [[SW48 (line)]] | wt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -10.9) |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANG]] | +0.88 | +0.91 / +0.84 | both halves | 7e-06 | STRING 988; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RAB40C]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[EFNA3]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[CDKN2D]] | +0.68 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CARHSP1]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ARL3]] | +0.67 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[OCEL1]] | +0.66 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[FBXO33]] | +0.66 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[NDUFA2]] | +0.65 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[SIRT2]] | +0.65 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL3L]] | -0.74 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.70 | -0.67 / -0.70 | both halves | 7e-06 |  |
| [[PRMT3]] | -0.69 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[UTP20]] | -0.67 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[WDR77]] | -0.66 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.66 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.65 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[PSME3]] | -0.65 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[MRPS25]] | -0.64 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[DPH5-DT]] | -0.64 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.64 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.63 | -0.56 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA5]] | B | HOXA5 activity raises RNASE4's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without HOXA5 | 0.032 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[TOP2A]] | B | TOP2A activity raises RNASE4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AT7519 (drug)]] 5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.44× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.68× the cells of the other lines | 0.005 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Infigratinib (drug)]] 5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.60× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | [[ANG]], RNASE4 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 1.37× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.79× the cells of the other lines | 0.040 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.66× the cells of the other lines | 0.044 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[PF-06260933 (drug)]] 5 µM | C | [[ANG]], RNASE4 activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 1.46× the cells of the other lines | 0.045 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Bimiralisib (drug)]] 5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under Bimiralisib 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.53× the cells of the other lines | 0.053 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Naproxen (drug)]] 5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.79× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Tolcapone (drug)]] 5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.81× the cells of the other lines | 0.058 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[IQ 1 (drug)]] 5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.76× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[GSK1059615 (drug)]] 5 µM | C | [[ANG]], RNASE4 activity raises the cells' numbers under GSK1059615 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.47× the cells of the other lines | 0.074 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.9, -33.1); signed map (-25.3, 16.4). **Vector** length 87.8, 26.8% of its response variance represented; |z| ≥ 3 in 1,344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.5 | -9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.5 | -10.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | -6.1 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -5.4 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease A family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,684,560-20,701,216 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAB1 |
| Gene groups (HGNC) | Ribonuclease A family |
| Matched by | ensembl_id |

**Function**, from UniProt [P34096](https://www.uniprot.org/uniprotkb/P34096) (Ribonuclease 4):

> Cleaves preferentially after uridine bases. Has antimicrobial activity against uropathogenic E.coli (UPEC). Probably contributes to urinary tract sterility.

**Summary**, from NCBI Gene [6038](https://www.ncbi.nlm.nih.gov/gene/6038):

> The protein encoded by this gene belongs to the pancreatic ribonuclease family. It plays an important role in mRNA cleavage and has marked specificity towards the 3' side of uridine nucleotides. Alternative splicing results in four transcript variants encoding the same protein. This gene and the gene that encodes angiogenin share promoters and 5' exons. Each gene splices to a unique downstream exon that contains its complete coding region. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:10047](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10047) · Entrez [6038](https://www.ncbi.nlm.nih.gov/gene/6038) · UniProt [P34096](https://www.uniprot.org/uniprotkb/P34096) · Ensembl [ENSG00000258818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258818)

## Data

Gene col 15142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15142); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15142]; `tensor/DDL_lfc|DDL_z.npy` [15142]; `embed/gene_vectors.npy` [15142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15142 or target_col == 15142). Every well: [[RNASE4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASE4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
