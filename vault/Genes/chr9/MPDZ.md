---
symbol: "MPDZ"
type: "gene"
col: 2833
ensembl_id: "ENSG00000107186"
name: "multiple PDZ domain crumbs cell polarity complex component"
location: "9p23"
module: 207
arm: "-"
pooled_cpm: 45.73
n_lines_expressing: 33
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# MPDZ

*multiple PDZ domain crumbs cell polarity complex component* — 9p23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +8.8, q 7e-16, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.420× (z -19.6, q 0e+00, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF180]] (+0.65, fdr 1e-05), [[ZNF518B]] (+0.63, fdr 7e-06), [[UBE2E3]] (+0.62, fdr 1e-05); moves opposite to [[CRLS1]] (-0.58, fdr 1e-05), [[PMS2P4-1]] (-0.57, fdr 3e-05), [[GLE1]] (-0.55, fdr 4e-05).
> It sits in the **-** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[FAM171B]] → it (grade B ⚠); 9 go from it, the strongest it → [[TXNDC11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +8.8 | 7e-16 | 26/31 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +7.3 | 1e-10 | 26/31 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.026 | 16/30 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.062 | 13/31 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.23× | +3.3 | 0.12 | 12/31 (CFPAC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.23× | +3.2 | 0.14 | 11/30 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | 1.44× | +3.0 | 0.20 | 12/30 (J82, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.420×** | -19.6 | 0e+00 | 29/31 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.611×** | -7.9 | 9e-13 | 23/31 (LOX-IMVI, A-427, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -7.8 | 2e-12 | 24/32 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.609×** | -7.6 | 4e-12 | 26/31 (NCI-H460, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.670×** | -6.2 | 7e-08 | 21/30 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.681×** | -6.1 | 7e-08 | 21/31 (C-33 A, NCI-H1792, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.676×** | -6.0 | 1e-07 | 23/30 (C32, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.735×** | -4.9 | 6e-05 | 17/31 (A-427, LOX-IMVI, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~21% of this change | **0.766×** | -4.3 | 0.001 | 21/29 (hTERT-HPNE, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.813×** | -3.3 | 0.051 | 15/31 (J82, NCI-H2347, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.690×** | -3.1 | 0.095 | 13/31 (LOX-IMVI, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.824×** | -3.1 | 0.095 | 13/30 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 132 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -21.8) |
| [[HOP62 (line)]] | alt | 110 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -19.0) |
| [[A-427 (line)]] | wt | 83.4 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.0) ⚠ cell-cycle shift, explains ~44% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 78.4 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.5) |
| [[C32 (line)]] | wt | 53.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -14.4) |
| [[A549 (line)]] | wt | 83.1 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.8) ⚠ cell-cycle shift, explains ~70% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -15.4) |
| [[AN3 CA (line)]] | alt | 158 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 76.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 95.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -17.3) |
| [[Panc 03.27 (line)]] | alt | 75.5 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.83× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.3) |
| [[H4 (line)]] | wt | 79.6 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0912× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.175× (z -10.5) |
| [[SW 900 (line)]] | alt | 76.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -15.6) |
| [[A-172 (line)]] | wt | 81.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -15.8) |
| [[CHP-212 (line)]] | wt | 123 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -8.8) |
| [[HS-578T (line)]] | alt | 53.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -11.4) |
| [[J82 (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 64.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 40.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.5) |
| [[PANC-1 (line)]] | alt | 34.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 74.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.6) |
| [[SHP-77 (line)]] | alt | 98.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.36× (z +8.8) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 87.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -11.4) |
| [[A498 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF180]] | +0.65 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[ZNF518B]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[UBE2E3]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PCNX2]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ATRNL1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[DST]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MMP16]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[EVC]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TNPO1]] | +0.56 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[ZFHX4]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SYNE1]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LSAMP]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRLS1]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PMS2P4-1]] | -0.57 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[GLE1]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[MED26]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[QPCTL]] | -0.53 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[APAF1]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RNASET2]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[DNAJC25]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TMEM41A]] | -0.51 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[DPM1]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RECQL5]] | -0.50 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[TXNDC11]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM171B]] | B | FAM171B activity raises MPDZ's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 6.59× lower at baseline in the lines without FAM171B | 0.049 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises MPDZ's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CHN1]] | B | CHN1 activity raises MPDZ's level | lines that do not express CHN1 (10) vs lines expressing it (40) | 4.59× lower at baseline in the lines without CHN1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HHIPL2, CARMIL2; maybe low, not absent |
| [[NEGR1]] | C | NEGR1 activity raises MPDZ's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 7.16× lower at baseline in the lines without NEGR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[JAZF1]] | C | JAZF1 activity raises MPDZ's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 8.96× lower at baseline in the lines without JAZF1 | 0.016 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent; co-absent with the target |
| [[CACNA2D1]] | C | CACNA2D1 activity raises MPDZ's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 6.31× lower at baseline in the lines without CACNA2D1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |
| [[AKT3]] | C | AKT3 activity raises MPDZ's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 6.29× lower at baseline in the lines without AKT3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041; co-absent with the target |
| [[PRKD1]] | C | PRKD1 activity raises MPDZ's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 10.13× lower at baseline in the lines without PRKD1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD; co-absent with the target |
| [[ATRNL1]] | C | ATRNL1 activity raises MPDZ's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 5.95× lower at baseline in the lines without ATRNL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises MPDZ's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 5.36× lower at baseline in the lines without TCF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[MIR137HG]] | C | MIR137HG activity raises MPDZ's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 4.14× lower at baseline in the lines without MIR137HG | 0.099 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNDC11]] | B | MPDZ activity lowers TXNDC11's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 1.31× higher at baseline in the lines without MPDZ | 0.073 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1 |
| [[FAM171B]] | B | MPDZ activity raises FAM171B's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without MPDZ | 0.078 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1 |
| [[AKT3]] | C | MPDZ activity raises AKT3's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 7.94× lower at baseline in the lines without MPDZ | 0.018 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[NEGR1]] | C | MPDZ activity raises NEGR1's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 4.83× lower at baseline in the lines without MPDZ | 0.033 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[JAZF1]] | C | MPDZ activity raises JAZF1's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 2.73× lower at baseline in the lines without MPDZ | 0.040 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[MICU3]] | C | MPDZ activity raises MICU3's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 8.07× lower at baseline in the lines without MPDZ | 0.047 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[ATRNL1]] | C | MPDZ activity raises ATRNL1's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 4.31× lower at baseline in the lines without MPDZ | 0.055 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[KCNQ5]] | C | MPDZ activity raises KCNQ5's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 7.67× lower at baseline in the lines without MPDZ | 0.068 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[CACNA2D1]] | C | MPDZ activity raises CACNA2D1's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 6.40× lower at baseline in the lines without MPDZ | 0.084 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **-** arm (projection on the module's main direction -0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-32.9, 23.7); signed map (12.3, -10.6). **Vector** length 87.2, 24.8% of its response variance represented; |z| ≥ 3 in 659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.6 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.1 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +0.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.3 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -19.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -7.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | multiple PDZ domain crumbs cell polarity complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p23 — chr9:13,105,706-13,279,692 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MUPP1 |
| Gene groups (HGNC) | PDZ domain containing; Crumbs complex components |
| Matched by | ensembl_id |

**Function**, from UniProt [O75970](https://www.uniprot.org/uniprotkb/O75970) (Multiple PDZ domain protein):

> Member of the NMDAR signaling complex that may play a role in control of AMPAR potentiation and synaptic plasticity in excitatory synapses. Promotes clustering of HT2RC at the cell surface (By similarity).

**Summary**, from NCBI Gene [8777](https://www.ncbi.nlm.nih.gov/gene/8777):

> The protein encoded by this gene has multiple PDZ domains, which are hallmarks of protein-protein interactions. The encoded protein is known to interact with the HTR2C receptor and may cause it to clump at the cell surface. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:7208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7208) · Entrez [8777](https://www.ncbi.nlm.nih.gov/gene/8777) · UniProt [O75970](https://www.uniprot.org/uniprotkb/O75970) · Ensembl [ENSG00000107186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107186)

## Data

Gene col 2833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2833); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2833]; `tensor/DDL_lfc|DDL_z.npy` [2833]; `embed/gene_vectors.npy` [2833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2833 or target_col == 2833). Every well: [[MPDZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPDZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
