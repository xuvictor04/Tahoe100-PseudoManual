---
symbol: "APH1B"
type: "gene"
col: 6193
ensembl_id: "ENSG00000138613"
name: "aph-1B gamma-secretase subunit"
location: "15q22.2"
module: 39
arm: "+"
pooled_cpm: 11.92
n_lines_expressing: 44
n_dd_up: 22
n_dd_down: 31
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# APH1B

*aph-1B gamma-secretase subunit* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.93× (z +10.0, q 1e-20, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (22 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.434× (z -12.6, q 2e-33, down in 30 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.614× (z -7.3, q 1e-11, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPLN]] (+0.59, fdr 1e-05), [[STON1]] (+0.58, fdr 1e-05), [[RSPH9]] (+0.56, fdr 3e-05); moves opposite to [[GMDS]] (-0.47, fdr 6e-05), [[MLPH]] (-0.45, fdr 8e-05), [[ABHD2]] (-0.44, fdr 1e-04).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CLDN14-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[SLC30A4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +10.0 | 1e-20 | 30/41 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.40×** | +7.2 | 2e-10 | 19/41 (A498, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.54×** | +6.6 | 1e-08 | 22/41 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.3 | 2e-05 | 19/42 (A498, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.36×** | +4.8 | 2e-04 | 15/42 (HOP62, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 2e-04 | 13/40 (HOP62, C32, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.6 | 4e-04 | 4/42 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.005 | 9/41 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.014 | 12/42 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.27×** | +3.7 | 0.014 | 5/36 (A-172, SW 1271, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.022 | 9/42 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.025 | 4/41 (A549, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.027 | 9/41 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.030 | 11/40 (A549, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.037 | 8/42 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.041 | 5/42 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.041 | 8/42 (A549, SW1417, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.065 | 9/42 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.081 | 3/42 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.081 | 4/41 (A498, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.434×** | -12.6 | 2e-33 | 30/38 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.437×** | -12.5 | 3e-33 | 34/42 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.341×** | -12.3 | 2e-32 | 29/35 (J82, Hs 766T, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.515×** | -10.0 | 2e-21 | 28/42 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.517×** | -9.9 | 3e-21 | 25/42 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.634×** | -9.7 | 3e-20 | 22/39 (NCI-H1573, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.578×** | -8.3 | 1e-14 | 23/42 (LOX-IMVI, NCI-H1792, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.495×** | -8.0 | 7e-14 | 24/41 (A549, NCI-H1573, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.565×** | -7.9 | 1e-13 | 19/26 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **0.591×** | -7.9 | 1e-13 | 20/30 (LOX-IMVI, A-172, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -7.3 | 1e-11 | 24/42 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -6.8 | 3e-10 | 26/42 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.653×** | -6.4 | 6e-09 | 22/42 (HCT15, AN3 CA, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.653×** | -6.4 | 6e-09 | 22/38 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.653×** | -6.4 | 6e-09 | 22/42 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.519×** | -5.2 | 8e-06 | 14/38 (Panc 03.27, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.711×** | -5.1 | 9e-06 | 16/42 (LOX-IMVI, C-33 A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.755×** | -4.0 | 0.002 | 16/41 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.716×** | -3.8 | 0.003 | 7/42 (A549, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **0.799×** | -3.4 | 0.016 | 6/42 (COLO 205, Panc 03.27, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.763×** | -2.9 | 0.071 | 4/42 (A498, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **0.815×** | -2.8 | 0.084 | 10/38 (HT-29, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 32.5 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0931× (z -17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.316× (z -8.5) |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -14.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.298× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 17.4 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -18.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A549 (line)]] | wt | 30.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.8) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[Hs 766T (line)]] | wt | 8.11 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0438× (z -10.7) ⚠ toxic · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.106× (z -10.2) |
| [[H4 (line)]] | wt | 18.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0675× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -10.3) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 8.02 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 1271 (line)]] | alt | 45.6 | 0 | 2 | — | [[Sunitinib (drug)]] 0.05 µM 0.0638× (z -9.2) |
| [[A-172 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.224× (z -8.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 7.28 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 7.13 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0552× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0725× (z -11.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 4.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0976× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.6) ⚠ cell-cycle shift, explains ~81% of this change |
| [[RKO (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPLN]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[STON1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RSPH9]] | +0.56 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[MIR137HG]] | +0.54 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[BASP1-AS1]] | +0.54 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[UBE2Q2P13]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ADAP2]] | +0.52 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[TTC23L]] | +0.51 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[CDKL2]] | +0.50 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[LINC01030]] | +0.49 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[DSE]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[FGF11]] | +0.49 | +0.46 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMDS]] | -0.47 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[MLPH]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ABHD2]] | -0.44 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[BDH1]] | -0.44 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[POLA1]] | -0.43 | -0.32 / -0.45 | both halves | 1e-04 |  |
| [[ENTPD6]] | -0.43 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[PROM1]] | -0.42 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[IL20RA]] | -0.42 | -0.50 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises APH1B's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.76× lower at baseline in the lines without CLDN14-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[LINC03041]] | B | LINC03041 activity raises APH1B's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without LINC03041 | 0.028 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[DNAH11]] | B | DNAH11 activity raises APH1B's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without DNAH11 | 0.033 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[OR9Q1]] | B | OR9Q1 activity raises APH1B's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without OR9Q1 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[MAP2K1]] | B | MAP2K1 activity lowers APH1B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BASP1-AS1]] | B | BASP1-AS1 activity raises APH1B's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without BASP1-AS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[PAPPA]] | B | PAPPA activity raises APH1B's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.18× lower at baseline in the lines without PAPPA | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[TTC23L]] | B | TTC23L activity raises APH1B's level | lines that do not express TTC23L (5) vs lines expressing it (45) | 3.20× lower at baseline in the lines without TTC23L | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAJC18, NXPE3, TBKBP1; maybe low, not absent; its own permutation p |
| [[PLAGL1]] | B | PLAGL1 activity raises APH1B's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without PLAGL1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5 |
| [[JAM2]] | B | JAM2 activity raises APH1B's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.23× lower at baseline in the lines without JAM2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[CCDC3]] | C | CCDC3 activity raises APH1B's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 3.37× lower at baseline in the lines without CCDC3 | 0.078 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC30A4]] | B | APH1B activity raises SLC30A4's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without APH1B | 0.011 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[USP50]] | B | APH1B activity raises USP50's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without APH1B | 0.031 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[PLA2G4C]] | B | APH1B activity raises PLA2G4C's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without APH1B | 0.031 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[UBE2Q2P13]] | B | APH1B activity raises UBE2Q2P13's level | lines that do not express APH1B (6) vs lines expressing it (44) | 2.29× lower at baseline in the lines without APH1B | 0.071 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[CTSK]] | B | APH1B activity raises CTSK's level | lines that do not express APH1B (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without APH1B | 0.082 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[CLDN14-AS1]] | B | APH1B activity raises CLDN14-AS1's level | lines that do not express APH1B (6) vs lines expressing it (44) | 3.65× lower at baseline in the lines without APH1B | 0.095 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.5, -12.1); signed map (23.8, 20.2). **Vector** length 68.2, 12.0% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +6.1 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +3.9 | +6.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +2.3 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.0 | -10.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.9 | -12.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -1.7 | -12.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.7 | -4.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -1.6 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | aph-1B gamma-secretase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:63,276,018-63,309,126 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PSFL, APH-1B, DKFZp564D0372 |
| Gene groups (HGNC) | Gamma-secretase complex subunits |
| Reactome | 33 pathways, smallest: Noncanonical activation of NOTCH3; NOTCH4 Activation and Transmission of Signal to the Nucleus; Regulated proteolysis of p75NTR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WW43](https://www.uniprot.org/uniprotkb/Q8WW43) (Gamma-secretase subunit APH-1B):

> Probable subunit of the gamma-secretase complex, an endoprotease complex that catalyzes the intramembrane cleavage of integral proteins such as Notch receptors and APP (amyloid-beta precursor protein). It probably represents a stabilizing cofactor for the presenilin homodimer that promotes the formation of a stable complex. Probably present in a minority of gamma-secretase complexes compared to APH1A.

**Summary**, from NCBI Gene [83464](https://www.ncbi.nlm.nih.gov/gene/83464):

> This gene encodes a multi-pass transmembrane protein that is a functional component of the gamma-secretase complex, which also contains presenilin and nicastrin. This protein represents a stabilizing cofactor for the presenilin holoprotein in the complex. The gamma-secretase complex catalyzes the cleavage of integral proteins such as notch receptors and beta-amyloid precursor protein. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:24080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24080) · Entrez [83464](https://www.ncbi.nlm.nih.gov/gene/83464) · UniProt [Q8WW43](https://www.uniprot.org/uniprotkb/Q8WW43) · Ensembl [ENSG00000138613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138613)

## Data

Gene col 6193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6193); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6193]; `tensor/DDL_lfc|DDL_z.npy` [6193]; `embed/gene_vectors.npy` [6193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6193 or target_col == 6193). Every well: [[APH1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APH1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
