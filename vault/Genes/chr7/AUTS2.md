---
symbol: "AUTS2"
type: "gene"
col: 8153
ensembl_id: "ENSG00000158321"
name: "activator of transcription and developmental regulator AUTS2"
location: "7q11.22"
module: 9
arm: "+"
pooled_cpm: 166.5
n_lines_expressing: 32
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# AUTS2

*activator of transcription and developmental regulator AUTS2* — 7q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +11.9, q 4e-30, up in 20 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.492× (z -13.1, q 3e-36, down in 22 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.637× (z -8.6, q 6e-16, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAM2]] (+0.62, fdr 1e-05), [[PCDH9]] (+0.58, fdr 1e-04), [[XYLT1]] (+0.58, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TTTY14]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MAPK10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +11.9 | 4e-30 | 20/30 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +9.2 | 7e-18 | 19/31 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +7.2 | 1e-10 | 14/30 (NCI-H1792, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.3 | 1e-05 | 16/29 (C32, Hs 766T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.011 | 12/31 (C32, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.22×** | +3.5 | 0.041 | 15/32 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.045 | 14/32 (A-172, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.045 | 13/30 (C32, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.492×** | -13.1 | 3e-36 | 22/27 (CHP-212, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.548×** | -11.5 | 3e-28 | 25/30 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -9.7 | 5e-20 | 25/29 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.602×** | -9.0 | 4e-17 | 22/28 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.637×** | -8.6 | 6e-16 | 19/30 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -7.7 | 1e-12 | 20/30 (A-172, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.683×** | -7.0 | 2e-10 | 21/30 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.697×** | -6.9 | 3e-10 | 24/30 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.659×** | -6.9 | 4e-10 | 22/31 (A-172, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.511×** | -6.7 | 1e-09 | 21/31 (H4, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.763×** | -5.2 | 1e-05 | 20/30 (LS 180, SW48, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.609×** | -5.0 | 3e-05 | 13/20 (A-172, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.742×** | -4.9 | 4e-05 | 17/30 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.839× | -4.7 | 9e-05 | 16/30 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.781×** | -4.7 | 9e-05 | 17/30 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.799×** | -4.3 | 7e-04 | 17/30 (LS 180, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.795×** | -3.9 | 0.002 | 16/30 (LS 180, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.827×** | -3.6 | 0.007 | 14/30 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.010 | 7/30 (A549, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.822×** | -3.5 | 0.013 | 13/29 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.885× | -3.3 | 0.023 | 11/31 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.842× | -3.1 | 0.034 | 10/31 (NCI-H661, C32, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.894× | -3.0 | 0.053 | 6/31 (LoVo, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 750 | 0 | 16 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -26.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0747× (z -21.7) |
| [[NCI-H460 (line)]] | wt | 662 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -20.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -16.9) |
| [[LS 180 (line)]] | wt | 232 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0923× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -11.7) |
| [[A-172 (line)]] | wt | 798 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0867× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.218× (z -8.5) |
| [[C32 (line)]] | wt | 98.0 | 11 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +14.0) | — |
| [[KATO III (line)]] | alt | 341 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.169× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.6) |
| [[LoVo (line)]] | wt | 293 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -16.9) |
| [[A-427 (line)]] | wt | 172 | 1 | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -11.4) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SNU-1 (line)]] | wt | 72.2 | 3 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.57× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 551 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0205× (z -30.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 346 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 123 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.40× (z +12.1) | [[Harringtonine (drug)]] 5 µM 0.303× (z -11.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[C-33 A (line)]] | alt | 640 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0963× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SHP-77 (line)]] | alt | 540 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -11.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 257 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 258 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 95.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.236× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 76.1 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.319× (z -11.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 93.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0897× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 56.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 242 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 36.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 36.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 41.0 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 22.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAM2]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PCDH9]] | +0.58 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[XYLT1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CACNB2]] | +0.57 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[FBXL7]] | +0.57 | +0.43 / +0.61 | both halves | 3e-05 | **novel candidate** |
| [[GALNT13]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CADM2]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[RALYL]] | +0.54 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[KCNJ6]] | +0.54 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[FREM2]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[PEG10]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[B3GALT1]] | +0.53 | +0.44 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTTY14]] | B | TTTY14 activity raises AUTS2's level | lines that do not express TTTY14 (26) vs lines expressing it (24) | 3.26× lower at baseline in the lines without TTTY14 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KDM5D, UTY, EIF1AY |
| [[LINC02506]] | B | LINC02506 activity raises AUTS2's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.43× lower at baseline in the lines without LINC02506 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168 |
| [[FREM2]] | B | FREM2 activity weakens AUTS2's drug response | lines that do not express FREM2 (15) vs lines expressing it (16) | the lines without FREM2 respond 1.40× as strongly (z diff -0.68); strongest at Dinaciclib 5 µM: 0.23x vs 0.47x (z diff -4.0) | 0.075 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[BCL2]] | B | BCL2 activity raises AUTS2's level | lines that do not express BCL2 (11) vs lines expressing it (39) | 3.07× lower at baseline in the lines without BCL2 | 0.080 | ⚠ within organs, on part of the lines; also absent: CD226 |
| [[KLHL13]] | B | KLHL13 activity raises AUTS2's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without KLHL13 | 0.083 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AUTS2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[KCNJ6]] | C | KCNJ6 activity raises AUTS2's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 3.70× lower at baseline in the lines without KCNJ6 | 0.018 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK10]] | B | AUTS2 activity raises MAPK10's level | lines that do not express AUTS2 (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without AUTS2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZMAT4, KCNJ6, ENSG00000249111 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.9, 34.7); signed map (41.4, 36.5). **Vector** length 95.2, 25.6% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +9.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | +6.2 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +6.1 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.1 | -4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.8 | +0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | +1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | +1.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | activator of transcription and developmental regulator AUTS2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.22 — chr7:69,598,296-70,793,506 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0442, FBRSL2 |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 2 pathways, smallest: RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXX7](https://www.uniprot.org/uniprotkb/Q8WXX7) (Autism susceptibility gene 2 protein):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. The PRC1-like complex that contains PCGF5, RNF2, CSNK2B, RYBP and AUTS2 has decreased histone H2A …

**Summary**, from NCBI Gene [26053](https://www.ncbi.nlm.nih.gov/gene/26053):

> This gene has been implicated in neurodevelopment and as a candidate gene for numerous neurological disorders, including autism spectrum disorders, intellectual disability, and developmental delay. Mutations in this gene have also been associated with non-neurological disorders, such as acute lymphoblastic leukemia, aging of the skin, early-onset androgenetic alopecia, and certain cancers. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by …

**Accessions** — [HGNC:14262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14262) · Entrez [26053](https://www.ncbi.nlm.nih.gov/gene/26053) · UniProt [Q8WXX7](https://www.uniprot.org/uniprotkb/Q8WXX7) · Ensembl [ENSG00000158321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158321)

## Data

Gene col 8153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8153); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8153]; `tensor/DDL_lfc|DDL_z.npy` [8153]; `embed/gene_vectors.npy` [8153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8153 or target_col == 8153). Every well: [[AUTS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AUTS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
