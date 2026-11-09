---
symbol: "TLR3"
type: "gene"
col: 8935
ensembl_id: "ENSG00000164342"
name: "toll like receptor 3"
location: "4q35.1"
module: 70
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 38
n_dd_up: 22
n_dd_down: 35
n_dd_up_clean: 19
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 15
direction_downstream: 31
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TLR3

*toll like receptor 3* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 2.50× (z +7.4, q 8e-11, up in 26 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.255× (z -11.5, q 8e-28, down in 24 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRANK1]] (+0.82, fdr 7e-06), [[PSMB8]] (+0.81, fdr 7e-06), [[GBP1]] (+0.80, fdr 7e-06); moves opposite to [[CTNNBIP1]] (-0.58, fdr 2e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[PLCH1]] → it (grade B ⚠); 31 go from it, the strongest it → [[PLCH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8935.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **2.50×** | +7.4 | 8e-11 | 26/32 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.96×** | +6.7 | 6e-09 | 17/35 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.77×** | +6.6 | 8e-09 | 22/36 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.18×** | +6.6 | 8e-09 | 22/35 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.22×** | +6.4 | 1e-08 | 25/31 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.85×** | +6.2 | 6e-08 | 16/36 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **2.00×** | +5.8 | 4e-07 | 16/33 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **2.08×** | +5.8 | 5e-07 | 14/33 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.86×** | +5.5 | 2e-06 | 19/36 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **2.02×** | +5.5 | 2e-06 | 15/35 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.91×** | +5.5 | 2e-06 | 15/35 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.83×** | +5.1 | 2e-05 | 15/35 (NCI-H2347, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.57×** | +5.1 | 2e-05 | 9/35 (KATO III, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **1.89×** | +5.0 | 2e-05 | 12/36 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.47×** | +4.4 | 4e-04 | 14/36 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.53×** | +3.6 | 0.013 | 5/36 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.255×** | -11.5 | 8e-28 | 24/35 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.317×** | -9.7 | 1e-19 | 26/35 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.401×** | -7.7 | 3e-12 | 25/35 (H4, RPMI-7951, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.484×** | -6.1 | 1e-07 | 21/34 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.490×** | -6.0 | 2e-07 | 21/35 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.495×** | -5.9 | 3e-07 | 15/35 (LS 180, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.498×** | -5.9 | 4e-07 | 18/34 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.505×** | -5.8 | 6e-07 | 21/35 (RKO, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.488×** | -5.7 | 9e-07 | 17/31 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.526×** | -5.4 | 4e-06 | 15/22 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.514×** | -5.4 | 4e-06 | 13/21 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.522×** | -5.3 | 7e-06 | 15/34 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.541×** | -5.2 | 9e-06 | 14/28 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.608×** | -5.2 | 9e-06 | 15/35 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.557×** | -4.9 | 3e-05 | 14/35 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.623×** | -4.8 | 4e-05 | 14/36 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.584×** | -4.5 | 2e-04 | 12/36 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.592×** | -4.4 | 3e-04 | 12/35 (HCT15, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.614×** | -4.1 | 0.001 | 9/34 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.697×** | -3.8 | 0.003 | 16/34 (CFPAC-1, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.8 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0455× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.114× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.137× (z -11.3) |
| [[LS 180 (line)]] | wt | 7.86 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0710× (z -10.7) |
| [[A498 (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -9.4) |
| [[HCT15 (line)]] | alt | 5.15 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0379× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 8.63 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0293× (z -13.6) |
| [[A-172 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.939 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.551 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRANK1]] | +0.82 | +0.76 / +0.82 | both halves | 7e-06 |  |
| [[PSMB8]] | +0.81 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[GBP1]] | +0.80 | +0.71 / +0.80 | both halves | 7e-06 | STRING 431 |
| [[APOL6]] | +0.77 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[EPSTI1]] | +0.77 | +0.68 / +0.75 | both halves | 7e-06 | STRING 516 |
| [[NMI]] | +0.77 | +0.65 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[ADAR]] | +0.76 | +0.66 / +0.77 | both halves | 7e-06 | STRING 528 |
| [[TNFSF10]] | +0.76 | +0.69 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 537 |
| [[SAMD9L]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 | STRING 515 |
| [[TRIM22]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[IFI35]] | +0.75 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[APOL1]] | +0.73 | +0.62 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBIP1]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCH1]] | B | PLCH1 activity raises TLR3's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 2.10× lower at baseline in the lines without PLCH1 | 0.017 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises TLR3's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without MX1 | 0.026 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[SIDT1]] | B | SIDT1 activity raises TLR3's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 1.78× lower at baseline in the lines without SIDT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[APOL1]] | B | APOL1 activity raises TLR3's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 1.75× lower at baseline in the lines without APOL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[EPSTI1]] | B | EPSTI1 activity raises TLR3's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without EPSTI1 | 0.066 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TLR3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[SLC34A2]] | B | SLC34A2 activity raises TLR3's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.96× lower at baseline in the lines without SLC34A2 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[CD5L]] | B | CD5L activity raises TLR3's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without CD5L | 0.071 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises TLR3's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.93× lower at baseline in the lines without NRIR | 0.080 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[STEAP4]] | B | STEAP4 activity raises TLR3's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 1.68× lower at baseline in the lines without STEAP4 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[RHEX]] | B | RHEX activity raises TLR3's level | lines that do not express RHEX (43) vs lines expressing it (7) | 2.12× lower at baseline in the lines without RHEX | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[CP]] | B | CP activity raises TLR3's level | lines that do not express CP (39) vs lines expressing it (11) | 1.65× lower at baseline in the lines without CP | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 28, C 3. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCH1]] | B | TLR3 activity raises PLCH1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without TLR3 | 0.008 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[APOL1]] | B | TLR3 activity raises APOL1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 3.28× lower at baseline in the lines without TLR3 | 0.016 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[RSAD2]] | B | TLR3 activity raises RSAD2's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 3.21× lower at baseline in the lines without TLR3 | 0.024 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[GBP1]] | B | TLR3 activity raises GBP1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 3.75× lower at baseline in the lines without TLR3 | 0.025 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[GBP2]] | B | TLR3 activity raises GBP2's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 3.39× lower at baseline in the lines without TLR3 | 0.031 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[C4orf33]] | B | TLR3 activity raises C4orf33's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without TLR3 | 0.031 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[TNFAIP2]] | B | TLR3 activity raises TNFAIP2's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.96× lower at baseline in the lines without TLR3 | 0.035 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[HERC6]] | B | TLR3 activity raises HERC6's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.43× lower at baseline in the lines without TLR3 | 0.037 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[CFH]] | B | TLR3 activity raises CFH's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 3.11× lower at baseline in the lines without TLR3 | 0.039 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[NRIR]] | B | TLR3 activity raises NRIR's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 1.93× lower at baseline in the lines without TLR3 | 0.040 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[DDX60L]] | B | TLR3 activity raises DDX60L's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.89× lower at baseline in the lines without TLR3 | 0.043 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[ALPK1]] | B | TLR3 activity raises ALPK1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without TLR3 | 0.054 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.7, 52.0); signed map (61.7, 29.9). **Vector** length 82.2, 19.3% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.54 to 25); *interferon alpha response* (hallmark, mean cos +0.51 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.53 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +7.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +5.0 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.2 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.8 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | toll like receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:186,068,911-186,088,073 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD283 |
| Gene groups (HGNC) | CD molecules; Toll like receptors |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE |
| Reactome | 18 pathways, smallest: TRAF3 deficiency - HSE; TLR3-mediated TICAM1-dependent programmed cell death; Trafficking and processing of endosomal TLR |
| Matched by | ensembl_id |

