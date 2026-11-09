---
symbol: "KLRC4-KLRK1"
type: "gene"
col: 14959
ensembl_id: "ENSG00000255819"
name: "KLRC4-KLRK1 readthrough"
location: "12p13.2"
module: 223
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 21
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 26
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# KLRC4-KLRK1

*KLRC4-KLRK1 readthrough* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.17× (z +20.4, q 0e+00, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.548× (z -5.3, q 7e-05, down in 15 of 19 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.713× (z -4.2, q 0.007, down in 10 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 3 lines (NCI-H1573 0.0172×, SW 900 0.0479×, SW480 0.0802×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.0426×, NCI-H2030 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.109×, NCI-H23 0.140×; ⚠ unreliable plate only); [[Peretinoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0421×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRC3]] (+0.95, fdr 7e-06, ⚠ same locus), [[KLRK1]] (+0.95, fdr 7e-06, ⚠ same locus), [[KLRC2]] (+0.93, fdr 7e-06, ⚠ same locus), [[BMP5]] (+0.73, fdr 7e-06), [[CXXC4]] (+0.68, fdr 7e-06), [[ID4]] (+0.62, fdr 2e-05); moves opposite to [[RABEPK]] (-0.48, fdr 3e-05), [[SGTB]] (-0.47, fdr 4e-05), [[IL17RA]] (-0.47, fdr 4e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KLRC3]] → it (grade C ⚠); 26 go from it, the strongest it → cells under [[Econazole (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.17×** | +20.4 | 0e+00 | 13/17 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.20×** | +12.1 | 2e-31 | 1/3 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.49×** | +11.4 | 1e-27 | 12/19 (SNU-1, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.56×** | +11.2 | 8e-27 | 8/16 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.94×** | +11.1 | 8e-27 | 3/7 (NCI-H2030, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.60×** | +8.4 | 4e-15 | 9/17 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +7.4 | 1e-11 | 2/8 (NCI-H2030, NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.4 | 1e-08 | 4/19 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.81×** | +5.2 | 1e-05 | 5/13 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.74×** | +4.9 | 6e-05 | 10/19 (NCI-H23, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +4.7 | 1e-04 | 6/18 (BT-474, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.5 | 0.023 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.73×** | +3.4 | 0.026 | 0/9 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.4 | 0.030 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.050 | 2/19 (NCI-H460, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14959.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 3 lines (NCI-H1573 0.0172×, SW 900 0.0479×, SW480 0.0802×); [[Digitoxin (drug)]] 5 µM in 2 lines (SW480 0.0426×, NCI-H2030 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.109×, NCI-H23 0.140×; ⚠ unreliable plate only); [[Peretinoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0421×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.548×** | -5.3 | 7e-05 | 15/19 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.713×** | -4.2 | 0.007 | 10/19 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.662×** | -3.6 | 0.053 | 11/19 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.681× | -3.3 | 0.14 | 8/18 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.696× | -3.2 | 0.14 | 3/19 (HCT15, SNU-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.700× | -3.1 | 0.14 | 15/18 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-733 (drug)]] 5 µM |  | 0.506× | -3.1 | 0.14 | 6/13 (SW 900, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.704× | -3.1 | 0.14 | 11/17 (NCI-H1573, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 53.3 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 5.84 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0426× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0802× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 33.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.109× (z -10.5) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0479× (z -11.2) |
| [[A-427 (line)]] | wt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 1.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 120× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 5.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 8.05 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0172× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 1.81 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0421× (z -8.8) |
| [[A-172 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRC3]] | +0.95 | +0.95 / +0.94 | both halves | 7e-06 | ⚠ same locus (2.2 kb, same strand: neighbours can correlate without regulation) |
| [[KLRK1]] | +0.95 | +0.96 / +0.91 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[KLRC2]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | ⚠ same locus (16.7 kb, same strand: neighbours can correlate without regulation) |
| [[BMP5]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[CXXC4]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ID4]] | +0.62 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[NR4A3]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ZFHX2]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[MIR1915HG]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[NR4A2]] | +0.57 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[ID2-AS1]] | +0.55 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[IGFL4]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[MIR2052HG]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[GUCY1B2]] | +0.55 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[CFAP300]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABEPK]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SGTB]] | -0.47 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[IL17RA]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[GPR89A]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[EIF4EBP1]] | -0.46 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[DYM]] | -0.46 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[SRD5A1]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[NEIL2]] | -0.45 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRC3]] | C | KLRC3 activity raises KLRC4-KLRK1's level | lines that do not express KLRC3 (27) vs lines expressing it (23) | 4.27× lower at baseline in the lines without KLRC3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4; co-absent with the target |
| [[KLRC2]] | C | KLRC2 activity raises KLRC4-KLRK1's level | lines that do not express KLRC2 (27) vs lines expressing it (23) | 3.87× lower at baseline in the lines without KLRC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRK1, TRPM2-AS; co-absent with the target |
| [[IGFL4]] | C | IGFL4 activity raises KLRC4-KLRK1's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.45× lower at baseline in the lines without IGFL4 | 0.051 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 23, C 3. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Econazole (drug)]] 0.5 µM | B | KLRC4-KLRK1, [[KLRK1]] activity raises the cells' numbers under Econazole 0.5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.83× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | B | KLRC4-KLRK1, [[KLRK1]] activity raises the cells' numbers under Riluzole hydrochloride 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.86× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[LINC01091]] | B | KLRC4-KLRK1, [[KLRK1]] activity raises LINC01091's level | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (21) | 2.23× lower at baseline in the lines without KLRC4-KLRK1, KLRK1 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[DYM]] | B | KLRC4-KLRK1 activity weakens DYM's drug response | lines that do not express KLRC4-KLRK1 (29) vs lines expressing it (20) | the lines without KLRC4-KLRK1 respond 1.32× as strongly (z diff -1.19); strongest at Idarubicin (hydrochloride) 5 µM: 0.59x vs 0.73x (z diff -2.1) | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B; target measured in part of the lines; artifact flags |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | KLRC4-KLRK1, [[KLRK1]] activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.86× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[EIF4EBP1]] | B | KLRC4-KLRK1 activity lowers EIF4EBP1's level | lines that do not express KLRC4-KLRK1 (29) vs lines expressing it (21) | 1.67× higher at baseline in the lines without KLRC4-KLRK1 | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | B | KLRC4-KLRK1, [[KLRK1]] activity lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.18× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Rutin (trihydrate) (drug)]] 0.05 µM | B | KLRC4-KLRK1, [[KLRK1]] activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.85× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[PPP1R1C]] | B | KLRC4-KLRK1, [[KLRK1]] activity raises PPP1R1C's level | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (21) | 1.72× lower at baseline in the lines without KLRC4-KLRK1, KLRK1 | 0.068 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[AGBL4]] | B | KLRC4-KLRK1 activity raises AGBL4's level | lines that do not express KLRC4-KLRK1 (29) vs lines expressing it (21) | 2.24× lower at baseline in the lines without KLRC4-KLRK1 | 0.069 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KLRC3, KLRC2, PIP5K1B |
| cells under [[Bendamustine (drug)]] 5 µM | B | KLRC4-KLRK1, [[KLRK1]] activity lowers the cells' numbers under Bendamustine 5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.18× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| cells under [[Fenofibrate (drug)]] 0.05 µM | B | KLRC4-KLRK1, [[KLRK1]] activity raises the cells' numbers under Fenofibrate 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.81× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.930). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.5, 33.7); signed map (51.3, 20.0). **Vector** length 52.7, 13.8% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +4.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | KLRC4-KLRK1 readthrough |
| Locus type | readthrough (other) |
| Location | 12p13.2 — chr12:10,372,353-10,410,146 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100528032](https://www.ncbi.nlm.nih.gov/gene/100528032):

> This locus represents naturally occurring read-through transcription between the neighboring KLRC4 (killer cell lectin-like receptor subfamily C, member 4) and KLRK1 (killer cell lectin-like receptor subfamily K, member 1) genes on chromosome 12. The read-through transcript includes an alternate 5' exon and lacks a significant portion of the KLRC4 coding sequence, including the start codon, and it thus encodes the KLRK1 protein. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:48357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48357) · Entrez [100528032](https://www.ncbi.nlm.nih.gov/gene/100528032) · Ensembl [ENSG00000255819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255819)

## Data

Gene col 14959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14959); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14959]; `tensor/DDL_lfc|DDL_z.npy` [14959]; `embed/gene_vectors.npy` [14959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14959 or target_col == 14959). Every well: [[KLRC4-KLRK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRC4-KLRK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
