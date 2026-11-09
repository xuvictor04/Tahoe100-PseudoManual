---
symbol: "STAU2"
type: "gene"
col: 467
ensembl_id: "ENSG00000040341"
name: "staufen double-stranded RNA binding protein 2"
location: "8q21.11"
module: 222
arm: "+"
pooled_cpm: 151.7
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# STAU2

*staufen double-stranded RNA binding protein 2* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +4.6, q 0.003, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.460× (z -12.1, q 1e-30, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.279× (z -10.4, q 8e-23, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAN1A2]] (+0.56, fdr 3e-05), [[EIF4G3]] (+0.56, fdr 1e-05), [[LRP6]] (+0.54, fdr 2e-05); moves opposite to [[ZNF333]] (-0.57, fdr 2e-05), [[ZNF550]] (-0.54, fdr 3e-05), [[ARHGAP1]] (-0.54, fdr 3e-05).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NFIB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.6 | 0.003 | 27/48 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.037 | 25/49 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.074 | 28/47 (AsPC-1, NCI-H23, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.092 | 25/48 (RKO, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.26 | 12/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.460×** | -12.1 | 1e-30 | 42/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.469×** | -11.7 | 3e-29 | 42/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -10.4 | 8e-23 | 47/49 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -10.0 | 2e-21 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.539×** | -9.2 | 3e-18 | 42/48 (A-427, J82, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.337×** | -8.8 | 1e-16 | 42/48 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.600×** | -7.9 | 2e-13 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.699×** | -7.8 | 3e-13 | 33/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.592×** | -7.8 | 3e-13 | 39/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.623×** | -7.3 | 1e-11 | 36/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.677×** | -6.0 | 8e-08 | 36/48 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -5.2 | 1e-05 | 29/48 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.691×** | -4.8 | 8e-05 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -4.7 | 1e-04 | 27/49 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **0.753×** | -4.4 | 4e-04 | 29/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -4.2 | 9e-04 | 25/49 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.770×** | -4.0 | 0.002 | 29/48 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.714×** | -3.7 | 0.006 | 35/48 (LoVo, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.6 | 0.008 | 26/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.803×** | -3.2 | 0.029 | 26/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.810×** | -3.1 | 0.052 | 25/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.817×** | -3.0 | 0.060 | 22/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.691×** | -3.0 | 0.060 | 19/48 (NCI-H460, HT-29, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 124 | 0 | 13 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.344× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 210 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -23.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.227× (z -15.6) |
| [[HT-29 (line)]] | alt | 188 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -16.2) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.366× (z -12.8) |
| [[PANC-1 (line)]] | alt | 154 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -22.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.225× (z -19.6) |
| [[A-427 (line)]] | wt | 189 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.293× (z -14.5) |
| [[LoVo (line)]] | wt | 163 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.438× (z -11.3) |
| [[SW480 (line)]] | alt | 154 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.280× (z -16.4) |
| [[LOX-IMVI (line)]] | wt | 217 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -11.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.151× (z -10.7) |
| [[LS 180 (line)]] | wt | 210 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.1) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.173× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.294× (z -11.4) |
| [[A549 (line)]] | wt | 153 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -16.8) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.337× (z -10.4) |
| [[J82 (line)]] | alt | 198 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -14.1) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.226× (z -9.5) |
| [[KATO III (line)]] | alt | 162 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -18.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.409× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -11.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.160× (z -9.1) |
| [[SNU-1 (line)]] | wt | 176 | 0 | 5 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.123× (z -10.1) |
| [[COLO 205 (line)]] | alt | 142 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.412× (z -9.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.230× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 131 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -11.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.258× (z -10.0) |
| [[RKO (line)]] | wt | 302 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0922× (z -15.2) |
| [[SW1417 (line)]] | alt | 87.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.1) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.418× (z -8.9) |
| [[BT-474 (line)]] | alt | 169 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.6) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.415× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 79.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.315× (z -10.8) |
| [[SW 900 (line)]] | alt | 175 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.329× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -11.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -12.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.401× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 90.6 | 0 | 2 (1 ⚠) | — | [[vincristine (drug)]] 5 µM 0.102× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.333× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.225× (z -8.9) |
| [[SW48 (line)]] | wt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-172 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -11.1) ⚠ cell-cycle shift, explains ~73% of this change |
| [[A498 (line)]] | wt | 177 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.460× (z -8.7) |
| [[AN3 CA (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.221× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 221 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 197 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.401× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 270 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.260× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 100.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAN1A2]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[EIF4G3]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[LRP6]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[NUTM2B-AS1]] | +0.54 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[TBL1X]] | +0.54 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[CDC42BPA]] | +0.54 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[PATJ]] | +0.52 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[NBEA]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PTPN4]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[PARD3]] | +0.51 | +0.32 / +0.34 | both halves | 2e-04 |  |
| [[GKAP1]] | +0.50 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[GSK3B]] | +0.50 | +0.30 / +0.43 | both halves | 2e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF333]] | -0.57 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[ZNF550]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP1]] | -0.54 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[FAM220A]] | -0.53 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[TBCCD1]] | -0.51 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[TUT1]] | -0.51 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[PLXNB3]] | -0.50 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[COG1]] | -0.50 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ZNF17]] | -0.49 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[ZNF70]] | -0.49 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[ZNF526]] | -0.49 | -0.60 / -0.26 | both halves | 4e-04 |  |
| [[KLHL12]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIB]] | B | NFIB activity raises STAU2's level | lines that do not express NFIB (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without NFIB | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.7, 15.2); signed map (4.5, 12.0). **Vector** length 81.2, 28.9% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.8 | -12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.0 | -10.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +2.1 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.6 | +0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | -4.6 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | -4.1 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -8.8 |

## What is on record

|  |  |
|---|---|
| Name | staufen double-stranded RNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:73,420,369-73,747,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 39K2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUL3](https://www.uniprot.org/uniprotkb/Q9NUL3) (Double-stranded RNA-binding protein Staufen homolog 2):

> RNA-binding protein required for the microtubule-dependent transport of neuronal RNA from the cell body to the dendrite. As protein synthesis occurs within the dendrite, the localization of specific mRNAs to dendrites may be a prerequisite for neurite outgrowth and plasticity at sites distant from the cell body (By similarity).

**Summary**, from NCBI Gene [27067](https://www.ncbi.nlm.nih.gov/gene/27067):

> Staufen homolog 2 is a member of the family of double-stranded RNA (dsRNA)-binding proteins involved in the transport and/or localization of mRNAs to different subcellular compartments and/or organelles. These proteins are characterized by the presence of multiple dsRNA-binding domains which are required to bind RNAs having double-stranded secondary structures. Staufen homolog 2 shares 48.5% and 59.9% similarity with drosophila and human staufen, respectively. The exact function of Staufen …

**Accessions** — [HGNC:11371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11371) · Entrez [27067](https://www.ncbi.nlm.nih.gov/gene/27067) · UniProt [Q9NUL3](https://www.uniprot.org/uniprotkb/Q9NUL3) · Ensembl [ENSG00000040341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000040341)

## Data

Gene col 467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 467); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 467]; `tensor/DDL_lfc|DDL_z.npy` [467]; `embed/gene_vectors.npy` [467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 467 or target_col == 467). Every well: [[STAU2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAU2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