**Function**, from UniProt [O15455](https://www.uniprot.org/uniprotkb/O15455) (Toll-like receptor 3):

> Transmembrane receptor that functions as a pattern recognition receptor recognizing double-stranded RNA (dsRNA), a sign of viral infection, to induce innate immune responses via downstream signaling pathways. Acts via the adapter TRIF/TICAM1, leading to NF-kappa-B activation, IRF3 nuclear translocation, cytokine secretion and the inflammatory response. Acts as an activator of necroptosis, a programmed cell death process, in macrophages. In response to dsRNA-binding, recruits the adapter …

**Summary**, from NCBI Gene [7098](https://www.ncbi.nlm.nih.gov/gene/7098):

> The protein encoded by this gene is a member of the Toll-like receptor (TLR) family which plays a fundamental role in pathogen recognition and activation of innate immunity. TLRs are highly conserved from Drosophila to humans and share structural and functional similarities. They recognize pathogen-associated molecular patterns (PAMPs) that are expressed on infectious agents, and mediate the production of cytokines necessary for the development of effective immunity. The various TLRs exhibit …

**Accessions** — [HGNC:11849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11849) · Entrez [7098](https://www.ncbi.nlm.nih.gov/gene/7098) · UniProt [O15455](https://www.uniprot.org/uniprotkb/O15455) · Ensembl [ENSG00000164342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164342)

## Data

Gene col 8935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8935); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8935]; `tensor/DDL_lfc|DDL_z.npy` [8935]; `embed/gene_vectors.npy` [8935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8935 or target_col == 8935). Every well: [[TLR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
