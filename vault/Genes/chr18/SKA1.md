---
symbol: "SKA1"
type: "gene"
col: 7845
ensembl_id: "ENSG00000154839"
name: "spindle and kinetochore associated complex subunit 1"
location: "18q21.1"
module: 22
arm: "+"
pooled_cpm: 11.74
n_lines_expressing: 48
n_dd_up: 24
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SKA1

*spindle and kinetochore associated complex subunit 1* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (18 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.84× (z +8.8, q 5e-16, up in 28 of 40 measured lines) ⚠ toxic; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.34× (z +4.4, q 6e-04, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.564× (z -12.1, q 6e-31, down in 27 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKA3]] (+0.89, fdr 7e-06), [[NCAPH]] (+0.87, fdr 7e-06), [[CENPI]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.84×** | +8.8 | 5e-16 | 28/40 (LoVo, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.74×** | +8.3 | 2e-14 | 22/37 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.69×** | +7.6 | 5e-12 | 11/19 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.61×** | +7.2 | 8e-11 | 23/37 (HOP62, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.58×** | +6.9 | 5e-10 | 21/45 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **1.52×** | +5.9 | 4e-07 | 13/28 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +5.3 | 1e-05 | 16/45 (RKO, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.42×** | +5.1 | 2e-05 | 15/44 (A-427, LoVo, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +4.6 | 3e-04 | 12/45 (SW48, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +4.6 | 3e-04 | 13/45 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 6e-04 | 12/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.32×** | +4.2 | 0.001 | 11/46 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.37×** | +4.2 | 0.001 | 7/45 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.30×** | +3.9 | 0.004 | 7/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.29×** | +3.9 | 0.004 | 14/42 (RKO, C-33 A, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.018 | 10/46 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.047 | 8/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.047 | 5/45 (PANC-1, LoVo, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +2.9 | 0.077 | 1/46 (A498) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +2.8 | 0.094 | 6/45 (LoVo, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -12.1 | 6e-31 | 27/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.635×** | -9.6 | 2e-19 | 28/45 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.518×** | -8.7 | 7e-16 | 27/44 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.474×** | -5.9 | 6e-07 | 22/45 (A-427, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.678×** | -5.8 | 6e-07 | 20/46 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.581×** | -5.8 | 6e-07 | 22/46 (KATO III, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.609×** | -5.7 | 1e-06 | 20/44 (KATO III, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.513×** | -5.2 | 1e-05 | 20/42 (C-33 A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.801×** | -4.7 | 2e-04 | 20/46 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.561×** | -4.5 | 3e-04 | 15/42 (RKO, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.814×** | -4.3 | 7e-04 | 10/46 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -3.9 | 0.004 | 21/46 (A498, NCI-H460, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.774×** | -3.8 | 0.005 | 9/45 (A-427, SNU-1, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **0.775×** | -3.8 | 0.005 | 9/45 (SK-MEL-2, HS-578T, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.750×** | -3.8 | 0.005 | 14/43 (NCI-H1792, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.705×** | -3.7 | 0.006 | 10/46 (HCT15, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.783×** | -3.7 | 0.008 | 10/45 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.649×** | -3.4 | 0.019 | 9/46 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.030 | 19/43 (H4, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.0 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.195× (z -15.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -13.5) |
| [[H4 (line)]] | wt | 13.9 | 0 | 4 (3 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0477× (z -10.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -10.4) |
| [[A-427 (line)]] | wt | 21.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.157× (z -17.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[BT-474 (line)]] | alt | 9.62 | 0 | 2 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0785× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 9.38 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.111× (z -14.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[LS 180 (line)]] | wt | 9.11 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.150× (z -11.1) ⚠ cell-cycle shift, explains ~62% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[GSK1059615 (drug)]] 0.5 µM 0.0536× (z -10.8) |
| [[PANC-1 (line)]] | alt | 17.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.5) |
| [[A-172 (line)]] | wt | 9.79 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -9.0) |
| [[HCT15 (line)]] | alt | 19.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -8.8) |
| [[HOP62 (line)]] | alt | 6.22 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -8.9) |
| [[KATO III (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.148× (z -8.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LoVo (line)]] | wt | 9.86 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.144× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H1792 (line)]] | alt | 7.82 | 0 | 1 | — | [[Norepinephrine (hydrochloride) (drug)]] 0.05 µM 0.0768× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 9.91 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.321× (z -9.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[Panc 03.27 (line)]] | alt | 9.77 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0587× (z -11.5) |
| [[RKO (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0911× (z -8.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0665× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -12.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA3]] | +0.89 | +0.87 / +0.87 | both halves | 7e-06 | STRING 999 |
| [[NCAPH]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 535 |
| [[CENPI]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 805 |
| [[MELK]] | +0.84 | +0.86 / +0.82 | both halves | 7e-06 | STRING 816 |
| [[PBK]] | +0.83 | +0.82 / +0.80 | both halves | 7e-06 | STRING 773 |
| [[RACGAP1]] | +0.83 | +0.80 / +0.82 | both halves | 7e-06 | STRING 477 |
| [[KIF15]] | +0.83 | +0.81 / +0.85 | both halves | 7e-06 | STRING 618 |
| [[CIT]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[KNL1]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 768 |
| [[AURKB]] | +0.82 | +0.82 / +0.76 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 883 |
| [[NCAPG2]] | +0.81 | +0.81 / +0.76 | both halves | 7e-06 | STRING 553 |
| [[NCAPG]] | +0.81 | +0.80 / +0.81 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 743 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises SKA1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without E2F8 | 0.087 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises SKA1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.88× lower at baseline in the lines without NDC80 | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises SKA1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without PBK | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[CDCA3]] | C | CDCA3 activity raises SKA1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.29× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.8, -52.8); signed map (-46.1, -42.6). **Vector** length 109, 27.7% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.61 to 60); *DREAM G2/M down* (control, mean cos +0.64 to 28); *E2F targets* (hallmark, mean cos +0.59 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | +3.2 | +8.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.1 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | +3.1 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | +2.9 | +7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +4.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.9 | +3.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.7 | +2.6 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.6 | -8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -12.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -5.2 | -9.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | spindle and kinetochore associated complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:50,375,040-50,394,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10200; previously C18orf24 |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BD8](https://www.uniprot.org/uniprotkb/Q96BD8) (SKA complex subunit 1):

> Component of the SKA complex, a microtubule plus end-binding complex of the outer kinetochore that stabilizes spindle microtubule-kinetochore attachments, promotes alignment of chromosomes at the mitotic spindle equator (chromosome congression) and assists suppression of the spindle assembly checkpoint. Kinetochores, consisting of a centromere-associated inner segment and a microtubule-contacting outer segment, play a crucial role in chromosome segregation by mediating the physical connection …

**Summary**, from NCBI Gene [220134](https://www.ncbi.nlm.nih.gov/gene/220134):

> Enables microtubule binding activity. Involved in attachment of mitotic spindle microtubules to kinetochore; negative regulation of mitotic spindle assembly checkpoint signaling; and positive regulation of microtubule polymerization. Located in centrosome; kinetochore; and mitotic spindle microtubule. Part of SKA complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28109) · Entrez [220134](https://www.ncbi.nlm.nih.gov/gene/220134) · UniProt [Q96BD8](https://www.uniprot.org/uniprotkb/Q96BD8) · Ensembl [ENSG00000154839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154839)

## Data

Gene col 7845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7845); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7845]; `tensor/DDL_lfc|DDL_z.npy` [7845]; `embed/gene_vectors.npy` [7845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7845 or target_col == 7845). Every well: [[SKA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
