---
symbol: "WWOX"
type: "gene"
col: 11783
ensembl_id: "ENSG00000186153"
name: "WW domain containing oxidoreductase"
location: "16q23.1-q23.2"
module: 200
arm: "+"
pooled_cpm: 210.51
n_lines_expressing: 45
n_dd_up: 37
n_dd_down: 41
n_dd_up_clean: 37
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# WWOX

*WW domain containing oxidoreductase* — 16q23.1-q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.44× (z +6.8, q 8e-09, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.209× (z -28.6, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHIT]] (+0.68, fdr 7e-06), [[FGGY]] (+0.64, fdr 1e-05), [[RAD51B]] (+0.61, fdr 1e-05); moves opposite to [[ZSWIM3]] (-0.54, fdr 5e-05), [[SPACDR]] (-0.52, fdr 4e-05), [[RAB5B]] (-0.51, fdr 7e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PRKN]] → it (grade B ⚠); 17 go from it, the strongest it → [[CCDC171]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, none with an alert; shown: the 15 strongest. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.8 | 8e-09 | 35/43 (HS-578T, SHP-77, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.70×** | +6.6 | 1e-08 | 36/43 (LS 180, NCI-H1573, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.62×** | +6.0 | 4e-07 | 36/42 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +4.6 | 6e-04 | 28/44 (HepG2/C3A, LoVo, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.49×** | +4.4 | 0.001 | 33/44 (LoVo, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.40×** | +4.4 | 0.001 | 35/44 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.003 | 33/44 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.1 | 0.003 | 28/42 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.003 | 31/43 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.012 | 20/43 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.012 | 24/43 (Panc 03.27, SK-MEL-2, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.012 | 30/43 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.020 | 26/43 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.020 | 26/43 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.022 | 21/43 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.209×** | -28.6 | 0e+00 | 41/43 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.248×** | -18.0 | 0e+00 | 43/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.301×** | -15.5 | 0e+00 | 43/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.288×** | -15.5 | 0e+00 | 42/42 (NCI-H23, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.305×** | -15.3 | 0e+00 | 41/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.308×** | -15.2 | 0e+00 | 42/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.308×** | -15.2 | 0e+00 | 39/43 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.457×** | -14.3 | 2e-44 | 40/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.323×** | -14.0 | 7e-43 | 40/43 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.329×** | -13.8 | 2e-41 | 43/43 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.168×** | -12.1 | 8e-32 | 41/43 (COLO 205, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.180×** | -11.6 | 2e-29 | 42/44 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.490×** | -9.2 | 1e-18 | 36/43 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.506×** | -8.4 | 1e-15 | 29/43 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.564×** | -7.4 | 6e-12 | 35/43 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.598×** | -6.6 | 1e-09 | 35/43 (A-427, J82, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.699×** | -6.5 | 2e-09 | 38/44 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -6.4 | 5e-09 | 34/43 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 313 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -38.8) |
| [[NCI-H23 (line)]] | alt | 467 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -29.1) |
| [[PANC-1 (line)]] | alt | 162 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -32.0) |
| [[LoVo (line)]] | wt | 272 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -25.8) |
| [[LOX-IMVI (line)]] | wt | 172 | 0 | 14 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.160× (z -16.9) |
| [[SW480 (line)]] | alt | 628 | 0 | 14 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -21.2) |
| [[C32 (line)]] | wt | 138 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -15.4) |
| [[J82 (line)]] | alt | 213 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -21.4) |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -26.8) |
| [[HOP62 (line)]] | alt | 231 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -25.4) |
| [[KATO III (line)]] | alt | 216 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -20.8) |
| [[SW1417 (line)]] | alt | 239 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -25.1) |
| [[A549 (line)]] | wt | 277 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -27.9) |
| [[HS-578T (line)]] | alt | 142 | 1 | 10 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.32× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.6) |
| [[RKO (line)]] | wt | 183 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0513× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.148× (z -23.0) |
| [[SNU-423 (line)]] | alt | 173 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -23.5) |
| [[HEC-1-A (line)]] | alt | 403 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -23.5) |
| [[HT-29 (line)]] | alt | 127 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.8) |
| [[NCI-H2030 (line)]] | alt | 583 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -22.3) |
| [[AN3 CA (line)]] | alt | 293 | 0 | 9 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0627× (z -17.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.183× (z -16.1) |
| [[H4 (line)]] | wt | 214 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -24.5) |
| [[HCT15 (line)]] | alt | 326 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -20.7) |
| [[NCI-H1573 (line)]] | alt | 138 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -21.0) |
| [[RPMI-7951 (line)]] | alt | 127 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -19.4) |
| [[SHP-77 (line)]] | alt | 472 | 1 | 8 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.75× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.200× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -15.2) |
| [[COLO 205 (line)]] | alt | 244 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -24.6) |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.3) |
| [[SNU-1 (line)]] | wt | 135 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -13.6) |
| [[C-33 A (line)]] | alt | 170 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -10.7) |
| [[SW48 (line)]] | wt | 211 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.9) |
| [[MIA PaCa-2 (line)]] | alt | 64.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 83.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -16.3) |
| [[SW 900 (line)]] | alt | 101 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -16.9) |
| [[A498 (line)]] | wt | 123 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -19.3) |
| [[SW 1271 (line)]] | alt | 267 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -10.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -9.5) |
| [[LS 180 (line)]] | wt | 98.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.2) |
| [[CHP-212 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.175× (z -8.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 110 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 4.55× (z +10.7) | — |
| [[A-172 (line)]] | wt | 48.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 197 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIT]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 | STRING 938 |
| [[FGGY]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[RAD51B]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[IMMP2L]] | +0.60 | +0.64 / +0.64 | both halves | 7e-06 | STRING 451 |
| [[HCCS-DT]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CCDC171]] | +0.59 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[MACROD2]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 | STRING 513 |
| [[AIG1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SPIDR]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[BABAM2]] | +0.56 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[G3BP1]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[STX18-AS1]] | +0.55 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM3]] | -0.54 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SPACDR]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RAB5B]] | -0.51 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[ZBTB43]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZNF547]] | -0.49 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[METTL21EP-1]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[KLHL7]] | -0.48 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[LINC01772]] | -0.48 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[SRRM5]] | -0.48 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ZFYVE1]] | -0.48 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[TNXB]] | -0.47 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[ZBTB34]] | -0.47 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKN]] | B | PRKN activity raises WWOX's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without PRKN | 0.018 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |
| [[ZC3H12B]] | B | ZC3H12B activity raises WWOX's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 1.52× lower at baseline in the lines without ZC3H12B | 0.084 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[TOP1]] | B | TOP1 activity raises WWOX's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FOXRED2]] | C | FOXRED2 activity raises WWOX's level | lines that do not express FOXRED2 (3) vs lines expressing it (47) | 3.12× lower at baseline in the lines without FOXRED2 | 0.052 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |
| [[CCDC171]] | C | CCDC171 activity raises WWOX's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 3.53× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC171]] | B | WWOX activity raises CCDC171's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.63× lower at baseline in the lines without WWOX | 0.010 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[LHPP]] | B | WWOX activity raises LHPP's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without WWOX | 0.012 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[BABAM2]] | B | WWOX activity raises BABAM2's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without WWOX | 0.035 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[LINC01473]] | B | WWOX activity raises LINC01473's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without WWOX | 0.040 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[FAF1]] | B | WWOX activity raises FAF1's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.61× lower at baseline in the lines without WWOX | 0.048 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[ATG10]] | B | WWOX activity raises ATG10's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without WWOX | 0.053 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[LHPP]] | B | WWOX activity strengthens LHPP's drug response | lines that do not express WWOX (5) vs lines expressing it (43) | the lines without WWOX respond 0.58× as strongly (z diff +2.38); strongest at Homoharringtonine 0.5 µM: 0.47x vs 0.26x (z diff +3.9) | 0.055 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CASC2]] | B | WWOX activity raises CASC2's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without WWOX | 0.056 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[IMMP2L]] | B | WWOX activity raises IMMP2L's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without WWOX | 0.058 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[STX18-AS1]] | B | WWOX activity raises STX18-AS1's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without WWOX | 0.059 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[SPIDR]] | B | WWOX activity raises SPIDR's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without WWOX | 0.060 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[HCCS-DT]] | B | WWOX activity raises HCCS-DT's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without WWOX | 0.062 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.7, 31.3); signed map (9.7, -11.9). **Vector** length 103, 41.0% of its response variance represented; |z| ≥ 3 in 1,898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +6.0 | +6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +0.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.3 | -15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -14.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.1 | -13.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.4 | -5.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.3 | -5.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | -3.2 | -4.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | WW domain containing oxidoreductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1-q23.2 — chr16:78,099,400-79,212,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FOR, WOX1, SDR41C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 6 pathways, smallest: Activation of the TFAP2 (AP-2) family of transcription factors; Negative regulation of activity of TFAP2 (AP-2) family transcription factors; Nuclear signaling by ERBB4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZC7](https://www.uniprot.org/uniprotkb/Q9NZC7) (WW domain-containing oxidoreductase):

