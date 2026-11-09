---
symbol: "RGL3"
type: "gene"
col: 12983
ensembl_id: "ENSG00000205517"
name: "ral guanine nucleotide dissociation stimulator like 3"
location: "19p13.2"
module: 3
arm: "+"
pooled_cpm: 38.05
n_lines_expressing: 38
n_dd_up: 2
n_dd_down: 33
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RGL3

*ral guanine nucleotide dissociation stimulator like 3* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.28× (z +4.2, q 0.014, up in 16 of 35 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 3.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.466× (z -18.2, q 0e+00, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK6]] (+0.60, fdr 7e-06), [[LMBR1L]] (+0.58, fdr 1e-05), [[PGPEP1]] (+0.58, fdr 9e-06); moves opposite to [[WDR46]] (-0.54, fdr 3e-05), [[ABCF2]] (-0.53, fdr 2e-05), [[ERH]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NRP2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NRP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12983.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 3.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +4.2 | 0.014 | 16/35 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +3.6 | 0.086 | 13/36 (PANC-1, LS 180, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.23× | +3.4 | 0.11 | 13/35 (SW 900, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.21× | +3.3 | 0.15 | 11/36 (HOP62, SK-MEL-2, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.29× | +3.1 | 0.19 | 11/34 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.0 | 0.22 | 13/36 (HOP62, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 1.19× | +3.0 | 0.22 | 14/35 (LS 180, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.466×** | -18.2 | 0e+00 | 30/36 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.431×** | -14.2 | 2e-43 | 30/35 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.486×** | -12.2 | 9e-32 | 27/35 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.495×** | -11.2 | 5e-27 | 26/35 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.525×** | -10.5 | 2e-23 | 25/35 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.549×** | -10.1 | 4e-22 | 29/35 (SW480, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.330×** | -9.8 | 1e-20 | 33/37 (NCI-H23, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.349×** | -9.3 | 1e-18 | 30/35 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -9.2 | 2e-18 | 29/34 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.563×** | -8.9 | 2e-17 | 22/31 (Panc 03.27, NCI-H23, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.588×** | -8.6 | 4e-16 | 24/35 (NCI-H1573, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.635×** | -7.7 | 9e-13 | 21/35 (LS 180, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.648×** | -7.3 | 1e-11 | 23/35 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.748×** | -6.9 | 2e-10 | 19/35 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.676×** | -6.6 | 2e-09 | 20/36 (Panc 03.27, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -6.4 | 6e-09 | 20/35 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -5.0 | 2e-05 | 20/36 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.752×** | -4.8 | 4e-05 | 17/35 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[EX229 (drug)]] 5 µM |  | **0.604×** | -4.4 | 2e-04 | 17/35 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.765×** | -4.3 | 4e-04 | 19/35 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.765×** | -4.2 | 5e-04 | 17/35 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -3.8 | 0.003 | 18/35 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -3.3 | 0.018 | 16/35 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.026 | 10/35 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 56.4 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0443× (z -27.2) |
| [[NCI-H1573 (line)]] | alt | 99.2 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.5) |
| [[NCI-H460 (line)]] | wt | 24.9 | 0 | 10 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 96.0 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.453× (z -12.6) |
| [[SW480 (line)]] | alt | 51.1 | 0 | 10 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -8.6) |
| [[HCT15 (line)]] | alt | 97.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 46.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.4) |
| [[A-172 (line)]] | wt | 23.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.8) |
| [[LS 180 (line)]] | wt | 51.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -19.2) |
| [[NCI-H2347 (line)]] | alt | 103 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.7) |
| [[A498 (line)]] | wt | 26.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.4) |
| [[COLO 205 (line)]] | alt | 43.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 55.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -19.3) |
| [[BT-474 (line)]] | alt | 151 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.538× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 149 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.2) |
| [[HT-29 (line)]] | alt | 49.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -16.6) |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.187× (z -10.8) |
| [[J82 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -11.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 23.5 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.296× (z -10.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.1) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SHP-77 (line)]] | alt | 41.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.74× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Belinostat (drug)]] 5 µM 0.288× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.0) |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -8.6) |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.4) |
| [[A-427 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.81 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK6]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LMBR1L]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PGPEP1]] | +0.58 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[MOGAT3]] | +0.57 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[FAM182B]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ARID3A]] | +0.55 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[KYAT1]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TMEM63A]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PHLDB3]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ABCD4]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[ABHD3]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CHRNB1]] | +0.52 | +0.39 / +0.44 | both halves | 6e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR46]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ABCF2]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ERH]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SNX19]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[WDR77]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TRIM44]] | -0.50 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SF3B4]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SRFBP1]] | -0.49 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[EIF2S1]] | -0.48 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TMEM33]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP2]] | B | NRP2 activity lowers RGL3's level | lines that do not express NRP2 (24) vs lines expressing it (26) | 2.29× higher at baseline in the lines without NRP2 | 0.080 | ⚠ within organs, on part of the lines; also absent: NLRP1, RFX8, TNFAIP6 |
| [[NOXA1]] | B | NOXA1 activity raises RGL3's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 3.95× lower at baseline in the lines without NOXA1 | 0.081 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP2]] | B | RGL3 activity lowers NRP2's level | lines that do not express RGL3 (12) vs lines expressing it (38) | 2.46× higher at baseline in the lines without RGL3 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC16A14 |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (14.6, -23.2); signed map (-25.6, 21.0). **Vector** length 90.3, 22.9% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +3.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -14.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -9.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ral guanine nucleotide dissociation stimulator like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,384,341-11,419,328 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32585 |
| Gene groups (HGNC) | Ral guanine nucleotide dissociation stimulator family |
| Reactome | 3 pathways, smallest: RAF/MAP kinase cascade; MAPK1/MAPK3 signaling; MAPK family signaling cascades |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MIN7](https://www.uniprot.org/uniprotkb/Q3MIN7) (Ral guanine nucleotide dissociation stimulator-like 3):

> Guanine nucleotide exchange factor (GEF) for Ral-A. Potential effector of GTPase HRas and Ras-related protein M-Ras. Negatively regulates Elk-1-dependent gene induction downstream of HRas and MEKK1 (By similarity).

**Summary**, from NCBI Gene [57139](https://www.ncbi.nlm.nih.gov/gene/57139):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in Ras protein signal transduction. Predicted to be located in cytosol. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30282) · Entrez [57139](https://www.ncbi.nlm.nih.gov/gene/57139) · UniProt [Q3MIN7](https://www.uniprot.org/uniprotkb/Q3MIN7) · Ensembl [ENSG00000205517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205517)

## Data

Gene col 12983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12983); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12983]; `tensor/DDL_lfc|DDL_z.npy` [12983]; `embed/gene_vectors.npy` [12983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12983 or target_col == 12983). Every well: [[RGL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
