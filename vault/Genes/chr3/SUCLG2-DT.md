---
symbol: "SUCLG2-DT"
type: "gene"
col: 14265
ensembl_id: "ENSG00000241316"
name: "SUCLG2 divergent transcript"
location: "3p14.1"
module: 10
arm: "+"
pooled_cpm: 17.72
n_lines_expressing: 43
n_dd_up: 32
n_dd_down: 27
n_dd_up_clean: 25
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 13
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SUCLG2-DT

*SUCLG2 divergent transcript* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.16× (z +10.5, q 3e-23, up in 33 of 40 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.64× (z +9.4, q 2e-18, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.254× (z -13.3, q 2e-37, down in 35 of 41 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF1B-AS1]] (+0.82, fdr 7e-06), [[DPH6-DT]] (+0.81, fdr 2e-05), [[ZRANB2-DT]] (+0.76, fdr 1e-05); moves opposite to [[ETHE1]] (-0.67, fdr 2e-05), [[TMEM120B]] (-0.66, fdr 4e-05), [[TSEN54]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC25A21]] → it (grade B ⚠); 13 go from it, the strongest it → [[RGS10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.16×** | +10.5 | 3e-23 | 33/40 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **2.64×** | +9.4 | 2e-18 | 32/40 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.8 | 3e-16 | 24/32 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.2 | 4e-14 | 23/26 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +7.6 | 4e-12 | 22/37 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +6.7 | 3e-09 | 19/28 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.2 | 5e-08 | 28/40 (SW1417, HS-578T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +5.5 | 3e-06 | 27/41 (RKO, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.67×** | +4.9 | 5e-05 | 27/41 (RPMI-7951, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.66×** | +4.9 | 6e-05 | 23/39 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +4.7 | 2e-04 | 19/37 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.64×** | +4.7 | 2e-04 | 22/39 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 6e-04 | 18/39 (A-172, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.0 | 0.002 | 11/39 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.002 | 13/41 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Afatinib (drug)]] 5 µM |  | **1.56×** | +3.9 | 0.004 | 17/40 (HEC-1-A, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.004 | 15/36 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.007 | 17/38 (NCI-H23, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.010 | 14/39 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +3.6 | 0.010 | 15/40 (HOP62, J82, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.010 | 15/40 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.254×** | -13.3 | 2e-37 | 35/41 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.291×** | -11.9 | 2e-30 | 35/41 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.304×** | -11.5 | 2e-28 | 34/40 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.386×** | -9.2 | 5e-18 | 30/36 (Panc 03.27, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.443×** | -7.9 | 4e-13 | 34/40 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.462×** | -7.5 | 7e-12 | 32/40 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.462×** | -7.5 | 7e-12 | 30/41 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.474×** | -7.2 | 3e-11 | 30/41 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.463×** | -6.8 | 5e-10 | 31/41 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.538×** | -6.0 | 1e-07 | 27/40 (H4, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.543×** | -5.9 | 2e-07 | 27/36 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.539×** | -5.8 | 4e-07 | 20/33 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.563×** | -5.1 | 1e-05 | 24/41 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.563×** | -5.1 | 1e-05 | 21/39 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -4.6 | 1e-04 | 16/39 (HEC-1-A, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.715×** | -4.6 | 2e-04 | 24/40 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.411×** | -4.5 | 2e-04 | 17/36 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.457×** | -4.0 | 0.002 | 17/37 (HOP62, SK-MEL-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.522×** | -3.3 | 0.027 | 16/37 (CFPAC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.713×** | -3.3 | 0.027 | 15/38 (AN3 CA, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.526×** | -3.3 | 0.028 | 16/39 (SNU-423, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 30.3 | 1 (1 ⚠) | 10 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +9.4) ⚠ position not correctable | [[Belinostat (drug)]] 5 µM 0.0997× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 54.3 | 2 (2 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.242× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 73.5 | 2 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.35× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.176× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 86.1 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.03× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0702× (z -12.5) |
| [[SNU-423 (line)]] | alt | 35.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.138× (z -11.9) |
| [[J82 (line)]] | alt | 30.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.168× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0344× (z -15.2) |
| [[PANC-1 (line)]] | alt | 11.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.39× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.283× (z -8.5) |
| [[SW480 (line)]] | alt | 9.04 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.177× (z -9.4) |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0523× (z -9.7) |
| [[C32 (line)]] | wt | 24.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 24.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.127× (z -9.3) |
| [[LS 180 (line)]] | wt | 9.63 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 5.20× (z +10.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Belinostat (drug)]] 0.5 µM 0.145× (z -8.6) |
| [[A498 (line)]] | wt | 8.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +9.0) | — |
| [[H4 (line)]] | wt | 15.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0316× (z -12.2) |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -9.6) |
| [[HS-578T (line)]] | alt | 19.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.167× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 9.38 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0631× (z -10.6) |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0706× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 6.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1B-AS1]] | +0.82 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[DPH6-DT]] | +0.81 | +0.82 / +0.48 | both halves | 2e-05 | same gene group |
| [[ZRANB2-DT]] | +0.76 | +0.79 / +0.57 | both halves | 1e-05 | same gene group |
| [[TMEM202-AS1]] | +0.75 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[PCNX4-DT]] | +0.75 | +0.70 / +0.47 | both halves | 2e-05 | same gene group |
| [[CFAP418-AS1]] | +0.74 | +0.76 / +0.38 | both halves | 6e-05 |  |
| [[PKN2-AS1]] | +0.74 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[THBS4]] | +0.74 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[PDIA3P1]] | +0.73 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CATSPERE]] | +0.73 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | +0.72 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[MFF-DT]] | +0.71 | +0.64 / +0.35 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETHE1]] | -0.67 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[TMEM120B]] | -0.66 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TSEN54]] | -0.65 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.64 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[MPG]] | -0.64 | -0.65 / -0.33 | both halves | 1e-04 |  |
| [[TECPR1]] | -0.63 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[RGS10]] | -0.63 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.63 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[MPST]] | -0.62 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[LPCAT4]] | -0.62 | -0.60 / -0.25 | both halves | 4e-04 |  |
| [[GRAMD4]] | -0.62 | -0.60 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A21]] | B | SLC25A21 activity raises SUCLG2-DT's level | lines that do not express SLC25A21 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without SLC25A21 | 0.031 | ⚠ within organs, on part of the lines; also absent: MIPOL1, EHD3, ZNF790; maybe low, not absent |
| [[JHY]] | B | JHY activity raises SUCLG2-DT's level | lines that do not express JHY (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without JHY | 0.031 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[MRAS]] | B | MRAS activity raises SUCLG2-DT's level | lines that do not express MRAS (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without MRAS | 0.075 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[FLRT2]] | B | FLRT2 activity raises SUCLG2-DT's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without FLRT2 | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[DPH6-DT]] | C | DPH6-DT activity raises SUCLG2-DT's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |
| [[CHST3]] | C | CHST3 activity raises SUCLG2-DT's level | lines that do not express CHST3 (4) vs lines expressing it (46) | 3.06× lower at baseline in the lines without CHST3 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS10]] | B | SUCLG2-DT activity raises RGS10's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without SUCLG2-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[DOCK7]] | B | SUCLG2-DT activity raises DOCK7's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without SUCLG2-DT | 0.008 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[CHST3]] | B | SUCLG2-DT activity raises CHST3's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.82× lower at baseline in the lines without SUCLG2-DT | 0.020 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[SLC25A25]] | B | SUCLG2-DT activity lowers SLC25A25's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.31× higher at baseline in the lines without SUCLG2-DT | 0.025 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[DPH6-DT]] | B | SUCLG2-DT activity raises DPH6-DT's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without SUCLG2-DT | 0.028 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[NEXN]] | B | SUCLG2-DT activity raises NEXN's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without SUCLG2-DT | 0.030 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[CC2D2A]] | B | SUCLG2-DT activity raises CC2D2A's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without SUCLG2-DT | 0.035 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[ZBTB1]] | B | SUCLG2-DT activity raises ZBTB1's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without SUCLG2-DT | 0.050 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[GAS2]] | B | SUCLG2-DT activity lowers GAS2's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.60× higher at baseline in the lines without SUCLG2-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[PCNX4-DT]] | B | SUCLG2-DT activity raises PCNX4-DT's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without SUCLG2-DT | 0.069 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[MFF-DT]] | B | SUCLG2-DT activity raises MFF-DT's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without SUCLG2-DT | 0.069 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[TRIM11]] | B | SUCLG2-DT activity strengthens TRIM11's drug response | lines that do not express SUCLG2-DT (7) vs lines expressing it (41) | the lines without SUCLG2-DT respond 0.79× as strongly (z diff +0.57); strongest at Panobinostat 5 µM: 0.90x vs 1.51x (z diff +3.4) | 0.080 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.1, 16.5); signed map (30.2, -10.2). **Vector** length 108, 30.0% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.3 | +9.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +8.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.0 | -13.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.7 | -9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -11.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | SUCLG2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.1 — chr3:67,654,669-67,947,713 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SUCLG2-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49643) · Entrez [101927111](https://www.ncbi.nlm.nih.gov/gene/101927111) · Ensembl [ENSG00000241316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241316)

## Data

Gene col 14265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14265); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14265]; `tensor/DDL_lfc|DDL_z.npy` [14265]; `embed/gene_vectors.npy` [14265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14265 or target_col == 14265). Every well: [[SUCLG2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUCLG2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
