---
symbol: "TNFRSF14"
type: "gene"
col: 8110
ensembl_id: "ENSG00000157873"
name: "TNF receptor superfamily member 14"
location: "1p36.32"
module: 14
arm: "+"
pooled_cpm: 6.57
n_lines_expressing: 38
n_dd_up: 3
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 10
direction_downstream: 6
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNFRSF14

*TNF receptor superfamily member 14* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.72× (z +3.7, q 0.061, up in 4 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.274× (z -12.6, q 2e-33, down in 29 of 34 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.445× (z -7.9, q 4e-13, down in 26 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF14-AS1]] (+0.72, fdr 7e-06, ⚠ same locus), [[DDR1]] (+0.67, fdr 7e-06), [[ANO9]] (+0.63, fdr 1e-05), [[SULT1C2]] (+0.61, fdr 1e-05); moves opposite to [[RAP1GDS1]] (-0.60, fdr 1e-05), [[ITGB1BP1]] (-0.56, fdr 3e-05), [[NLN]] (-0.56, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[UBA7]] → it (grade B ⚠); 6 go from it, the strongest it → [[HSD17B14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.7 | 0.061 | 4/28 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.061 | 7/34 (AsPC-1, C32, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.061 | 4/29 (COLO 205, NCI-H2347, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.57× | +3.1 | 0.25 | 6/30 (Panc 03.27, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.274×** | -12.6 | 2e-33 | 29/34 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.278×** | -12.4 | 5e-33 | 29/34 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.295×** | -11.9 | 4e-30 | 29/34 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.554×** | -8.1 | 7e-14 | 22/30 (HT-29, RPMI-7951, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.445×** | -7.9 | 4e-13 | 26/34 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.455×** | -7.7 | 2e-12 | 24/34 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -6.0 | 2e-07 | 19/31 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.542×** | -5.7 | 8e-07 | 14/24 (HT-29, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.584×** | -5.2 | 1e-05 | 18/33 (SW 900, LoVo, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.586×** | -5.2 | 1e-05 | 16/29 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -5.0 | 3e-05 | 14/29 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -4.5 | 3e-04 | 17/33 (HT-29, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.646×** | -4.1 | 0.002 | 14/25 (Panc 03.27, COLO 205, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.004 | 14/31 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -3.9 | 0.004 | 12/34 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -3.6 | 0.010 | 10/31 (HT-29, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.010 | 13/33 (PANC-1, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.773×** | -3.5 | 0.012 | 15/35 (C32, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.688×** | -3.5 | 0.013 | 9/33 (SW 900, LOX-IMVI, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.694×** | -3.4 | 0.017 | 7/35 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -3.3 | 0.020 | 12/29 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rosiglitazone (drug)]] 5 µM |  | **0.720×** | -3.1 | 0.050 | 9/31 (LS 180, KATO III, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.716×** | -3.0 | 0.059 | 8/28 (HT-29, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.2 | 0 | 6 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.103× (z -13.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.9) |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0989× (z -14.4) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.144× (z -11.9) |
| [[C32 (line)]] | wt | 58.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 5.18 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0750× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0883× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0948× (z -9.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[J82 (line)]] | alt | 7.39 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 4.88 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0430× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 6.32 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0590× (z -11.0) |
| [[SW480 (line)]] | alt | 3.61 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.149× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.598 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF14-AS1]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DDR1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | same gene group |
| [[ANO9]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SULT1C2]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[COL16A1]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PLXNB2]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SLC12A7]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[STAP2]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CES3]] | +0.57 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[TRAF4]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[APBA3]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GPRC5C]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP1GDS1]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[ITGB1BP1]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NLN]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[BCAR3]] | -0.54 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[FAM20B]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[DNM1L]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TTL]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[KPNB1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PAFAH1B2]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LRRC20]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[RUSC2]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[DOCK5]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBA7]] | B | UBA7 activity raises TNFRSF14's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without UBA7 | 0.004 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[C11orf52]] | B | C11orf52 activity raises TNFRSF14's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without C11orf52 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[FXYD3]] | B | FXYD3 activity raises TNFRSF14's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 2.53× lower at baseline in the lines without FXYD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2 |
| [[C11orf52]] | B | C11orf52 activity strengthens TNFRSF14's drug response | lines that do not express C11orf52 (14) vs lines expressing it (21) | the lines without C11orf52 respond 0.67× as strongly (z diff +1.38); strongest at Panobinostat 0.5 µM: 0.39x vs 0.23x (z diff +3.1) | 0.020 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39; target measured in part of the lines; artifact flags |
| [[STAT5A]] | B | STAT5A activity raises TNFRSF14's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 3.02× lower at baseline in the lines without STAT5A | 0.036 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[TRIM31]] | B | TRIM31 activity raises TNFRSF14's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.33× lower at baseline in the lines without TRIM31 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[RHBDL2]] | B | RHBDL2 activity raises TNFRSF14's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without RHBDL2 | 0.050 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |
| [[UGT1A8]], [[UGT1A9]] | B | UGT1A8, UGT1A9 activity raises TNFRSF14's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.84× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.085 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[TMPRSS3]] | B | TMPRSS3 activity raises TNFRSF14's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 1.56× lower at baseline in the lines without TMPRSS3 | 0.092 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises TNFRSF14's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 3.94× lower at baseline in the lines without TNFRSF14-AS1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD17B14]] | B | TNFRSF14 activity lowers HSD17B14's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 2.06× higher at baseline in the lines without TNFRSF14 | 0.010 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[STK32A]] | B | TNFRSF14 activity raises STK32A's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without TNFRSF14 | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[FAM20B]] | B | TNFRSF14 activity lowers FAM20B's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 1.27× higher at baseline in the lines without TNFRSF14 | 0.076 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[TTL]] | B | TNFRSF14 activity lowers TTL's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 1.64× higher at baseline in the lines without TNFRSF14 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[NLN]] | B | TNFRSF14 activity lowers NLN's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 1.75× higher at baseline in the lines without TNFRSF14 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[TNFRSF14-AS1]] | C | TNFRSF14 activity raises TNFRSF14-AS1's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 2.21× lower at baseline in the lines without TNFRSF14 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, 3.3); signed map (46.3, 7.6). **Vector** length 66.8, 13.7% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.2 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.8 | -5.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:2,555,639-2,565,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HVEM, ATAR, TR2, LIGHTR, HVEA, CD270 |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Reactome | 6 pathways, smallest: Co-inhibition by BTLA; TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92956](https://www.uniprot.org/uniprotkb/Q92956) (Tumor necrosis factor receptor superfamily member 14):

