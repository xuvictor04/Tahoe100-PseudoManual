---
symbol: "MIR4713HG"
type: "gene"
col: 15179
ensembl_id: "ENSG00000259240"
name: "MIR4713 host gene"
location: "15q21.2"
module: 27
arm: "+"
pooled_cpm: 58.26
n_lines_expressing: 20
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 19
direction_downstream: 24
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# MIR4713HG

*MIR4713 host gene* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +10.9, q 8e-25, up in 0 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.252× (z -18.0, q 0e+00, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLDN]] (+0.86, fdr 7e-06, ⚠ same locus), [[DLEU1]] (+0.71, fdr 7e-06), [[LINC00649]] (+0.66, fdr 1e-05), [[ABO]] (+0.64, fdr 7e-06); moves opposite to [[TSHZ3-AS1]] (-0.52, fdr 2e-05), [[TSHZ3]] (-0.48, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[SORBS2]] → it (grade B ⚠); 24 go from it, the strongest it → [[DLEU1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +10.9 | 8e-25 | 0/19 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.7 | 5e-12 | 0/19 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.28×** | +4.6 | 7e-04 | 14/18 (KATO III, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +4.5 | 1e-03 | 13/18 (SW480, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.4 | 1e-03 | 0/17 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 0/19 | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.013 | 7/18 (J82, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.019 | 10/18 (KATO III, J82, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.031 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.033 | 3/18 (J82, SW48, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.049 | 14/18 (Hs 766T, SW480, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.049 | 14/18 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.052 | 0/19 | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.075 | 8/18 (SW480, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.075 | 0/20 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.084 | 8/18 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.252×** | -18.0 | 0e+00 | 18/18 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.361×** | -13.3 | 5e-38 | 18/18 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.535×** | -11.5 | 1e-28 | 18/18 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.492×** | -9.3 | 3e-18 | 18/18 (KATO III, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.493×** | -9.3 | 3e-18 | 18/18 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.519×** | -8.6 | 1e-15 | 17/18 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.534×** | -8.2 | 2e-14 | 17/18 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.586×** | -7.0 | 2e-10 | 17/18 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.605×** | -6.3 | 2e-08 | 14/18 (COLO 205, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.621×** | -6.2 | 3e-08 | 16/18 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -5.4 | 3e-06 | 18/18 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -5.4 | 3e-06 | 12/18 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.613×** | -5.3 | 5e-06 | 16/18 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.507×** | -4.6 | 1e-04 | 15/19 (SHP-77, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.5 | 3e-04 | 9/18 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.707×** | -4.3 | 5e-04 | 9/18 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.755×** | -3.7 | 0.007 | 10/18 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.690×** | -3.5 | 0.015 | 7/18 (MIA PaCa-2, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.017 | 17/18 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.616×** | -3.3 | 0.022 | 16/18 (KATO III, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.789×** | -3.1 | 0.043 | 0/18 | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.779×** | -3.0 | 0.053 | 1/18 (HepG2/C3A) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **0.803×** | -2.9 | 0.088 | 0/19 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 228 | 0 | 23 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0904× (z -27.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0837× (z -20.2) |
| [[MIA PaCa-2 (line)]] | alt | 179 | 0 | 18 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 202 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0467× (z -33.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -16.6) |
| [[KATO III (line)]] | alt | 118 | 0 | 12 (8 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0603× (z -24.2) |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -15.1) |
| [[HT-29 (line)]] | alt | 245 | 0 | 11 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.104× (z -17.0) |
| [[Hs 766T (line)]] | wt | 73.6 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0996× (z -15.9) |
| [[COLO 205 (line)]] | alt | 94.6 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -19.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0895× (z -15.8) |
| [[LoVo (line)]] | wt | 53.8 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -9.0) |
| [[LS 180 (line)]] | wt | 78.7 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -11.8) |
| [[SW48 (line)]] | wt | 137 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0747× (z -15.5) |
| [[SW480 (line)]] | alt | 116 | 0 | 8 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.126× (z -16.5) |
| [[SHP-77 (line)]] | alt | 243 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -19.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.146× (z -19.1) |
| [[Panc 03.27 (line)]] | alt | 59.8 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.103× (z -15.0) |
| [[PANC-1 (line)]] | alt | 35.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.3) |
| [[HCT15 (line)]] | alt | 204 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0828× (z -14.6) |
| [[J82 (line)]] | alt | 39.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.243× (z -9.4) |
| [[SW1417 (line)]] | alt | 31.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.55 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.89 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLDN]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 | ⚠ same locus (47.7 kb, same strand: neighbours can correlate without regulation) |
| [[DLEU1]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[LINC00649]] | +0.66 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ABO]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[B3GAT1-DT]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[KCNE3]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[LINC02058]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[UGT1A8]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[UGT1A9]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PROM1]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[AXIN2]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[BANK1]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TNFRSF14-AS1]] | +0.59 | +0.61 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSHZ3-AS1]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TSHZ3]] | -0.48 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORBS2]] | B | SORBS2 activity raises MIR4713HG's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 3.93× lower at baseline in the lines without SORBS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR |
| [[GLDN]] | C | GLDN activity raises MIR4713HG's level | lines that do not express GLDN (25) vs lines expressing it (25) | 7.62× lower at baseline in the lines without GLDN | 1e-04 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595; co-absent with the target |
| [[PIP5K1B]] | C | PIP5K1B activity raises MIR4713HG's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 5.64× lower at baseline in the lines without PIP5K1B | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises MIR4713HG's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 4.38× lower at baseline in the lines without AXIN2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[WDR72]] | C | WDR72 activity raises MIR4713HG's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 3.69× lower at baseline in the lines without WDR72 | 0.037 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[ASB4]] | C | ASB4 activity raises MIR4713HG's level | lines that do not express ASB4 (31) vs lines expressing it (19) | 3.94× lower at baseline in the lines without ASB4 | 0.044 | ⚠ within organs, on part of the lines; also absent: ST18, PCK1, FAM3D; co-absent with the target |
| [[CHN2]] | C | CHN2 activity raises MIR4713HG's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 4.08× lower at baseline in the lines without CHN2 | 0.049 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15; co-absent with the target |
| [[UGT1A8]], [[UGT1A9]] | C | UGT1A8, UGT1A9 activity raises MIR4713HG's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 3.80× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.051 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[ST18]] | C | ST18 activity raises MIR4713HG's level | lines that do not express ST18 (39) vs lines expressing it (11) | 4.44× lower at baseline in the lines without ST18 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[LINC00649]] | C | LINC00649 activity raises MIR4713HG's level | lines that do not express LINC00649 (25) vs lines expressing it (25) | 2.99× lower at baseline in the lines without LINC00649 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000287923, RMST, SERPINF1; maybe low, not absent; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises MIR4713HG's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 4.66× lower at baseline in the lines without LGR5 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[LINC02058]] | C | LINC02058 activity raises MIR4713HG's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without LINC02058 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 9, C 15. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLEU1]] | B | MIR4713HG activity raises DLEU1's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 4.40× lower at baseline in the lines without MIR4713HG | 0.002 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[NDUFA4L2]] | B | MIR4713HG activity raises NDUFA4L2's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without MIR4713HG | 0.009 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[BANK1]] | B | MIR4713HG activity raises BANK1's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.38× lower at baseline in the lines without MIR4713HG | 0.017 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[ANK3]] | B | MIR4713HG activity raises ANK3's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without MIR4713HG | 0.024 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[FGD3]] | B | MIR4713HG activity raises FGD3's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without MIR4713HG | 0.035 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[SORBS2]] | B | MIR4713HG activity raises SORBS2's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.24× lower at baseline in the lines without MIR4713HG | 0.062 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[ZNF503-AS1]] | B | MIR4713HG activity raises ZNF503-AS1's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.04× lower at baseline in the lines without MIR4713HG | 0.062 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[MGST2]] | B | MIR4713HG activity raises MGST2's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without MIR4713HG | 0.064 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[KCTD14]] | B | MIR4713HG activity raises KCTD14's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without MIR4713HG | 0.0996 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA |
| [[GLDN]] | C | MIR4713HG activity raises GLDN's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 3.71× lower at baseline in the lines without MIR4713HG | 5e-04 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA; co-absent with the target |
| [[PRR15-DT]] | C | MIR4713HG activity raises PRR15-DT's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 3.27× lower at baseline in the lines without MIR4713HG | 0.028 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA; co-absent with the target |
| [[LINC00649]] | C | MIR4713HG activity raises LINC00649's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without MIR4713HG | 0.031 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, 45.4); signed map (59.1, 16.7). **Vector** length 91.9, 37.5% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +5.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.6 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.5 | -18.0 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.3 | -5.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -4.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MIR4713 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q21.2 — chr15:51,037,488-51,293,912 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-108K3.1 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53124](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53124) · Entrez [109729174](https://www.ncbi.nlm.nih.gov/gene/109729174) · Ensembl [ENSG00000259240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259240)

## Data

Gene col 15179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15179); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15179]; `tensor/DDL_lfc|DDL_z.npy` [15179]; `embed/gene_vectors.npy` [15179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15179 or target_col == 15179). Every well: [[MIR4713HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR4713HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
