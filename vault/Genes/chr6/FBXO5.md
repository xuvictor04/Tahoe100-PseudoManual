---
symbol: "FBXO5"
type: "gene"
col: 3312
ensembl_id: "ENSG00000112029"
name: "F-box protein 5"
location: "6q25.2"
module: 22
arm: "+"
pooled_cpm: 24.91
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# FBXO5

*F-box protein 5* — 6q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (23 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.93× (z +12.0, q 3e-30, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.399× (z -11.4, q 3e-27, down in 29 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.519× (z -8.5, q 8e-15, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK1]] (+0.85, fdr 7e-06), [[ERCC6L]] (+0.84, fdr 7e-06), [[NCAPG]] (+0.83, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 23 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.93×** | +12.0 | 3e-30 | 45/47 (SW480, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.61×** | +8.6 | 1e-15 | 29/47 (PANC-1, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.44×** | +8.3 | 2e-14 | 29/47 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.57×** | +8.2 | 3e-14 | 30/46 (SW480, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.5 | 8e-09 | 24/44 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.66×** | +6.5 | 9e-09 | 29/47 (RKO, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.68×** | +6.4 | 1e-08 | 28/47 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +5.6 | 1e-06 | 25/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.49×** | +5.2 | 2e-05 | 21/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +4.9 | 7e-05 | 21/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.44×** | +4.7 | 2e-04 | 21/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +4.6 | 2e-04 | 22/47 (NCI-H460, RKO, …) | all doses, flat |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.26×** | +4.2 | 9e-04 | 17/47 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +4.2 | 0.001 | 18/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.26×** | +4.1 | 0.001 | 19/47 (SW480, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.079 | 11/46 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.25×** | +2.8 | 0.100 | 6/47 (HOP62, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3312.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -11.4 | 3e-27 | 29/33 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.519×** | -8.5 | 8e-15 | 33/47 (A-427, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -7.8 | 2e-12 | 30/43 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.557×** | -7.1 | 2e-10 | 31/47 (A-427, HEC-1-A, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.588×** | -6.9 | 8e-10 | 37/46 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.699×** | -6.5 | 6e-09 | 26/47 (A498, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.617×** | -6.2 | 4e-08 | 32/47 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.684×** | -4.9 | 7e-05 | 21/47 (SW 1271, H4, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.688×** | -4.8 | 9e-05 | 22/46 (Hs 766T, SW48, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.690×** | -4.8 | 9e-05 | 23/47 (HS-578T, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.699×** | -4.5 | 4e-04 | 22/47 (A498, HOP62, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.714×** | -4.4 | 6e-04 | 26/47 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **0.554×** | -4.0 | 0.003 | 17/39 (BT-474, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.009 | 17/47 (SW480, Hs 766T, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.015 | 14/47 (RKO, HCT15, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.850× | -3.0 | 0.081 | 13/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 31.3 | 3 (2 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 12.9× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.229× (z -10.7) |
| [[A-427 (line)]] | wt | 55.3 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.233× (z -11.1) |
| [[A498 (line)]] | wt | 25.6 | 0 | 5 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.192× (z -17.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 33.4 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.24× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.100× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -10.4) |
| [[PANC-1 (line)]] | alt | 29.2 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.246× (z -12.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 42.1 | 4 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.45× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.8 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.178× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 74.6 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.69× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -9.2) |
| [[SHP-77 (line)]] | alt | 47.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.292× (z -9.6) |
| [[A549 (line)]] | wt | 18.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.208× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 51.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0879× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.156× (z -8.7) |
| [[H4 (line)]] | wt | 21.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0978× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 23.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 41.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -13.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 8.51 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0735× (z -8.7) |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.283× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0843× (z -9.5) |
| [[HOP62 (line)]] | alt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0678× (z -13.1) |
| [[KATO III (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.209× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.231× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.199× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK1]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 937 |
| [[ERCC6L]] | +0.84 | +0.82 / +0.85 | both halves | 7e-06 | pathway: Mitotic Metaphase and Anaphase; STRING 575 |
| [[NCAPG]] | +0.83 | +0.88 / +0.79 | both halves | 7e-06 | STRING 624 |
| [[AURKB]] | +0.83 | +0.84 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 536 |
| [[KIF11]] | +0.81 | +0.88 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 784 |
| [[CDCA5]] | +0.81 | +0.76 / +0.83 | both halves | 7e-06 | pathway: Mitotic Metaphase and Anaphase |
| [[KIF2C]] | +0.81 | +0.81 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 585 |
| [[KIF22]] | +0.81 | +0.78 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIFC1]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 |  |
| [[SHCBP1]] | +0.80 | +0.82 / +0.77 | both halves | 7e-06 | STRING 409 |
| [[PLK4]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 785 |
| [[CDCA8]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 | pathway: Mitotic Metaphase and Anaphase; STRING 662 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises FBXO5's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without PIMREG | 0.031 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises FBXO5's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without AURKB | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises FBXO5's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.76× lower at baseline in the lines without PBK | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises FBXO5's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.67× lower at baseline in the lines without NDC80 | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises FBXO5's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.76× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDCA3]] | C | CDCA3 activity raises FBXO5's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.67× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises FBXO5's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.63× lower at baseline in the lines without C21orf58, SKA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises FBXO5's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without CDC20 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.1, -52.8); signed map (-46.6, -43.8). **Vector** length 134, 41.1% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.67 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.59 to 48); *E2F targets* (hallmark, mean cos +0.60 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.2 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.0 | +8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +8.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +3.6 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.1 | +4.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.8 | +2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.4 | +2.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.2 | +2.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -9.8 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.8 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.5 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -11.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -4.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.2 — chr6:152,970,519-152,983,579 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX5, Fbxo31, EMI1 |
| Gene groups (HGNC) | F-boxes other |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 12 pathways, smallest: Phosphorylation of Emi1; G1/S-Specific Transcription; SCF-beta-TrCP mediated degradation of Emi1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKT4](https://www.uniprot.org/uniprotkb/Q9UKT4) (F-box only protein 5):

> Regulator of APC activity during mitotic and meiotic cell cycle. During mitotic cell cycle plays a role as both substrate and inhibitor of APC-FZR1 complex. During G1 phase, plays a role as substrate of APC-FZR1 complex E3 ligase. Then switches as an inhibitor of APC-FZR1 complex during S and G2 leading to cell-cycle commitment. As APC inhibitor, prevents the degradation of APC substrates at multiple levels: by interacting with APC and blocking access of APC substrates to the D-box coreceptor, …

**Summary**, from NCBI Gene [26271](https://www.ncbi.nlm.nih.gov/gene/26271):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13584) · Entrez [26271](https://www.ncbi.nlm.nih.gov/gene/26271) · UniProt [Q9UKT4](https://www.uniprot.org/uniprotkb/Q9UKT4) · Ensembl [ENSG00000112029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112029)

## Data

Gene col 3312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3312); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3312]; `tensor/DDL_lfc|DDL_z.npy` [3312]; `embed/gene_vectors.npy` [3312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3312 or target_col == 3312). Every well: [[FBXO5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
