---
symbol: "DTX3L"
type: "gene"
col: 8791
ensembl_id: "ENSG00000163840"
name: "deltex E3 ubiquitin ligase 3L"
location: "3q21.1"
module: 32
arm: "+"
pooled_cpm: 64.77
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 33
n_dd_up_clean: 21
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 33
direction_downstream: 21
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# DTX3L

*deltex E3 ubiquitin ligase 3L* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.84× (z +9.8, q 5e-20, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.195× (z -16.9, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT5]] (+0.92, fdr 7e-06), [[PARP14]] (+0.92, fdr 7e-06), [[PARP9]] (+0.88, fdr 7e-06, ⚠ same locus), [[ADAR]] (+0.88, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 21 go from it, the strongest it → [[PSMB9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, none with an alert; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.84×** | +9.8 | 5e-20 | 38/45 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +7.0 | 8e-10 | 32/44 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.92×** | +6.8 | 2e-09 | 37/45 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.84×** | +6.1 | 1e-07 | 41/44 (NCI-H23, Hs 766T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.002 | 30/44 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.002 | 30/46 (A-427, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.002 | 29/44 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.006 | 27/45 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.007 | 29/44 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.007 | 28/45 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.009 | 26/44 (HS-578T, C32, …) | all doses, flat | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.011 | 27/45 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.020 | 27/45 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.030 | 20/45 (A498, SW480, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.033 | 22/45 (CFPAC-1, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8791.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.195×** | -16.9 | 0e+00 | 44/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.206×** | -16.3 | 0e+00 | 45/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.209×** | -16.2 | 0e+00 | 44/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.444×** | -11.8 | 4e-30 | 35/45 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.480×** | -10.7 | 1e-24 | 39/46 (NCI-H23, C-33 A, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.432×** | -8.6 | 5e-16 | 42/45 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -8.5 | 1e-15 | 34/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.455×** | -8.1 | 4e-14 | 41/44 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.456×** | -8.1 | 4e-14 | 44/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -7.9 | 2e-13 | 33/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.473×** | -7.7 | 7e-13 | 36/45 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.479×** | -7.6 | 2e-12 | 34/45 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.550×** | -6.2 | 3e-08 | 35/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.340×** | -5.8 | 2e-07 | 36/46 (BT-474, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.571×** | -5.8 | 3e-07 | 32/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -5.3 | 4e-06 | 34/45 (NCI-H23, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -4.9 | 3e-05 | 32/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 79.6 | 1 | 15 (6 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.72× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.106× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 76.8 | 0 | 16 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0272× (z -22.3) |
| [[BT-474 (line)]] | alt | 86.1 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0864× (z -17.3) |
| [[A-172 (line)]] | wt | 138 | 3 | 10 | [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -18.4) |
| [[LoVo (line)]] | wt | 102 | 1 | 11 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.0921× (z -21.1) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 12 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.179× (z -16.0) |
| [[C-33 A (line)]] | alt | 49.6 | 0 | 10 | — | [[Panobinostat (drug)]] 0.5 µM 0.0541× (z -16.2) |
| [[SW480 (line)]] | alt | 32.3 | 0 | 10 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.101× (z -22.0) |
| [[RKO (line)]] | wt | 51.9 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -20.0) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0518× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 135 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -16.5) |
| [[COLO 205 (line)]] | alt | 158 | 2 | 6 | [[Harringtonine (drug)]] 0.5 µM 3.67× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.117× (z -16.1) |
| [[HS-578T (line)]] | alt | 75.3 | 3 | 5 | [[Homoharringtonine (drug)]] 0.5 µM 6.63× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 82.8 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 5.77× (z +14.2) | [[Tofacitinib (drug)]] 5 µM 0.394× (z -10.8) |
| [[A549 (line)]] | wt | 78.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.9) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.127× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 119 | 2 | 5 | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +9.9) | [[Tofacitinib (drug)]] 5 µM 0.281× (z -14.2) |
| [[KATO III (line)]] | alt | 102 | 1 | 6 | [[Harringtonine (drug)]] 0.5 µM 4.70× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.121× (z -15.4) |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.0878× (z -14.4) |
| [[SNU-423 (line)]] | alt | 89.8 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.0663× (z -17.9) |
| [[C32 (line)]] | wt | 32.8 | 5 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 7.42× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.206× (z -8.8) |
| [[HT-29 (line)]] | alt | 49.0 | 2 | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.03× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 50.5 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.177× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 145 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -13.2) |
| [[A498 (line)]] | wt | 73.7 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.202× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 45.8 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -12.0) |
| [[Hs 766T (line)]] | wt | 61.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 44.3 | 1 | 3 | [[Homoharringtonine (drug)]] 0.05 µM 2.58× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.205× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.121× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.209× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 168 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.297× (z -9.4) |
| [[HCT15 (line)]] | alt | 50.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -10.8) |
| [[J82 (line)]] | alt | 76.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 22.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -9.8) |
| [[PANC-1 (line)]] | alt | 38.8 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.09× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SW1417 (line)]] | alt | 92.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -10.0) |
| [[A-427 (line)]] | wt | 36.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -11.1) |
| [[SNU-1 (line)]] | wt | 45.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -10.3) |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0906× (z -8.7) |
| [[CHP-212 (line)]] | wt | 50.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0860× (z -9.2) |
| [[H4 (line)]] | wt | 45.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -8.5) |
| [[HOP62 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT5]] | +0.92 | +0.88 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[PARP14]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | STRING 975 |
| [[PARP9]] | +0.88 | +0.81 / +0.92 | both halves | 7e-06 | STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ADAR]] | +0.88 | +0.80 / +0.91 | both halves | 7e-06 | STRING 427 |
| [[DDX60L]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | STRING 512 |
| [[TRIM21]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[HERC6]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 474 |
| [[NMI]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[DDX60]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | STRING 562 |
| [[OAS3]] | +0.87 | +0.80 / +0.91 | both halves | 7e-06 | STRING 468 |
| [[OAS2]] | +0.86 | +0.76 / +0.91 | both halves | 7e-06 | STRING 547 |
| [[PHF11]] | +0.86 | +0.76 / +0.88 | both halves | 7e-06 |  |
| [[EIF2AK2]] | +0.86 | +0.77 / +0.89 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 29, C 4. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises DTX3L's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.27× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PARP9]] | B | PARP9 activity raises DTX3L's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 3.15× lower at baseline in the lines without PARP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises DTX3L's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.71× lower at baseline in the lines without PLSCR1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises DTX3L's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without IFI6 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises DTX3L's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.15× lower at baseline in the lines without CMPK2 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[OAS1]] | B | OAS1 activity raises DTX3L's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without OAS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[BTC]] | B | BTC activity raises DTX3L's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.35× lower at baseline in the lines without BTC | 0.007 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises DTX3L's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without SAMD9 | 0.009 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[RASGRP3]] | B | RASGRP3 activity raises DTX3L's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without RASGRP3 | 0.009 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[CCDC194]] | B | CCDC194 activity raises DTX3L's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without CCDC194 | 0.009 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[FBXO39]] | B | FBXO39 activity raises DTX3L's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without FBXO39 | 0.012 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[RSAD2]] | B | RSAD2 activity raises DTX3L's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without RSAD2 | 0.013 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB9]] | C | DTX3L's natural level strengthens PSMB9's drug response | DTX3L's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.16; direction clear | 0.006 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[SAMHD1]] | C | DTX3L's natural level strengthens SAMHD1's drug response | DTX3L's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.53; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NMI]] | C | DTX3L's natural level strengthens NMI's drug response | DTX3L's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.33; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | DTX3L's natural level strengthens IFIT5's drug response | DTX3L's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.63; direction not clear | 0.026 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | DTX3L's natural level strengthens TDRD7's drug response | DTX3L's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.41; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFI35]] | C | DTX3L's natural level strengthens IFI35's drug response | DTX3L's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.51; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB8]] | C | DTX3L's natural level strengthens PSMB8's drug response | DTX3L's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.15; direction clear | 0.050 | ⚠ tissue can mimic it; precision caveat |
| [[PLSCR1]] | C | DTX3L, [[PARP14]] activity raises PLSCR1's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 4.95× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[CMPK2]] | C | DTX3L, [[PARP14]] activity raises CMPK2's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 4.48× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[PARP9]] | C | DTX3L, [[PARP14]] activity raises PARP9's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 4.44× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[HERC6]] | C | DTX3L, [[PARP14]] activity raises HERC6's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 3.81× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |
| [[SP110]] | C | DTX3L, [[PARP14]] activity raises SP110's level | lines that do not express DTX3L, PARP14 (3) vs lines expressing them (47) | 3.53× lower at baseline in the lines without DTX3L, PARP14 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CRYBG3, TTC39C; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.8, 54.1); signed map (63.0, 32.4). **Vector** length 151, 59.5% of its response variance represented; |z| ≥ 3 in 1,631 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.72 to 56); *interferon gamma response* (hallmark, mean cos +0.74 to 60); *interferon* (control, mean cos +0.78 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +16.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.2 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.9 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.9 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.8 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.9 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.6 | +4.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.3 | +2.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.7 | -11.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.2 | -10.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.9 | -7.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.2 | -7.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.8 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | deltex E3 ubiquitin ligase 3L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:122,564,338-122,575,203 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BBAP, RNF143 |
| Gene groups (HGNC) | Ring finger proteins; Deltex E3 ubiquitin ligase family |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDB6](https://www.uniprot.org/uniprotkb/Q8TDB6) (E3 ubiquitin-protein ligase DTX3L):

> E3 ubiquitin-protein ligase which, in association with ADP-ribosyltransferase PARP9, plays a role in DNA damage repair and in interferon-mediated antiviral responses. Monoubiquitinates several histones, including histone H2A, H2B, H3 and H4. In response to DNA damage, mediates monoubiquitination of 'Lys-91' of histone H4 (H4K91ub1). The exact role of H4K91ub1 in DNA damage response is still unclear but it may function as a licensing signal for additional histone H4 post-translational …

**Summary**, from NCBI Gene [151636](https://www.ncbi.nlm.nih.gov/gene/151636):

> Enables several functions, including STAT family protein binding activity; histone H4K91 ubiquitin ligase activity; and protein ADP-ribosyltransferase-substrate adaptor activity. Involved in several processes, including DNA repair-dependent chromatin remodeling; positive regulation of protein localization; and protein ubiquitination. Located in several cellular components, including early endosome; lysosome; and nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome …

**Accessions** — [HGNC:30323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30323) · Entrez [151636](https://www.ncbi.nlm.nih.gov/gene/151636) · UniProt [Q8TDB6](https://www.uniprot.org/uniprotkb/Q8TDB6) · Ensembl [ENSG00000163840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163840)

## Data

Gene col 8791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8791); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8791]; `tensor/DDL_lfc|DDL_z.npy` [8791]; `embed/gene_vectors.npy` [8791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8791 or target_col == 8791). Every well: [[DTX3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTX3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
