---
symbol: "ATP11A"
type: "gene"
col: 895
ensembl_id: "ENSG00000068650"
name: "ATPase phospholipid transporting 11A"
location: "13q34"
module: 195
arm: "+"
pooled_cpm: 193.6
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# ATP11A

*ATPase phospholipid transporting 11A* — 13q34

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 1.76×; ⚠ cell-cycle shift, explains ~0% of this change); [[PF-06260933 (drug)]] 5 µM in 1 line (SW480 2.42×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.467× (z -18.9, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT7]] (+0.62, fdr 1e-05), [[BRI3BP]] (+0.61, fdr 1e-05), [[RCOR1]] (+0.60, fdr 1e-05); moves opposite to [[WASHC3]] (-0.53, fdr 1e-05), [[RAB21]] (-0.52, fdr 3e-05), [[ZNF44]] (-0.51, fdr 3e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MCF2L]] → it (grade B ⚠); 5 go from it, the strongest it → [[CMTM8]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 895.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 1.76×; ⚠ cell-cycle shift, explains ~0% of this change); [[PF-06260933 (drug)]] 5 µM in 1 line (SW480 2.42×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +4.2 | 0.013 | 18/43 (A-172, HEC-1-A, …) | two highest doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.27× | +3.1 | 0.52 | 13/44 (SW480, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.467×** | -18.9 | 0e+00 | 42/44 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.605×** | -17.7 | 0e+00 | 34/44 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.476×** | -14.4 | 2e-44 | 41/44 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -12.0 | 5e-31 | 38/44 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -11.1 | 1e-26 | 28/45 (C-33 A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.661×** | -9.5 | 2e-19 | 34/41 (SW480, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -9.4 | 7e-19 | 34/45 (LoVo, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -7.7 | 1e-12 | 23/40 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.743×** | -7.4 | 1e-11 | 31/45 (HCT15, A-427, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.701×** | -6.9 | 4e-10 | 28/43 (NCI-H1573, SNU-1, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.763×** | -6.7 | 1e-09 | 29/44 (A-427, C-33 A, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -6.3 | 1e-08 | 24/44 (C-33 A, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.788×** | -5.9 | 2e-07 | 23/44 (RKO, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.792×** | -5.8 | 4e-07 | 30/44 (C32, C-33 A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **0.795×** | -5.7 | 5e-07 | 25/44 (J82, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -5.7 | 5e-07 | 21/44 (C-33 A, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -5.7 | 5e-07 | 28/44 (CFPAC-1, HepG2/C3A, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -5.2 | 8e-06 | 21/44 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.686×** | -4.9 | 3e-05 | 25/44 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.852× | -4.7 | 6e-05 | 17/44 (SW480, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.844× | -4.2 | 7e-04 | 19/44 (KATO III, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.849× | -4.0 | 0.001 | 20/45 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.867× | -3.5 | 0.009 | 14/44 (C-33 A, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 801 | 0 | 18 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -28.9) |
| [[A-427 (line)]] | wt | 468 | 0 | 14 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -18.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 203 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 632 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -38.1) |
| [[NCI-H2030 (line)]] | alt | 364 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -28.2) |
| [[KATO III (line)]] | alt | 426 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.6) |
| [[C32 (line)]] | wt | 209 | 0 | 8 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.260× (z -14.3) |
| [[RKO (line)]] | wt | 164 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.355× (z -14.4) |
| [[SW480 (line)]] | alt | 258 | 2 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 0.05 µM 1.76× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 2.42× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.486× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 95.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.8) |
| [[SW48 (line)]] | wt | 201 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.290× (z -12.6) |
| [[A549 (line)]] | wt | 87.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -17.5) |
| [[HCT15 (line)]] | alt | 242 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.8) |
| [[LoVo (line)]] | wt | 125 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 405 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 341 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 394 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -13.5) |
| [[PANC-1 (line)]] | alt | 132 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -15.5) |
| [[AN3 CA (line)]] | alt | 329 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.7) |
| [[COLO 205 (line)]] | alt | 725 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -13.9) |
| [[SW 900 (line)]] | alt | 196 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.361× (z -11.9) |
| [[A-172 (line)]] | wt | 108 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.470× (z -10.7) |
| [[BT-474 (line)]] | alt | 82.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -15.1) |
| [[HepG2_C3A (line)]] | wt | 233 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -9.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.481× (z -9.3) |
| [[A498 (line)]] | wt | 83.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.531× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 88.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -8.6) |
| [[CHP-212 (line)]] | wt | 87.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -10.1) |
| [[H4 (line)]] | wt | 87.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.347× (z -8.5) |
| [[Hs 766T (line)]] | wt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -12.0) |
| [[J82 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.522× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~19% of this change |
| [[LS 180 (line)]] | wt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 93.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.2) |
| [[SNU-1 (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -11.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 170 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT7]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[BRI3BP]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[RCOR1]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[LMBR1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP8]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[KIAA1958]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[MMP15]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GLDC]] | +0.55 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[HPCAL1]] | +0.55 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[OSBPL10]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[LINC00659]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SKI]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC3]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RAB21]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ZNF44]] | -0.51 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ZNF407-AS1]] | -0.51 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[COPS5]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[C3orf38]] | -0.50 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[METTL6]] | -0.50 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[IFT74]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[RNF146]] | -0.49 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ZNF181]] | -0.49 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[COG4]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[FAM204A]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCF2L]] | B | MCF2L activity raises ATP11A's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without MCF2L | 0.003 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[LINC00659]] | B | LINC00659 activity raises ATP11A's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without LINC00659 | 0.010 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[B4GALNT3]] | B | B4GALNT3 activity raises ATP11A's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without B4GALNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[CMTM8]] | B | CMTM8 activity raises ATP11A's level | lines that do not express CMTM8 (9) vs lines expressing it (41) | 3.12× lower at baseline in the lines without CMTM8 | 0.033 | ⚠ within organs, on part of the lines; also absent: ALDH5A1, NUP210, PLEKHG3; maybe low, not absent |
| [[MCF2L]] | B | MCF2L activity strengthens ATP11A's drug response | lines that do not express MCF2L (10) vs lines expressing it (35) | the lines without MCF2L respond 0.78× as strongly (z diff +2.20); strongest at Dinaciclib 0.5 µM: 0.85x vs 0.60x (z diff +3.5) | 0.054 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2; target measured in part of the lines; artifact flags |
| [[ARHGAP8]] | B | ARHGAP8 activity raises ATP11A's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without ARHGAP8 | 0.073 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM8]] | C | ATP11A activity raises CMTM8's level | lines that do not express ATP11A (4) vs lines expressing it (46) | 6.62× lower at baseline in the lines without ATP11A | 0.004 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| [[BRI3BP]] | C | ATP11A activity raises BRI3BP's level | lines that do not express ATP11A (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without ATP11A | 0.052 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| [[CLMN]] | C | ATP11A activity raises CLMN's level | lines that do not express ATP11A (4) vs lines expressing it (46) | 3.64× lower at baseline in the lines without ATP11A | 0.056 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| [[TMC6]] | C | ATP11A activity raises TMC6's level | lines that do not express ATP11A (4) vs lines expressing it (46) | 4.19× lower at baseline in the lines without ATP11A | 0.088 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | C | ATP11A, [[LGALSL]], [[LGALSL-DT]] activity raises the cells' numbers under Vinblastine (sulfate) 0.05 µM (protects the cells) | lines that do not express ATP11A, LGALSL, LGALSL-DT (4) vs lines expressing them (44) | the lines without ATP11A, LGALSL, LGALSL-DT: 0.81× the cells of the other lines | 0.088 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.0, 31.1); signed map (-18.3, 42.2). **Vector** length 111, 32.3% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.0 | -3.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -18.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -14.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -5.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.5 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase phospholipid transporting 11A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:112,690,038-112,887,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATPIH, ATPIS, KIAA1021 |
| Gene groups (HGNC) | ATPase phospholipid transporting |
| Reactome | 5 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P98196](https://www.uniprot.org/uniprotkb/P98196) (Phospholipid-transporting ATPase IH):

> Catalytic component of a P4-ATPase flippase complex which catalyzes the hydrolysis of ATP coupled to the transport of aminophospholipids, phosphatidylserines (PS) and phosphatidylethanolamines (PE), from the outer to the inner leaflet of the plasma membrane. Does not show flippase activity toward phosphatidylcholine (PC). Contributes to the maintenance of membrane lipid asymmetry with a specific role in morphogenesis of muscle cells. In myoblasts, mediates PS enrichment at the inner leaflet of …

**Summary**, from NCBI Gene [23250](https://www.ncbi.nlm.nih.gov/gene/23250):

> The protein encoded by this gene is an integral membrane ATPase. The encoded protein is probably phosphorylated in its intermediate state and likely drives the transport of ions such as calcium across membranes. [provided by RefSeq, Apr 2022]

**Accessions** — [HGNC:13552](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13552) · Entrez [23250](https://www.ncbi.nlm.nih.gov/gene/23250) · UniProt [P98196](https://www.uniprot.org/uniprotkb/P98196) · Ensembl [ENSG00000068650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068650)

## Data

Gene col 895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 895); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 895]; `tensor/DDL_lfc|DDL_z.npy` [895]; `embed/gene_vectors.npy` [895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 895 or target_col == 895). Every well: [[ATP11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
