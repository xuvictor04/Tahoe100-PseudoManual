---
symbol: "ZNF69"
type: "gene"
col: 12589
ensembl_id: "ENSG00000198429"
name: "zinc finger protein 69"
location: "19p13.2"
module: 27
arm: "+"
pooled_cpm: 11.71
n_lines_expressing: 35
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ZNF69

*zinc finger protein 69* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.08× (z +7.7, q 6e-12, up in 12 of 18 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 5.19×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.522× (z -7.1, q 6e-10, down in 21 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHDH]] (+0.63, fdr 1e-05), [[LINC02058]] (+0.61, fdr 9e-06), [[LGR5]] (+0.61, fdr 1e-05); moves opposite to [[RAB6A]] (-0.52, fdr 3e-05), [[TXNDC11]] (-0.51, fdr 2e-05), [[UBE2O]] (-0.51, fdr 2e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARMCX4]] → it (grade B ⚠); 3 go from it, the strongest it → [[ARMCX4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12589.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 5.19×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +7.7 | 6e-12 | 12/18 (SW1417, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.8 | 5e-04 | 14/26 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +3.9 | 0.018 | 10/21 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.35× | +3.3 | 0.11 | 8/33 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.35× | +3.3 | 0.11 | 8/32 (PANC-1, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.34× | +3.2 | 0.13 | 8/33 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.522×** | -7.1 | 6e-10 | 21/32 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -6.8 | 3e-09 | 22/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.562×** | -6.3 | 5e-08 | 19/32 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -5.8 | 8e-07 | 17/32 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -5.8 | 8e-07 | 19/31 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -5.0 | 7e-05 | 17/32 (Panc 03.27, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -4.1 | 0.003 | 14/30 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.688×** | -4.1 | 0.003 | 15/32 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.690×** | -4.1 | 0.003 | 14/32 (LS 180, CFPAC-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.676×** | -4.1 | 0.003 | 14/32 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.707×** | -3.8 | 0.008 | 7/32 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -3.7 | 0.009 | 13/32 (AN3 CA, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -3.6 | 0.013 | 12/25 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.534×** | -3.6 | 0.013 | 14/32 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -3.4 | 0.027 | 15/32 (SHP-77, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[EX229 (drug)]] 5 µM |  | **0.576×** | -3.2 | 0.057 | 13/30 (COLO 205, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.585×** | -3.1 | 0.072 | 8/32 (HT-29, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.761×** | -3.0 | 0.085 | 9/32 (COLO 205, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.684×** | -3.0 | 0.085 | 7/33 (LS 180, COLO 205, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.0 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -11.1) |
| [[COLO 205 (line)]] | alt | 81.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.215× (z -9.1) |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0719× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 36.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -10.2) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -9.7) |
| [[Hs 766T (line)]] | wt | 6.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0737× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 9.21 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.137× (z -8.8) |
| [[J82 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -9.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.5 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.230× (z -9.0) |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -13.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHDH]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.61 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[LGR5]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TMEM139]] | +0.59 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[ROCK2]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LINC01622]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[KCNE3]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CLRN3]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GJB1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[VIL1]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[VWA2]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[MYB]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[TXNDC11]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[UBE2O]] | -0.51 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC25]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TBC1D20]] | -0.49 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[IFI27L1]] | -0.49 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[GUK1]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[TBC1D22A-DT]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RPL12]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MYDGF]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[NDUFAF7]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ZMAT5]] | -0.47 | -0.32 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX4]] | B | ARMCX4 activity raises ZNF69's level | lines that do not express ARMCX4 (18) vs lines expressing it (32) | 2.30× lower at baseline in the lines without ARMCX4 | 0.008 | ⚠ within organs, on part of the lines; also absent: TLR2, LYPD5, GALC |
| [[ST18]] | B | ST18 activity raises ZNF69's level | lines that do not express ST18 (39) vs lines expressing it (11) | 2.99× lower at baseline in the lines without ST18 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises ZNF69's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 3.28× lower at baseline in the lines without TNFRSF14-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX4]] | B | ZNF69 activity raises ARMCX4's level | lines that do not express ZNF69 (15) vs lines expressing it (35) | 3.15× lower at baseline in the lines without ZNF69 | 0.010 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, TNFRSF14-AS1, CIART |
| [[RPL12]] | B | ZNF69 activity lowers RPL12's level | lines that do not express ZNF69 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without ZNF69 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, TNFRSF14-AS1, CIART |
| [[TNFRSF14-AS1]] | C | ZNF69 activity raises TNFRSF14-AS1's level | lines that do not express ZNF69 (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without ZNF69 | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, TNFRSF14-AS1, CIART; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 45.9); signed map (62.6, 13.6). **Vector** length 64.7, 13.8% of its response variance represented; |z| ≥ 3 in 659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.3 | -4.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 69 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,887,782-11,914,329 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cos5 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UC07](https://www.uniprot.org/uniprotkb/Q9UC07) (Zinc finger protein 69):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7620](https://www.ncbi.nlm.nih.gov/gene/7620):

> Enables identical protein binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13138](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13138) · Entrez [7620](https://www.ncbi.nlm.nih.gov/gene/7620) · UniProt [Q9UC07](https://www.uniprot.org/uniprotkb/Q9UC07) · Ensembl [ENSG00000198429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198429)

## Data

Gene col 12589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12589); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12589]; `tensor/DDL_lfc|DDL_z.npy` [12589]; `embed/gene_vectors.npy` [12589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12589 or target_col == 12589). Every well: [[ZNF69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
