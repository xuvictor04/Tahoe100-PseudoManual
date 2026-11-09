---
symbol: "RAB22A"
type: "gene"
col: 4499
ensembl_id: "ENSG00000124209"
name: "RAB22A, member RAS oncogene family"
location: "20q13.32"
module: 17
arm: "-"
pooled_cpm: 177.45
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# RAB22A

*RAB22A, member RAS oncogene family* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +11.3, q 6e-27, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.696× (z -8.1, q 1e-13, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.729× (z -6.8, q 1e-09, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SWT1]] (+0.64, fdr 1e-05), [[KLC1]] (+0.62, fdr 7e-06), [[SLC25A53]] (+0.58, fdr 1e-05); moves opposite to [[EHMT2]] (-0.58, fdr 1e-05), [[SLC25A12]] (-0.58, fdr 1e-05), [[EBAG9]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +11.3 | 6e-27 | 45/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +10.0 | 6e-21 | 43/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +9.3 | 2e-18 | 42/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +6.9 | 7e-10 | 33/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.8 | 8e-10 | 29/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +5.3 | 9e-06 | 32/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +4.6 | 3e-04 | 30/48 (A498, BT-474, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.003 | 24/47 (H4, RKO, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.20×** | +4.0 | 0.004 | 23/47 (H4, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +3.9 | 0.006 | 20/48 (SHP-77, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.012 | 18/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.015 | 19/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.5 | 0.024 | 16/47 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.3 | 0.042 | 16/49 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +3.2 | 0.061 | 19/47 (SHP-77, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.696×** | -8.1 | 1e-13 | 36/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.697×** | -8.1 | 1e-13 | 36/48 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.718×** | -7.5 | 2e-11 | 35/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.729×** | -6.8 | 1e-09 | 30/48 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.735×** | -6.4 | 2e-08 | 26/45 (SNU-1, A549, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.787×** | -5.4 | 7e-06 | 33/48 (CHP-212, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.788×** | -5.1 | 2e-05 | 24/44 (SNU-1, BT-474, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.793×** | -5.0 | 3e-05 | 31/48 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.808×** | -4.8 | 1e-04 | 29/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.811×** | -4.7 | 1e-04 | 25/48 (A-427, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.816×** | -4.6 | 3e-04 | 27/49 (NCI-H23, BT-474, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.829×** | -4.2 | 0.001 | 25/48 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -4.0 | 0.003 | 13/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 0.843× | -3.8 | 0.005 | 22/48 (SW 900, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.845× | -3.8 | 0.006 | 19/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.847× | -3.7 | 0.007 | 19/48 (BT-474, COLO 205, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.738×** | -3.6 | 0.011 | 23/49 (A498, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.874× | -3.0 | 0.072 | 15/48 (NCI-H1792, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 831 | 5 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SNU-1 (line)]] | wt | 136 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.571× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 218 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.71× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.464× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 194 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +13.0) | — |
| [[LoVo (line)]] | wt | 124 | 1 | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.94× (z +9.0) | [[Tucidinostat (drug)]] 5 µM 0.607× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 150 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +15.3) | — |
| [[A549 (line)]] | wt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.471× (z -9.4) |
| [[COLO 205 (line)]] | alt | 224 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 150 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 212 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SW1417 (line)]] | alt | 256 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.550× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 154 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.479× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 334 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 86.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.561× (z -8.8) |
| [[A498 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.546× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 349 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 272 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[J82 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LS 180 (line)]] | wt | 116 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 227 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -15.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.508× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.136× (z -12.9) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 119 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +12.5) | — |
| [[RKO (line)]] | wt | 185 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 133 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 201 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SWT1]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[KLC1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A53]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MROH1]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[RUBCN]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[RABGEF1]] | +0.52 | +0.54 / +0.57 | both halves | 1e-05 | STRING 938 |
| [[LRP10]] | +0.51 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SLC35F5]] | +0.51 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.51 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MAP1LC3B]] | +0.51 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[UBE2F-SCLY]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SENP5]] | +0.51 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHMT2]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SLC25A12]] | -0.58 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[EBAG9]] | -0.57 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ZNF45]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[FAM133B]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[RIOK2]] | -0.56 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[GEMIN2]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[RP9]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[EXOSC9]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DIXDC1]] | -0.54 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[KBTBD6]] | -0.54 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[KCTD3]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers RAB22A's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises RAB22A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-12.8, -0.3); signed map (-14.0, 17.1). **Vector** length 112, 36.4% of its response variance represented; |z| ≥ 3 in 1,395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.9 | +3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.3 | +10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.8 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -6.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.8 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB22A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,309,715-58,367,507 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL26](https://www.uniprot.org/uniprotkb/Q9UL26) (Ras-related protein Rab-22A):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB22A plays a role in endocytosis and intracellular protein transport. Mediates trafficking of transferrin/TF from …

**Summary**, from NCBI Gene [57403](https://www.ncbi.nlm.nih.gov/gene/57403):

> The protein encoded by this gene is a member of the RAB family of small GTPases. The GTP-bound form of the encoded protein has been shown to interact with early-endosomal antigen 1, and may be involved in the trafficking of and interaction between endosomal compartments. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9764) · Entrez [57403](https://www.ncbi.nlm.nih.gov/gene/57403) · UniProt [Q9UL26](https://www.uniprot.org/uniprotkb/Q9UL26) · Ensembl [ENSG00000124209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124209)

## Data

Gene col 4499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4499); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4499]; `tensor/DDL_lfc|DDL_z.npy` [4499]; `embed/gene_vectors.npy` [4499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4499 or target_col == 4499). Every well: [[RAB22A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB22A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
