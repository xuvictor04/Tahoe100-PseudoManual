---
symbol: "SLCO4A1"
type: "gene"
col: 2087
ensembl_id: "ENSG00000101187"
name: "solute carrier organic anion transporter family member 4A1"
location: "20q13.33"
module: 195
arm: "+"
pooled_cpm: 77.58
n_lines_expressing: 41
n_dd_up: 0
n_dd_down: 43
n_dd_up_clean: 0
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 21
direction_downstream: 22
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# SLCO4A1

*solute carrier organic anion transporter family member 4A1* — 20q13.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.599× (z -9.1, q 5e-17, down in 29 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN2]] (+0.71, fdr 7e-06), [[SHB]] (+0.69, fdr 7e-06), [[HPCAL1]] (+0.68, fdr 7e-06); moves opposite to [[TLK1]] (-0.56, fdr 3e-05), [[FIGN]] (-0.55, fdr 1e-05), [[RNF115]] (-0.55, fdr 3e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[CDCP1]] → it (grade B ⚠); 22 go from it, the strongest it → [[CDCP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.33× | +3.6 | 0.17 | 19/39 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.49 | 13/39 (NCI-H23, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -9.1 | 5e-17 | 29/40 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -8.5 | 4e-15 | 34/39 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.524×** | -8.1 | 8e-14 | 28/37 (HCT15, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -8.0 | 2e-13 | 30/38 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.601×** | -7.9 | 4e-13 | 34/39 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.525×** | -7.8 | 6e-13 | 32/39 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.532×** | -7.6 | 2e-12 | 31/38 (HOP62, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.553×** | -7.5 | 6e-12 | 32/38 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.541×** | -7.4 | 6e-12 | 35/39 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.522×** | -7.3 | 1e-11 | 32/41 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.626×** | -7.1 | 5e-11 | 32/39 (HOP62, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.550×** | -7.0 | 2e-10 | 33/39 (HOP62, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -6.9 | 2e-10 | 23/31 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.576×** | -6.9 | 2e-10 | 36/39 (HOP62, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.579×** | -6.9 | 2e-10 | 30/39 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.597×** | -6.5 | 3e-09 | 33/40 (HOP62, SK-MEL-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.694×** | -6.5 | 3e-09 | 26/39 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.608×** | -6.4 | 4e-09 | 33/40 (HOP62, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 173 | 0 | 25 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.520× (z -16.9) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0867× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 98.5 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -15.6) |
| [[CFPAC-1 (line)]] | alt | 169 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -22.1) |
| [[PANC-1 (line)]] | alt | 115 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -21.2) |
| [[J82 (line)]] | alt | 130 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 215 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0358× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.0) |
| [[A498 (line)]] | wt | 43.2 | 0 | 6 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.188× (z -12.4) |
| [[A-172 (line)]] | wt | 96.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.370× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.253× (z -10.9) |
| [[SW480 (line)]] | alt | 65.1 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -11.1) |
| [[CHP-212 (line)]] | wt | 100 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0792× (z -16.6) |
| [[Hs 766T (line)]] | wt | 279 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.249× (z -11.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 113 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -13.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.2) |
| [[A549 (line)]] | wt | 24.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.4) |
| [[BT-474 (line)]] | alt | 63.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 66.4 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.569× (z -12.3) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 92.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 81.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.7) |
| [[SW 1271 (line)]] | alt | 189 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -9.4) |
| [[HCT15 (line)]] | alt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0785× (z -16.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 73.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 37.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.374× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 93.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -9.5) |
| [[SW1417 (line)]] | alt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -11.5) |
| [[SW48 (line)]] | wt | 111 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.318× (z -8.8) |
| [[A-427 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.53 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN2]] | +0.71 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[SHB]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RASA3]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ITPR3]] | +0.66 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[ZFYVE28]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[SEMA4B]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[GALNT18]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PAQR5]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[STMN3]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[PTGS1]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[IQSEC1]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLK1]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[FIGN]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[RNF115]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[PAIP1]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ZSCAN31]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[BORCS7]] | -0.53 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[DECR1]] | -0.53 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[ADI1]] | -0.52 | -0.51 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | CDCP1 activity raises SLCO4A1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 3.16× lower at baseline in the lines without CDCP1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[PODXL]] | B | PODXL activity raises SLCO4A1's level | lines that do not express PODXL (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without PODXL | 0.007 | ⚠ within organs, on part of the lines; also absent: IL32, LGR6, SERPINB9; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises SLCO4A1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.18× lower at baseline in the lines without PLEK2 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[KRT15]] | B | KRT15 activity raises SLCO4A1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.59× lower at baseline in the lines without KRT15 | 0.012 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[LINC00887]] | B | LINC00887 activity raises SLCO4A1's level | lines that do not express LINC00887 (8) vs lines expressing it (42) | 3.23× lower at baseline in the lines without LINC00887 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC02036, STAMBPL1, CFAP45; maybe low, not absent |
| [[GALNT18]] | B | GALNT18 activity raises SLCO4A1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without GALNT18 | 0.013 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[NTSR1]] | B | NTSR1 activity raises SLCO4A1's level | lines that do not express NTSR1 (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without NTSR1 | 0.014 | ⚠ within organs, on part of the lines; also absent: TNFRSF6B, LINC02432, COL17A1 |
| [[S100A16]] | B | S100A16 activity raises SLCO4A1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 3.46× lower at baseline in the lines without S100A16 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[ADGRE2]] | B | ADGRE2 activity raises SLCO4A1's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without ADGRE2 | 0.025 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[SLC16A3]] | B | SLC16A3 activity raises SLCO4A1's level | lines that do not express SLC16A3 (7) vs lines expressing it (43) | 3.31× lower at baseline in the lines without SLC16A3 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL4R, SDC4, ARHGAP27; maybe low, not absent |
| [[TOR4A]] | B | TOR4A activity raises SLCO4A1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.74× lower at baseline in the lines without TOR4A | 0.047 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[CELSR1]] | B | CELSR1 activity raises SLCO4A1's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.33× lower at baseline in the lines without CELSR1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 22, C 0. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | SLCO4A1 activity raises CDCP1's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 4.85× lower at baseline in the lines without SLCO4A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[ASAP2]] | B | SLCO4A1 activity raises ASAP2's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without SLCO4A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[LINC00887]] | B | SLCO4A1 activity raises LINC00887's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.45× lower at baseline in the lines without SLCO4A1 | 0.011 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[FLNB]] | B | SLCO4A1 activity raises FLNB's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.26× lower at baseline in the lines without SLCO4A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[KIAA1671]] | B | SLCO4A1 activity raises KIAA1671's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.34× lower at baseline in the lines without SLCO4A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[KRT15]] | B | SLCO4A1 activity raises KRT15's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 3.00× lower at baseline in the lines without SLCO4A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[ITPR3]] | B | SLCO4A1 activity raises ITPR3's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.57× lower at baseline in the lines without SLCO4A1 | 0.030 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[NIBAN2]] | B | SLCO4A1 activity raises NIBAN2's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without SLCO4A1 | 0.030 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[PAQR5]] | B | SLCO4A1 activity raises PAQR5's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.93× lower at baseline in the lines without SLCO4A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[EPHA2]] | B | SLCO4A1 activity raises EPHA2's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 3.13× lower at baseline in the lines without SLCO4A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[SLC16A3]] | B | SLCO4A1 activity raises SLC16A3's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.55× lower at baseline in the lines without SLCO4A1 | 0.047 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[TNFAIP8]] | B | SLCO4A1 activity raises TNFAIP8's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without SLCO4A1 | 0.053 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.9, 2.5); signed map (2.0, 50.5). **Vector** length 132, 42.2% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | -3.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.4 | +2.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.0 | -7.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.7 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.8 | -7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.6 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.6 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.4 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 4A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,642,503-62,685,785 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OATP-E, OATP4A1; previously SLC21A12 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Reactome | 4 pathways, smallest: Organic anion transport by SLCO transporters; SLC-mediated transport of organic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BD0](https://www.uniprot.org/uniprotkb/Q96BD0) (Solute carrier organic anion transporter family member 4A1):

> Organic anion antiporter with apparent broad substrate specificity. Recognizes various substrates including thyroid hormones 3,3',5-triiodo-L-thyronine (T3), L-thyroxine (T4) and 3,3',5'-triiodo-L-thyronine (rT3), conjugated steroids such as estrone 3-sulfate and estradiol 17-beta glucuronide, bile acids such as taurocholate and prostanoids such as prostaglandin E2, likely operating in a tissue-specific manner. May be involved in uptake of metabolites from the circulation into organs such as …

**Summary**, from NCBI Gene [28231](https://www.ncbi.nlm.nih.gov/gene/28231):

> Enables prostaglandin transmembrane transporter activity. Predicted to be involved in sodium-independent organic anion transport. Located in cell junction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10953) · Entrez [28231](https://www.ncbi.nlm.nih.gov/gene/28231) · UniProt [Q96BD0](https://www.uniprot.org/uniprotkb/Q96BD0) · Ensembl [ENSG00000101187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101187)

## Data

Gene col 2087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2087); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2087]; `tensor/DDL_lfc|DDL_z.npy` [2087]; `embed/gene_vectors.npy` [2087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2087 or target_col == 2087). Every well: [[SLCO4A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO4A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
