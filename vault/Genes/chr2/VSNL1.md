---
symbol: "VSNL1"
type: "gene"
col: 8621
ensembl_id: "ENSG00000163032"
name: "visinin like 1"
location: "2p24.2"
module: 55
arm: "+"
pooled_cpm: 16.1
n_lines_expressing: 16
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 41
direction_downstream: 41
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# VSNL1

*visinin like 1* — 2p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +11.6, q 2e-28, up in 2 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.590× (z -5.6, q 1e-05, down in 9 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJB1]] (+0.80, fdr 7e-06), [[AXIN2]] (+0.78, fdr 7e-06), [[CLRN3]] (+0.77, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 41 arrows point to it, the strongest [[BAMBI]] → it (grade B ⚠); 41 go from it, the strongest it → [[SNTB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +11.6 | 2e-28 | 2/14 (COLO 205, hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.6 | 3e-19 | 3/13 (HepG2/C3A, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +9.2 | 5e-18 | 5/14 (HepG2/C3A, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +8.4 | 6e-15 | 2/10 (SW1417, HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +8.2 | 2e-14 | 2/9 (HepG2/C3A, HCT15) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +5.6 | 2e-06 | 1/13 (LS 180) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.3 | 1e-05 | 1/13 (COLO 205) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +4.6 | 3e-04 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.6 | 3e-04 | 1/12 (SW1417) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.0 | 0.004 | 1/13 (SW1417) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.011 | 0/13 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.013 | 3/14 (COLO 205, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.016 | 5/13 (hTERT-HPNE, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.4 | 0.030 | 1/5 (LoVo) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.030 | 0/13 | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.037 | 5/13 (LS 180, HCT15, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.053 | 4/13 (HCT15, LoVo, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.083 | 0/13 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.590×** | -5.6 | 1e-05 | 9/12 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.616×** | -5.1 | 8e-05 | 9/13 (AN3 CA, LS 180, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -4.7 | 4e-04 | 9/13 (SW480, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.694×** | -3.9 | 0.014 | 8/13 (KATO III, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -3.8 | 0.014 | 7/12 (SW48, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.643×** | -3.8 | 0.014 | 9/13 (LS 180, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.692×** | -3.8 | 0.014 | 7/13 (SW1417, LS 180, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.727×** | -3.4 | 0.052 | 0/14 | two highest doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.549×** | -3.3 | 0.057 | 6/13 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -3.2 | 0.067 | 9/13 (SW480, LS 180, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.562×** | -3.2 | 0.074 | 3/14 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.094 | 11/13 (hTERT-HPNE, COLO 205, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.748×** | -3.1 | 0.095 | 1/13 (COLO 205) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 89.9 | 0 | 12 (9 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.135× (z -15.9) |
| [[LoVo (line)]] | wt | 63.1 | 0 | 7 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0945× (z -13.8) |
| [[LS 180 (line)]] | wt | 64.3 | 0 | 5 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.156× (z -12.4) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.217× (z -10.8) |
| [[SW48 (line)]] | wt | 131 | 0 | 4 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.141× (z -9.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.159× (z -9.8) |
| [[C32 (line)]] | wt | 91.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.119× (z -10.3) |
| [[KATO III (line)]] | alt | 19.6 | 0 | 2 (1 ⚠) | — | [[5-Azacytidine (drug)]] 5 µM 0.0864× (z -10.1) |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0600× (z -8.9) |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0942× (z -8.8) |
| [[Hs 766T (line)]] | wt | 6.52 | 0 | 1 | — | [[Triamcinolone (drug)]] 5 µM 0.101× (z -10.8) |
| [[SW1417 (line)]] | alt | 87.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.239× (z -9.8) |
| [[A-172 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJB1]] | +0.80 | +0.74 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.77 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[LGR5]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[BMP4]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[EDAR]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[VWA2]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.72 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[VIL1]] | +0.70 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[IL20RA]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.70 | +0.67 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 1, C 40. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAMBI]] | B | BAMBI activity raises VSNL1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without BAMBI | 0.072 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[AXIN2]] | C | AXIN2 activity raises VSNL1's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 4.86× lower at baseline in the lines without AXIN2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises VSNL1's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 4.84× lower at baseline in the lines without HNF4A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises VSNL1's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 5.92× lower at baseline in the lines without VWA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |
| [[IGFL4]] | C | IGFL4 activity raises VSNL1's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 3.78× lower at baseline in the lines without IGFL4 | 0.008 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises VSNL1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 4.96× lower at baseline in the lines without LGR5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises VSNL1's level | lines that do not express EDAR (36) vs lines expressing it (14) | 6.01× lower at baseline in the lines without EDAR | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises VSNL1's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 4.56× lower at baseline in the lines without LINC01819 | 0.011 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[LINC00299]] | C | LINC00299 activity raises VSNL1's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 3.68× lower at baseline in the lines without LINC00299 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2; co-absent with the target |
| [[LINC01814]] | C | LINC01814 activity raises VSNL1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 3.96× lower at baseline in the lines without LINC01814 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3; co-absent with the target |
| [[KLK7]] | C | KLK7 activity raises VSNL1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 4.19× lower at baseline in the lines without KLK7 | 0.021 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[ZNF503-AS1]] | C | ZNF503-AS1 activity raises VSNL1's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.94× lower at baseline in the lines without ZNF503-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 11, C 30. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNTB1]] | B | VSNL1 activity raises SNTB1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 4.40× lower at baseline in the lines without VSNL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[ABHD12B]] | B | VSNL1 activity raises ABHD12B's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.12× lower at baseline in the lines without VSNL1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[HUNK]] | B | VSNL1 activity raises HUNK's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without VSNL1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[TNFRSF19]] | B | VSNL1 activity raises TNFRSF19's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 1.90× lower at baseline in the lines without VSNL1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| cells under [[BAY1125976 (drug)]] 0.5 µM | B | VSNL1 activity lowers the cells' numbers under BAY1125976 0.5 µM (makes them more sensitive) | lines that do not express VSNL1 (34) vs lines expressing it (14) | the lines without VSNL1: 1.37× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[TGFBR3]] | B | VSNL1 activity raises TGFBR3's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.85× lower at baseline in the lines without VSNL1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[PLEKHS1]] | B | VSNL1 activity raises PLEKHS1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.09× lower at baseline in the lines without VSNL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[PAQR8]] | B | VSNL1 activity raises PAQR8's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 1.57× lower at baseline in the lines without VSNL1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[NCALD]] | B | VSNL1 activity raises NCALD's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.27× lower at baseline in the lines without VSNL1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[MAN1A1]] | B | VSNL1 activity raises MAN1A1's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without VSNL1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[ZNRF3]] | B | VSNL1 activity raises ZNRF3's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without VSNL1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[IGFL4]] | C | VSNL1 activity raises IGFL4's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without VSNL1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.1, 46.9); signed map (62.6, 12.7). **Vector** length 62.6, 23.5% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.0 | +2.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | visinin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.2 — chr2:17,539,126-17,657,018 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VILIP, HPCAL3, HUVISL1, HLP3, VILIP-1 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P62760](https://www.uniprot.org/uniprotkb/P62760) (Visinin-like protein 1):

> Regulates (in vitro) the inhibition of rhodopsin phosphorylation in a calcium-dependent manner.

**Summary**, from NCBI Gene [7447](https://www.ncbi.nlm.nih.gov/gene/7447):

> This gene is a member of the visinin/recoverin subfamily of neuronal calcium sensor proteins. The encoded protein is strongly expressed in granule cells of the cerebellum where it associates with membranes in a calcium-dependent manner and modulates intracellular signaling pathways of the central nervous system by directly or indirectly regulating the activity of adenylyl cyclase. Alternatively spliced transcript variants have been observed, but their full-length nature has not been determined. …

**Accessions** — [HGNC:12722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12722) · Entrez [7447](https://www.ncbi.nlm.nih.gov/gene/7447) · UniProt [P62760](https://www.uniprot.org/uniprotkb/P62760) · Ensembl [ENSG00000163032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163032)

## Data

Gene col 8621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8621); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8621]; `tensor/DDL_lfc|DDL_z.npy` [8621]; `embed/gene_vectors.npy` [8621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8621 or target_col == 8621). Every well: [[VSNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VSNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
