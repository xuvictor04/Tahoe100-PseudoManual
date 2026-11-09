---
symbol: "SDHAF3"
type: "gene"
col: 12252
ensembl_id: "ENSG00000196636"
name: "succinate dehydrogenase complex assembly factor 3"
location: "7q21.3"
module: 65
arm: "+"
pooled_cpm: 13.31
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# SDHAF3

*succinate dehydrogenase complex assembly factor 3* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.50× (z +21.9, q 0e+00, up in 44 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 4.38× (z +21.5, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.470× (z -15.5, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6]] (+0.75, fdr 7e-06), [[SKP2]] (+0.73, fdr 7e-06), [[METAP1]] (+0.72, fdr 7e-06); moves opposite to [[ANKHD1-EIF4EBP3]] (-0.74, fdr 1e-05), [[AKT1S1]] (-0.72, fdr 1e-05), [[LINC00571]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPD1L]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **4.50×** | +21.9 | 0e+00 | 44/45 (A498, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.38×** | +21.5 | 0e+00 | 45/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.25×** | +21.0 | 0e+00 | 45/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.79×** | +15.0 | 0e+00 | 44/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +11.7 | 1e-29 | 38/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.97×** | +9.9 | 4e-21 | 39/45 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.82×** | +8.8 | 2e-16 | 26/37 (HEC-1-A, LoVo, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.88×** | +8.0 | 6e-14 | 35/46 (AsPC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +7.1 | 9e-11 | 24/45 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.65×** | +7.0 | 1e-10 | 24/38 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.58×** | +6.5 | 6e-09 | 15/22 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.60×** | +6.4 | 9e-09 | 19/29 (A549, LS 180, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +6.2 | 2e-08 | 22/45 (A549, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +4.8 | 6e-05 | 16/45 (LS 180, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.38×** | +4.7 | 1e-04 | 14/45 (A498, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 15/45 (C32, PANC-1, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 15/45 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.012 | 7/46 (A549, LS 180, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.045 | 5/45 (C32, HEC-1-A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.068 | 6/44 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.470×** | -15.5 | 0e+00 | 38/44 (SK-MEL-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -8.6 | 3e-15 | 28/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -6.0 | 4e-07 | 18/45 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -5.9 | 6e-07 | 19/45 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -5.7 | 1e-06 | 20/45 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.706×** | -5.0 | 5e-05 | 20/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.532×** | -4.8 | 1e-04 | 19/45 (RKO, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 3e-04 | 13/45 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -4.2 | 0.002 | 6/46 (HT-29, CHP-212, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.003 | 14/45 (KATO III, SW480, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.772×** | -3.7 | 0.009 | 13/45 (COLO 205, C32, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.773×** | -3.7 | 0.010 | 18/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.638×** | -3.4 | 0.028 | 10/45 (H4, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.640×** | -3.4 | 0.028 | 5/45 (A-427, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.784×** | -3.4 | 0.028 | 14/45 (H4, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.046 | 15/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 54.1 | 3 (1 ⚠) | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.98× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.51× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 15.8 | 3 (1 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.48× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.21× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -13.4) |
| [[PANC-1 (line)]] | alt | 13.5 | 3 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 4.14× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 9.43 | 3 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 12.1× (z +11.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 8.99× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -13.0) |
| [[A498 (line)]] | wt | 11.5 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 7.25× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.38× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 2 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.01× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.54× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -14.2) |
| [[SW480 (line)]] | alt | 18.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.88× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 2 (1 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 4.46× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 15.4 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 5.19× (z +10.4) | — |
| [[LoVo (line)]] | wt | 7.77 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.25× (z +10.0) | — |
| [[A-427 (line)]] | wt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -9.6) |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0827× (z -9.2) |
| [[H4 (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.0) |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0622× (z -10.2) |
| [[HOP62 (line)]] | alt | 6.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.5) |
| [[Hs 766T (line)]] | wt | 5.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -10.9) |
| [[HT-29 (line)]] | alt | 6.95 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.72× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 8.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.6) |
| [[RKO (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -14.4) |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.110× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.81 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0815× (z -10.8) |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -10.6) |
| [[A-172 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | +0.75 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[SKP2]] | +0.73 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[METAP1]] | +0.72 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.71 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[ATG4C]] | +0.70 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[WASF3]] | +0.69 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ABHD10]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SDHB]] | +0.68 | +0.66 / +0.51 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 930 |
| [[ACTR5]] | +0.67 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.67 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[POGLUT2]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TBC1D2B]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKHD1-EIF4EBP3]] | -0.74 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.72 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.70 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | -0.69 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[KANSL1L]] | -0.68 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ZHX2]] | -0.68 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[FAM151B]] | -0.67 | -0.65 / -0.37 | both halves | 7e-05 |  |
| [[LINC01004]] | -0.67 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.67 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CFAP70]] | -0.67 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[MCF2]] | -0.66 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.66 | -0.58 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPD1L]] | C | GPD1L activity raises SDHAF3's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without GPD1L | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.7, -8.8); signed map (-37.7, -12.8). **Vector** length 99.0, 23.8% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +21.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +11.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +21.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.3 | +21.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.3 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.9 | -15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.3 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | succinate dehydrogenase complex assembly factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:97,117,698-97,181,763 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DC11, Sdh7, LYRM10; previously ACN9 |
| Gene groups (HGNC) | LYR motif containing; Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRP4](https://www.uniprot.org/uniprotkb/Q9NRP4) (Succinate dehydrogenase assembly factor 3, mitochondrial):

> Plays an essential role in the assembly of succinate dehydrogenase (SDH), an enzyme complex (also referred to as respiratory complex II) that is a component of both the tricarboxylic acid (TCA) cycle and the mitochondrial electron transport chain, and which couples the oxidation of succinate to fumarate with the reduction of ubiquinone (coenzyme Q) to ubiquinol. Promotes maturation of the iron-sulfur protein subunit SDHB of the SDH catalytic dimer, protecting it from the deleterious effects of …

**Summary**, from NCBI Gene [57001](https://www.ncbi.nlm.nih.gov/gene/57001):

> Predicted to be involved in mitochondrial respiratory chain complex II assembly and regulation of gluconeogenesis. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21752) · Entrez [57001](https://www.ncbi.nlm.nih.gov/gene/57001) · UniProt [Q9NRP4](https://www.uniprot.org/uniprotkb/Q9NRP4) · Ensembl [ENSG00000196636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196636)

## Data

Gene col 12252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12252); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12252]; `tensor/DDL_lfc|DDL_z.npy` [12252]; `embed/gene_vectors.npy` [12252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12252 or target_col == 12252). Every well: [[SDHAF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDHAF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
