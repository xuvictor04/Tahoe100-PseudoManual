---
symbol: "PCK2"
type: "gene"
col: 2036
ensembl_id: "ENSG00000100889"
name: "phosphoenolpyruvate carboxykinase 2, mitochondrial"
location: "14q11.2-q12"
module: 133
arm: "+"
pooled_cpm: 12.4
n_lines_expressing: 49
n_dd_up: 42
n_dd_down: 30
n_dd_up_clean: 36
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# PCK2

*phosphoenolpyruvate carboxykinase 2, mitochondrial* — 14q11.2-q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +17.5, q 0e+00, up in 36 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.402× (z -12.7, q 6e-34, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YARS1]] (+0.82, fdr 7e-06), [[SLC6A9]] (+0.81, fdr 7e-06), [[CEBPG]] (+0.78, fdr 7e-06).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +17.5 | 0e+00 | 36/46 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.98×** | +13.5 | 6e-39 | 42/47 (NCI-H2030, HCT15, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.33×** | +11.8 | 1e-29 | 39/45 (BT-474, NCI-H23, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.27×** | +11.4 | 5e-28 | 35/44 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.13×** | +10.5 | 1e-23 | 38/46 (Panc 03.27, BT-474, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.59×** | +9.1 | 7e-18 | 31/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.54×** | +8.5 | 1e-15 | 29/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.84×** | +8.4 | 2e-15 | 35/46 (BT-474, J82, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.82×** | +8.3 | 5e-15 | 31/47 (HCT15, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +6.3 | 1e-08 | 20/46 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.3 | 2e-08 | 20/43 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.2 | 4e-08 | 6/20 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.56×** | +6.1 | 4e-08 | 18/45 (BT-474, SHP-77, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.49×** | +5.5 | 1e-06 | 21/46 (NCI-H2030, BT-474, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.5 | 1e-06 | 14/35 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.93×** | +4.8 | 6e-05 | 17/43 (NCI-H2030, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 6e-05 | 15/46 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.88×** | +4.6 | 2e-04 | 10/47 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -12.7 | 6e-34 | 38/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.428×** | -11.8 | 1e-29 | 35/43 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.465×** | -10.7 | 3e-24 | 38/46 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.458×** | -10.4 | 3e-23 | 32/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.485×** | -10.1 | 9e-22 | 33/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.603×** | -9.9 | 3e-21 | 28/44 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.506×** | -9.5 | 3e-19 | 33/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -8.9 | 6e-17 | 30/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.534×** | -8.7 | 2e-16 | 33/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.587×** | -7.4 | 7e-12 | 31/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.614×** | -6.8 | 6e-10 | 21/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.631×** | -6.4 | 7e-09 | 23/44 (PANC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.634×** | -6.3 | 1e-08 | 26/45 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -5.9 | 2e-07 | 18/45 (HOP62, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.665×** | -5.7 | 6e-07 | 20/46 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -5.5 | 2e-06 | 21/42 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -5.3 | 5e-06 | 18/45 (KATO III, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.690×** | -5.2 | 8e-06 | 18/46 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.682×** | -5.0 | 2e-05 | 21/43 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.699×** | -4.7 | 7e-05 | 19/46 (RPMI-7951, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.2 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0748× (z -27.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0785× (z -19.4) |
| [[LoVo (line)]] | wt | 30.0 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0877× (z -17.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.102× (z -16.9) |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -17.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.141× (z -11.7) |
| [[KATO III (line)]] | alt | 35.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -13.5) |
| [[SW480 (line)]] | alt | 13.0 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.156× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -9.0) |
| [[A-427 (line)]] | wt | 19.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.201× (z -10.1) |
| [[H4 (line)]] | wt | 21.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -12.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.0487× (z -11.8) |
| [[A549 (line)]] | wt | 8.26 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HCT15 (line)]] | alt | 26.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.181× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 6.53 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0549× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 14.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.0) | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -12.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 7.05 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[CFPAC-1 (line)]] | alt | 7.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0848× (z -8.8) |
| [[HS-578T (line)]] | alt | 8.93 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -11.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.6 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.45× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 6.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0726× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.191× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.111× (z -8.5) |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS1]] | +0.82 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A9]] | +0.81 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CEBPG]] | +0.78 | +0.71 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[DMGDH]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[NBR2]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TARS1]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[AARS1]] | +0.77 | +0.81 / +0.82 | both halves | 7e-06 |  |
| [[VLDLR-AS1]] | +0.77 | +0.61 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CARS1]] | +0.75 | +0.74 / +0.84 | both halves | 7e-06 |  |
| [[SLC1A4]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[MARS1]] | +0.74 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[PSAT1]] | +0.73 | +0.77 / +0.78 | both halves | 7e-06 | STRING 528 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers PCK2's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.6% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds |
| [[CHAC1]] | B | CHAC1 activity raises PCK2's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without CHAC1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[LINC00662]] | C | LINC00662 activity lowers PCK2's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 2.44× higher at baseline in the lines without LINC00662 | 0.087 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.881). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.4, 47.3); signed map (-13.2, 23.2). **Vector** length 110, 29.0% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +7.6 | +13.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.5 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +17.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.5 | +9.1 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +6.2 | +11.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +5.6 | +8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.4 | +11.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +5.0 | +8.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -8.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -11.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphoenolpyruvate carboxykinase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2-q12 — chr14:24,094,053-24,110,598 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEPCK, PEPCK2 |
| Gene groups (HGNC) | Decarboxylases |
| Reactome | 3 pathways, smallest: Gluconeogenesis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16822](https://www.uniprot.org/uniprotkb/Q16822) (Phosphoenolpyruvate carboxykinase):

> Mitochondrial phosphoenolpyruvate carboxykinase that catalyzes the conversion of oxaloacetate (OAA) to phosphoenolpyruvate (PEP), the rate-limiting step in the metabolic pathway that produces glucose from lactate and other precursors derived from the citric acid cycle. Can play an active role in glyceroneogenesis and gluconeogenesis. In lipogenic cells such as adipocytes, it generates PEP via the mitochondrial pyruvate-to-PEP bypass, driving the PEP flux required for cytosolic glycerol …

**Summary**, from NCBI Gene [5106](https://www.ncbi.nlm.nih.gov/gene/5106):

> This gene encodes a mitochondrial enzyme that catalyzes the conversion of oxaloacetate to phosphoenolpyruvate in the presence of guanosine triphosphate (GTP). A cytosolic form of this protein is encoded by a different gene and is the key enzyme of gluconeogenesis in the liver. Alternatively spliced transcript variants have been described. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:8725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8725) · Entrez [5106](https://www.ncbi.nlm.nih.gov/gene/5106) · UniProt [Q16822](https://www.uniprot.org/uniprotkb/Q16822) · Ensembl [ENSG00000100889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100889)

## Data

Gene col 2036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2036); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2036]; `tensor/DDL_lfc|DDL_z.npy` [2036]; `embed/gene_vectors.npy` [2036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2036 or target_col == 2036). Every well: [[PCK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
