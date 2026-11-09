---
symbol: "EPB41"
type: "gene"
col: 8209
ensembl_id: "ENSG00000159023"
name: "erythrocyte membrane protein band 4.1"
location: "1p35.3"
module: 147
arm: "+"
pooled_cpm: 137.5
n_lines_expressing: 47
n_dd_up: 15
n_dd_down: 17
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# EPB41

*erythrocyte membrane protein band 4.1* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +10.8, q 2e-24, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.599× (z -9.8, q 6e-20, down in 36 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.664× (z -8.1, q 1e-13, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM102A]] (+0.59, fdr 1e-05), [[ARHGEF3]] (+0.54, fdr 2e-05), [[KIF16B]] (+0.54, fdr 3e-05); moves opposite to [[FOXL1]] (-0.59, fdr 1e-05), [[HMGA2]] (-0.57, fdr 1e-05), [[POLR2D]] (-0.56, fdr 2e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[KIAA1522]] → it (grade B ⚠); 4 go from it, the strongest it → [[KIAA1549L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +10.8 | 2e-24 | 31/45 (HepG2/C3A, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.45×** | +6.8 | 3e-09 | 34/45 (C32, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.3 | 7e-08 | 28/45 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.9 | 5e-07 | 30/45 (HOP62, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.34×** | +5.4 | 9e-06 | 29/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +5.2 | 2e-05 | 31/44 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 2e-05 | 29/45 (C32, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 2e-05 | 26/45 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 19/46 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 22/45 (MIA PaCa-2, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 20/46 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.004 | 24/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +3.9 | 0.005 | 14/46 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.005 | 17/45 (MIA PaCa-2, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.14× | +3.5 | 0.020 | 7/45 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.020 | 13/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.031 | 15/45 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -9.8 | 6e-20 | 36/44 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.664×** | -8.1 | 1e-13 | 30/45 (SNU-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.665×** | -8.1 | 1e-13 | 36/45 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.728×** | -6.3 | 3e-08 | 28/45 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.728×** | -6.3 | 3e-08 | 32/45 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.719×** | -6.1 | 1e-07 | 30/44 (NCI-H661, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **0.760×** | -5.5 | 4e-06 | 29/45 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.767×** | -5.3 | 1e-05 | 25/45 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -5.2 | 1e-05 | 26/45 (RKO, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.798×** | -4.5 | 4e-04 | 25/45 (SNU-1, SW480, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -4.2 | 0.002 | 16/45 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.804×** | -4.0 | 0.003 | 20/44 (RKO, AN3 CA, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.862× | -3.9 | 0.004 | 20/46 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.825×** | -3.8 | 0.005 | 20/45 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.822×** | -3.8 | 0.007 | 22/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.009 | 22/45 (NCI-H1792, LoVo, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.743×** | -3.5 | 0.012 | 19/45 (MIA PaCa-2, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.842× | -3.4 | 0.016 | 16/45 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.060 | 17/45 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.060 | 12/45 (HCT15, KATO III, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.862× | -3.0 | 0.064 | 15/45 (Hs 766T, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 225 | 1 (1 ⚠) | 7 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.83× (z +20.9) ⚠ position not correctable | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.273× (z -12.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.308× (z -12.1) |
| [[SW480 (line)]] | alt | 268 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.333× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.515× (z -9.0) |
| [[HT-29 (line)]] | alt | 331 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -16.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 58.4 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +15.2) | — |
| [[SNU-1 (line)]] | wt | 153 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.228× (z -12.0) |
| [[KATO III (line)]] | alt | 242 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.266× (z -15.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.477× (z -9.0) |
| [[C32 (line)]] | wt | 38.0 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.01× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 167 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.306× (z -13.4) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 59.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -8.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H460 (line)]] | wt | 81.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.7) | — |
| [[A-172 (line)]] | wt | 79.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +14.9) | — |
| [[COLO 205 (line)]] | alt | 244 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 146 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +22.5) | — |
| [[HOP62 (line)]] | alt | 47.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.432× (z -8.9) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 171 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.413× (z -11.2) ⚠ toxic |
| [[SW48 (line)]] | wt | 203 | 2 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.48× (z +8.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.6) | — |
| [[A-427 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.1) | — |
| [[A549 (line)]] | wt | 77.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.141× (z -8.7) ⚠ toxic |
| [[H4 (line)]] | wt | 80.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 173 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.4) | — |
| [[Hs 766T (line)]] | wt | 123 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.317× (z -8.5) |
| [[HS-578T (line)]] | alt | 119 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.386× (z -9.0) |
| [[J82 (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +20.3) | — |
| [[NCI-H1792 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -12.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.1) | — |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[RKO (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[SHP-77 (line)]] | alt | 224 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.473× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[SK-MEL-2 (line)]] | alt | 79.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 117 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 162 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 195 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 218 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM102A]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ARHGEF3]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[KIF16B]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CGNL1]] | +0.53 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ARMCX3]] | +0.52 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CPEB3]] | +0.52 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[GOLGA4]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[QPRT]] | +0.52 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[LDAF1]] | +0.52 | +0.62 / +0.39 | both halves | 5e-05 |  |
| [[WDFY1]] | +0.51 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[PALS1]] | +0.51 | +0.54 / +0.44 | both halves | 3e-05 | STRING 805 |
| [[KCP]] | +0.51 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXL1]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[HMGA2]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[POLR2D]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[TFAM]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[MSANTD2]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SNRPB]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[PTPN12]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TRMT6]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CLMP]] | -0.52 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ERRFI1]] | -0.52 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[MOSMO]] | -0.51 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TBRG4]] | -0.51 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | B | KIAA1522 activity raises EPB41's level | lines that do not express KIAA1522 (5) vs lines expressing it (45) | 2.65× lower at baseline in the lines without KIAA1522 | 0.018 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[CGNL1]] | B | CGNL1 activity raises EPB41's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without CGNL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[MAP2K1]] | B | MAP2K1 activity lowers EPB41's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GPRC5B]] | B | GPRC5B activity raises EPB41's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 1.10× lower at baseline in the lines without GPRC5B | 0.064 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |
| [[KIAA1549L]] | B | KIAA1549L activity lowers EPB41's level | lines that do not express KIAA1549L (20) vs lines expressing it (30) | 1.70× higher at baseline in the lines without KIAA1549L | 0.085 | ⚠ within organs, on part of the lines; also absent: NLRP3, PLPP4, PHACTR1 |
| [[ELK3]] | C | ELK3 activity lowers EPB41's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 1.85× higher at baseline in the lines without ELK3 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent |
| [[PIK3C2B]] | C | PIK3C2B activity raises EPB41's level | lines that do not express PIK3C2B (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without PIK3C2B | 0.099 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MCF2L2, CYB561, PTPN3; maybe low, not absent; co-absent with the target |
| [[TP53]] | C | TP53 activity weakens EPB41's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 15 not recorded | the TP53-altered lines respond 0.99× as strongly (z diff -0.20); strongest at Harringtonine 0.5 µM: 0.64x vs 0.81x (z diff -3.2) | 0.907 over the table, 0.090 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; the reference differs; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1549L]] | C | EPB41 activity lowers KIAA1549L's level | lines that do not express EPB41 (3) vs lines expressing it (47) | 11.06× higher at baseline in the lines without EPB41 | 0.035 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |
| [[MMAB]] | C | EPB41 activity raises MMAB's level | lines that do not express EPB41 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without EPB41 | 0.044 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |
| [[FHIP1A]] | C | EPB41 activity strengthens FHIP1A's drug response | lines that do not express EPB41 (3) vs lines expressing it (39) | the lines without EPB41 respond 0.48× as strongly (z diff +3.93); strongest at Dinaciclib 0.5 µM: 0.94x vs 0.28x (z diff +7.7) | 0.047 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CD59]] | C | EPB41 activity lowers CD59's level | lines that do not express EPB41 (3) vs lines expressing it (47) | 3.27× higher at baseline in the lines without EPB41 | 0.091 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction -0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, 2.3); signed map (-18.3, 33.4). **Vector** length 142, 47.4% of its response variance represented; |z| ≥ 3 in 1,488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | +6.6 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +3.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.0 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.8 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.3 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | erythrocyte membrane protein band 4.1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,887,091-29,120,046 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 4.1R; previously EL1 |
| Gene groups (HGNC) | Erythrocyte membrane protein band 4.1; FERM domain containing |
| Hallmark sets | HEME_METABOLISM, MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [P11171](https://www.uniprot.org/uniprotkb/P11171) (Protein 4.1):

> Protein 4.1 is a major structural element of the erythrocyte membrane skeleton. It plays a key role in regulating membrane physical properties of mechanical stability and deformability by stabilizing spectrin-actin interaction. Recruits DLG1 to membranes. Required for dynein-dynactin complex and NUMA1 recruitment at the mitotic cell cortex during anaphase.

**Summary**, from NCBI Gene [2035](https://www.ncbi.nlm.nih.gov/gene/2035):

> The protein encoded by this gene, together with spectrin and actin, constitute the red cell membrane cytoskeletal network. This complex plays a critical role in erythrocyte shape and deformability. Mutations in this gene are associated with type 1 elliptocytosis (EL1). Alternatively spliced transcript variants encoding different isoforms have been described for this gene.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:3377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3377) · Entrez [2035](https://www.ncbi.nlm.nih.gov/gene/2035) · UniProt [P11171](https://www.uniprot.org/uniprotkb/P11171) · Ensembl [ENSG00000159023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159023)

## Data

Gene col 8209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8209); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8209]; `tensor/DDL_lfc|DDL_z.npy` [8209]; `embed/gene_vectors.npy` [8209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8209 or target_col == 8209). Every well: [[EPB41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPB41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
