---
symbol: "LONP1"
type: "gene"
col: 12187
ensembl_id: "ENSG00000196365"
name: "lon peptidase 1, mitochondrial"
location: "19p13.2"
module: 105
arm: "+"
pooled_cpm: 53.98
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 19
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# LONP1

*lon peptidase 1, mitochondrial* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.81× (z +8.9, q 3e-16, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -12.7, q 2e-34, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPT2]] (+0.73, fdr 7e-06), [[CTDP1]] (+0.67, fdr 7e-06), [[CDC26]] (+0.66, fdr 7e-06); moves opposite to [[NFKB1]] (-0.54, fdr 3e-05), [[NFAT5]] (-0.53, fdr 8e-05), [[NRIP1]] (-0.52, fdr 7e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12187.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +8.9 | 3e-16 | 41/48 (SHP-77, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.96×** | +8.5 | 6e-15 | 43/49 (COLO 205, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +8.2 | 4e-14 | 35/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +7.1 | 2e-10 | 42/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +5.2 | 3e-05 | 34/48 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.27×** | +4.8 | 1e-04 | 29/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 3e-04 | 29/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.71×** | +4.2 | 0.002 | 29/48 (SW480, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.002 | 28/48 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 25/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.004 | 23/48 (SHP-77, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.005 | 23/48 (hTERT-HPNE, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.006 | 26/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.007 | 23/48 (LOX-IMVI, A498, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.015 | 21/48 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.015 | 18/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12187.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.535×** | -12.7 | 2e-34 | 40/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.483×** | -10.5 | 2e-23 | 41/48 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.565×** | -8.6 | 2e-15 | 42/48 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -8.3 | 1e-14 | 38/48 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.681×** | -7.9 | 4e-13 | 39/48 (A498, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.621×** | -7.1 | 9e-11 | 38/48 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.676×** | -5.9 | 3e-07 | 37/48 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -5.7 | 8e-07 | 35/48 (A498, SW 900, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -5.6 | 2e-06 | 3/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.782×** | -5.1 | 2e-05 | 28/48 (SNU-1, CHP-212, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.771×** | -3.9 | 0.005 | 24/48 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.767×** | -3.8 | 0.006 | 25/48 (A498, SK-MEL-2, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.769×** | -3.8 | 0.007 | 21/47 (C32, SW48, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.788×** | -3.6 | 0.014 | 23/48 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -3.5 | 0.016 | 20/48 (A498, CHP-212, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.813×** | -3.1 | 0.059 | 15/48 (NCI-H23, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12187. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 66.4 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.505× (z -11.3) |
| [[C32 (line)]] | wt | 70.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 46.4 | 3 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +12.4) | [[Harringtonine (drug)]] 5 µM 0.369× (z -9.2) |
| [[C-33 A (line)]] | alt | 81.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 103 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -19.0) |
| [[SNU-1 (line)]] | wt | 79.4 | 1 | 2 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.42× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.3) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.407× (z -8.6) |
| [[SW48 (line)]] | wt | 63.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -14.4) |
| [[A-172 (line)]] | wt | 68.3 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.97× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.448× (z -8.9) |
| [[A-427 (line)]] | wt | 74.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -17.3) |
| [[CHP-212 (line)]] | wt | 71.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -9.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HOP62 (line)]] | alt | 42.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 60.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.1) |
| [[LoVo (line)]] | wt | 64.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.47× (z +8.9) | [[Harringtonine (drug)]] 5 µM 0.401× (z -8.7) |
| [[SW480 (line)]] | alt | 43.5 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.8) |
| [[BT-474 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.247× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 30.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.89× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -8.8) |
| [[J82 (line)]] | alt | 50.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 57.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.0) |
| [[LS 180 (line)]] | wt | 64.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 71.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 41.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.373× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0887× (z -8.8) |
| [[PANC-1 (line)]] | alt | 45.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +8.6) | — |
| [[RKO (line)]] | wt | 71.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.2) |
| [[SHP-77 (line)]] | alt | 55.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.61× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 64.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -9.8) |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.6) |
| [[A549 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12187), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPT2]] | +0.73 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[CTDP1]] | +0.67 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[CDC26]] | +0.66 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CRYBB2P1-1]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[POM121]] | +0.64 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[AK2]] | +0.64 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[GARS1]] | +0.63 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[PRKRIP1]] | +0.62 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[STC2]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TRMU]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SLC35E1]] | +0.61 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[AARS1]] | +0.60 | +0.48 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB1]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[NFAT5]] | -0.53 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[NRIP1]] | -0.52 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[CMTM6]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PRKAA1]] | -0.49 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[PNRC2]] | -0.49 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises LONP1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without ANK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[NRIP1]] | B | NRIP1 activity lowers LONP1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without NRIP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[PSAT1]] | B | PSAT1 activity raises LONP1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without PSAT1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.5, -20.9); signed map (-41.0, 23.6). **Vector** length 120, 37.3% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.1 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +5.2 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.2 | -10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.6 | -7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -2.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | lon peptidase 1, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:5,691,834-5,720,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LonHS, hLON, PIM1; previously PRSS15 |
| Gene groups (HGNC) | AAA ATPases; Serine proteases; Mitochondrial nucleoid associated proteins |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); Mitochondrial protein degradation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P36776](https://www.uniprot.org/uniprotkb/P36776) (Lon protease homolog, mitochondrial):

> ATP-dependent serine protease that mediates the selective degradation of misfolded, unassembled or oxidatively damaged polypeptides as well as certain short-lived regulatory proteins in the mitochondrial matrix. Endogenous substrates include mitochondrial steroidogenic acute regulatory (StAR) protein, DELE1, helicase Twinkle (TWNK) and the large ribosomal subunit protein MRPL32/bL32m. MRPL32/bL32m is protected from degradation by LONP1 when it is bound to a nucleic acid (RNA), but TWNK is not. …

**Summary**, from NCBI Gene [9361](https://www.ncbi.nlm.nih.gov/gene/9361):

> This gene encodes a mitochondrial matrix protein that belongs to the Lon family of ATP-dependent proteases. This protein mediates the selective degradation of misfolded, unassembled or oxidatively damaged polypeptides in the mitochondrial matrix. It may also have a chaperone function in the assembly of inner membrane protein complexes, and participate in the regulation of mitochondrial gene expression and maintenance of the integrity of the mitochondrial genome. Decreased expression of this …

**Accessions** — [HGNC:9479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9479) · Entrez [9361](https://www.ncbi.nlm.nih.gov/gene/9361) · UniProt [P36776](https://www.uniprot.org/uniprotkb/P36776) · Ensembl [ENSG00000196365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196365)

## Data

Gene col 12187: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12187); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12187, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12187]; `tensor/DDL_lfc|DDL_z.npy` [12187]; `embed/gene_vectors.npy` [12187]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12187 or target_col == 12187). Every well: [[LONP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LONP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
