---
symbol: "GEMIN5"
type: "gene"
col: 1352
ensembl_id: "ENSG00000082516"
name: "gem nuclear organelle associated protein 5"
location: "5q33.2"
module: 33
arm: "+"
pooled_cpm: 32.44
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# GEMIN5

*gem nuclear organelle associated protein 5* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.31× (z +19.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.624× (z -10.9, q 1e-24, down in 29 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.735× (z -7.0, q 3e-10, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR3]] (+0.83, fdr 7e-06), [[PRMT7]] (+0.76, fdr 7e-06), [[TAMM41]] (+0.75, fdr 7e-06); moves opposite to [[SMIM14]] (-0.59, fdr 1e-05), [[KANSL1L]] (-0.58, fdr 7e-05), [[UBE2A]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM216A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +19.1 | 0e+00 | 47/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +17.9 | 0e+00 | 44/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +17.6 | 0e+00 | 46/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +13.1 | 3e-37 | 40/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +11.3 | 2e-27 | 37/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.92×** | +7.9 | 4e-13 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.26×** | +7.5 | 4e-12 | 26/48 (Hs 766T, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +7.3 | 3e-11 | 29/48 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +6.6 | 3e-09 | 26/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.72×** | +6.5 | 5e-09 | 23/48 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.4 | 1e-08 | 22/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.66×** | +6.1 | 4e-08 | 21/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +5.4 | 3e-06 | 19/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 6e-05 | 11/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.7 | 1e-04 | 13/48 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +4.4 | 3e-04 | 14/47 (SK-MEL-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +4.4 | 4e-04 | 14/48 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 1.18× | +3.7 | 0.006 | 7/48 (HOP62, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.624×** | -10.9 | 1e-24 | 29/47 (AN3 CA, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -8.7 | 1e-15 | 22/40 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -7.9 | 7e-13 | 27/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.735×** | -7.0 | 3e-10 | 25/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.828×** | -6.2 | 8e-08 | 25/48 (A-427, NCI-H1792, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.774×** | -5.5 | 4e-06 | 23/44 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.810×** | -4.9 | 9e-05 | 15/48 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -4.6 | 4e-04 | 19/48 (HOP62, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.844× | -3.9 | 0.006 | 13/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.796×** | -3.8 | 0.010 | 13/48 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.849× | -3.6 | 0.014 | 16/48 (HOP62, SW48, …) | top dose only | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.760×** | -3.3 | 0.045 | 12/48 (RKO, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.875× | -3.0 | 0.100 | 16/48 (A-172, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.5 | 4 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.69× (z +11.5) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 5.06× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.470× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.476× (z -8.7) |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 5 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.478× (z -10.6) |
| [[PANC-1 (line)]] | alt | 41.2 | 4 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.25× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -11.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 38.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 22.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +11.6) | — |
| [[SW480 (line)]] | alt | 36.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.418× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 48.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -17.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +10.7) | — |
| [[LoVo (line)]] | wt | 26.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -13.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 40.3 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.72× (z +9.8) | — |
| [[A498 (line)]] | wt | 29.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.5) | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 35.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0607× (z -16.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -9.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0974× (z -10.0) |
| [[HT-29 (line)]] | alt | 9.95 | 1 | 0 | [[Belinostat (drug)]] 5 µM 5.49× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 73.5 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.84× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[Panc 03.27 (line)]] | alt | 31.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +8.7) | — |
| [[RKO (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -17.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.204× (z -8.5) |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR3]] | +0.83 | +0.78 / +0.81 | both halves | 7e-06 | same gene group |
| [[PRMT7]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[DHODH]] | +0.74 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[MTERF3]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[NLE1]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 | same gene group |
| [[POLR1B]] | +0.71 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[RMND1]] | +0.71 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ORC5]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[LYAR]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[NUFIP1]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[DDX55]] | +0.67 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[KANSL1L]] | -0.58 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[UBE2A]] | -0.58 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[ENSA]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TP53INP2]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM216A]] | B | FAM216A activity raises GEMIN5's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without FAM216A | 0.094 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[TSEN2]] | C | TSEN2 activity raises GEMIN5's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without TSEN2 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |
| [[GARNL3]] | C | GARNL3 activity raises GEMIN5's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without GARNL3 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.5, -41.5); signed map (-8.2, -51.1). **Vector** length 109, 27.5% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.59 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.58 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.58 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +13.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +17.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +17.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +19.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.6 | +6.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.6 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.2 | +6.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.9 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.4 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.1 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | gem nuclear organelle associated protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,887,411-154,938,211 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; Gemins |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates host translation machinery; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEQ6](https://www.uniprot.org/uniprotkb/Q8TEQ6) (Gem-associated protein 5):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [25929](https://www.ncbi.nlm.nih.gov/gene/25929):

> This gene encodes a WD repeat protein that is a component of the survival of motor neurons (SMN) complex. The SMN complex plays a critical role in mRNA splicing through the assembly of spliceosomal small nuclear ribonucleoproteins (snRNPs), and may also mediate the assembly and transport of other classes of ribonucleoproteins. The encoded protein is the snRNA-binding component of the SMN complex. Dysregulation of this gene may play a role in alternative mRNA splicing and tumor cell motility. …

**Accessions** — [HGNC:20043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20043) · Entrez [25929](https://www.ncbi.nlm.nih.gov/gene/25929) · UniProt [Q8TEQ6](https://www.uniprot.org/uniprotkb/Q8TEQ6) · Ensembl [ENSG00000082516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082516)

## Data

Gene col 1352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1352); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1352]; `tensor/DDL_lfc|DDL_z.npy` [1352]; `embed/gene_vectors.npy` [1352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1352 or target_col == 1352). Every well: [[GEMIN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEMIN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
