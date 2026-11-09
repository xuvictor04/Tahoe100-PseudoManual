---
symbol: "CLPX"
type: "gene"
col: 9373
ensembl_id: "ENSG00000166855"
name: "caseinolytic mitochondrial matrix peptidase chaperone subunit X"
location: "15q22.31"
module: 198
arm: "+"
pooled_cpm: 60.88
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# CLPX

*caseinolytic mitochondrial matrix peptidase chaperone subunit X* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.93× (z +7.7, q 6e-12, up in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (KATO III 3.04×, SW480 1.98×, NCI-H460 2.10×, PANC-1 1.89×; ⚠ cell-cycle shift, explains ~24% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (SW480 1.98×, KATO III 2.48×, NCI-H460 2.15×, LoVo 1.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 2.23×, SW480 1.72×; ⚠ cell-cycle shift, explains ~23% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (SW480 2.94×); [[TAK-901 (drug)]] 5 µM in 1 line (LoVo 3.51×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.748× (z -6.5, q 5e-08, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.432×, C32 0.387×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.270×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C32 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pimitespib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO9]] (+0.67, fdr 8e-06), [[PAPOLG]] (+0.65, fdr 1e-05), [[PAIP1]] (+0.64, fdr 7e-06); moves opposite to [[STK40]] (-0.57, fdr 1e-05), [[C3orf52]] (-0.55, fdr 3e-05), [[CMIP]] (-0.52, fdr 2e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[UBE2Q1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9373.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (KATO III 3.04×, SW480 1.98×, NCI-H460 2.10×, PANC-1 1.89×; ⚠ cell-cycle shift, explains ~24% of this change); [[Digitoxin (drug)]] 5 µM in 4 lines (SW480 1.98×, KATO III 2.48×, NCI-H460 2.15×, LoVo 1.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H460 2.23×, SW480 1.72×; ⚠ cell-cycle shift, explains ~23% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (SW480 2.94×); [[TAK-901 (drug)]] 5 µM in 1 line (LoVo 3.51×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +7.7 | 6e-12 | 36/49 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +7.7 | 6e-12 | 36/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +7.5 | 1e-11 | 31/48 (KATO III, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.32×** | +6.2 | 6e-08 | 28/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.29×** | +5.5 | 4e-06 | 29/48 (SW480, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.24×** | +4.8 | 2e-04 | 24/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +4.7 | 2e-04 | 23/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.24×** | +4.6 | 3e-04 | 21/47 (LoVo, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +4.2 | 0.002 | 20/48 (SW480, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.8 | 0.009 | 17/48 (A549, A498, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.7 | 0.013 | 15/48 (Panc 03.27, A-172, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.18× | +3.6 | 0.013 | 20/48 (A-427, HEC-1-A, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.34×** | +3.4 | 0.025 | 14/47 (LoVo, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.077 | 17/48 (RKO, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9373.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.432×, C32 0.387×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (SW480 0.270×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C32 0.346×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pimitespib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.748×** | -6.5 | 5e-08 | 27/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.771×** | -5.8 | 2e-06 | 25/48 (NCI-H2347, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.796×** | -5.1 | 6e-05 | 24/48 (SW 1088, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.872× | -4.3 | 0.002 | 16/48 (SW1417, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.816×** | -4.2 | 0.003 | 19/45 (RKO, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -4.1 | 0.003 | 22/49 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.4 | 0.051 | 14/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trimetrexate (drug)]] 0.5 µM |  | 0.868× | -3.2 | 0.11 | 10/48 (H4, SHP-77, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.869× | -3.1 | 0.11 | 16/48 (NCI-H1792, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 79.9 | 4 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +11.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.94× (z +9.4) | [[Lonafarnib (drug)]] 5 µM 0.270× (z -11.3) ⚠ toxic |
| [[LoVo (line)]] | wt | 66.6 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.07× (z +9.4) ⚠ toxic; cell-cycle shift, explains ~18% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.51× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 55.1 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.23× (z +9.8) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[C32 (line)]] | wt | 63.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 68.0 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +13.0) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[A498 (line)]] | wt | 39.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 69.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0772× (z -10.0) |
| [[PANC-1 (line)]] | alt | 62.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.0) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[RKO (line)]] | wt | 78.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0584× (z -8.6) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A-172 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO9]] | +0.67 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[PAPOLG]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RBM33]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KCTD3]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[RPRD2]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[TLK2]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[METTL14]] | +0.60 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MBIP]] | +0.60 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[POLR3GL]] | +0.58 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[HOXA7]] | +0.57 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[RCOR3]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK40]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[C3orf52]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CMIP]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[C13orf46]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[LINC01589]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[RELT]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[AGPAT4]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SPTBN5]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[FAM131A]] | -0.50 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[TBILA]] | -0.50 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[KIF21B]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MPP3]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CLPX's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[C3orf52]] | B | C3orf52 activity lowers CLPX's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 1.57× higher at baseline in the lines without C3orf52 | 0.088 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q1]] | C | CLPX's natural level weakens UBE2Q1's drug response | CLPX's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.22; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, 0.2); signed map (-22.9, -8.2). **Vector** length 89.3, 19.0% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | caseinolytic mitochondrial matrix peptidase chaperone subunit X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,148,219-65,185,342 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | AAA ATPases; Mitochondrial nucleoid associated proteins |
| Reactome | 1 pathways, smallest: Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O76031](https://www.uniprot.org/uniprotkb/O76031) (ATP-dependent clpX-like chaperone, mitochondrial):

> ATP-dependent chaperone that functions as an unfoldase. As part of the ClpXP protease complex, it recognizes specific protein substrates, unfolds them using energy derived from ATP hydrolysis, and then translocates them to the proteolytic subunit (CLPP) of the ClpXP complex for degradation. Thanks to its chaperone activity, it also functions in the incorporation of the pyridoxal phosphate cofactor into 5-aminolevulinate synthase, thereby activating 5-aminolevulinate (ALA) synthesis, the first …

**Summary**, from NCBI Gene [10845](https://www.ncbi.nlm.nih.gov/gene/10845):

> The protein encoded by this gene is part of a protease found in mitochondria. This protease is ATP-dependent and targets specific proteins for degradation. The protease consists of two heptameric rings of the CLPP catalytic subunit sandwiched between two hexameric rings of the chaperone subunit encoded by this gene. Targeted proteins are unwound by this protein and then passed on to the CLPP subunit for degradation. Two transcript variants, one protein-coding and the other non-protein coding, …

**Accessions** — [HGNC:2088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2088) · Entrez [10845](https://www.ncbi.nlm.nih.gov/gene/10845) · UniProt [O76031](https://www.uniprot.org/uniprotkb/O76031) · Ensembl [ENSG00000166855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166855)

## Data

Gene col 9373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9373); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9373]; `tensor/DDL_lfc|DDL_z.npy` [9373]; `embed/gene_vectors.npy` [9373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9373 or target_col == 9373). Every well: [[CLPX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLPX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
