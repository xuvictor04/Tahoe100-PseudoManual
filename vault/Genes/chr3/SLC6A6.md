---
symbol: "SLC6A6"
type: "gene"
col: 5203
ensembl_id: "ENSG00000131389"
name: "solute carrier family 6 member 6"
location: "3p25.1"
module: 99
arm: "+"
pooled_cpm: 129.76
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 12
direction_downstream: 6
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# SLC6A6

*solute carrier family 6 member 6* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.45× (z +5.6, q 1e-05, up in 23 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.503× (z -14.7, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLTP]] (+0.64, fdr 1e-05), [[LOXL2]] (+0.63, fdr 7e-06), [[LINC00887]] (+0.59, fdr 1e-05); moves opposite to [[GABPB2]] (-0.57, fdr 3e-05), [[FAIM]] (-0.56, fdr 3e-05), [[RNF115]] (-0.56, fdr 2e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[KCNMA1]] → it (grade B ⚠); 6 go from it, the strongest it → [[ABCB6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.6 | 1e-05 | 23/44 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.4 | 2e-05 | 25/44 (LS 180, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.027 | 21/44 (SW480, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +3.7 | 0.034 | 23/45 (LS 180, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.043 | 22/44 (SW480, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.059 | 19/44 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.503×** | -14.7 | 0e+00 | 38/44 (CHP-212, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.441×** | -11.9 | 5e-30 | 39/44 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -11.6 | 1e-28 | 31/45 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.505×** | -9.9 | 5e-21 | 34/43 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -9.4 | 5e-19 | 35/44 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.567×** | -8.5 | 1e-15 | 33/44 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.686×** | -8.1 | 7e-14 | 34/44 (C32, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.684×** | -5.7 | 7e-07 | 26/45 (A-172, SW 900, …) | two highest doses | composition shift; position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.700×** | -5.4 | 4e-06 | 28/44 (Hs 766T, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.701×** | -5.2 | 1e-05 | 24/38 (SK-MEL-2, A-172, …) | two highest doses | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.716×** | -4.9 | 6e-05 | 28/44 (H4, HOP62, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.742×** | -4.5 | 3e-04 | 26/44 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.752×** | -4.3 | 8e-04 | 24/44 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.591×** | -4.1 | 0.001 | 28/45 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.766×** | -4.0 | 0.002 | 24/44 (SW 900, PANC-1, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -4.0 | 0.002 | 24/44 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -3.7 | 0.009 | 23/44 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.790×** | -3.6 | 0.011 | 21/44 (Hs 766T, H4, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.856× | -3.3 | 0.025 | 22/44 (A549, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -3.1 | 0.055 | 23/44 (C32, RPMI-7951, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 260 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -15.4) |
| [[C32 (line)]] | wt | 160 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -17.6) |
| [[Hs 766T (line)]] | wt | 334 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.8) |
| [[RPMI-7951 (line)]] | alt | 422 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -19.5) |
| [[A-172 (line)]] | wt | 211 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.182× (z -13.8) |
| [[CHP-212 (line)]] | wt | 339 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0378× (z -25.6) |
| [[H4 (line)]] | wt | 294 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -17.5) |
| [[HOP62 (line)]] | alt | 383 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -14.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -14.3) |
| [[SW480 (line)]] | alt | 53.7 | 4 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.30× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 246 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -15.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 136 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.5) |
| [[PANC-1 (line)]] | alt | 113 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 89.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.3) |
| [[RKO (line)]] | wt | 58.8 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 69.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.4) |
| [[A498 (line)]] | wt | 127 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.287× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 122 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.9) |
| [[HS-578T (line)]] | alt | 296 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 381 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -18.0) |
| [[SHP-77 (line)]] | alt | 187 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.0) |
| [[A549 (line)]] | wt | 205 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.5) |
| [[HCT15 (line)]] | alt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.2) |
| [[HT-29 (line)]] | alt | 83.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.11× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.0972× (z -17.9) |
| [[NCI-H460 (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -10.7) |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0913× (z -15.5) |
| [[J82 (line)]] | alt | 122 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.527× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.354× (z -10.0) |
| [[LS 180 (line)]] | wt | 65.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.00× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 169 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 37.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 48.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -12.9) |
| [[SW48 (line)]] | wt | 68.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.1) |
| [[A-427 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLTP]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[LOXL2]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[LINC00887]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ALDOA]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[CDON]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[P4HB]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[AFAP1]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PGK1]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[ZMIZ1]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[P3H1]] | +0.56 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[GPI]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[NDRG1]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB2]] | -0.57 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[FAIM]] | -0.56 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[RNF115]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[SLC24A1]] | -0.55 | -0.59 / -0.37 | both halves | 8e-05 | pathway: SLC-mediated transmembrane transport |
| [[KDF1]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[POLR3C]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[COMMD1]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | -0.51 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[TLK1]] | -0.50 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NIPAL2]] | -0.50 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[SENP6]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[IQCH-AS1]] | -0.50 | -0.60 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMA1]] | B | KCNMA1 activity raises SLC6A6's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.73× lower at baseline in the lines without KCNMA1 | 0.004 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[COL5A1]] | B | COL5A1 activity raises SLC6A6's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without COL5A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R |
| [[CA12]] | B | CA12 activity raises SLC6A6's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.31× lower at baseline in the lines without CA12 | 0.016 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[SNAP25]] | B | SNAP25 activity raises SLC6A6's level | lines that do not express SNAP25 (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without SNAP25 | 0.042 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[LINC01583]] | B | LINC01583 activity raises SLC6A6's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without LINC01583 | 0.045 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |
| [[PLOD2]] | B | PLOD2 activity raises SLC6A6's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without PLOD2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[NDNF]] | B | NDNF activity raises SLC6A6's level | lines that do not express NDNF (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without NDNF | 0.069 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SLC6A6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TIMP3]] | B | TIMP3 activity raises SLC6A6's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without TIMP3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[IGFBP5]] | B | IGFBP5 activity raises SLC6A6's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without IGFBP5 | 0.078 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2 |
| [[COL5A1]] | B | COL5A1 activity strengthens SLC6A6's drug response | lines that do not express COL5A1 (27) vs lines expressing it (18) | the lines without COL5A1 respond 0.81× as strongly (z diff +1.37); strongest at Dinaciclib 0.5 µM: 0.90x vs 0.46x (z diff +5.2) | 0.085 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; target measured in part of the lines; both ways; artifact flags |
| [[ASPH]] | B | ASPH activity raises SLC6A6's level | lines that do not express ASPH (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without ASPH | 0.089 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCB6]] | C | SLC6A6 activity raises ABCB6's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without SLC6A6 | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |
| [[LMAN1]] | C | SLC6A6 activity raises LMAN1's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without SLC6A6 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |
| [[AK2]] | C | SLC6A6 activity raises AK2's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.71× lower at baseline in the lines without SLC6A6 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |
| [[PFKP]] | C | SLC6A6 activity raises PFKP's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without SLC6A6 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |
| [[UBE2O]] | C | SLC6A6 activity raises UBE2O's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without SLC6A6 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |
| [[ECE1]] | C | SLC6A6 activity raises ECE1's level | lines that do not express SLC6A6 (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without SLC6A6 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000288891; maybe low, not absent |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, -9.1); signed map (-9.2, 48.4). **Vector** length 135, 44.1% of its response variance represented; |z| ≥ 3 in 1,421 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.5 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +6.9 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.3 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.6 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.2 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.5 | -8.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.5 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -14.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.9 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.7 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,402,576-14,489,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAUT |
| Gene groups (HGNC) | Solute carrier family 6 |
| Hallmark sets | XENOBIOTIC_METABOLISM, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P31641](https://www.uniprot.org/uniprotkb/P31641) (Sodium- and chloride-dependent taurine transporter):

> Mediates sodium- and chloride-dependent transport of taurine, a key amino acid. Taurine acts as an anti-aging agent by reducing cellular senescence and combating oxidative stress: levels decline with age and supplementation has been shown to extend lifespan (By similarity). In addition to mediate extracellular taurine uptake, also able to mediate transport of taurine into mitochondria, sustaining mitochondrial translation. Can also mediate transport of beta-alanine, hypotaurine and …

**Summary**, from NCBI Gene [6533](https://www.ncbi.nlm.nih.gov/gene/6533):

> This gene encodes a multi-pass membrane protein that is a member of a family of sodium and chloride-ion dependent transporters. The encoded protein transports taurine and beta-alanine. There is a pseudogene for this gene on chromosome 21. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:11052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11052) · Entrez [6533](https://www.ncbi.nlm.nih.gov/gene/6533) · UniProt [P31641](https://www.uniprot.org/uniprotkb/P31641) · Ensembl [ENSG00000131389](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131389)

## Data

Gene col 5203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5203); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5203]; `tensor/DDL_lfc|DDL_z.npy` [5203]; `embed/gene_vectors.npy` [5203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5203 or target_col == 5203). Every well: [[SLC6A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
