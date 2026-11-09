---
symbol: "FAM13A-AS1"
type: "gene"
col: 14513
ensembl_id: "ENSG00000248019"
name: "FAM13A antisense RNA 1"
location: "4q22.1"
module: 99
arm: "+"
pooled_cpm: 11.75
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# FAM13A-AS1

*FAM13A antisense RNA 1* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +7.4, q 7e-11, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.288× (z -19.8, q 0e+00, down in 43 of 44 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.306× (z -13.3, q 3e-38, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC3]] (+0.74, fdr 7e-06, ⚠ same locus), [[AK2]] (+0.63, fdr 7e-06), [[QSOX1]] (+0.61, fdr 1e-05), [[FAM210A]] (+0.57, fdr 1e-05); moves opposite to [[INTS14]] (-0.56, fdr 2e-05), [[NME6]] (-0.55, fdr 3e-05), [[ZBED1]] (-0.53, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +7.4 | 7e-11 | 32/47 (HOP62, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.4 | 0.003 | 18/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.005 | 17/47 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.007 | 14/46 (J82, HT-29, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.011 | 17/44 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.022 | 12/47 (A-172, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.33× | +3.2 | 0.11 | 17/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.19 | 15/46 (C-33 A, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.288×** | -19.8 | 0e+00 | 43/44 (Hs 766T, SK-MEL-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.257×** | -14.7 | 0e+00 | 43/46 (RPMI-7951, Hs 766T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.306×** | -13.3 | 3e-38 | 39/44 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.333×** | -11.9 | 2e-30 | 30/40 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.340×** | -11.7 | 2e-29 | 33/39 (HCT15, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.442×** | -9.2 | 4e-18 | 33/45 (NCI-H23, KATO III, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.485×** | -8.1 | 4e-14 | 36/47 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.607×** | -5.6 | 1e-06 | 25/46 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -5.4 | 4e-06 | 24/46 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.624×** | -5.3 | 7e-06 | 24/46 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -5.3 | 7e-06 | 21/46 (C32, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.628×** | -5.2 | 8e-06 | 23/46 (SNU-423, SW 900, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.643×** | -5.0 | 3e-05 | 24/45 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.702×** | -4.0 | 0.003 | 17/47 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.514×** | -3.9 | 0.003 | 15/44 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.004 | 23/47 (NCI-H1792, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.737×** | -3.4 | 0.019 | 13/46 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -9.4) |
| [[C32 (line)]] | wt | 21.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -11.7) |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0524× (z -22.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -10.7) |
| [[J82 (line)]] | alt | 11.5 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0618× (z -13.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -19.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0803× (z -11.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 8.65 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0599× (z -20.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0834× (z -12.6) |
| [[SW480 (line)]] | alt | 10.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 8.78 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Talc (drug)]] 0.05 µM 0.117× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 24.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -14.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -8.8) |
| [[H4 (line)]] | wt | 23.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -16.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0867× (z -11.1) |
| [[HCT15 (line)]] | alt | 26.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0397× (z -13.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 12.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 15.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.1) ⚠ cell-cycle shift, explains ~13% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -12.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0332× (z -12.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Vismodegib (drug)]] 0.5 µM 0.0615× (z -10.6) |
| [[A-427 (line)]] | wt | 8.17 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 7.07 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0592× (z -10.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0881× (z -8.6) |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0909× (z -9.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -12.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.202× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 6.51 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.125× (z -8.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 8.59 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0854× (z -10.8) ⚠ toxic |
| [[RKO (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -8.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 8.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -14.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 8.03 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -11.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC3]] | +0.74 | +0.72 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.8 kb, same strand: neighbours can correlate without regulation) |
| [[AK2]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[QSOX1]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[P4HB]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[HDAC3]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PGK1]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[HK1]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PDIA4]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PDK1]] | +0.54 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[KDM4B]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ARFGEF3]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[HK2]] | +0.54 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS14]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[NME6]] | -0.55 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ZBED1]] | -0.53 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[CPLANE1]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[HCG11]] | -0.50 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ZNF480]] | -0.50 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PEX1]] | -0.49 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[C1orf131]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[TTC8]] | -0.48 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[SRSF8]] | -0.48 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[RPL7L1]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FAM13A-AS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PFKP]] | C | PFKP activity raises FAM13A-AS1's level | lines that do not express PFKP (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, -19.4); signed map (-39.6, 24.8). **Vector** length 72.7, 13.8% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +2.9 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -3.9 |
|  | [[Roxadustat (drug)]] 5 µM |  | +1.3 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.4 | -19.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.9 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -11.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -13.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.3 | +0.7 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.3 | -0.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | FAM13A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q22.1 — chr4:88,709,298-88,730,103 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00039; previously FAM13A1OS, FAM13AOS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:19370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19370) · Entrez [285512](https://www.ncbi.nlm.nih.gov/gene/285512) · Ensembl [ENSG00000248019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248019)

## Data

Gene col 14513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14513); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14513]; `tensor/DDL_lfc|DDL_z.npy` [14513]; `embed/gene_vectors.npy` [14513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14513 or target_col == 14513). Every well: [[FAM13A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM13A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
