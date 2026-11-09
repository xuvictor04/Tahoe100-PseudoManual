---
symbol: "EVL"
type: "gene"
col: 12198
ensembl_id: "ENSG00000196405"
name: "Enah/Vasp-like"
location: "14q32.2"
module: 10
arm: "-"
pooled_cpm: 39.68
n_lines_expressing: 34
n_dd_up: 9
n_dd_down: 31
n_dd_up_clean: 8
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# EVL

*Enah/Vasp-like* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.36× (z +7.1, q 8e-10, up in 20 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -23.7, q 0e+00, down in 29 of 32 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.425× (z -19.7, q 0e+00, down in 28 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRL1]] (+0.55, fdr 3e-05), [[ADA]] (+0.55, fdr 2e-05), [[PDE7A]] (+0.55, fdr 1e-05); moves opposite to [[AK9]] (-0.53, fdr 8e-05), [[KRR1]] (-0.52, fdr 5e-05), [[DUS4L]] (-0.52, fdr 4e-05).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[GPR155]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +7.1 | 8e-10 | 20/32 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +6.2 | 2e-07 | 17/31 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +6.1 | 2e-07 | 19/32 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +6.1 | 2e-07 | 20/33 (NCI-H2347, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +5.1 | 3e-05 | 14/32 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +5.1 | 4e-05 | 14/31 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.52×** | +5.0 | 4e-05 | 10/32 (A498, C32, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +4.9 | 6e-05 | 14/32 (C32, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.9 | 6e-05 | 12/32 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 1e-04 | 14/33 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +4.4 | 6e-04 | 12/32 (C32, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 7e-04 | 13/32 (NCI-H2347, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.003 | 11/32 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.006 | 13/32 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.7 | 0.010 | 10/32 (C32, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.022 | 13/31 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.065 | 7/32 (C32, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.484×** | -23.7 | 0e+00 | 29/32 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.425×** | -19.7 | 0e+00 | 28/32 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.458×** | -17.3 | 0e+00 | 29/32 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.516×** | -15.2 | 0e+00 | 27/32 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.540×** | -14.2 | 1e-43 | 31/32 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -13.7 | 9e-41 | 21/28 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.561×** | -13.3 | 1e-38 | 20/32 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -12.2 | 1e-32 | 20/30 (CHP-212, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -11.7 | 1e-29 | 17/32 (Panc 03.27, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -10.9 | 8e-26 | 22/31 (H4, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.640×** | -10.3 | 4e-23 | 21/31 (BT-474, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.430×** | -10.2 | 1e-22 | 21/33 (NCI-H460, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.672×** | -9.2 | 2e-18 | 23/30 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.684×** | -8.7 | 1e-16 | 21/32 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.689×** | -8.6 | 4e-16 | 19/32 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -8.0 | 5e-14 | 22/32 (C32, LOX-IMVI, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -6.5 | 2e-09 | 16/32 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.821×** | -6.4 | 4e-09 | 15/32 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.758×** | -5.9 | 1e-07 | 16/31 (NCI-H460, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -5.6 | 5e-07 | 16/33 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.788×** | -5.5 | 1e-06 | 15/32 (LOX-IMVI, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.790×** | -5.4 | 1e-06 | 15/32 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.788×** | -5.3 | 3e-06 | 12/32 (Panc 03.27, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 66.3 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -20.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.229× (z -15.0) |
| [[C32 (line)]] | wt | 66.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -21.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.214× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 93.9 | 0 | 10 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.207× (z -23.9) |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 71.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.9) |
| [[BT-474 (line)]] | alt | 139 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -20.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 33.5 | 0 | 7 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.149× (z -15.2) |
| [[HOP62 (line)]] | alt | 33.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -11.1) |
| [[SNU-423 (line)]] | alt | 77.0 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 78.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.315× (z -10.7) |
| [[A-172 (line)]] | wt | 45.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -12.7) |
| [[PANC-1 (line)]] | alt | 50.7 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.366× (z -14.3) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 58.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.376× (z -10.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.432× (z -9.1) |
| [[A498 (line)]] | wt | 30.8 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.73× (z +10.9) ⚠ unreliable plate only | [[Harringtonine (drug)]] 0.5 µM 0.387× (z -10.3) |
| [[CHP-212 (line)]] | wt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0682× (z -16.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0607× (z -18.1) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 34.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -20.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 2 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0550× (z -9.4) |
| [[A549 (line)]] | wt | 69.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -11.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 98.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -12.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 50.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 10.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.296× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRL1]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ADA]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PDE7A]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[RAC3]] | +0.54 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[C6orf136]] | +0.52 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[HACE1]] | +0.52 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[MRPL34]] | +0.52 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[NR2F6]] | +0.52 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[L2HGDH]] | +0.51 | +0.42 / +0.45 | both halves | 4e-05 | same gene group |
| [[GNB2]] | +0.51 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[SLC9A6]] | +0.51 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[CHCHD10]] | +0.51 | +0.47 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK9]] | -0.53 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[KRR1]] | -0.52 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[DUS4L]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GLIPR1-AS1]] | -0.51 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[SSUH2]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[TSGA10]] | -0.50 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[ADGRL4]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[LEKR1]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[LPXN]] | -0.50 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[NEPRO-AS1]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CYREN]] | -0.50 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[BCL10-AS1]] | -0.49 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EVL's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers EVL's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | EVL activity raises GPR155's level | lines that do not express EVL (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without EVL | 0.047 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, GNB4 |
| [[SUFU]] | B | EVL activity raises SUFU's level | lines that do not express EVL (16) vs lines expressing it (34) | 1.12× lower at baseline in the lines without EVL | 0.084 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, GNB4 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-2.7, 2.9); signed map (-43.0, 18.6). **Vector** length 94.5, 23.4% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +6.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -19.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -15.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | -23.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | Enah/Vasp-like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:99,971,449-100,144,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNB6 |
| Gene groups (HGNC) | ENAH/VASPs; MicroRNA protein coding host genes |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 10 pathways, smallest: Generation of second messenger molecules; TCR signaling; RHO GTPases Activate Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI08](https://www.uniprot.org/uniprotkb/Q9UI08) (Ena/VASP-like protein):

> Ena/VASP proteins are actin-associated proteins involved in a range of processes dependent on cytoskeleton remodeling and cell polarity such as axon guidance and lamellipodial and filopodial dynamics in migrating cells. EVL enhances actin nucleation and polymerization.

**Summary**, from NCBI Gene [51466](https://www.ncbi.nlm.nih.gov/gene/51466):

> Predicted to enable SH3 domain binding activity and profilin binding activity. Involved in negative regulation of epithelial cell migration; negative regulation of ruffle assembly; and positive regulation of stress fiber assembly. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20234) · Entrez [51466](https://www.ncbi.nlm.nih.gov/gene/51466) · UniProt [Q9UI08](https://www.uniprot.org/uniprotkb/Q9UI08) · Ensembl [ENSG00000196405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196405)

## Data

Gene col 12198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12198); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12198]; `tensor/DDL_lfc|DDL_z.npy` [12198]; `embed/gene_vectors.npy` [12198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12198 or target_col == 12198). Every well: [[EVL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EVL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
