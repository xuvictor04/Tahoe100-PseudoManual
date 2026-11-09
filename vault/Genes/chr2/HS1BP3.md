---
symbol: "HS1BP3"
type: "gene"
col: 4029
ensembl_id: "ENSG00000118960"
name: "HCLS1 binding protein 3"
location: "2p24.1"
module: 122
arm: "+"
pooled_cpm: 15.92
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 15
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# HS1BP3

*HCLS1 binding protein 3* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +8.1, q 3e-13, up in 17 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.45× (z +5.8, q 2e-06, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.440× (z -13.0, q 6e-36, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.668× (z -9.1, q 2e-17, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM50A]] (+0.62, fdr 1e-05), [[GNPDA1]] (+0.60, fdr 1e-05), [[MBD6]] (+0.59, fdr 1e-05); moves opposite to [[SNRPB]] (-0.55, fdr 2e-05), [[MYCBP]] (-0.54, fdr 1e-05), [[ARPC5L]] (-0.51, fdr 4e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.1 | 3e-13 | 17/29 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +5.8 | 2e-06 | 20/48 (KATO III, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.28×** | +5.5 | 6e-06 | 22/48 (A-427, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.41×** | +5.5 | 6e-06 | 19/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.2 | 2e-05 | 12/36 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.8 | 1e-04 | 19/48 (SW480, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.32×** | +4.3 | 0.001 | 10/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.001 | 12/48 (MIA PaCa-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.002 | 13/47 (NCI-H23, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.003 | 12/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.003 | 10/47 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.0 | 0.003 | 8/48 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +4.0 | 0.003 | 15/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.27×** | +3.6 | 0.012 | 8/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.015 | 10/47 (LoVo, SW480, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.040 | 7/48 (KATO III, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.040 | 7/48 (J82, PANC-1, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.044 | 4/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.045 | 11/47 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.049 | 6/48 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.049 | 9/47 (Hs 766T, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.049 | 3/48 (HepG2/C3A, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.440×** | -13.0 | 6e-36 | 41/48 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.449×** | -12.7 | 2e-34 | 37/46 (SW480, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.548×** | -9.5 | 2e-19 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -9.1 | 2e-17 | 28/47 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.579×** | -8.7 | 5e-16 | 29/47 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -6.4 | 2e-08 | 31/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.684×** | -5.8 | 5e-07 | 25/48 (SW48, H4, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.476×** | -5.8 | 5e-07 | 25/46 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.695×** | -5.8 | 5e-07 | 22/48 (HT-29, RPMI-7951, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -5.2 | 1e-05 | 21/47 (HepG2/C3A, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.731×** | -5.0 | 3e-05 | 17/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.745×** | -4.7 | 1e-04 | 19/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.761×** | -4.2 | 0.001 | 20/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | **0.763×** | -4.1 | 0.001 | 18/43 (RKO, HOP62, …) | top dose only |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.859× | -3.4 | 0.025 | 9/48 (HEC-1-A, SW1417, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.032 | 15/47 (Hs 766T, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.5 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0617× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 18.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.169× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.239× (z -12.7) |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -9.6) |
| [[SHP-77 (line)]] | alt | 7.79 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.126× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -11.1) |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 9.37 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0625× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.79× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 61.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.141× (z -9.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.327× (z -8.9) |
| [[SW48 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0916× (z -10.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM50A]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GNPDA1]] | +0.60 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MBD6]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[VPS41]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PRXL2C]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[UAP1L1]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[SLC4A2]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[WASHC2A]] | +0.54 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SNX15]] | +0.54 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[AMDHD2]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[WASHC2C]] | +0.53 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[VPS13C]] | +0.53 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[MYCBP]] | -0.54 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RFWD3]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PGP]] | -0.50 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[FBXW7]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RASA1]] | -0.48 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[HAUS8]] | -0.48 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[WT1]] | -0.48 | -0.32 / -0.50 | both halves | 1e-04 |  |
| [[HSPA14]] | -0.47 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[DBF4B]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[FEN1]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HS1BP3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[WT1]] | B | WT1 activity raises HS1BP3's level | lines that do not express WT1 (29) vs lines expressing it (21) | 1.18× lower at baseline in the lines without WT1 | 0.090 | ⚠ within organs, on part of the lines; also absent: WT1-AS, INA, ZNF677 |
| [[CLIP3]] | C | CLIP3 activity raises HS1BP3's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.8, 13.6); signed map (11.7, -16.6). **Vector** length 78.1, 14.9% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.1 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.8 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.0 | -5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -2.4 | -12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Brimonidine (drug)]] 5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | HCLS1 binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:20,560,448-20,651,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HS1-BP3, FLJ14249 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53T59](https://www.uniprot.org/uniprotkb/Q53T59) (HCLS1-binding protein 3):

> May be a modulator of IL-2 signaling.

**Summary**, from NCBI Gene [64342](https://www.ncbi.nlm.nih.gov/gene/64342):

> The protein encoded by this gene shares similarity with mouse Hs1bp3, an Hcls1/Hs1-interacting protein that may be involved in lymphocyte activation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24979) · Entrez [64342](https://www.ncbi.nlm.nih.gov/gene/64342) · UniProt [Q53T59](https://www.uniprot.org/uniprotkb/Q53T59) · Ensembl [ENSG00000118960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118960)

## Data

Gene col 4029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4029); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4029]; `tensor/DDL_lfc|DDL_z.npy` [4029]; `embed/gene_vectors.npy` [4029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4029 or target_col == 4029). Every well: [[HS1BP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HS1BP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
