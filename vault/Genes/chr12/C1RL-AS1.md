---
symbol: "C1RL-AS1"
type: "gene"
col: 13019
ensembl_id: "ENSG00000205885"
name: "C1RL antisense RNA 1"
location: "12p13.31"
module: 99
arm: "+"
pooled_cpm: 21.99
n_lines_expressing: 43
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# C1RL-AS1

*C1RL antisense RNA 1* — 12p13.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.139× (z -19.3, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIP12]] (+0.65, fdr 1e-05), [[CLSTN3]] (+0.58, fdr 7e-06, ⚠ same locus), [[CFLAR]] (+0.58, fdr 7e-05), [[SPRY3]] (+0.56, fdr 1e-04); moves opposite to [[HSDL1]] (-0.61, fdr 2e-05), [[GPR160]] (-0.57, fdr 3e-05), [[SNAPC3]] (-0.55, fdr 6e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CACNG8]] → it (grade B ⚠); 4 go from it, the strongest it → [[C1RL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.92 | 12/40 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.139×** | -19.3 | 0e+00 | 41/41 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.144×** | -19.0 | 0e+00 | 40/41 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.144×** | -18.9 | 0e+00 | 40/41 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.373×** | -13.6 | 4e-40 | 34/40 (LoVo, RKO, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.330×** | -10.8 | 2e-25 | 30/39 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.372×** | -9.7 | 4e-20 | 35/41 (H4, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.385×** | -8.4 | 3e-15 | 38/41 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.470×** | -7.4 | 1e-11 | 30/39 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.502×** | -6.7 | 1e-09 | 32/41 (SW480, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.516×** | -6.5 | 6e-09 | 30/40 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.503×** | -6.4 | 6e-09 | 27/40 (SW480, AsPC-1, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.289×** | -6.3 | 1e-08 | 33/40 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.536×** | -5.8 | 2e-07 | 27/38 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.562×** | -5.6 | 8e-07 | 24/40 (LS 180, NCI-H1573, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -5.5 | 1e-06 | 28/41 (NCI-H1792, H4, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -4.9 | 3e-05 | 24/40 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.701×** | -4.9 | 3e-05 | 27/41 (LS 180, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.629×** | -4.5 | 2e-04 | 25/40 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.666×** | -4.0 | 0.002 | 26/41 (NCI-H23, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -3.7 | 0.005 | 20/40 (NCI-H23, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.510×** | -3.4 | 0.013 | 19/40 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -3.2 | 0.029 | 18/40 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.721×** | -3.2 | 0.030 | 17/41 (H4, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 63.9 | 0 | 10 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.100× (z -18.4) |
| [[LoVo (line)]] | wt | 40.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -20.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0835× (z -20.6) |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0492× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0751× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 31.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -18.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0965× (z -14.0) |
| [[A-427 (line)]] | wt | 54.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -14.7) |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0179× (z -20.5) |
| [[H4 (line)]] | wt | 38.3 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0676× (z -12.6) |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0475× (z -16.1) |
| [[SW480 (line)]] | alt | 33.7 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.112× (z -18.1) |
| [[A549 (line)]] | wt | 51.5 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0873× (z -14.8) |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.130× (z -13.4) |
| [[KATO III (line)]] | alt | 15.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -16.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.122× (z -12.1) |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -17.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0772× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0562× (z -18.3) |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.104× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0929× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 48.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -11.4) |
| [[RKO (line)]] | wt | 29.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0823× (z -20.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.113× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.135× (z -11.6) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -10.9) |
| [[A498 (line)]] | wt | 28.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -12.5) |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.120× (z -9.8) |
| [[HCT15 (line)]] | alt | 28.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -14.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.116× (z -11.2) |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0924× (z -12.6) |
| [[J82 (line)]] | alt | 24.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -13.4) |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -16.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -8.8) |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -9.3) |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.151× (z -11.3) |
| [[SW48 (line)]] | wt | 13.5 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0772× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.178× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -8.6) |
| [[HT-29 (line)]] | alt | 9.52 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.158× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 9.48 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.100× (z -10.1) |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0342× (z -9.0) |
| [[AN3 CA (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP12]] | +0.65 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CLSTN3]] | +0.58 | +0.61 / +0.74 | both halves | 7e-06 | ⚠ same locus (7.2 kb, same strand: neighbours can correlate without regulation) |
| [[CFLAR]] | +0.58 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[SPRY3]] | +0.56 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[MOB3C]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[TASOR]] | +0.55 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[C1RL]] | +0.55 | +0.40 / +0.51 | both halves | 4e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SERPINB9P1]] | +0.54 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[ERMAP]] | +0.54 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[CLHC1]] | +0.54 | +0.29 / +0.37 | both halves | 2e-04 |  |
| [[MC1R]] | +0.53 | +0.47 / +0.28 | both halves | 3e-04 |  |
| [[AVEN]] | +0.53 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[KRT8P12]] | +0.52 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[KRR1]] | +0.52 | +0.38 / +0.43 | both halves | 7e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSDL1]] | -0.61 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[GPR160]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SNAPC3]] | -0.55 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[CDS1]] | -0.55 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ANAPC11]] | -0.55 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[HEBP1]] | -0.55 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[CDON]] | -0.54 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TPD52]] | -0.54 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ARL3]] | -0.54 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[VKORC1]] | -0.54 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD37]] | -0.54 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[LIN7B]] | -0.53 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG8]] | B | CACNG8 activity strengthens C1RL-AS1's drug response | lines that do not express CACNG8 (10) vs lines expressing it (31) | the lines without CACNG8 respond 0.64× as strongly (z diff +1.82); strongest at Digitoxin 5 µM: 0.72x vs 0.29x (z diff +4.6) | 0.029 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1; target measured in part of the lines; artifact flags |
| [[MLKL]] | B | MLKL activity raises C1RL-AS1's level | lines that do not express MLKL (7) vs lines expressing it (43) | 4.47× lower at baseline in the lines without MLKL | 0.053 | ⚠ within organs, on part of the lines; also absent: PSD4; maybe low, not absent |
| [[RHCG]] | B | RHCG activity raises C1RL-AS1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.96× lower at baseline in the lines without RHCG | 0.074 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[CACNG8]] | B | CACNG8 activity raises C1RL-AS1's level | lines that do not express CACNG8 (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without CACNG8 | 0.075 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1 |
| [[CLSTN3]] | C | CLSTN3 activity raises C1RL-AS1's level | lines that do not express CLSTN3 (3) vs lines expressing it (47) | 7.35× lower at baseline in the lines without CLSTN3 | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: PIM1, HACD1, ENSG00000286782 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1RL]] | B | C1RL-AS1 activity raises C1RL's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 4.57× lower at baseline in the lines without C1RL-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |
| [[IL4R]] | B | C1RL-AS1 activity raises IL4R's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 2.84× lower at baseline in the lines without C1RL-AS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |
| [[PIEZO1]] | B | C1RL-AS1 activity raises PIEZO1's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 1.92× lower at baseline in the lines without C1RL-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |
| [[CLSTN3]] | B | C1RL-AS1 activity raises CLSTN3's level | lines that do not express C1RL-AS1 (7) vs lines expressing it (43) | 2.90× lower at baseline in the lines without C1RL-AS1 | 0.085 | ⚠ within organs, on part of the lines; also absent: EGFR, HFE, SH2D4A |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction -0.497). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.4, -6.5); signed map (23.9, -25.1). **Vector** length 81.1, 21.0% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +2.8 | -6.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +0.3 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +1.7 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.5 | +1.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.1 | -19.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.7 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | C1RL antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.31 — chr12:7,108,052-7,122,524 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MATL2963 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [283314](https://www.ncbi.nlm.nih.gov/gene/283314):

> Predicted to enable U4 snRNA binding activity. Predicted to be involved in formation of quadruple SL/U4/U5/U6 snRNP and spliceosomal tri-snRNP complex assembly. Predicted to be part of U4/U6 x U5 tri-snRNP complex and U6 snRNP. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27461) · Entrez [283314](https://www.ncbi.nlm.nih.gov/gene/283314) · Ensembl [ENSG00000205885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205885)

## Data

Gene col 13019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13019); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13019]; `tensor/DDL_lfc|DDL_z.npy` [13019]; `embed/gene_vectors.npy` [13019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13019 or target_col == 13019). Every well: [[C1RL-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1RL-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
