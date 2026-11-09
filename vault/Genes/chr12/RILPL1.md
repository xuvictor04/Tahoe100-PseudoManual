---
symbol: "RILPL1"
type: "gene"
col: 11970
ensembl_id: "ENSG00000188026"
name: "Rab interacting lysosomal protein like 1"
location: "12q24.31"
module: 18
arm: "+"
pooled_cpm: 49.43
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# RILPL1

*Rab interacting lysosomal protein like 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.51× (z +6.6, q 3e-08, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.247× (z -44.0, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB11FIP3]] (+0.80, fdr 7e-06), [[PTDSS2]] (+0.68, fdr 7e-06), [[PRELID3A]] (+0.67, fdr 7e-06); moves opposite to [[SRP9]] (-0.60, fdr 3e-05), [[ATP7A]] (-0.59, fdr 1e-05), [[ARL5B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); 3 go from it, the strongest it → [[TTC7B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +6.6 | 3e-08 | 34/46 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 0.004 | 21/45 (J82, A549, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +4.1 | 0.007 | 8/46 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.010 | 8/46 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.12× | +3.7 | 0.022 | 3/47 (A498, HCT15, …) | all doses, stronger at high dose |  |
| [[Larotrectinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.031 | 12/47 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.4 | 0.054 | 12/46 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.16× | +3.3 | 0.066 | 13/46 (A549, HCT15, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.3 | 0.066 | 10/46 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.089 | 7/46 (SW480, LS 180, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | 1.15× | +3.1 | 0.089 | 13/46 (NCI-H23, A498, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.10 | 3/46 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.247×** | -44.0 | 0e+00 | 45/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.315×** | -24.7 | 0e+00 | 43/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -16.1 | 0e+00 | 35/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.516×** | -14.7 | 0e+00 | 38/46 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.557×** | -13.0 | 2e-36 | 37/46 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.560×** | -12.9 | 6e-36 | 35/46 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -11.1 | 1e-26 | 36/47 (SNU-423, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.634×** | -10.1 | 3e-22 | 35/46 (C32, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.677×** | -8.6 | 3e-16 | 25/45 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -7.3 | 1e-11 | 30/46 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.704×** | -7.2 | 3e-11 | 27/44 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **0.738×** | -6.7 | 8e-10 | 24/45 (SK-MEL-2, SHP-77, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.741×** | -6.6 | 1e-09 | 24/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.742×** | -6.3 | 9e-09 | 23/43 (C32, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.785×** | -5.4 | 3e-06 | 24/46 (BT-474, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.8 | 6e-05 | 20/46 (NCI-H460, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.665×** | -4.7 | 8e-05 | 22/46 (LOX-IMVI, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.859× | -3.4 | 0.023 | 7/46 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.910× | -2.9 | 0.074 | 16/46 (A-172, SNU-1, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.880× | -2.8 | 0.092 | 13/45 (NCI-H1573, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Simotinib (drug)]] 0.5 µM |  | 0.881× | -2.8 | 0.100 | 7/45 (Hs 766T, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 101 | 0 | 20 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -27.0) |
| [[A-172 (line)]] | wt | 83.2 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -42.0) |
| [[NCI-H460 (line)]] | wt | 76.3 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -35.4) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -21.4) |
| [[SK-MEL-2 (line)]] | alt | 53.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -26.6) |
| [[SNU-423 (line)]] | alt | 49.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -28.4) |
| [[HOP62 (line)]] | alt | 48.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -23.7) |
| [[J82 (line)]] | alt | 59.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -23.5) |
| [[LOX-IMVI (line)]] | wt | 55.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -23.8) |
| [[NCI-H1573 (line)]] | alt | 32.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.4) |
| [[RKO (line)]] | wt | 71.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -21.7) |
| [[SNU-1 (line)]] | wt | 94.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.1) |
| [[A549 (line)]] | wt | 66.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -30.0) |
| [[NCI-H1792 (line)]] | alt | 58.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.1) |
| [[NCI-H23 (line)]] | alt | 80.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -23.1) |
| [[PANC-1 (line)]] | alt | 55.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -33.4) |
| [[A-427 (line)]] | wt | 66.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.258× (z -14.2) |
| [[A498 (line)]] | wt | 48.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -19.4) |
| [[BT-474 (line)]] | alt | 68.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -22.0) |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.3) |
| [[C-33 A (line)]] | alt | 103 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 53.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.2) |
| [[HS-578T (line)]] | alt | 42.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -23.6) |
| [[NCI-H2030 (line)]] | alt | 56.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -17.6) |
| [[SW 900 (line)]] | alt | 26.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.9) |
| [[SW48 (line)]] | wt | 56.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -17.1) |
| [[LoVo (line)]] | wt | 60.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -19.0) |
| [[RPMI-7951 (line)]] | alt | 33.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -16.2) |
| [[SW1417 (line)]] | alt | 30.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.9) |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.2) |
| [[CHP-212 (line)]] | wt | 65.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.2) |
| [[H4 (line)]] | wt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.5) |
| [[Hs 766T (line)]] | wt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.0) |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0943× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[COLO 205 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11FIP3]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PTDSS2]] | +0.68 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[PRELID3A]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[PUS7]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PAM16]] | +0.65 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[PTPN9]] | +0.63 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[BCL7A]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MZT2A]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ANKRD16]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MRPS5]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NPRL3]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CRTC3]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP9]] | -0.60 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[ATP7A]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ARL5B]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ENPP1]] | -0.59 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[NAB1]] | -0.56 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[C4orf33]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SUB1]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[IFT80]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[SF3B1]] | -0.53 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.52 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[ABLIM1]] | -0.52 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[ADD3]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises RILPL1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 3.24× lower at baseline in the lines without NT5M | 0.016 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[FGD1]] | B | FGD1 activity raises RILPL1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 2.42× lower at baseline in the lines without FGD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[PUS7]] | C | PUS7's natural level strengthens RILPL1's drug response | PUS7's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.07; direction clear | 0.002 | ⚠ tissue can mimic it; precision caveat |
| [[ANKRD13B]] | C | ANKRD13B activity raises RILPL1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.92× lower at baseline in the lines without ANKRD13B | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC7B]] | C | RILPL1's natural level strengthens TTC7B's drug response | RILPL1's natural level across 39 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.56; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ZFYVE9]] | C | RILPL1's natural level strengthens ZFYVE9's drug response | RILPL1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.17; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RAB11FIP3]] | C | RILPL1's natural level strengthens RAB11FIP3's drug response | RILPL1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.52; direction not clear | 0.090 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.5, -2.6); signed map (-40.7, 1.8). **Vector** length 103, 28.1% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -24.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -3.8 | -7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -44.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -16.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -2.1 | -1.7 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Rab interacting lysosomal protein like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,470,054-123,533,719 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39378 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5EBL4](https://www.uniprot.org/uniprotkb/Q5EBL4) (RILP-like protein 1):

