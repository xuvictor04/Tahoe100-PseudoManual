---
symbol: "NMNAT1"
type: "gene"
col: 10410
ensembl_id: "ENSG00000173614"
name: "nicotinamide nucleotide adenylyltransferase 1"
location: "1p36.22"
module: 23
arm: "+"
pooled_cpm: 20.82
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# NMNAT1

*nicotinamide nucleotide adenylyltransferase 1* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +20.8, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.573× (z -9.6, q 7e-19, down in 34 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.368× (z -9.0, q 5e-17, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF785]] (+0.74, fdr 7e-06), [[ZNF425]] (+0.73, fdr 1e-05), [[MFF-DT]] (+0.70, fdr 2e-05); moves opposite to [[TRAK1]] (-0.70, fdr 7e-06), [[SOAT1]] (-0.66, fdr 1e-05), [[EDA]] (-0.63, fdr 9e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +20.8 | 0e+00 | 45/47 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +13.5 | 6e-39 | 39/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.8 | 2e-20 | 36/48 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +8.6 | 1e-15 | 31/44 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +7.5 | 7e-12 | 32/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.5 | 7e-12 | 30/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +5.1 | 3e-05 | 20/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.27×** | +4.1 | 0.003 | 15/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +4.0 | 0.005 | 12/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.008 | 8/48 (CFPAC-1, SHP-77, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.067 | 4/48 (NCI-H2347, A-427, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.1 | 0.094 | 4/48 (SHP-77, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -9.6 | 7e-19 | 34/46 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -9.2 | 7e-18 | 30/45 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.368×** | -9.0 | 5e-17 | 32/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.372×** | -8.9 | 1e-16 | 32/47 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.597×** | -8.8 | 1e-16 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -7.8 | 4e-13 | 32/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -6.5 | 5e-09 | 24/47 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.695×** | -6.2 | 3e-08 | 25/47 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -6.1 | 7e-08 | 27/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.780×** | -4.3 | 0.001 | 16/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.773×** | -4.2 | 0.001 | 17/47 (NCI-H2030, SNU-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.785×** | -4.1 | 0.002 | 17/40 (MIA PaCa-2, HCT15, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.802×** | -3.8 | 0.007 | 12/48 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.804×** | -3.7 | 0.008 | 17/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.795×** | -3.7 | 0.008 | 13/48 (CFPAC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.6 | 0.009 | 18/48 (PANC-1, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.1 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -16.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 32.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 50.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 23.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.335× (z -8.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0928× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 16.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 11.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 24.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 33.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 23.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[J82 (line)]] | alt | 25.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[SW480 (line)]] | alt | 18.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.393× (z -8.8) |
| [[A549 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -9.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.6) | — |
| [[KATO III (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.314× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.9) | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0440× (z -9.1) |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0939× (z -11.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[A-172 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF785]] | +0.74 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ZNF425]] | +0.73 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[MFF-DT]] | +0.70 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[C2orf42]] | +0.69 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[RECQL5]] | +0.69 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.69 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[USP34-DT]] | +0.68 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ATE1OSP]] | +0.68 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[ZNF460-AS1]] | +0.68 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MTG2]] | +0.67 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | -0.70 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[SOAT1]] | -0.66 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[EDA]] | -0.63 | -0.58 / -0.37 | both halves | 9e-05 | same gene group |
| [[ATP1A3]] | -0.62 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[PLXND1]] | -0.61 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[HPSE]] | -0.60 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PRKAR2B]] | -0.59 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CDCA7L]] | -0.59 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LRBA]] | -0.57 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[HLTF]] | -0.57 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NMNAT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SORT1]] | B | SORT1 activity raises NMNAT1's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without SORT1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers NMNAT1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-5.4, 17.4); signed map (22.6, -10.6). **Vector** length 88.2, 18.6% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +20.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +8.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | -6.4 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -3.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide nucleotide adenylyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,943,428-9,985,501 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NMNAT, PNAT1; previously LCA9 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Nicotinate metabolism; NAD+ and Sirtuins regulate the circadian clock; Regulation of the circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAN9](https://www.uniprot.org/uniprotkb/Q9HAN9) (Nicotinamide/nicotinic acid mononucleotide adenylyltransferase 1):

> Catalyzes the formation of NAD(+) from nicotinamide mononucleotide (NMN) and ATP. Can also use the deamidated form; nicotinic acid mononucleotide (NaMN) as substrate with the same efficiency. Can use triazofurin monophosphate (TrMP) as substrate. Also catalyzes the reverse reaction, i.e. the pyrophosphorolytic cleavage of NAD(+). For the pyrophosphorolytic activity, prefers NAD(+) and NaAD as substrates and degrades NADH, nicotinic acid adenine dinucleotide phosphate (NHD) and nicotinamide …

**Summary**, from NCBI Gene [64802](https://www.ncbi.nlm.nih.gov/gene/64802):

> This gene encodes an enzyme which catalyzes a key step in the biosynthesis of nicotinamide adenine dinucleotide (NAD). The encoded enzyme is one of several nicotinamide nucleotide adenylyltransferases, and is specifically localized to the cell nucleus. Activity of this protein leads to the activation of a nuclear deacetylase that functions in the protection of damaged neurons. Mutations in this gene have been associated with Leber congenital amaurosis 9. Alternative splicing results in multiple …

**Accessions** — [HGNC:17877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17877) · Entrez [64802](https://www.ncbi.nlm.nih.gov/gene/64802) · UniProt [Q9HAN9](https://www.uniprot.org/uniprotkb/Q9HAN9) · Ensembl [ENSG00000173614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173614)

## Data

Gene col 10410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10410); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10410]; `tensor/DDL_lfc|DDL_z.npy` [10410]; `embed/gene_vectors.npy` [10410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10410 or target_col == 10410). Every well: [[NMNAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMNAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
