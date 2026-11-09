---
symbol: "PTER"
type: "gene"
col: 9218
ensembl_id: "ENSG00000165983"
name: "phosphotriesterase related"
location: "10p13"
module: 1
arm: "+"
pooled_cpm: 39.65
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PTER

*phosphotriesterase related* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.26× (z +6.4, q 1e-07, up in 20 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.476× (z -14.6, q 1e-45, down in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.251× (z -14.2, q 2e-43, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPHOSPH6]] (+0.58, fdr 1e-05), [[HUS1]] (+0.58, fdr 1e-05), [[BCAN-AS2]] (+0.57, fdr 1e-05); moves opposite to [[LAPTM4A]] (-0.61, fdr 1e-05), [[KDELR1]] (-0.57, fdr 1e-05), [[GINM1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +6.4 | 1e-07 | 20/41 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +5.9 | 1e-06 | 23/42 (A498, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.8 | 1e-06 | 22/42 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.2 | 3e-05 | 20/41 (BT-474, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.003 | 16/42 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.005 | 20/42 (AsPC-1, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.005 | 12/42 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.006 | 11/42 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.5 | 0.032 | 16/42 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.10 | 15/41 (SW480, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.13 | 12/42 (BT-474, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9218.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -14.6 | 1e-45 | 37/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.251×** | -14.2 | 2e-43 | 40/43 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -13.8 | 7e-41 | 38/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.293×** | -12.6 | 3e-34 | 32/41 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -11.9 | 1e-30 | 33/43 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -9.0 | 2e-17 | 27/42 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.657×** | -8.2 | 2e-14 | 29/42 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -7.3 | 3e-11 | 31/42 (PANC-1, HT-29, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -6.1 | 8e-08 | 22/41 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -5.6 | 1e-06 | 21/42 (HCT15, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.761×** | -5.4 | 4e-06 | 26/42 (J82, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.8 | 6e-05 | 1/43 (Hs 766T) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.781×** | -4.6 | 2e-04 | 20/42 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.836× | -3.5 | 0.019 | 13/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.4 | 0.025 | 17/42 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -3.1 | 0.063 | 12/43 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.0 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.287× (z -14.4) |
| [[PANC-1 (line)]] | alt | 31.2 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -15.0) |
| [[RKO (line)]] | wt | 81.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.3) |
| [[HCT15 (line)]] | alt | 120 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.425× (z -8.9) |
| [[LS 180 (line)]] | wt | 68.9 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.143× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 68.6 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -18.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.5) |
| [[SNU-423 (line)]] | alt | 21.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.193× (z -10.8) |
| [[SW480 (line)]] | alt | 61.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.461× (z -10.8) |
| [[A-427 (line)]] | wt | 58.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.164× (z -9.3) |
| [[COLO 205 (line)]] | alt | 44.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.295× (z -10.0) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.148× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 51.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -12.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 23.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -10.1) |
| [[SNU-1 (line)]] | wt | 48.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.9) |
| [[A498 (line)]] | wt | 26.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.08× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.7) | — |
| [[C32 (line)]] | wt | 20.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 35.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 59.9 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.158× (z -10.2) |
| [[LoVo (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.309× (z -11.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.185× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.127× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -11.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 41.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.2) |
| [[A-172 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[HUS1]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[BCAN-AS2]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZBTB38]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[C12orf29]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LINC00460]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MYSM1]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[DIAPH2-AS1]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PPID]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SLC35A4]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CAAP1]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4A]] | -0.61 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[GINM1]] | -0.56 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[UBE2G1]] | -0.54 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[RAB5B]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[SEC61A2]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RCN2]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SEC11A]] | -0.53 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[SDHAP4]] | -0.53 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[AP2A1]] | -0.52 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CDS2]] | -0.51 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[SOD3]] | -0.51 | -0.51 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | C | PTER activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express PTER (6) vs lines expressing it (42) | the lines without PTER: 0.76× the cells of the other lines | 0.046 | ⚠ tissue-confounded; across organs; also absent: ENSG00000287925, VRK2, ZC3HAV1L |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | PTER activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PTER (6) vs lines expressing it (42) | the lines without PTER: 0.79× the cells of the other lines | 0.075 | ⚠ tissue-confounded; across organs; also absent: ENSG00000287925, VRK2, ZC3HAV1L |
| cells under [[Tucidinostat (drug)]] 5 µM | C | PTER activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express PTER (6) vs lines expressing it (42) | the lines without PTER: 0.88× the cells of the other lines | 0.083 | ⚠ tissue-confounded; across organs; also absent: ENSG00000287925, VRK2, ZC3HAV1L |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.5, 0.9); signed map (14.9, -32.8). **Vector** length 91.6, 20.8% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +1.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -11.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -12.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -14.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphotriesterase related |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:16,436,943-16,513,745 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BW5](https://www.uniprot.org/uniprotkb/Q96BW5) (N-acetyltaurine hydrolase):

> N-acetyltaurine hydrolase that regulates feeding by catalyzing the hydrolysis of N-acetyltaurine into taurine and acetate. N-acetyltaurine has anorexigenic and anti-obesity effects that are dependent on GFRAL receptor and GDF15 (By similarity). PTER also acts on other N-acetyl amino acids (Met, Ile, Leu, Val) and N-propionyltaurine, but at lower rates (By similarity).

**Summary**, from NCBI Gene [9317](https://www.ncbi.nlm.nih.gov/gene/9317):

> Enables N-acetyltaurine hydrolase activity. Involved in epithelial cell differentiation and taurine metabolic process. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9590) · Entrez [9317](https://www.ncbi.nlm.nih.gov/gene/9317) · UniProt [Q96BW5](https://www.uniprot.org/uniprotkb/Q96BW5) · Ensembl [ENSG00000165983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165983)

## Data

Gene col 9218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9218); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9218]; `tensor/DDL_lfc|DDL_z.npy` [9218]; `embed/gene_vectors.npy` [9218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9218 or target_col == 9218). Every well: [[PTER — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTER.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
