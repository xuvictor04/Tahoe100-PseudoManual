---
symbol: "GPNMB"
type: "gene"
col: 5837
ensembl_id: "ENSG00000136235"
name: "glycoprotein nmb"
location: "7p15.3"
module: 9
arm: "+"
pooled_cpm: 15.23
n_lines_expressing: 20
n_dd_up: 42
n_dd_down: 2
n_dd_up_clean: 30
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 14
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GPNMB

*glycoprotein nmb* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.89× (z +16.4, q 0e+00, up in 12 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.68× (z +14.3, q 3e-44, up in 10 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.660× (z -4.0, q 0.039, down in 0 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCN3]] (+0.67, fdr 7e-06), [[DCT]] (+0.62, fdr 7e-06), [[COL12A1]] (+0.59, fdr 1e-05); moves opposite to [[MARCHF2]] (-0.50, fdr 8e-05), [[ZBED4]] (-0.46, fdr 4e-05), [[IL9RP3]] (-0.44, fdr 3e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[P2RX7]] → it (grade B ⚠); 14 go from it, the strongest it → [[NNT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.89×** | +16.4 | 0e+00 | 12/14 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.68×** | +14.3 | 3e-44 | 10/15 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.89×** | +13.5 | 4e-39 | 8/11 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +11.7 | 1e-29 | 5/12 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.7 | 3e-20 | 9/16 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +7.6 | 3e-12 | 12/17 (SK-MEL-2, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +7.4 | 1e-11 | 11/18 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +6.8 | 9e-10 | 6/15 (BT-474, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +6.1 | 5e-08 | 9/15 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.88×** | +5.7 | 7e-07 | 5/9 (A-172, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +5.5 | 2e-06 | 5/18 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.4 | 3e-06 | 5/14 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +5.1 | 1e-05 | 6/15 (NCI-H661, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.7 | 1e-04 | 13/18 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.38×** | +4.6 | 1e-04 | 7/17 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.6 | 2e-04 | 8/18 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +4.4 | 3e-04 | 6/16 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 5e-04 | 4/17 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.12×** | +4.0 | 0.001 | 8/14 (SK-MEL-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.003 | 7/17 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.004 | 4/17 (SK-MEL-2, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.004 | 6/18 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.660×** | -4.0 | 0.039 | 0/18 | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.064 | 0/18 | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.740× | -3.1 | 0.32 | 2/18 (CHP-212, RPMI-7951) | top dose only |  |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.745× | -3.0 | 0.32 | 0/18 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +16.8) | — |
| [[J82 (line)]] | alt | 22.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 6.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.25× (z +11.8) | — |
| [[A-427 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 319 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCN3]] | +0.67 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[DCT]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 | STRING 471 |
| [[COL12A1]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SH3BGRL]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[PRUNE2]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PLXDC2]] | +0.57 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[PRLR]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PDZRN3]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PSG4]] | +0.55 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[RHOBTB3]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SGCD]] | +0.54 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[MMP2]] | +0.54 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF2]] | -0.50 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[ZBED4]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[IL9RP3]] | -0.44 | -0.26 / -0.34 | both halves | 3e-04 |  |
| [[TUBB6]] | -0.44 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[CCM2]] | -0.44 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[RHBDF2]] | -0.44 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[ZMYND19]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[FBXL18]] | -0.43 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[NLK]] | -0.43 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[SPTLC2]] | -0.42 | -0.39 / -0.29 | both halves | 3e-04 |  |
| [[RSKR]] | -0.42 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[RMND5B]] | -0.42 | -0.23 / -0.33 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RX7]] | B | P2RX7 activity raises GPNMB's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without P2RX7 | 0.048 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[PPP2R2B]] | C | PPP2R2B activity raises GPNMB's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 4.00× lower at baseline in the lines without PPP2R2B | 0.016 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[COL11A1]] | C | COL11A1 activity raises GPNMB's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 5.12× lower at baseline in the lines without COL11A1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[TF]] | C | TF activity raises GPNMB's level | lines that do not express TF (41) vs lines expressing it (9) | 6.79× lower at baseline in the lines without TF | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |
| [[PDZRN3]] | C | PDZRN3 activity raises GPNMB's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.11× lower at baseline in the lines without PDZRN3 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098; co-absent with the target |
| [[MOXD1]] | C | MOXD1 activity raises GPNMB's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 3.40× lower at baseline in the lines without MOXD1 | 0.070 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[NR1H4]] | C | NR1H4 activity raises GPNMB's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without NR1H4 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises GPNMB's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 3.45× lower at baseline in the lines without COL3A1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[CLSTN2]] | C | CLSTN2 activity raises GPNMB's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 2.80× lower at baseline in the lines without CLSTN2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660; co-absent with the target |
| [[DCT]] | C | DCT activity raises GPNMB's level | lines that do not express DCT (42) vs lines expressing it (8) | 5.76× lower at baseline in the lines without DCT | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 6, C 8. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT]] | B | GPNMB activity raises NNT's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without GPNMB | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[CLIC2]] | B | GPNMB activity raises CLIC2's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.15× lower at baseline in the lines without GPNMB | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[ATP6V1B2]] | B | GPNMB activity raises ATP6V1B2's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without GPNMB | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[RSKR]] | B | GPNMB activity lowers RSKR's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.15× higher at baseline in the lines without GPNMB | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[ATP6V1C1]] | B | GPNMB activity raises ATP6V1C1's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.19× lower at baseline in the lines without GPNMB | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[ANO9]] | B | GPNMB activity lowers ANO9's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.25× higher at baseline in the lines without GPNMB | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[PDZRN3]] | C | GPNMB activity raises PDZRN3's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 4.04× lower at baseline in the lines without GPNMB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[CCN3]] | C | GPNMB activity raises CCN3's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without GPNMB | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[LRRN1]] | C | GPNMB activity raises LRRN1's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without GPNMB | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[STK32A]] | C | GPNMB activity raises STK32A's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without GPNMB | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[MOXD1]] | C | GPNMB activity raises MOXD1's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without GPNMB | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[PRUNE2]] | C | GPNMB activity raises PRUNE2's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 3.16× lower at baseline in the lines without GPNMB | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, 36.8); signed map (46.2, 29.8). **Vector** length 57.8, 18.3% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Oxaliplatin (drug)]] 0.5 µM |  | -0.8 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | glycoprotein nmb |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,235,967-23,275,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NMB, HGFIN |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: PTK6 promotes HIF1A stabilization; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14956](https://www.uniprot.org/uniprotkb/Q14956) (Transmembrane glycoprotein NMB):

> Could be a melanogenic enzyme.

**Summary**, from NCBI Gene [10457](https://www.ncbi.nlm.nih.gov/gene/10457):

> The protein encoded by this gene is a type I transmembrane glycoprotein which shows homology to the pMEL17 precursor, a melanocyte-specific protein. GPNMB shows expression in the lowly metastatic human melanoma cell lines and xenografts but does not show expression in the highly metastatic cell lines. GPNMB may be involved in growth delay and reduction of metastatic potential. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4462](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4462) · Entrez [10457](https://www.ncbi.nlm.nih.gov/gene/10457) · UniProt [Q14956](https://www.uniprot.org/uniprotkb/Q14956) · Ensembl [ENSG00000136235](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136235)

## Data

Gene col 5837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5837); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5837]; `tensor/DDL_lfc|DDL_z.npy` [5837]; `embed/gene_vectors.npy` [5837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5837 or target_col == 5837). Every well: [[GPNMB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPNMB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
