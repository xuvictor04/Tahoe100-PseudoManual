---
symbol: "C9orf72"
type: "gene"
col: 7232
ensembl_id: "ENSG00000147894"
name: "C9orf72-SMCR8 complex subunit"
location: "9p21.2"
module: 227
arm: "+"
pooled_cpm: 28.86
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/227"]
generated_by: "tahoemap"
---

# C9orf72

*C9orf72-SMCR8 complex subunit* — 9p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.05× (z +12.0, q 3e-30, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.484× (z -12.8, q 7e-35, down in 37 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.450× (z -7.3, q 4e-11, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISCA1]] (+0.59, fdr 1e-05), [[PNPLA8]] (+0.59, fdr 1e-05), [[FAM219A]] (+0.55, fdr 4e-05); moves opposite to [[CAV1]] (-0.55, fdr 1e-05), [[AJUBA]] (-0.53, fdr 2e-05), [[HNRNPD]] (-0.52, fdr 2e-05).
> It is in [[Module 227]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[GSTO1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.05×** | +12.0 | 3e-30 | 41/46 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +9.6 | 3e-19 | 34/47 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +7.4 | 3e-11 | 32/46 (HT-29, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.1 | 5e-05 | 21/47 (SW480, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +5.0 | 8e-05 | 20/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +4.6 | 4e-04 | 20/47 (HEC-1-A, RKO, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +4.5 | 6e-04 | 21/47 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.28×** | +4.3 | 0.001 | 13/47 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.1 | 0.003 | 16/47 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.011 | 12/47 (RKO, SW1417, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.011 | 7/45 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +3.6 | 0.014 | 15/47 (A-172, A549, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.019 | 13/47 (RKO, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.043 | 11/47 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.20×** | +3.2 | 0.050 | 15/47 (SW480, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.053 | 9/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.055 | 12/47 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.056 | 11/47 (MIA PaCa-2, SNU-423, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.484×** | -12.8 | 7e-35 | 37/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.572×** | -9.9 | 1e-20 | 30/47 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.638×** | -7.6 | 4e-12 | 23/34 (SHP-77, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.659×** | -7.4 | 2e-11 | 27/42 (A-427, J82, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.450×** | -7.3 | 4e-11 | 30/47 (A549, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.714×** | -5.7 | 8e-07 | 23/45 (J82, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.715×** | -5.7 | 8e-07 | 24/46 (A498, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.736×** | -5.0 | 4e-05 | 20/40 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.584×** | -4.9 | 6e-05 | 19/44 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **0.762×** | -4.8 | 8e-05 | 20/45 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.769×** | -4.7 | 2e-04 | 21/46 (A498, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.609×** | -4.5 | 3e-04 | 18/46 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.5 | 3e-04 | 18/47 (RKO, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.745×** | -4.3 | 7e-04 | 19/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.629×** | -4.2 | 9e-04 | 17/47 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.038 | 11/43 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.839× | -3.1 | 0.052 | 11/47 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.844× | -3.0 | 0.069 | 12/47 (LS 180, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 74.9 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 53.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HT-29 (line)]] | alt | 27.1 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.18× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[KATO III (line)]] | alt | 41.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 9.88 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 33.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A549 (line)]] | wt | 43.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 32.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0841× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[LS 180 (line)]] | wt | 44.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.314× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H460 (line)]] | wt | 67.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 40.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[SNU-423 (line)]] | alt | 28.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.245× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H1573 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[RKO (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -13.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 23.8 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.100× (z -10.8) |
| [[AN3 CA (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[PNPLA8]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FAM219A]] | +0.55 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[NBPF15]] | +0.55 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[FLYWCH1]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CSGALNACT2]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[GSTO1]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[ZFAND2A]] | +0.53 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[GK]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[MID2]] | +0.53 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[GID4]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[WIPI1]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAV1]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[AJUBA]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPD]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[S100A4]] | -0.51 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[SMAD6]] | -0.49 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[ZNF532]] | -0.48 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TNS3]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[STAG1]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SKA2]] | -0.47 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[NFIX]] | -0.47 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[FAT1]] | -0.47 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[CDK6]] | -0.47 | -0.44 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTO1]] | C | C9orf72's natural level strengthens GSTO1's drug response | C9orf72's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.11; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 227]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.6, -26.4); signed map (-40.0, 32.6). **Vector** length 98.5, 22.6% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.5 | +12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +9.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +3.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -4.5 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.3 | -9.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -3.9 | -12.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | C9orf72-SMCR8 complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.2 — chr9:27,535,640-27,573,866 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23980, DENNL72, DENND9 |
| Gene groups (HGNC) | DENN domain containing; SWC tripartite complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LT7](https://www.uniprot.org/uniprotkb/Q96LT7) (Guanine nucleotide exchange factor C9orf72):

> Acts as a guanine-nucleotide releasing factor (GEF) for Rab GTPases by promoting the conversion of inactive RAB-GDP to the active form RAB-GTP. Acts as a GEF for RAB39A which enables HOPS-mediated autophagosome-lysosome membrane tethering and fusion in mammalian autophagy. Component of the C9orf72-SMCR8 complex where both subunits display GEF activity and that regulates autophagy. As part of the C9orf72-SMCR8-WDR41 (CSW) complex, functions as GEF for RAB8A and RAB39B, thereby promoting …

**Summary**, from NCBI Gene [203228](https://www.ncbi.nlm.nih.gov/gene/203228):

> The protein encoded by this gene plays an important role in the regulation of endosomal trafficking, and has been shown to interact with Rab proteins that are involved in autophagy and endocytic transport. Expansion of a GGGGCC repeat from 2-22 copies to 700-1600 copies in the intronic sequence between alternate 5' exons in transcripts from this gene is associated with 9p-linked ALS (amyotrophic lateral sclerosis) and FTD (frontotemporal dementia) (PMID: 21944778, 21944779). Studies suggest …

**Accessions** — [HGNC:28337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28337) · Entrez [203228](https://www.ncbi.nlm.nih.gov/gene/203228) · UniProt [Q96LT7](https://www.uniprot.org/uniprotkb/Q96LT7) · Ensembl [ENSG00000147894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147894)

## Data

Gene col 7232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7232); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7232]; `tensor/DDL_lfc|DDL_z.npy` [7232]; `embed/gene_vectors.npy` [7232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7232 or target_col == 7232). Every well: [[C9orf72 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C9orf72.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
