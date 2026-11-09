---
symbol: "PAAF1"
type: "gene"
col: 10624
ensembl_id: "ENSG00000175575"
name: "proteasomal ATPase associated factor 1"
location: "11q13.4"
module: 89
arm: "+"
pooled_cpm: 24.6
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# PAAF1

*proteasomal ATPase associated factor 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.44× (z +9.0, q 1e-16, up in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.34× (z +7.2, q 2e-10, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.365× (z -17.3, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIX23]] (+0.71, fdr 7e-06), [[GPALPP1]] (+0.71, fdr 7e-06), [[ALKBH3]] (+0.69, fdr 7e-06); moves opposite to [[CADM4]] (-0.60, fdr 3e-05), [[GDF11]] (-0.57, fdr 1e-04), [[MAPK8]] (-0.56, fdr 4e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF675]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.44×** | +9.0 | 1e-16 | 32/48 (KATO III, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.2 | 2e-10 | 29/48 (SW1417, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +6.1 | 1e-07 | 30/48 (KATO III, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.17× | +3.9 | 0.012 | 20/47 (A-427, PANC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.015 | 6/46 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.8 | 0.015 | 13/48 (H4, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.029 | 10/48 (KATO III, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.034 | 6/48 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.034 | 14/48 (KATO III, J82, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.049 | 6/48 (LOX-IMVI, A549, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.051 | 15/47 (SW480, A498, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.099 | 11/48 (SHP-77, Panc 03.27, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.19× | +3.0 | 0.11 | 7/48 (SW480, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.365×** | -17.3 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.379×** | -16.6 | 0e+00 | 38/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.440×** | -9.9 | 6e-21 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -9.4 | 9e-19 | 36/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.697×** | -8.7 | 4e-16 | 30/47 (SNU-423, A498, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.523×** | -7.8 | 5e-13 | 31/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -7.8 | 7e-13 | 33/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.645×** | -7.2 | 4e-11 | 27/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.754×** | -6.8 | 7e-10 | 32/48 (HT-29, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.524×** | -5.8 | 4e-07 | 22/46 (A-427, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.710×** | -5.4 | 3e-06 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.733×** | -5.3 | 6e-06 | 21/48 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.734×** | -4.9 | 5e-05 | 19/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.761×** | -4.6 | 1e-04 | 17/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.765×** | -4.6 | 2e-04 | 20/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.772×** | -4.4 | 4e-04 | 22/48 (SW1417, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.787×** | -4.1 | 0.002 | 14/47 (CFPAC-1, SW48, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.010 | 14/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.687×** | -3.3 | 0.023 | 15/46 (KATO III, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.831×** | -3.1 | 0.048 | 3/48 (NCI-H2030, NCI-H661, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.782×** | -2.9 | 0.085 | 9/47 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.7 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -22.2) |
| [[KATO III (line)]] | alt | 30.7 | 1 (1 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.59× (z +10.9) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.128× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 19.9 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -13.1) |
| [[J82 (line)]] | alt | 31.9 | 0 | 4 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0649× (z -12.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.331× (z -9.8) |
| [[SW480 (line)]] | alt | 30.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -16.3) |
| [[BT-474 (line)]] | alt | 52.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 21.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.43× (z +8.8) ⚠ cell-cycle shift, explains ~46% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.7) |
| [[A498 (line)]] | wt | 18.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.7) ⚠ cell-cycle shift, explains ~73% of this change |
| [[A549 (line)]] | wt | 19.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 24.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -8.5) |
| [[HOP62 (line)]] | alt | 18.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -10.5) |
| [[HT-29 (line)]] | alt | 17.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.362× (z -8.9) |
| [[A-427 (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -12.2) ⚠ cell-cycle shift, explains ~74% of this change |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0903× (z -8.5) |
| [[C-33 A (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -10.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -13.3) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0951× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -11.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.253× (z -9.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 50.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.98× (z +8.9) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 55.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -11.2) |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.111× (z -9.8) |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.3) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -9.3) |
| [[A-172 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIX23]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[GPALPP1]] | +0.71 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[TRMT61B]] | +0.69 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[SART3]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[VPS33A]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[POLR3F]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ZUP1]] | +0.66 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[IREB2]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TEFM]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[UQCC1]] | +0.64 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[MTRF1]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CADM4]] | -0.60 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[GDF11]] | -0.57 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MAPK8]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DIAPH1]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TMSB4X]] | -0.55 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[BCAM]] | -0.55 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[KLF12]] | -0.54 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[TIMP2]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises PAAF1's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.78× lower at baseline in the lines without ZNF675 | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PAAF1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, TAK-733) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[FAM156A]] | C | FAM156A's natural level strengthens PAAF1's drug response | FAM156A's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.43; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.5, 7.6); signed map (-9.3, -17.3). **Vector** length 75.9, 15.2% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.1 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +1.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.2 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasomal ATPase associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,876,699-73,931,114 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11848, Rpn14; previously WDR71 |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRP4](https://www.uniprot.org/uniprotkb/Q9BRP4) (Proteasomal ATPase-associated factor 1):

> Inhibits proteasome 26S assembly and proteolytic activity by impairing the association of the 19S regulatory complex with the 20S core. In case of HIV-1 infection, recruited by viral Tat to the HIV-1 promoter, where it promotes the recruitment of 19S regulatory complex through dissociation of the proteasome 26S. This presumably promotes provirus transcription efficiency. Protects SUPT6H from proteasomal degradation.

**Summary**, from NCBI Gene [80227](https://www.ncbi.nlm.nih.gov/gene/80227):

> This gene encodes a WD repeat-containing protein involved in regulation of association of proteasome components. During HIV infection, the encoded protein is thought to promote provirus transcription through recruitment of the 19S regulatory complex. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:25687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25687) · Entrez [80227](https://www.ncbi.nlm.nih.gov/gene/80227) · UniProt [Q9BRP4](https://www.uniprot.org/uniprotkb/Q9BRP4) · Ensembl [ENSG00000175575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175575)

## Data

Gene col 10624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10624); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10624]; `tensor/DDL_lfc|DDL_z.npy` [10624]; `embed/gene_vectors.npy` [10624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10624 or target_col == 10624). Every well: [[PAAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
