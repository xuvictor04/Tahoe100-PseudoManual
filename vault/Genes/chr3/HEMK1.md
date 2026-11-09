---
symbol: "HEMK1"
type: "gene"
col: 3577
ensembl_id: "ENSG00000114735"
name: "HemK methyltransferase 1, mitochondrial release factors N(5)-glutamine"
location: "3p21.31"
module: 2
arm: "+"
pooled_cpm: 12.04
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# HEMK1

*HemK methyltransferase 1, mitochondrial release factors N(5)-glutamine* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.46× (z +4.7, q 0.001, up in 17 of 48 measured lines) ⚠ cell-cycle shift, explains ~48% of this change.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.386× (z -16.8, q 0e+00, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.514× (z -11.7, q 1e-29, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXNA3]] (+0.59, fdr 4e-05), [[BAIAP3]] (+0.58, fdr 1e-04), [[APBB3]] (+0.58, fdr 3e-05); moves opposite to [[PRDM6]] (-0.56, fdr 4e-04), [[CLOCK]] (-0.56, fdr 6e-05), [[NCOA2]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PITX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.46×** | +4.7 | 0.001 | 17/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.32 | 11/44 (C32, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.386×** | -16.8 | 0e+00 | 37/47 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.328×** | -13.9 | 1e-41 | 44/48 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.335×** | -13.1 | 4e-37 | 42/47 (Panc 03.27, NCI-H23, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.514×** | -11.7 | 1e-29 | 35/45 (SK-MEL-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.403×** | -11.4 | 8e-28 | 39/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.435×** | -10.4 | 3e-23 | 33/46 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.446×** | -10.1 | 5e-22 | 33/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.217×** | -10.0 | 1e-21 | 36/48 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.469×** | -9.1 | 6e-18 | 30/40 (LoVo, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.485×** | -9.0 | 9e-18 | 35/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.270×** | -8.5 | 6e-16 | 37/44 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.510×** | -8.4 | 2e-15 | 31/46 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -7.8 | 4e-13 | 28/45 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -7.2 | 3e-11 | 30/47 (C32, SW480, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.556×** | -6.9 | 2e-10 | 26/45 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -6.4 | 5e-09 | 27/44 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -5.1 | 1e-05 | 21/45 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Silodosin (drug)]] 5 µM |  | **0.720×** | -3.9 | 0.002 | 17/44 (SW48, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.770×** | -3.1 | 0.038 | 9/48 (RKO, NCI-H2030, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.717×** | -3.0 | 0.067 | 7/48 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 30.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -12.6) |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0544× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0220× (z -11.4) |
| [[PANC-1 (line)]] | alt | 9.32 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.273× (z -9.5) |
| [[A549 (line)]] | wt | 8.96 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.162× (z -9.4) |
| [[SW480 (line)]] | alt | 12.7 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0315× (z -17.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0274× (z -9.7) |
| [[LoVo (line)]] | wt | 13.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -8.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.180× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0617× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.164× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 9.98 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0670× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -12.3) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0843× (z -11.3) |
| [[A498 (line)]] | wt | 9.26 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.5 µM 0.0576× (z -11.0) |
| [[KATO III (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0947× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 7.13 | 0 | 2 (1 ⚠) | — | [[Peretinoin (drug)]] 0.5 µM 0.0834× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 28.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0680× (z -20.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.2) |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0765× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -10.1) |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 9.44 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -9.8) |
| [[C32 (line)]] | wt | 8.90 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0468× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 7.73 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0923× (z -10.7) |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -11.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0699× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -10.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0876× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 6.78 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0744× (z -9.0) |
| [[AN3 CA (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNA3]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[BAIAP3]] | +0.58 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[APBB3]] | +0.58 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[FCHSD1]] | +0.56 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[NECAP1]] | +0.56 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[DPH7]] | +0.56 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[PIGH]] | +0.56 | +0.44 / +0.36 | both halves | 9e-05 |  |
| [[GGA1]] | +0.56 | +0.33 / +0.40 | both halves | 1e-04 |  |
| [[SKIC2]] | +0.56 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[SDHAP1-1]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[UVSSA]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[E4F1]] | +0.55 | +0.50 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM6]] | -0.56 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[CLOCK]] | -0.56 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[NCOA2]] | -0.54 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[SNHG31]] | -0.54 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[NXT2]] | -0.52 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[MIER3]] | -0.52 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[CGAS]] | -0.51 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[MAP2K4]] | -0.51 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[PARP8]] | -0.50 | -0.27 / -0.42 | both halves | 3e-04 |  |
| [[STARD4-AS1]] | -0.50 | -0.33 / -0.25 | both halves | 4e-04 |  |
| [[DNAJB14]] | -0.50 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[PPP2R3C]] | -0.50 | -0.28 / -0.31 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PITX1]] | B | PITX1 activity lowers HEMK1's level | lines that do not express PITX1 (10) vs lines expressing it (40) | 1.30× higher at baseline in the lines without PITX1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: MNX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (11.0, -3.6); signed map (-29.7, 1.3). **Vector** length 61.5, 10.7% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | -0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -11.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.9 | -16.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -8.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | HemK methyltransferase 1, mitochondrial release factors N(5)-glutamine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,569,152-50,596,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTQ1 |
| Gene groups (HGNC) | Glutamine methyltransferases; 7BS protein glutamine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5R4](https://www.uniprot.org/uniprotkb/Q9Y5R4) (MTRF1L release factor glutamine methyltransferase):

> N5-glutamine methyltransferase responsible for the methylation of the glutamine residue in the universally conserved GGQ motif of the mitochondrial translation release factors MTRF1, MTRF1L, MRPL58/ICT1 and MTRFR.

**Summary**, from NCBI Gene [51409](https://www.ncbi.nlm.nih.gov/gene/51409):

> Enables peptide chain release factor N(5)-glutamine methyltransferase activity. Predicted to be involved in translational termination. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24923) · Entrez [51409](https://www.ncbi.nlm.nih.gov/gene/51409) · UniProt [Q9Y5R4](https://www.uniprot.org/uniprotkb/Q9Y5R4) · Ensembl [ENSG00000114735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114735)

## Data

Gene col 3577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3577); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3577]; `tensor/DDL_lfc|DDL_z.npy` [3577]; `embed/gene_vectors.npy` [3577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3577 or target_col == 3577). Every well: [[HEMK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEMK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
