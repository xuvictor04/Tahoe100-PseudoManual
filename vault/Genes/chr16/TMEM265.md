---
symbol: "TMEM265"
type: "gene"
col: 15990
ensembl_id: "ENSG00000281991"
name: "transmembrane protein 265"
location: "16p11.2"
module: 12
arm: "+"
pooled_cpm: 18.64
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TMEM265

*transmembrane protein 265* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.79× (z +16.6, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.384× (z -11.1, q 5e-26, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG11]] (+0.73, fdr 7e-06), [[TMEM42]] (+0.72, fdr 7e-06), [[MED18]] (+0.70, fdr 7e-06); moves opposite to [[BCAP31]] (-0.69, fdr 7e-06), [[MAPK9]] (-0.67, fdr 1e-05), [[ELAVL1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[EDN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.79×** | +16.6 | 0e+00 | 40/44 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.58×** | +14.2 | 1e-43 | 42/45 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.82×** | +12.0 | 4e-31 | 39/42 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.26×** | +9.5 | 4e-19 | 37/45 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.6 | 6e-09 | 26/42 (BT-474, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.61×** | +5.5 | 4e-06 | 17/38 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.9 | 0.008 | 16/38 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.028 | 13/41 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.34×** | +3.4 | 0.040 | 14/42 (A-427, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.062 | 8/44 (SW480, Panc 03.27, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.384×** | -11.1 | 5e-26 | 39/44 (HT-29, C-33 A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.460×** | -9.0 | 4e-17 | 40/46 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -8.6 | 2e-15 | 37/45 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.524×** | -7.5 | 7e-12 | 36/45 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -6.5 | 8e-09 | 27/42 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.574×** | -6.5 | 9e-09 | 27/46 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.440×** | -5.0 | 4e-05 | 22/44 (BT-474, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -4.7 | 2e-04 | 15/23 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -4.1 | 0.003 | 19/41 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 44.8 | 6 (4 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.38× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -11.6) |
| [[HT-29 (line)]] | alt | 36.6 | 4 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +17.3) | [[Auranofin (drug)]] 5 µM 0.196× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 28.6 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -14.7) |
| [[A-172 (line)]] | wt | 26.4 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.191× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 58.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.35× (z +11.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.160× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.218× (z -10.5) |
| [[COLO 205 (line)]] | alt | 36.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -10.5) |
| [[HOP62 (line)]] | alt | 6.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +11.2) | — |
| [[KATO III (line)]] | alt | 12.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0657× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 9.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 34.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.69× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 9.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.3) | — |
| [[RKO (line)]] | wt | 8.17 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0970× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.128× (z -9.0) |
| [[A-427 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG11]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[MED18]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CEBPD]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ARRDC2]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TRIM47]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PEX12]] | +0.65 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[LIPT1]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[COIL]] | +0.64 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ELF1]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.69 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.67 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[ELAVL1]] | -0.66 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[BPNT2]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.63 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[HACD3]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[UGGT1]] | -0.62 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[STT3B]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[CHID1]] | -0.60 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[P3H1]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDN1]] | B | EDN1 activity raises TMEM265's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 2.00× lower at baseline in the lines without EDN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[CRB3]] | B | CRB3 activity raises TMEM265's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without CRB3 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1 |
| [[CCL20]] | B | CCL20 activity raises TMEM265's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without CCL20 | 0.029 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[IL15]] | B | IL15 activity raises TMEM265's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.72× lower at baseline in the lines without IL15 | 0.054 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[IL15]] | B | IL15 activity strengthens TMEM265's drug response | lines that do not express IL15 (10) vs lines expressing it (36) | the lines without IL15 respond 0.53× as strongly (z diff +1.52); rises at some drug-doses, falls at others (42% from rises): Panobinostat 0.5 µM: 0.61x vs 0.40x (z diff +2.6); Panobinostat 5 µM: 0.62x vs 0.40x (z diff +2.5); Digitoxin 5 µM: 1.36x vs 1.96x (z diff +2.4) | 0.065 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[CHMP4C]] | B | CHMP4C activity raises TMEM265's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without CHMP4C | 0.069 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |
| [[LTB]] | B | LTB activity raises TMEM265's level | lines that do not express LTB (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without LTB | 0.078 | ⚠ within organs, on part of the lines; also absent: HAVCR1, TIMD4, RHEX |
| [[MXRA7]] | B | MXRA7 activity lowers TMEM265's level | lines that do not express MXRA7 (6) vs lines expressing it (44) | 2.02× higher at baseline in the lines without MXRA7 | 0.090 | ⚠ within organs, on part of the lines; also absent: FKBP7, KIF3C, SNTA1 |
| [[HDAC6]] | B | HDAC6 activity raises TMEM265's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CRTAP]] | C | CRTAP activity lowers TMEM265's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 3.29× higher at baseline in the lines without CRTAP | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.6, 3.2); signed map (4.1, -19.4). **Vector** length 105, 25.8% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +0.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 265 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,740,642-30,745,196 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A087WTH1](https://www.uniprot.org/uniprotkb/A0A087WTH1) carries no function annotation.

**Summary**, from NCBI Gene [100862671](https://www.ncbi.nlm.nih.gov/gene/100862671):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:51241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51241) · Entrez [100862671](https://www.ncbi.nlm.nih.gov/gene/100862671) · UniProt [A0A087WTH1](https://www.uniprot.org/uniprotkb/A0A087WTH1) · Ensembl [ENSG00000281991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281991)

## Data

Gene col 15990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15990); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15990]; `tensor/DDL_lfc|DDL_z.npy` [15990]; `embed/gene_vectors.npy` [15990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15990 or target_col == 15990). Every well: [[TMEM265 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM265.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
