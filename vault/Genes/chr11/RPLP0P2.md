---
symbol: "RPLP0P2"
type: "gene"
col: 14376
ensembl_id: "ENSG00000243742"
name: "ribosomal protein lateral stalk subunit P0 pseudogene 2"
location: "11q12.2"
module: 125
arm: "+"
pooled_cpm: 4.87
n_lines_expressing: 43
n_dd_up: 52
n_dd_down: 4
n_dd_up_clean: 39
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# RPLP0P2

*ribosomal protein lateral stalk subunit P0 pseudogene 2* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 52 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.75× (z +20.3, q 0e+00, up in 31 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.622× (z -4.0, q 0.044, down in 16 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V0D2]] (+0.65, fdr 3e-05), [[NDRG4]] (+0.64, fdr 1e-05), [[LINC02511]] (+0.64, fdr 1e-05); moves opposite to [[CEP43]] (-0.55, fdr 1e-05), [[PIGS]] (-0.55, fdr 1e-05), [[NUP133]] (-0.55, fdr 3e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC01705]] → it (grade B ⚠); 9 go from it, the strongest it → [[GRB10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 52 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.75×** | +20.3 | 0e+00 | 31/36 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **5.47×** | +19.7 | 0e+00 | 39/39 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.46×** | +15.3 | 0e+00 | 36/38 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **6.21×** | +15.0 | 0e+00 | 37/38 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.81×** | +12.9 | 7e-36 | 36/37 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.12×** | +11.6 | 3e-29 | 31/38 (SW480, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **4.06×** | +11.5 | 1e-28 | 34/38 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.11×** | +11.1 | 5e-27 | 28/37 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.41×** | +10.1 | 5e-22 | 24/32 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **3.41×** | +10.0 | 6e-22 | 31/38 (H4, SNU-423, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.90×** | +8.7 | 1e-16 | 31/38 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.78×** | +7.9 | 1e-13 | 29/38 (LoVo, H4, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.42×** | +7.2 | 2e-11 | 31/38 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.42×** | +7.2 | 2e-11 | 25/38 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **4.81×** | +6.7 | 6e-10 | 27/36 (HS-578T, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **3.19×** | +5.0 | 2e-05 | 18/39 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.622×** | -4.0 | 0.044 | 16/38 (NCI-H1792, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.658×** | -3.5 | 0.096 | 15/38 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.454×** | -3.4 | 0.096 | 5/39 (HCT15, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.665×** | -3.4 | 0.096 | 8/38 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.55 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 12.9× (z +14.2) | — |
| [[SNU-423 (line)]] | alt | 9.32 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.5× (z +16.8) | — |
| [[A-172 (line)]] | wt | 9.57 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +15.8) | — |
| [[HS-578T (line)]] | alt | 13.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +11.1) | — |
| [[A498 (line)]] | wt | 4.29 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.3× (z +15.4) | — |
| [[NCI-H2347 (line)]] | alt | 5.28 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +13.9) | [[Tadalafil (drug)]] 5 µM 0.0632× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 18.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 3.11 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 4.42 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 14.5× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.48× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0960× (z -10.2) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW 900 (line)]] | alt | 7.41 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 11.5× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 8.87 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.84× (z +9.6) | — |
| [[C32 (line)]] | wt | 4.69 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.2× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 5.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +13.6) | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 26.8× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 7.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +10.3) | — |
| [[J82 (line)]] | alt | 4.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.9× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.02 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 19.4× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 2.30 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.7× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 2.38 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.39× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 1.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 28.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.79× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 6.57 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.05 µM 0.0483× (z -10.1) |
| [[A-427 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0D2]] | +0.65 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[NDRG4]] | +0.64 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.64 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TUBB2B]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[OSGIN1]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CRYM]] | +0.60 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[OSBP2]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SYT7]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[IER3]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CREB5]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RNF223]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP43]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PIGS]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[NUP133]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ACTL6A]] | -0.54 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TCTN3]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ARMC8]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[FAM120A]] | -0.51 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TMPO]] | -0.51 | -0.39 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01705]] | B | LINC01705 activity raises RPLP0P2's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without LINC01705 | 0.001 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[ROR1-AS1]] | B | ROR1-AS1 activity raises RPLP0P2's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without ROR1-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[LINC01885]] | B | LINC01885 activity raises RPLP0P2's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 2.01× lower at baseline in the lines without LINC01885 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383 |
| [[SLAMF7]] | B | SLAMF7 activity raises RPLP0P2's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without SLAMF7 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[ENTHD1]] | B | ENTHD1 activity raises RPLP0P2's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without ENTHD1 | 0.046 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[LINC02154]] | B | LINC02154 activity raises RPLP0P2's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 2.02× lower at baseline in the lines without LINC02154 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530 |
| [[IGFN1]] | B | IGFN1 activity raises RPLP0P2's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.04× lower at baseline in the lines without IGFN1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[ZNF365]] | B | ZNF365 activity raises RPLP0P2's level | lines that do not express ZNF365 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without ZNF365 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000285837, CHSY3, FLT1 |
| [[LINC00958]] | B | LINC00958 activity raises RPLP0P2's level | lines that do not express LINC00958 (39) vs lines expressing it (11) | 1.67× lower at baseline in the lines without LINC00958 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SSX1, LINC01320, LINC00879 |
| [[KLKP1-1]] | B | KLKP1-1 activity raises RPLP0P2's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 2.10× lower at baseline in the lines without KLKP1-1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[TNFRSF9]] | B | TNFRSF9 activity raises RPLP0P2's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without TNFRSF9 | 0.086 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRB10]] | B | RPLP0P2 activity raises GRB10's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 4.81× lower at baseline in the lines without RPLP0P2 | 0.009 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[ATP6V0A1]] | B | RPLP0P2 activity lowers ATP6V0A1's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.72× higher at baseline in the lines without RPLP0P2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[ROBO3]] | B | RPLP0P2 activity lowers ROBO3's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.85× higher at baseline in the lines without RPLP0P2 | 0.022 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[TMEM40]] | B | RPLP0P2 activity lowers TMEM40's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.62× higher at baseline in the lines without RPLP0P2 | 0.024 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[ZNF385A]] | B | RPLP0P2 activity raises ZNF385A's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 2.36× lower at baseline in the lines without RPLP0P2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[HMOX1]] | B | RPLP0P2 activity lowers HMOX1's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 2.44× higher at baseline in the lines without RPLP0P2 | 0.054 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[OLFM2]] | B | RPLP0P2 activity lowers OLFM2's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 3.30× higher at baseline in the lines without RPLP0P2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[CLN8]] | B | RPLP0P2 activity raises CLN8's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without RPLP0P2 | 0.064 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |
| [[RND3]] | B | RPLP0P2 activity raises RND3's level | lines that do not express RPLP0P2 (7) vs lines expressing it (43) | 3.18× lower at baseline in the lines without RPLP0P2 | 0.066 | ⚠ within organs, on part of the lines; also absent: CAMK2N1, ETS2, CSTB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.3, -0.1); signed map (35.5, 21.5). **Vector** length 95.5, 22.7% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.7 | +19.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.3 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +11.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +20.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +6.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.3 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein lateral stalk subunit P0 pseudogene 2 |
| Locus type | pseudogene |
| Location | 11q12.2 — chr11:61,636,680-61,637,640 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:17960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17960) · Entrez [113157](https://www.ncbi.nlm.nih.gov/gene/113157) · Ensembl [ENSG00000243742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243742)

## Data

Gene col 14376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14376); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14376]; `tensor/DDL_lfc|DDL_z.npy` [14376]; `embed/gene_vectors.npy` [14376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14376 or target_col == 14376). Every well: [[RPLP0P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPLP0P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
