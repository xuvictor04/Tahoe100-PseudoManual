---
symbol: "LIN54"
type: "gene"
col: 12114
ensembl_id: "ENSG00000189308"
name: "lin-54 DREAM MuvB core complex component"
location: "4q21.22"
module: 67
arm: "+"
pooled_cpm: 74.65
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# LIN54

*lin-54 DREAM MuvB core complex component* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.46× (z +14.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.464× (z -12.1, q 7e-31, down in 37 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.793× (z -5.4, q 1e-05, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCM]] (+0.70, fdr 7e-06), [[ORC1]] (+0.67, fdr 7e-06), [[ATAD5]] (+0.65, fdr 7e-06); moves opposite to [[ZNF783]] (-0.60, fdr 1e-05, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[ODC1]] (-0.55, fdr 1e-05), [[RRP15]] (-0.55, fdr 1e-05), [[AIMP2]] (-0.52, fdr 4e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIR924HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.46×** | +14.7 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +14.0 | 7e-42 | 40/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +10.8 | 8e-25 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.93×** | +10.8 | 8e-25 | 46/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.89×** | +10.4 | 4e-23 | 43/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.86×** | +10.1 | 5e-22 | 42/48 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +9.4 | 3e-19 | 44/48 (COLO 205, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +9.4 | 5e-19 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +8.2 | 1e-14 | 43/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +8.0 | 5e-14 | 40/48 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.65×** | +7.8 | 2e-13 | 33/48 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.39×** | +7.7 | 8e-13 | 34/49 (NCI-H460, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.55×** | +7.2 | 3e-11 | 41/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +6.8 | 3e-10 | 38/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +5.6 | 7e-07 | 30/48 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.8 | 5e-05 | 27/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.4 | 3e-04 | 29/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.003 | 23/49 (PANC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.005 | 24/49 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.092 | 19/48 (CFPAC-1, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -12.1 | 7e-31 | 37/43 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.538×** | -10.2 | 9e-22 | 40/49 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -8.0 | 2e-13 | 38/45 (AN3 CA, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -5.4 | 1e-05 | 28/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.756×** | -4.6 | 5e-04 | 27/48 (A-172, HT-29, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -3.6 | 0.024 | 22/48 (AsPC-1, A498, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.707×** | -3.6 | 0.024 | 22/48 (C32, AsPC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.728×** | -3.3 | 0.067 | 20/48 (COLO 205, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.737×** | -3.2 | 0.085 | 23/48 (CHP-212, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.691×** | -3.2 | 0.085 | 19/47 (H4, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.4 | 13 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.23× (z +17.5) | — |
| [[PANC-1 (line)]] | alt | 51.4 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +16.3) | — |
| [[SW480 (line)]] | alt | 84.7 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -15.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 64.6 | 5 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +10.6) | [[OTS514 (drug)]] 5 µM 0.0558× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 45.2 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.6) | [[Selinexor (drug)]] 5 µM 0.502× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 60.3 | 4 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.519× (z -9.7) |
| [[HOP62 (line)]] | alt | 83.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.73× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -9.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 65.2 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 47.9 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +10.9) | — |
| [[A498 (line)]] | wt | 97.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.619× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 61.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.9) | — |
| [[RKO (line)]] | wt | 86.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +14.7) | — |
| [[SW1417 (line)]] | alt | 61.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +14.1) | — |
| [[AN3 CA (line)]] | alt | 155 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0746× (z -16.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 56.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 76.5 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.95× (z +9.9) | [[Belzutifan (drug)]] 5 µM 0.0513× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -14.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 61.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 84.6 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -15.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 46.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +9.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 50.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.5) | — |
| [[A-172 (line)]] | wt | 91.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.459× (z -12.2) |
| [[A-427 (line)]] | wt | 81.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -19.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 72.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +16.9) | — |
| [[CFPAC-1 (line)]] | alt | 69.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -13.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 55.1 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.141× (z -8.7) |
| [[HT-29 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 45.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 73.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 87.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 71.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 82.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -12.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0990× (z -21.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 93.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.87× (z +8.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW 900 (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -10.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 73.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.5) | — |
| [[A549 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCM]] | +0.70 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[ORC1]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 | pathway: G1/S Transition |
| [[ATAD5]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TICRR]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 | pathway: G2/M Transition |
| [[CEP152]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 | pathway: G2/M Transition |
| [[DONSON]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DSN1]] | +0.64 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[ORC6]] | +0.63 | +0.47 / +0.70 | both halves | 2e-05 | pathway: G1/S Transition |
| [[CDCA5]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 | pathway: S Phase |
| [[HAUS8]] | +0.63 | +0.50 / +0.64 | both halves | 1e-05 | pathway: G2/M Transition |
| [[CKS1B]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 | pathway: Cyclin A:Cdk2-associated events at S phase entry |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF783]] ⚠ | -0.60 | -0.59 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ODC1]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RRP15]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[AIMP2]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[KICS2]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR924HG]] | B | MIR924HG activity raises LIN54's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without MIR924HG | 0.089 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.5, -49.3); signed map (-42.2, -41.1). **Vector** length 91.6, 28.8% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 12); *G2/M checkpoint* (hallmark, mean cos +0.54 to 9); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.1 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.9 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.1 | +10.1 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.6 | -0.2 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +1.5 | +0.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.2 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | lin-54 DREAM MuvB core complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,909,973-83,012,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIP120, DKFZp686L1814, JC8.6, CXCDC1, TCX1 |
| Gene groups (HGNC) | MuvB complex subunits |
| Reactome | 14 pathways, smallest: Polo-like kinase mediated events; Transcription of E2F targets under negative control by p107 (RBL1) and p130 (RBL2) in complex with HDAC1; Transcription of E2F targets under negative control by DREAM complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6MZP7](https://www.uniprot.org/uniprotkb/Q6MZP7) (Protein lin-54 homolog):

> Component of the DREAM complex, a multiprotein complex that can both act as a transcription activator or repressor depending on the context. In G0 phase, the complex binds to more than 800 promoters and is required for repression of E2F target genes. In S phase, the complex selectively binds to the promoters of G2/M genes whose products are required for mitosis and participates in their cell cycle dependent activation. In the complex, acts as a DNA-binding protein that binds the promoter of …

**Summary**, from NCBI Gene [132660](https://www.ncbi.nlm.nih.gov/gene/132660):

> LIN54 is a component of the LIN, or DREAM, complex, an essential regulator of cell cycle genes (Schmit et al., 2009 [PubMed 19725879]).[supplied by OMIM, Dec 2010]

**Accessions** — [HGNC:25397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25397) · Entrez [132660](https://www.ncbi.nlm.nih.gov/gene/132660) · UniProt [Q6MZP7](https://www.uniprot.org/uniprotkb/Q6MZP7) · Ensembl [ENSG00000189308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189308)

## Data

Gene col 12114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12114); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12114]; `tensor/DDL_lfc|DDL_z.npy` [12114]; `embed/gene_vectors.npy` [12114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12114 or target_col == 12114). Every well: [[LIN54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIN54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
