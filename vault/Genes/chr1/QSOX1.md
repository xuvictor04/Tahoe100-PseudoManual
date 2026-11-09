---
symbol: "QSOX1"
type: "gene"
col: 3783
ensembl_id: "ENSG00000116260"
name: "quiescin sulfhydryl oxidase 1"
location: "1q25.2"
module: 180
arm: "+"
pooled_cpm: 125.99
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# QSOX1

*quiescin sulfhydryl oxidase 1* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.48× (z +8.0, q 7e-13, up in 30 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.46× (z +7.7, q 5e-12, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.547× (z -17.5, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P4HB]] (+0.71, fdr 7e-06), [[PDIA4]] (+0.68, fdr 1e-05), [[NXPH4]] (+0.67, fdr 2e-05); moves opposite to [[MTPAP]] (-0.69, fdr 7e-06), [[ZNF280D]] (-0.65, fdr 7e-06), [[RPP38]] (-0.65, fdr 1e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GALNT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.0 | 7e-13 | 30/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +7.7 | 5e-12 | 30/48 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +7.6 | 6e-12 | 34/48 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +6.7 | 3e-09 | 30/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.2 | 7e-08 | 26/41 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.22×** | +3.7 | 0.020 | 23/45 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +3.6 | 0.025 | 17/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.043 | 16/48 (Panc 03.27, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.3 | 0.054 | 16/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.057 | 14/48 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.061 | 19/48 (LOX-IMVI, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.086 | 13/49 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Pimitespib (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.095 | 13/47 (SK-MEL-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.547×** | -17.5 | 0e+00 | 41/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.424×** | -16.9 | 0e+00 | 45/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -9.9 | 1e-20 | 43/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -9.7 | 4e-20 | 37/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.711×** | -7.0 | 3e-10 | 33/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -6.8 | 1e-09 | 31/47 (NCI-H1573, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.784×** | -4.8 | 1e-04 | 30/49 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.871× | -4.0 | 0.004 | 15/48 (NCI-H2347, RKO, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.832×** | -3.8 | 0.009 | 23/48 (LS 180, AsPC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.824×** | -3.7 | 0.012 | 23/47 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.830×** | -3.7 | 0.012 | 24/47 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.892× | -3.3 | 0.043 | 10/48 (BT-474, NCI-H1792, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.844× | -3.2 | 0.057 | 15/48 (SW 1088, SW480, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.897× | -3.2 | 0.061 | 2/48 (NCI-H1792, HepG2/C3A) | rises with dose | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.817×** | -3.0 | 0.092 | 17/48 (A-172, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.859× | -3.0 | 0.094 | 17/48 (SK-MEL-2, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 70.8 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -14.8) |
| [[LoVo (line)]] | wt | 129 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -19.2) |
| [[PANC-1 (line)]] | alt | 80.8 | 4 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 2.15× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 300 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -25.8) |
| [[SNU-423 (line)]] | alt | 80.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +11.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.385× (z -9.8) |
| [[J82 (line)]] | alt | 112 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.07× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 128 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -18.5) |
| [[A-172 (line)]] | wt | 192 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 328 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -13.0) |
| [[COLO 205 (line)]] | alt | 188 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.374× (z -9.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -9.0) |
| [[H4 (line)]] | wt | 125 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.322× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 70.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -16.5) |
| [[HT-29 (line)]] | alt | 208 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -12.9) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.6) |
| [[KATO III (line)]] | alt | 179 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -21.6) |
| [[LS 180 (line)]] | wt | 229 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.303× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 49.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 75.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 94.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -16.8) |
| [[A549 (line)]] | wt | 108 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.8) |
| [[AN3 CA (line)]] | alt | 79.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 143 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.291× (z -13.4) |
| [[HCT15 (line)]] | alt | 164 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -21.5) |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 177 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 60.1 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.35× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.401× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 139 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.353× (z -12.9) |
| [[BT-474 (line)]] | alt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.8) |
| [[C-33 A (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -9.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 199 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.392× (z -11.0) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.379× (z -10.1) |
| [[HS-578T (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 91.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -10.1) |
| [[RKO (line)]] | wt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.3) |
| [[SNU-1 (line)]] | wt | 53.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +9.3) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[SW480 (line)]] | alt | 82.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.463× (z -10.2) |
| [[A498 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P4HB]] | +0.71 | +0.71 / +0.58 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation |
| [[PDIA4]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[NXPH4]] | +0.67 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[IGSF8]] | +0.66 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[HSP90B1]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 | pathway: Post-translational protein phosphorylation |
| [[CALU]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ADIPOR1]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PLCB3]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SUN1]] | +0.61 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[NDRG1]] | +0.61 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[FAM13A-AS1]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ALDOA]] | +0.60 | +0.64 / +0.35 | both halves | 1e-04 | pathway: HALLMARK_GLYCOLYSIS; STRING 454 |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | -0.69 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ZNF280D]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[RPP38]] | -0.65 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[METTL18]] | -0.64 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[ZFY]] | -0.64 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ARL14EP]] | -0.63 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[RNF115]] | -0.63 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[SENP1]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CPLANE1]] | -0.62 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[MIER3]] | -0.62 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity raises QSOX1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without GALNT3 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[LIMCH1]] | B | LIMCH1 activity raises QSOX1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without LIMCH1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[IL1RAP]] | B | IL1RAP activity raises QSOX1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.91× lower at baseline in the lines without IL1RAP | 0.040 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[NXPH4]] | B | NXPH4 activity lowers QSOX1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without NXPH4 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers QSOX1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NDRG1]] | B | NDRG1 activity raises QSOX1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without NDRG1 | 0.095 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.7, 5.2); signed map (-30.5, 22.3). **Vector** length 134, 39.2% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.6 | +7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.5 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +2.6 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.0 | -16.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.0 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -17.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.2 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | quiescin sulfhydryl oxidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:180,154,869-180,204,030 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously QSCN6 |
| Gene groups (HGNC) | Flavoproteins |
| Hallmark sets | GLYCOLYSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O00391](https://www.uniprot.org/uniprotkb/O00391) (Sulfhydryl oxidase 1):

> Catalyzes the oxidation of sulfhydryl groups in peptide and protein thiols to disulfides with the reduction of oxygen to hydrogen peroxide. Plays a role in disulfide bond formation in a variety of extracellular proteins. In fibroblasts, required for normal incorporation of laminin into the extracellular matrix, and thereby for normal cell-cell adhesion and cell migration.

**Summary**, from NCBI Gene [5768](https://www.ncbi.nlm.nih.gov/gene/5768):

> This gene encodes a protein that contains domains of thioredoxin and ERV1, members of two long-standing gene families. The gene expression is induced as fibroblasts begin to exit the proliferative cycle and enter quiescence, suggesting that this gene plays an important role in growth regulation. Two transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9756) · Entrez [5768](https://www.ncbi.nlm.nih.gov/gene/5768) · UniProt [O00391](https://www.uniprot.org/uniprotkb/O00391) · Ensembl [ENSG00000116260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116260)

## Data

Gene col 3783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3783); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3783]; `tensor/DDL_lfc|DDL_z.npy` [3783]; `embed/gene_vectors.npy` [3783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3783 or target_col == 3783). Every well: [[QSOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QSOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