> Putative oxidoreductase. Acts as a tumor suppressor and plays a role in apoptosis. Required for normal bone development (By similarity). May function synergistically with p53/TP53 to control genotoxic stress-induced cell death. Plays a role in TGFB1 signaling and TGFB1-mediated cell death. May also play a role in tumor necrosis factor (TNF)-mediated cell death. Inhibits Wnt signaling, probably by sequestering DVL2 in the cytoplasm.

**Summary**, from NCBI Gene [51741](https://www.ncbi.nlm.nih.gov/gene/51741):

> This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) protein family. This gene spans the FRA16D common chromosomal fragile site and appears to function as a tumor suppressor gene. Expression of the encoded protein is able to induce apoptosis, while defects in this gene are associated with multiple types of cancer. Disruption of this gene is also associated with autosomal recessive spinocerebellar ataxia 12. Disruption of a similar gene in mouse results in impaired …

**Accessions** — [HGNC:12799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12799) · Entrez [51741](https://www.ncbi.nlm.nih.gov/gene/51741) · UniProt [Q9NZC7](https://www.uniprot.org/uniprotkb/Q9NZC7) · Ensembl [ENSG00000186153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186153)

## Data

Gene col 11783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11783); `tables/drug_effects.parquet` (80 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11783]; `tensor/DDL_lfc|DDL_z.npy` [11783]; `embed/gene_vectors.npy` [11783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11783 or target_col == 11783). Every well: [[WWOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WWOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
