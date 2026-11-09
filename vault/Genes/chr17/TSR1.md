---
symbol: "TSR1"
type: "gene"
col: 9528
ensembl_id: "ENSG00000167721"
name: "TSR1 ribosome maturation factor"
location: "17p13.3"
module: 5
arm: "+"
pooled_cpm: 89.57
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TSR1

*TSR1 ribosome maturation factor* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.32× (z +12.3, q 4e-32, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.735× (z -5.8, q 3e-06, down in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.768× (z -5.0, q 2e-04, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPAN]] (+0.80, fdr 7e-06), [[NAT10]] (+0.77, fdr 7e-06), [[MRTO4]] (+0.76, fdr 7e-06); moves opposite to [[HDAC5]] (-0.64, fdr 7e-06), [[GABARAP]] (-0.61, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM216A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9528.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.32×** | +12.3 | 4e-32 | 46/49 (SW480, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +11.4 | 1e-27 | 44/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +11.2 | 9e-27 | 47/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +10.0 | 3e-21 | 42/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +9.5 | 4e-19 | 39/48 (PANC-1, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.0 | 3e-17 | 32/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.49×** | +7.8 | 5e-13 | 36/48 (SW480, KATO III, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +7.6 | 2e-12 | 32/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.09×** | +7.6 | 2e-12 | 44/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +7.4 | 6e-12 | 39/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 1e-11 | 37/48 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +7.3 | 1e-11 | 33/49 (NCI-H2347, SW 900, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.43×** | +7.0 | 1e-10 | 33/48 (SW480, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.92×** | +6.7 | 1e-09 | 38/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.43×** | +6.5 | 3e-09 | 30/45 (HT-29, NCI-H460, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.2 | 3e-08 | 33/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.76×** | +5.8 | 2e-07 | 41/48 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.69×** | +5.4 | 2e-06 | 37/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.4 | 2e-06 | 22/48 (Hs 766T, NCI-H2347, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.55×** | +4.5 | 1e-04 | 29/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.735×** | -5.8 | 3e-06 | 32/47 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.768×** | -5.0 | 2e-04 | 27/47 (C32, SW480, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.794×** | -4.6 | 8e-04 | 31/49 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -4.5 | 8e-04 | 22/48 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.803×** | -4.3 | 0.002 | 28/47 (LoVo, HS-578T, …) | rises with dose | low cells (technical?); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.859× | -4.1 | 0.003 | 16/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.815×** | -4.0 | 0.004 | 27/49 (SW480, NCI-H460, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.874× | -3.7 | 0.012 | 11/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.696×** | -3.7 | 0.012 | 24/49 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.015 | 24/50 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.015 | 21/48 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.838× | -3.5 | 0.023 | 18/47 (LoVo, SW480, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.850× | -3.2 | 0.057 | 16/49 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.2 | 0.057 | 16/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.831×** | -3.2 | 0.057 | 15/50 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -3.1 | 0.078 | 13/48 (RKO, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 147 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 97.2 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 72.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +10.5) | — |
| [[KATO III (line)]] | alt | 83.8 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.40× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 78.0 | 3 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.91× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 97.5 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.66× (z +11.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 62.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.05× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 56.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 131 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.18× (z +9.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 34.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 154 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.95× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 59.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 89.1 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.65× (z +9.7) ⚠ unreliable plate only | — |
| [[A498 (line)]] | wt | 128 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 63.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.74× (z +8.7) ⚠ unreliable plate only | — |
| [[C-33 A (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 49.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +8.9) | — |
| [[LoVo (line)]] | wt | 83.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.02× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 94.4 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2347 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[RKO (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SNU-1 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 125 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPAN]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; STRING 614 |
| [[NAT10]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | pathway: rRNA processing; STRING 981 |
| [[MRTO4]] | +0.76 | +0.75 / +0.69 | both halves | 7e-06 | same gene group; STRING 936 |
| [[TWNK]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[GTPBP4]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 | STRING 923 |
| [[NOP16]] | +0.75 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[BCCIP]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[DHX37]] | +0.74 | +0.68 / +0.71 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 570 |
| [[TRMT1]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[DHX33]] | +0.73 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[PUM3]] | +0.72 | +0.78 / +0.69 | both halves | 7e-06 | STRING 871 |
| [[BYSL]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | -0.64 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | -0.61 | -0.59 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM216A]] | B | FAM216A activity raises TSR1's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without FAM216A | 0.004 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[ZFP69B]] | B | ZFP69B activity raises TSR1's level | lines that do not express ZFP69B (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without ZFP69B | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: LINC00888, PDE4C, RIMS3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.812). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.6, -36.0); signed map (-1.3, -46.9). **Vector** length 104, 34.1% of its response variance represented; |z| ≥ 3 in 1,473 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.65 to 13); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.61 to 11); *ribosome biogenesis* (control, mean cos +0.57 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.9 | +11.2 |
|  | [[EX229 (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.3 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +7.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.6 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | -3.7 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -3.4 | +7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -4.3 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | TSR1 ribosome maturation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,322,396-2,336,657 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10534 |
| Gene groups (HGNC) | Ribosome biogenesis factors; Small nucleolar RNA protein coding host genes |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2NL82](https://www.uniprot.org/uniprotkb/Q2NL82) (Pre-rRNA-processing protein TSR1 homolog):

> Required during maturation of the 40S ribosomal subunit in the nucleolus.

**Summary**, from NCBI Gene [55720](https://www.ncbi.nlm.nih.gov/gene/55720):

> Enables RNA binding activity. Predicted to be involved in endonucleolytic cleavage of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) and maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Predicted to be located in cytosol and nucleoplasm. Predicted to be part of 90S preribosome. Predicted to be active in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25542) · Entrez [55720](https://www.ncbi.nlm.nih.gov/gene/55720) · UniProt [Q2NL82](https://www.uniprot.org/uniprotkb/Q2NL82) · Ensembl [ENSG00000167721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167721)

## Data

Gene col 9528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9528); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9528]; `tensor/DDL_lfc|DDL_z.npy` [9528]; `embed/gene_vectors.npy` [9528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9528 or target_col == 9528). Every well: [[TSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
