---
symbol: "UGGT2"
type: "gene"
col: 2259
ensembl_id: "ENSG00000102595"
name: "UDP-glucose glycoprotein glucosyltransferase 2"
location: "13q32.1"
module: 59
arm: "-"
pooled_cpm: 140.26
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# UGGT2

*UDP-glucose glycoprotein glucosyltransferase 2* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +8.7, q 3e-15, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.454× (z -6.1, q 8e-07, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD14CP-1]] (+0.67, fdr 7e-06), [[RANBP17]] (+0.66, fdr 7e-06), [[HNRNPAB]] (+0.65, fdr 7e-06); moves opposite to [[OGA]] (-0.61, fdr 1e-05), [[CCDC115]] (-0.61, fdr 1e-05), [[THAP8]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +8.7 | 3e-15 | 45/48 (SW480, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +8.0 | 3e-13 | 33/49 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.66×** | +7.4 | 2e-11 | 41/48 (CFPAC-1, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +7.2 | 1e-10 | 44/48 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.50×** | +6.0 | 3e-07 | 36/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.52×** | +5.9 | 4e-07 | 35/48 (SW480, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +5.8 | 5e-07 | 41/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.7 | 1e-06 | 30/48 (NCI-H2347, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.6 | 1e-06 | 35/48 (HT-29, LS 180, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.46×** | +5.5 | 2e-06 | 32/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.3 | 5e-06 | 32/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 32/49 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +3.7 | 0.008 | 27/47 (SW 900, NCI-H23, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.008 | 30/49 (CFPAC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.023 | 24/48 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.060 | 25/48 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.068 | 23/48 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.454×** | -6.1 | 8e-07 | 37/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.489×** | -5.5 | 1e-05 | 41/47 (SNU-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.770×** | -3.9 | 0.021 | 31/48 (RPMI-7951, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.775×** | -3.8 | 0.021 | 28/48 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.7 | 0.021 | 22/48 (RKO, A-427, …) | all doses, flat | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.626×** | -3.6 | 0.026 | 25/48 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.842× | -3.6 | 0.026 | 23/48 (HS-578T, A498, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.785×** | -3.6 | 0.026 | 27/48 (KATO III, C32, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -3.1 | 0.13 | 18/48 (AsPC-1, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 37.8 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +13.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 269 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.77× (z +9.1) | — |
| [[A498 (line)]] | wt | 193 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 94.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.64× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.02× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 146 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.84× (z +8.9) | — |
| [[LoVo (line)]] | wt | 141 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.204× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 44.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 90.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.96× (z +9.7) | — |
| [[SW480 (line)]] | alt | 250 | 3 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 239 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 270 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 171 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.386× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 183 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 63.0 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 80.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +12.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 113 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.09× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 175 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 113 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.77× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 71.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 238 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.227× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 268 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.77× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 79.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 174 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 114 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 99.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP-1]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[RANBP17]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[HNRNPAB]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.65 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[TTL]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SPCS3]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[NBPF20]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[BICD1]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[HLCS]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ENOX2]] | +0.60 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[GART]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGA]] | -0.61 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[THAP8]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[DBP]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZNF14]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SNX2]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ASB8]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CCNG2]] | -0.55 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ZNF44]] | -0.55 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[USP30]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UGGT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.1, -34.5); signed map (3.1, -50.9). **Vector** length 141, 50.5% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.9 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +8.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.1 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.3 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.1 | -3.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.3 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.8 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | UDP-glucose glycoprotein glucosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:95,801,580-96,053,482 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11485, HUGT2, FLJ10873, MGC150689, MGC87276, MGC117360; previously UGCGL2 |
| Gene groups (HGNC) | UDP-glucose glycoprotein glucosyltransferases |
| Reactome | 4 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYU1](https://www.uniprot.org/uniprotkb/Q9NYU1) (UDP-glucose:glycoprotein glucosyltransferase 2):

> Recognizes glycoproteins with minor folding defects. Reglucosylates single N-glycans near the misfolded part of the protein, thus providing quality control for protein folding in the endoplasmic reticulum. Reglucosylated proteins are recognized by calreticulin for recycling to the endoplasmic reticulum and refolding or degradation.

**Summary**, from NCBI Gene [55757](https://www.ncbi.nlm.nih.gov/gene/55757):

> UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:15664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15664) · Entrez [55757](https://www.ncbi.nlm.nih.gov/gene/55757) · UniProt [Q9NYU1](https://www.uniprot.org/uniprotkb/Q9NYU1) · Ensembl [ENSG00000102595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102595)

## Data

Gene col 2259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2259); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2259]; `tensor/DDL_lfc|DDL_z.npy` [2259]; `embed/gene_vectors.npy` [2259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2259 or target_col == 2259). Every well: [[UGGT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGGT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
