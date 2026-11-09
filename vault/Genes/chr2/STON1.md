---
symbol: "STON1"
type: "gene"
col: 14346
ensembl_id: "ENSG00000243244"
name: "stonin 1"
location: "2p16.3"
module: 39
arm: "+"
pooled_cpm: 15.16
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# STON1

*stonin 1* — 2p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.50× (z +7.3, q 1e-10, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +5.3, q 3e-05, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.278× (z -16.4, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A14]] (+0.62, fdr 7e-06), [[KIAA1614]] (+0.62, fdr 7e-06), [[SLC5A11]] (+0.61, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NPAS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.50×** | +7.3 | 1e-10 | 30/47 (A498, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.3 | 3e-05 | 21/47 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 7e-05 | 23/47 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.36×** | +4.0 | 0.010 | 17/47 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.011 | 22/46 (NCI-H23, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.011 | 9/47 (CFPAC-1, H4, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.023 | 11/47 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +3.5 | 0.039 | 17/47 (NCI-H2347, A-427, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.30×** | +3.3 | 0.051 | 9/46 (C-33 A, BT-474, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.59× | +3.1 | 0.10 | 7/46 (C32, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.10 | 9/47 (C32, SW480, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.28× | +3.1 | 0.10 | 11/44 (A-427, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.278×** | -16.4 | 0e+00 | 46/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.295×** | -15.7 | 0e+00 | 37/44 (H4, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.348×** | -13.5 | 2e-39 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.349×** | -13.5 | 2e-39 | 39/47 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.405×** | -11.2 | 8e-27 | 32/42 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.225×** | -10.0 | 1e-21 | 37/47 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.328×** | -7.5 | 6e-12 | 31/44 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.552×** | -7.3 | 2e-11 | 29/46 (A-427, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.690×** | -6.7 | 1e-09 | 27/45 (NCI-H1792, CFPAC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -5.3 | 7e-06 | 24/47 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.615×** | -5.3 | 7e-06 | 25/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **0.667×** | -5.2 | 1e-05 | 20/44 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -5.0 | 2e-05 | 25/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.670×** | -4.7 | 9e-05 | 22/33 (SW480, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.648×** | -4.7 | 1e-04 | 22/45 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.714×** | -4.2 | 0.001 | 19/47 (NCI-H1573, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -3.5 | 0.015 | 14/45 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.697×** | -3.3 | 0.028 | 7/47 (NCI-H460, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.052 | 9/46 (COLO 205, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.052 | 16/46 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.644×** | -2.9 | 0.076 | 11/40 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 29.5 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -11.4) |
| [[A-172 (line)]] | wt | 35.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0939× (z -9.0) |
| [[A549 (line)]] | wt | 13.1 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0776× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0972× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.164× (z -12.6) |
| [[A-427 (line)]] | wt | 31.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0459× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0514× (z -13.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 50.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 9.60 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.118× (z -14.2) |
| [[C32 (line)]] | wt | 40.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 3 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0280× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0259× (z -9.9) |
| [[KATO III (line)]] | alt | 10.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.108× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -11.9) |
| [[SW 900 (line)]] | alt | 19.7 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0333× (z -9.5) |
| [[H4 (line)]] | wt | 32.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0401× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0772× (z -12.2) |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -9.6) |
| [[PANC-1 (line)]] | alt | 8.23 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -8.7) |
| [[A498 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -9.2) |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -10.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.196× (z -8.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 6.90 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0610× (z -9.1) |
| [[J82 (line)]] | alt | 9.36 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -8.6) |
| [[LoVo (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.212× (z -9.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 7.85 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -13.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 7.21 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0501× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.132× (z -8.5) |
| [[SW1417 (line)]] | alt | 5.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0587× (z -10.3) |
| [[AN3 CA (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A14]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[KIAA1614]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SLC5A11]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[FLACC1]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[POLN]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SGSM3-AS1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[APH1B]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[C9orf24]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[C9]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ANKDD1B]] | +0.57 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SCUBE2]] | +0.57 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CDKL4]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPAS1]] | B | NPAS1 activity raises STON1's level | lines that do not express NPAS1 (9) vs lines expressing it (41) | 1.93× lower at baseline in the lines without NPAS1 | 0.011 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADORA1]] | B | ADORA1 activity raises STON1's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without ADORA1 | 0.039 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.2, -12.6); signed map (18.7, 10.0). **Vector** length 70.0, 13.7% of its response variance represented; |z| ≥ 3 in 1,293 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.7 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.8 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | -3.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.1 | -4.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.7 | -2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -13.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -13.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | stonin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.3 — chr2:48,529,383-48,598,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SBLF, stoned-b1 |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Q2](https://www.uniprot.org/uniprotkb/Q9Y6Q2) (Stonin-1):

> May be involved in the endocytic machinery.

**Summary**, from NCBI Gene [11037](https://www.ncbi.nlm.nih.gov/gene/11037):

> Endocytosis of cell surface proteins is mediated by a complex molecular machinery that assembles on the inner surface of the plasma membrane. This gene encodes one of two human homologs of the Drosophila melanogaster stoned B protein. This protein is related to components of the endocytic machinery and exhibits a modular structure consisting of an N-terminal proline-rich domain, a central region of homology specific to the human stoned B-like proteins, and a C-terminal region homologous to the …

**Accessions** — [HGNC:17003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17003) · Entrez [11037](https://www.ncbi.nlm.nih.gov/gene/11037) · UniProt [Q9Y6Q2](https://www.uniprot.org/uniprotkb/Q9Y6Q2) · Ensembl [ENSG00000243244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243244)

## Data

Gene col 14346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14346); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14346]; `tensor/DDL_lfc|DDL_z.npy` [14346]; `embed/gene_vectors.npy` [14346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14346 or target_col == 14346). Every well: [[STON1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STON1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
