---
symbol: "FARS2"
type: "gene"
col: 7049
ensembl_id: "ENSG00000145982"
name: "phenylalanyl-tRNA synthetase 2, mitochondrial"
location: "6p25.1"
module: 185
arm: "+"
pooled_cpm: 104.45
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# FARS2

*phenylalanyl-tRNA synthetase 2, mitochondrial* — 6p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.31× (z +5.4, q 3e-05, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.630× (z -9.3, q 1e-17, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC4]] (+0.71, fdr 7e-06), [[QTRT2]] (+0.71, fdr 7e-06), [[RPTOR]] (+0.68, fdr 7e-06); moves opposite to [[RGS9]] (-0.61, fdr 1e-05), [[SYP]] (-0.58, fdr 4e-05), [[KIAA0513]] (-0.58, fdr 6e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HYCC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.4 | 3e-05 | 38/48 (SW1417, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +5.3 | 3e-05 | 39/48 (NCI-H2347, C-33 A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.27×** | +4.7 | 5e-04 | 27/48 (NCI-H1573, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +4.4 | 0.002 | 28/49 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.002 | 37/48 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.018 | 28/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.020 | 28/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.039 | 28/47 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.057 | 24/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.069 | 24/48 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.0 | 0.12 | 11/48 (SHP-77, HOP62, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.12 | 25/48 (LoVo, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.630×** | -9.3 | 1e-17 | 48/48 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.530×** | -8.7 | 1e-15 | 39/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -7.8 | 8e-13 | 32/44 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.589×** | -7.5 | 8e-12 | 41/48 (SHP-77, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.613×** | -6.9 | 4e-10 | 45/49 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.530×** | -6.8 | 1e-09 | 35/49 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -5.9 | 2e-07 | 32/48 (SW480, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.671×** | -5.7 | 1e-06 | 32/48 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.655×** | -5.5 | 2e-06 | 30/45 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.683×** | -5.4 | 4e-06 | 37/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.707×** | -4.7 | 1e-04 | 33/47 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.723×** | -4.6 | 2e-04 | 32/48 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.722×** | -4.4 | 4e-04 | 28/48 (MIA PaCa-2, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.803×** | -4.4 | 4e-04 | 25/48 (MIA PaCa-2, C32, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.735×** | -4.4 | 4e-04 | 26/48 (SHP-77, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.830×** | -3.8 | 0.006 | 23/49 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.007 | 25/49 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.611×** | -3.6 | 0.008 | 28/48 (CFPAC-1, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 189 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -18.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 145 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.550× (z -8.5) |
| [[HOP62 (line)]] | alt | 137 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 71.6 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.306× (z -12.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SHP-77 (line)]] | alt | 196 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -14.5) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 124 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -11.5) |
| [[C32 (line)]] | wt | 113 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -8.5) |
| [[LoVo (line)]] | wt | 83.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.369× (z -10.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 132 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 104 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.345× (z -10.8) ⚠ toxic |
| [[A498 (line)]] | wt | 65.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 203 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 102 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.348× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 91.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.213× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 86.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -9.4) ⚠ cell-cycle shift, explains ~76% of this change |
| [[AsPC-1 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 93.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.516× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 92.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 80.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.350× (z -8.5) |
| [[J82 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 93.5 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.194× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.519× (z -9.0) |
| [[SW 1088 (line)]] | alt | 128 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.102× (z -9.0) |
| [[SW 1271 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 94.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 108 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[RPTOR]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[IPO11]] | +0.67 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[GATB]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 | STRING 496 |
| [[PARG]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.66 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[COX10]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CDKAL1]] | +0.65 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[AFG1L]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[LINC00630]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[UTP20]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS9]] | -0.61 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[SYP]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[KIAA0513]] | -0.58 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[CCNYL1]] | -0.56 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[GRHL1]] | -0.55 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[OAZ1]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SLC30A4]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[AMN1]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ARID3A]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GLIPR2]] | -0.53 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[HDAC5]] | -0.52 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SYT7]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYCC1]] | B | HYCC1 activity raises FARS2's level | lines that do not express HYCC1 (8) vs lines expressing it (42) | 1.26× lower at baseline in the lines without HYCC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: FERMT2, CCDC88A, HEG1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.9, -32.5); signed map (-5.3, -40.8). **Vector** length 122, 44.4% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.0 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.4 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.6 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.1 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -14.5 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -12.1 | -6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.8 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | phenylalanyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.1 — chr6:5,261,044-5,829,192 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ236A3.1, mtPheRS; previously FARS1 |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95363](https://www.uniprot.org/uniprotkb/O95363) (Phenylalanine--tRNA ligase, mitochondrial):

> Is responsible for the charging of tRNA(Phe) with phenylalanine in mitochondrial translation. To a lesser extent, also catalyzes direct attachment of m-Tyr (an oxidized version of Phe) to tRNA(Phe), thereby opening the way for delivery of the misacylated tRNA to the ribosome and incorporation of ROS-damaged amino acid into proteins.

**Summary**, from NCBI Gene [10667](https://www.ncbi.nlm.nih.gov/gene/10667):

> This gene encodes a protein that transfers phenylalanine to its cognate tRNA. This protein localizes to the mitochondrion and plays a role in mitochondrial protein translation. Mutations in this gene can cause combined oxidative phosphorylation deficiency 14 (Alpers encephalopathy). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:21062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21062) · Entrez [10667](https://www.ncbi.nlm.nih.gov/gene/10667) · UniProt [O95363](https://www.uniprot.org/uniprotkb/O95363) · Ensembl [ENSG00000145982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145982)

## Data

Gene col 7049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7049); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7049]; `tensor/DDL_lfc|DDL_z.npy` [7049]; `embed/gene_vectors.npy` [7049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7049 or target_col == 7049). Every well: [[FARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
