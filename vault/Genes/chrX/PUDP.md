---
symbol: "PUDP"
type: "gene"
col: 5015
ensembl_id: "ENSG00000130021"
name: "pseudouridine 5'-phosphatase"
location: "Xp22.31"
module: 1
arm: "+"
pooled_cpm: 51.98
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PUDP

*pseudouridine 5'-phosphatase* — Xp22.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (20 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.253× (z -16.2, q 0e+00, down in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.382× (z -16.0, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THADA]] (+0.64, fdr 2e-05), [[GMDS-DT]] (+0.60, fdr 1e-05), [[COMMD10]] (+0.58, fdr 2e-05); moves opposite to [[LINC00674]] (-0.56, fdr 1e-05), [[HYKK]] (-0.50, fdr 1e-04), [[FXYD6]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02666]] → it (grade B ⚠); 5 go from it, the strongest it → [[YLPM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.33 | 24/43 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.22× | +3.2 | 0.33 | 17/44 (A549, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.31× | +3.1 | 0.33 | 19/43 (LoVo, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.253×** | -16.2 | 0e+00 | 43/43 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.382×** | -16.0 | 0e+00 | 42/44 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.384×** | -15.9 | 0e+00 | 40/44 (LoVo, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.266×** | -15.6 | 0e+00 | 44/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.396×** | -10.9 | 1e-25 | 38/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.398×** | -10.9 | 2e-25 | 41/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.186×** | -10.4 | 3e-23 | 43/45 (KATO III, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.461×** | -8.8 | 1e-16 | 37/44 (NCI-H460, SK-MEL-2, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.475×** | -8.8 | 1e-16 | 40/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.476×** | -8.7 | 1e-16 | 36/44 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.462×** | -8.7 | 1e-16 | 38/43 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.489×** | -8.4 | 2e-15 | 36/44 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.264×** | -8.2 | 1e-14 | 35/44 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.488×** | -8.1 | 2e-14 | 24/36 (SHP-77, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.517×** | -7.5 | 3e-12 | 36/43 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.562×** | -6.4 | 5e-09 | 38/44 (LoVo, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.667×** | -4.7 | 4e-05 | 21/44 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.631×** | -3.9 | 0.002 | 27/44 (LoVo, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.711×** | -3.8 | 0.002 | 24/44 (LoVo, HOP62, …) | top dose only |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.748×** | -3.2 | 0.023 | 20/44 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.763×** | -3.2 | 0.027 | 22/44 (BT-474, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 160 | 0 | 19 (13 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -20.7) |
| [[LoVo (line)]] | wt | 63.9 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -28.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 96.1 | 0 | 17 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -18.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -16.3) |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -15.9) |
| [[BT-474 (line)]] | alt | 131 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -16.5) |
| [[HT-29 (line)]] | alt | 137 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -12.3) |
| [[SNU-423 (line)]] | alt | 81.2 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.2) |
| [[SHP-77 (line)]] | alt | 71.3 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -13.9) |
| [[SW1417 (line)]] | alt | 79.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -14.5) |
| [[COLO 205 (line)]] | alt | 106 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -22.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -11.7) |
| [[J82 (line)]] | alt | 44.7 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 50.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -27.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0465× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 38.4 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.145× (z -13.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -10.5) |
| [[A549 (line)]] | wt | 84.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -13.7) |
| [[HOP62 (line)]] | alt | 29.8 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 64.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 61.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.9) |
| [[RKO (line)]] | wt | 67.2 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -12.3) |
| [[H4 (line)]] | wt | 52.9 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0851× (z -14.1) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -10.9) |
| [[LS 180 (line)]] | wt | 56.9 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 30.9 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0791× (z -17.0) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.244× (z -10.1) |
| [[Hs 766T (line)]] | wt | 50.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -13.3) |
| [[HS-578T (line)]] | alt | 48.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -14.2) |
| [[A-172 (line)]] | wt | 28.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.9) |
| [[A-427 (line)]] | wt | 31.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0584× (z -12.2) |
| [[A498 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -12.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.3) |
| [[C32 (line)]] | wt | 31.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -12.5) |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 36.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 31.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0617× (z -9.3) |
| [[AN3 CA (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THADA]] | +0.64 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[GMDS-DT]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[COMMD10]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[COA4]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[POLR1F]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PITPNB]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[DDX10]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[DNAH14]] | +0.54 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[DPH6]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PAK1IP1]] | +0.53 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[RRS1]] | +0.52 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[CRADD]] | +0.51 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00674]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[HYKK]] | -0.50 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[FXYD6]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.49 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[NTAN1]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[GNAS]] | -0.49 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[WDTC1]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[LMBR1L]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CERK]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SRP54-AS1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TMEM50B]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[IFI27L1]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02666]] | B | LINC02666 activity raises PUDP's level | lines that do not express LINC02666 (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without LINC02666 | 0.011 | ⚠ within organs, on part of the lines; also absent: MGMT |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YLPM1]] | C | PUDP activity lowers YLPM1's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.89× higher at baseline in the lines without PUDP | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |
| [[MGMT]] | C | PUDP activity raises MGMT's level | lines that do not express PUDP (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without PUDP | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |
| [[TIGD2]] | C | PUDP activity raises TIGD2's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.35× lower at baseline in the lines without PUDP | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |
| [[RIOK1]] | C | PUDP activity lowers RIOK1's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.76× higher at baseline in the lines without PUDP | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |
| [[NIP7]] | C | PUDP activity lowers NIP7's level | lines that do not express PUDP (4) vs lines expressing it (46) | 1.84× higher at baseline in the lines without PUDP | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.3, 31.8); signed map (6.1, -43.8). **Vector** length 71.6, 20.0% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -3.5 | -8.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.8 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.5 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | pseudouridine 5'-phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.31 — chrX:6,667,865-7,148,158 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXF68S1E, GS1; previously FAM16AX, HDHD1A, HDHD1 |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases; Haloacid dehalogenase like hydrolase domain containing |
| Reactome | 3 pathways, smallest: Pyrimidine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08623](https://www.uniprot.org/uniprotkb/Q08623) (Pseudouridine-5'-phosphatase):

> Dephosphorylates pseudouridine 5'-phosphate, a potential intermediate in rRNA degradation. Pseudouridine is then excreted intact in urine.

**Summary**, from NCBI Gene [8226](https://www.ncbi.nlm.nih.gov/gene/8226):

> This gene encodes a member of the haloacid dehalogenase-like (HAD) hydrolase superfamily. The encoded protein has no known biological function. This gene has a pseudogene on chromosome 1. Multiple alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:16818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16818) · Entrez [8226](https://www.ncbi.nlm.nih.gov/gene/8226) · UniProt [Q08623](https://www.uniprot.org/uniprotkb/Q08623) · Ensembl [ENSG00000130021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130021)

## Data

Gene col 5015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5015); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5015]; `tensor/DDL_lfc|DDL_z.npy` [5015]; `embed/gene_vectors.npy` [5015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5015 or target_col == 5015). Every well: [[PUDP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUDP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
