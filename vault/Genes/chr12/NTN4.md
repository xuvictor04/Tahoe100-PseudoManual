---
symbol: "NTN4"
type: "gene"
col: 1081
ensembl_id: "ENSG00000074527"
name: "netrin 4"
location: "12q22"
module: 155
arm: "+"
pooled_cpm: 73.99
n_lines_expressing: 32
n_dd_up: 29
n_dd_down: 20
n_dd_up_clean: 23
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 18
direction_downstream: 28
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# NTN4

*netrin 4* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.75× (z +7.7, q 7e-12, up in 21 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.266× (z -12.8, q 7e-35, down in 30 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBPMS]] (+0.66, fdr 1e-05), [[LINC02057]] (+0.59, fdr 1e-05), [[LINC02015]] (+0.56, fdr 3e-05); moves opposite to [[NBPF3]] (-0.53, fdr 7e-05), [[ANKRD36B]] (-0.47, fdr 5e-05), [[LINC01237]] (-0.46, fdr 5e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[NOVA1]] → it (grade B ⚠); 28 go from it, the strongest it → [[THOC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.7 | 7e-12 | 21/30 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.9 | 2e-09 | 12/31 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.3 | 6e-08 | 15/31 (hTERT-HPNE, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +4.9 | 2e-04 | 16/30 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.8 | 2e-04 | 17/30 (Hs 766T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.4 | 0.001 | 12/26 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.001 | 18/30 (hTERT-HPNE, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 0.001 | 21/29 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.002 | 12/32 (LoVo, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.003 | 16/29 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +4.0 | 0.003 | 14/32 (hTERT-HPNE, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.003 | 20/30 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.003 | 21/31 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.52×** | +3.9 | 0.004 | 20/29 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.005 | 14/31 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.006 | 17/31 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.013 | 9/31 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.018 | 7/31 (SW 900, A-172, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.018 | 11/31 (HEC-1-A, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.266×** | -12.8 | 7e-35 | 30/30 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.284×** | -12.2 | 1e-31 | 30/30 (NCI-H1792, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.299×** | -11.7 | 3e-29 | 29/30 (BT-474, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.357×** | -10.0 | 3e-21 | 26/29 (NCI-H1792, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.424×** | -8.0 | 2e-13 | 28/30 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.445×** | -7.8 | 5e-13 | 26/30 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.579×** | -7.5 | 7e-12 | 25/30 (NCI-H460, BT-474, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.468×** | -7.3 | 1e-11 | 20/30 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.575×** | -5.4 | 5e-06 | 21/30 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.598×** | -5.0 | 4e-05 | 20/30 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.615×** | -4.7 | 1e-04 | 19/30 (BT-474, HT-29, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.741×** | -4.1 | 0.002 | 13/30 (A498, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.566×** | -3.9 | 0.004 | 15/30 (NCI-H2030, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.667×** | -3.9 | 0.004 | 14/30 (BT-474, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -3.9 | 0.004 | 19/30 (NCI-H2030, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -3.8 | 0.005 | 17/30 (HT-29, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -3.1 | 0.059 | 15/30 (BT-474, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.545×** | -3.1 | 0.064 | 17/30 (NCI-H460, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 235 | 0 | 21 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0540× (z -19.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0385× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 301 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0245× (z -18.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0749× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 212 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -20.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0776× (z -15.9) |
| [[SW 900 (line)]] | alt | 266 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0460× (z -13.8) |
| [[HT-29 (line)]] | alt | 257 | 1 | 7 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.81× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.0326× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0487× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 178 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0730× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0960× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 377 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0881× (z -15.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0957× (z -15.3) |
| [[A498 (line)]] | wt | 37.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -17.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.129× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 64.9 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.183× (z -9.0) |
| [[A549 (line)]] | wt | 131 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0795× (z -14.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0725× (z -10.8) |
| [[LoVo (line)]] | wt | 32.2 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.166× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.191× (z -11.7) |
| [[KATO III (line)]] | alt | 46.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -10.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.168× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 97.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.161× (z -10.8) |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.209× (z -9.3) |
| [[SNU-423 (line)]] | alt | 84.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 48.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.155× (z -8.6) |
| [[Hs 766T (line)]] | wt | 59.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.194× (z -10.0) |
| [[A-172 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 123 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 56.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.194× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0411× (z -9.0) |
| [[A-427 (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.90 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBPMS]] | +0.66 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[LINC02057]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[LINC02015]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[RAB31]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TMEM217]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SERPINB4]] | +0.54 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CLIP1]] | +0.53 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[CYP1B1-AS1]] | +0.52 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[KYNU]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[SERPINB3]] | +0.51 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[FGB]] | +0.51 | +0.50 / +0.41 | both halves | 4e-05 | pathway: Extracellular matrix organization |
| [[LINC01348]] | +0.50 | +0.52 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.53 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ANKRD36B]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[LINC01237]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SFXN1]] | -0.46 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[THOC1]] | -0.45 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[RBFA]] | -0.44 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ZNF589]] | -0.44 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[HSPA12A]] | -0.44 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[ASIC1]] | -0.44 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ZNF215]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.43 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[ANKRD36]] | -0.43 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 12, C 6. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOVA1]] | B | NOVA1 activity raises NTN4's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 3.40× lower at baseline in the lines without NOVA1 | 0.015 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13 |
| [[LURAP1L]] | B | LURAP1L activity raises NTN4's level | lines that do not express LURAP1L (12) vs lines expressing it (38) | 3.86× lower at baseline in the lines without LURAP1L | 0.023 | ⚠ within organs, on part of the lines; also absent: KLF4; maybe low, not absent |
| [[CARD6]] | B | CARD6 activity raises NTN4's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 2.57× lower at baseline in the lines without CARD6 | 0.029 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[SIPA1L2]] | B | SIPA1L2 activity raises NTN4's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 2.29× lower at baseline in the lines without SIPA1L2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NTN4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RBPMS]] | B | RBPMS activity raises NTN4's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 3.10× lower at baseline in the lines without RBPMS | 0.038 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[SERPINB3]] | B | SERPINB3 activity raises NTN4's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 4.20× lower at baseline in the lines without SERPINB3 | 0.041 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A |
| [[CP]] | B | CP activity raises NTN4's level | lines that do not express CP (39) vs lines expressing it (11) | 3.74× lower at baseline in the lines without CP | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[KYNU]] | B | KYNU activity raises NTN4's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.29× lower at baseline in the lines without KYNU | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[LINC02889]] | B | LINC02889 activity raises NTN4's level | lines that do not express LINC02889 (12) vs lines expressing it (38) | 2.78× lower at baseline in the lines without LINC02889 | 0.084 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, SAMD5, ENSG00000226640; maybe low, not absent |
| [[ARHGAP42]] | B | ARHGAP42 activity raises NTN4's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without ARHGAP42 | 0.091 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[RDH10]] | B | RDH10 activity raises NTN4's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 3.30× lower at baseline in the lines without RDH10 | 0.097 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 25, C 3. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THOC1]] | B | NTN4 activity lowers THOC1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.57× higher at baseline in the lines without NTN4 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[RMND1]] | B | NTN4 activity lowers RMND1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.46× higher at baseline in the lines without NTN4 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[LINC02889]] | B | NTN4 activity raises LINC02889's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.27× lower at baseline in the lines without NTN4 | 0.009 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[OPN3]] | B | NTN4 activity raises OPN3's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without NTN4 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[CARD6]] | B | NTN4 activity raises CARD6's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.23× lower at baseline in the lines without NTN4 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[LINC01237]] | B | NTN4 activity lowers LINC01237's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.84× higher at baseline in the lines without NTN4 | 0.014 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[LINC02284]] | B | NTN4 activity raises LINC02284's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without NTN4 | 0.017 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[ZNF589]] | B | NTN4 activity lowers ZNF589's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.05× higher at baseline in the lines without NTN4 | 0.018 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[PDLIM5]] | B | NTN4 activity raises PDLIM5's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without NTN4 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[RBPMS]] | B | NTN4 activity raises RBPMS's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without NTN4 | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[ITSN1]] | B | NTN4 activity lowers ITSN1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.21× higher at baseline in the lines without NTN4 | 0.029 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[SIPA1L2]] | B | NTN4 activity raises SIPA1L2's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without NTN4 | 0.029 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.8, 21.2); signed map (48.3, 21.7). **Vector** length 112, 36.0% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.7 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.2 | -11.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.9 | -12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -12.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | netrin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:95,657,807-95,791,189 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Netrins |
| Reactome | 5 pathways, smallest: Netrin-1 signaling; Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB63](https://www.uniprot.org/uniprotkb/Q9HB63) (Netrin-4):

> May play an important role in neural, kidney and vascular development. Promotes neurite elongation from olfactory bulb explants.

**Summary**, from NCBI Gene [59277](https://www.ncbi.nlm.nih.gov/gene/59277):

> This gene encodes a member of the netrin family of proteins, which function in various biological processes including axon guidance, tumorogenesis, and angiogenesis. Netrins are laminin-related proteins that have an N-terminal laminin-type domain, epidermal growth factor-like repeat domain, and a positively charged heparin-binding domain at the C-terminus. The protein encoded by this gene is involved in processes including neurite growth and migration, angiogenesis and mural cell adhesion to …

**Accessions** — [HGNC:13658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13658) · Entrez [59277](https://www.ncbi.nlm.nih.gov/gene/59277) · UniProt [Q9HB63](https://www.uniprot.org/uniprotkb/Q9HB63) · Ensembl [ENSG00000074527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074527)

## Data

Gene col 1081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1081); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1081]; `tensor/DDL_lfc|DDL_z.npy` [1081]; `embed/gene_vectors.npy` [1081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1081 or target_col == 1081). Every well: [[NTN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
