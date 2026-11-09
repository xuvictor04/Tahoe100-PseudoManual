---
symbol: "SYT7"
type: "gene"
col: 236
ensembl_id: "ENSG00000011347"
name: "synaptotagmin 7"
location: "11q12.2"
module: 208
arm: "+"
pooled_cpm: 15.56
n_lines_expressing: 41
n_dd_up: 16
n_dd_down: 27
n_dd_up_clean: 15
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# SYT7

*synaptotagmin 7* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.08× (z +15.3, q 0e+00, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.567× (z -8.3, q 6e-14, down in 21 of 39 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.600× (z -7.7, q 1e-12, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXO6]] (+0.63, fdr 1e-05), [[RPLP0P2]] (+0.60, fdr 2e-05), [[KIF5C]] (+0.59, fdr 2e-05); moves opposite to [[FARS2]] (-0.52, fdr 3e-05), [[PDHX]] (-0.50, fdr 4e-05).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[DLGAP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +15.3 | 0e+00 | 32/39 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.24×** | +12.3 | 4e-32 | 28/38 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +7.7 | 4e-12 | 18/39 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +6.3 | 4e-08 | 16/39 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 1e-07 | 21/38 (H4, hTERT-HPNE, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.37×** | +4.6 | 5e-04 | 17/37 (H4, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.2 | 0.002 | 9/39 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.0 | 0.004 | 9/34 (SW1417, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.004 | 11/38 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.005 | 13/39 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.028 | 7/37 (CFPAC-1, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.052 | 6/37 (SW480, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Hesperidin (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.052 | 3/38 (AsPC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.083 | 7/38 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.16× | +3.0 | 0.090 | 4/39 (J82, HEC-1-A, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.094 | 3/38 (H4, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[SBI-0640756 (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.097 | 3/36 (NCI-H2347, H4, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.567×** | -8.3 | 6e-14 | 21/39 (NCI-H1792, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.686×** | -7.9 | 7e-13 | 19/38 (NCI-H1792, A-427, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.599×** | -7.8 | 1e-12 | 20/38 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -7.7 | 1e-12 | 21/37 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.602×** | -7.4 | 1e-11 | 25/38 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.623×** | -7.2 | 6e-11 | 23/38 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.717×** | -6.9 | 3e-10 | 18/39 (HS-578T, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.640×** | -6.8 | 8e-10 | 21/39 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.649×** | -6.6 | 4e-09 | 21/38 (J82, H4, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.7 | 6e-07 | 20/37 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.690×** | -5.6 | 1e-06 | 16/38 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -5.5 | 2e-06 | 14/39 (A-427, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.770×** | -5.5 | 2e-06 | 20/39 (HS-578T, J82, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 1e-04 | 17/39 (NCI-H1792, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.722×** | -4.7 | 1e-04 | 16/38 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.764×** | -4.1 | 0.001 | 10/39 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -3.8 | 0.005 | 14/37 (A-427, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.809×** | -3.2 | 0.034 | 8/39 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.811×** | -3.2 | 0.037 | 5/39 (J82, A-172, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **0.812×** | -3.2 | 0.037 | 10/39 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.037 | 8/38 (SK-MEL-2, HCT15, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 0.05 µM |  | **0.816×** | -3.1 | 0.046 | 1/39 (hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 44.5 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -21.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0794× (z -17.0) |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -13.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -11.1) |
| [[A-427 (line)]] | wt | 25.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -19.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -11.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -9.5) |
| [[COLO 205 (line)]] | alt | 46.8 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.259× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.284× (z -9.0) |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 31.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.5) ⚠ cell-cycle shift, explains ~58% of this change | [[Selinexor (drug)]] 5 µM 0.482× (z -9.0) |
| [[SHP-77 (line)]] | alt | 61.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -12.1) |
| [[SW480 (line)]] | alt | 12.8 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.49× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0674× (z -10.6) |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0968× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HT-29 (line)]] | alt | 44.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -10.2) |
| [[J82 (line)]] | alt | 7.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0794× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0952× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 96.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -9.2) |
| [[A-172 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO6]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[KIF5C]] | +0.59 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[ARVCF]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[LTBP4]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[RGS9]] | +0.58 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[JAKMIP1]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SULT4A1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CRTAC1]] | +0.57 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SLC17A7]] | +0.57 | +0.41 / +0.63 | both halves | 4e-05 | pathway: Neuronal System |
| [[TNNT1]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARS2]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PDHX]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SYT7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COLEC12]] | B | COLEC12 activity lowers SYT7's level | lines that do not express COLEC12 (25) vs lines expressing it (25) | 1.31× higher at baseline in the lines without COLEC12 | 0.039 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, PIEZO2, SLC22A17; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLGAP4]] | B | SYT7 activity lowers DLGAP4's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.18× higher at baseline in the lines without SYT7 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PPP2R5B]] | B | SYT7 activity lowers PPP2R5B's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.16× higher at baseline in the lines without SYT7 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NOVA2]] | B | SYT7 activity lowers NOVA2's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without SYT7 | 0.079 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPSM1]] | B | SYT7 activity lowers GPSM1's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.72× higher at baseline in the lines without SYT7 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SNPH]] | B | SYT7 activity lowers SNPH's level | lines that do not express SYT7 (9) vs lines expressing it (41) | 1.29× higher at baseline in the lines without SYT7 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.0, 36.1); signed map (28.8, 29.1). **Vector** length 97.3, 21.7% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.3 | +15.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.5 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.4 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.0 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | -5.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.0 | -6.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.8 | -7.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,513,714-61,581,148 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPCA-7, SYT-VII, MGC150517; previously PCANAP7 |
| Gene groups (HGNC) | Synaptotagmins |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O43581](https://www.uniprot.org/uniprotkb/O43581) (Synaptotagmin-7):

> Ca(2+) sensor involved in Ca(2+)-dependent exocytosis of secretory and synaptic vesicles through Ca(2+) and phospholipid binding to the C2 domain (By similarity). Ca(2+) induces binding of the C2-domains to phospholipid membranes and to assembled SNARE-complexes; both actions contribute to triggering exocytosis (By similarity). SYT7 binds Ca(2+) with high affinity and slow kinetics compared to other synaptotagmins (By similarity). Involved in Ca(2+)-triggered lysosomal exocytosis, a major …

**Summary**, from NCBI Gene [9066](https://www.ncbi.nlm.nih.gov/gene/9066):

> This gene is a member of the synaptotagmin gene family and encodes a protein similar to other family members that mediate calcium-dependent regulation of membrane trafficking in synaptic transmission. A similar protein in rodents mediates hormone secretion and lysosome exocytosis. In humans, expression of this gene has been associated with prostate cancer. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:11514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11514) · Entrez [9066](https://www.ncbi.nlm.nih.gov/gene/9066) · UniProt [O43581](https://www.uniprot.org/uniprotkb/O43581) · Ensembl [ENSG00000011347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011347)

## Data

Gene col 236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 236); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 236]; `tensor/DDL_lfc|DDL_z.npy` [236]; `embed/gene_vectors.npy` [236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 236 or target_col == 236). Every well: [[SYT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