> Receptor for four distinct ligands: The TNF superfamily members TNFSF14/LIGHT and homotrimeric LTA/lymphotoxin-alpha and the immunoglobulin superfamily members BTLA and CD160, altogether defining a complex stimulatory and inhibitory signaling network. Signals via the TRAF2-TRAF3 E3 ligase pathway to promote immune cell survival and differentiation. Participates in bidirectional cell-cell contact signaling between antigen presenting cells and lymphocytes. In response to ligation of …

**Summary**, from NCBI Gene [8764](https://www.ncbi.nlm.nih.gov/gene/8764):

> This gene encodes a member of the TNF (tumor necrosis factor) receptor superfamily. The encoded protein functions in signal transduction pathways that activate inflammatory and inhibitory T-cell immune response. It binds herpes simplex virus (HSV) viral envelope glycoprotein D (gD), mediating its entry into cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:11912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11912) · Entrez [8764](https://www.ncbi.nlm.nih.gov/gene/8764) · UniProt [Q92956](https://www.uniprot.org/uniprotkb/Q92956) · Ensembl [ENSG00000157873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157873)

## Data

Gene col 8110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8110); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8110]; `tensor/DDL_lfc|DDL_z.npy` [8110]; `embed/gene_vectors.npy` [8110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8110 or target_col == 8110). Every well: [[TNFRSF14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