> Plays a role in the regulation of cell shape and polarity (By similarity). Plays a role in cellular protein transport, including protein transport away from primary cilia (By similarity). Neuroprotective protein, which acts by sequestring GAPDH in the cytosol and prevent the apoptotic function of GAPDH in the nucleus (By similarity). Competes with SIAH1 for binding GAPDH (By similarity). Does not regulate lysosomal morphology and distribution. Binds to RAB10 following LRRK2-mediated RAB10 …

**Summary**, from NCBI Gene [353116](https://www.ncbi.nlm.nih.gov/gene/353116):

> Predicted to enable dynein light intermediate chain binding activity and small GTPase binding activity. Predicted to be involved in several processes, including epithelial cell morphogenesis; nitric oxide mediated signal transduction; and protein transport from ciliary membrane to plasma membrane. Located in centrosome; ciliary basal body; and cytosol. Implicated in oculopharyngodistal myopathy 4. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26814) · Entrez [353116](https://www.ncbi.nlm.nih.gov/gene/353116) · UniProt [Q5EBL4](https://www.uniprot.org/uniprotkb/Q5EBL4) · Ensembl [ENSG00000188026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188026)

## Data

Gene col 11970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11970); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11970]; `tensor/DDL_lfc|DDL_z.npy` [11970]; `embed/gene_vectors.npy` [11970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11970 or target_col == 11970). Every well: [[RILPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RILPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
