---
symbol: "CLEC2D"
type: "gene"
col: 920
ensembl_id: "ENSG00000069493"
name: "C-type lectin domain family 2 member D"
location: "12p13.31"
module: 68
arm: "+"
pooled_cpm: 35.68
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 35
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# CLEC2D

*C-type lectin domain family 2 member D* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.73× (z +7.0, q 2e-09, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (21 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.407× (z -11.5, q 1e-27, down in 36 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.451× (z -10.2, q 5e-22, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR3142HG]] (+0.59, fdr 5e-05), [[DPY19L2P2]] (+0.56, fdr 3e-05), [[IFNGR2]] (+0.56, fdr 9e-05); moves opposite to [[GTF2E2]] (-0.53, fdr 5e-05), [[SPRYD3]] (-0.50, fdr 1e-04), [[MCU]] (-0.47, fdr 7e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GYPC]] → it (grade B ⚠); 2 go from it, the strongest it → [[FAM227B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +7.0 | 2e-09 | 33/45 (SW 900, A498, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.44×** | +4.6 | 9e-04 | 24/45 (SW 900, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 0.003 | 25/45 (A-427, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.095 | 18/45 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.095 | 11/45 (C-33 A, BT-474, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.095 | 12/44 (NCI-H23, NCI-H1792, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.095 | 19/44 (BT-474, A-172, …) | top dose only | composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.29× | +3.1 | 0.12 | 14/45 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.27× | +3.1 | 0.12 | 17/45 (NCI-H2347, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 920.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.407×** | -11.5 | 1e-27 | 36/45 (SW480, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.425×** | -10.9 | 2e-25 | 35/45 (SW480, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.451×** | -10.2 | 5e-22 | 36/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.466×** | -9.7 | 3e-20 | 35/45 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.566×** | -7.3 | 4e-11 | 31/45 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.578×** | -7.0 | 2e-10 | 31/45 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.570×** | -6.8 | 1e-09 | 28/44 (Panc 03.27, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.597×** | -6.6 | 3e-09 | 29/45 (SW480, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -5.9 | 2e-07 | 28/41 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.418×** | -5.8 | 3e-07 | 28/43 (COLO 205, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.644×** | -5.4 | 4e-06 | 26/42 (HOP62, HCT15, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -5.2 | 1e-05 | 26/45 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.678×** | -5.0 | 3e-05 | 25/45 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.679×** | -4.9 | 3e-05 | 25/45 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.692×** | -4.7 | 1e-04 | 23/43 (SK-MEL-2, COLO 205, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.718×** | -4.2 | 7e-04 | 24/44 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.553×** | -4.0 | 0.002 | 19/44 (HCT15, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.003 | 20/44 (HEC-1-A, RPMI-7951, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.666×** | -3.7 | 0.005 | 14/45 (HCT15, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.601×** | -3.4 | 0.013 | 14/40 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.025 | 16/45 (COLO 205, HS-578T, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.774×** | -3.1 | 0.029 | 18/44 (C32, NCI-H23, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.790×** | -3.0 | 0.043 | 17/45 (HCT15, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.795×** | -2.9 | 0.054 | 13/44 (AN3 CA, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 104 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.332× (z -8.9) |
| [[SW480 (line)]] | alt | 40.2 | 0 | 11 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -16.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.201× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 252 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0172× (z -34.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 53.0 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.225× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 49.3 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.191× (z -11.9) |
| [[BT-474 (line)]] | alt | 52.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 200× (z +32.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 90.3× (z +18.6) | — |
| [[H4 (line)]] | wt | 79.7 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0904× (z -14.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 22.8 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +23.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.30× (z +10.0) | [[TAK-901 (drug)]] 0.05 µM 0.181× (z -10.1) |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.224× (z -8.5) |
| [[J82 (line)]] | alt | 32.6 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +18.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.169× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.269× (z -9.7) |
| [[SNU-423 (line)]] | alt | 48.9 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.72× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -10.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 29.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +21.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.04× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 33.6 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.212× (z -10.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 55.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +20.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.42× (z +11.3) | [[Vinblastine (sulfate) (drug)]] 5 µM 0.424× (z -8.5) |
| [[SW 900 (line)]] | alt | 67.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.59× (z +8.8) | [[Ixazomib citrate (drug)]] 5 µM 0.268× (z -9.5) |
| [[LoVo (line)]] | wt | 11.9 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.65× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 40.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.126× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 45.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 4.01× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 23.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.313× (z -9.2) |
| [[A498 (line)]] | wt | 38.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 54.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -8.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 79.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.249× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR3142HG]] | +0.59 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[DPY19L2P2]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[IFNGR2]] | +0.56 | +0.48 / +0.36 | both halves | 9e-05 |  |
| [[APLF]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[ZMAT1]] | +0.54 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[C1QTNF1]] | +0.53 | +0.59 / +0.30 | both halves | 2e-04 |  |
| [[NOTCH2NLB]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[TIFA]] | +0.53 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[FMNL3]] | +0.52 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[LINC01239]] | +0.52 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | +0.52 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[LINC00504]] | +0.51 | +0.49 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.53 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[SPRYD3]] | -0.50 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[MCU]] | -0.47 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[ZNF767P-1]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ZNF174]] | -0.46 | -0.44 / -0.29 | both halves | 3e-04 |  |
| [[NOMO2]] | -0.46 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[TUSC2]] | -0.46 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[MFN1]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[BAK1]] | -0.45 | -0.51 / -0.22 | both halves | 6e-04 |  |
| [[RAB5IF]] | -0.45 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[HIRA]] | -0.45 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TMEM184B]] | -0.45 | -0.48 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GYPC]] | B | GYPC activity raises CLEC2D's level | lines that do not express GYPC (35) vs lines expressing it (15) | 2.33× lower at baseline in the lines without GYPC | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[MIR3142HG]] | B | MIR3142HG activity raises CLEC2D's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without MIR3142HG | 0.030 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises CLEC2D's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without APCDD1L-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[TRAF1]] | B | TRAF1 activity raises CLEC2D's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without TRAF1 | 0.037 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[LINC00504]] | B | LINC00504 activity raises CLEC2D's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without LINC00504 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[ABCA10]] | B | ABCA10 activity raises CLEC2D's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without ABCA10 | 0.086 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[HHAT]] | C | HHAT activity raises CLEC2D's level | lines that do not express HHAT (4) vs lines expressing it (46) | 3.42× lower at baseline in the lines without HHAT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01341, C2orf92, GDAP1; maybe low, not absent; its own permutation p |
| [[UBA6-DT]] | C | UBA6-DT activity raises CLEC2D's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 3.71× lower at baseline in the lines without UBA6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM227B]] | C | CLEC2D activity raises FAM227B's level | lines that do not express CLEC2D (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without CLEC2D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IMPG2, GSTM2, ENSG00000286952; maybe low, not absent; its own permutation p |
| [[FAM200B]] | C | CLEC2D activity raises FAM200B's level | lines that do not express CLEC2D (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without CLEC2D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IMPG2, GSTM2, ENSG00000286952; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (18.6, 16.4); signed map (39.9, 4.6). **Vector** length 96.5, 24.7% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | +2.7 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.7 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.6 | +4.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.0 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -9.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.7 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -4.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | C-type lectin domain family 2 member D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:9,664,969-9,699,553 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LLT1, CLAX, OCIL |
| Gene groups (HGNC) | C-type lectin domain containing |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHP7](https://www.uniprot.org/uniprotkb/Q9UHP7) (C-type lectin domain family 2 member D):

> Receptor for KLRB1 that protects target cells against natural killer cell-mediated lysis. Inhibits osteoclast formation. Inhibits bone resorption. Modulates the release of interferon-gamma. Binds high molecular weight sulfated glycosaminoglycans.

**Summary**, from NCBI Gene [29121](https://www.ncbi.nlm.nih.gov/gene/29121):

> This gene encodes a member of the natural killer cell receptor C-type lectin family. The encoded protein inhibits osteoclast formation and contains a transmembrane domain near the N-terminus as well as the C-type lectin-like extracellular domain. Several alternatively spliced transcript variants have been identified for this gene. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:14351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14351) · Entrez [29121](https://www.ncbi.nlm.nih.gov/gene/29121) · UniProt [Q9UHP7](https://www.uniprot.org/uniprotkb/Q9UHP7) · Ensembl [ENSG00000069493](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069493)

## Data

Gene col 920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 920); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 920]; `tensor/DDL_lfc|DDL_z.npy` [920]; `embed/gene_vectors.npy` [920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 920 or target_col == 920). Every well: [[CLEC2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLEC2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
