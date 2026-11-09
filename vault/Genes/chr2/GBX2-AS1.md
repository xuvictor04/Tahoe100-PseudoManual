---
symbol: "GBX2-AS1"
type: "gene"
col: 13913
ensembl_id: "ENSG00000233611"
name: "GBX2 and ASB18 antisense RNA 1"
location: "2q37.2"
module: 5
arm: "+"
pooled_cpm: 8.83
n_lines_expressing: 37
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 12
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GBX2-AS1

*GBX2 and ASB18 antisense RNA 1* — 2q37.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +8.3, q 4e-14, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -9.3, q 1e-17, down in 19 of 31 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.344× (z -6.1, q 3e-07, down in 20 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLFNL1-AS1]] (+0.69, fdr 7e-06), [[ZNF876P]] (+0.64, fdr 1e-05), [[KCNQ5]] (+0.62, fdr 7e-06); moves opposite to [[HADHB]] (-0.59, fdr 1e-05), [[OPTN]] (-0.56, fdr 1e-05), [[SLC50A1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DLX1]] → it (grade B ⚠); 12 go from it, the strongest it → [[RFLNB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.3 | 4e-14 | 17/31 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +8.1 | 1e-13 | 20/33 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.0 | 1e-04 | 7/25 (CFPAC-1, A549, …) | two highest doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.051 | 8/34 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Brimonidine (drug)]] 0.5 µM |  | 1.35× | +3.3 | 0.10 | 4/33 (A-172, SW480, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | 1.32× | +3.0 | 0.17 | 5/34 (SW480, PANC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.17 | 9/33 (SHP-77, hTERT-HPNE, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.32× | +3.0 | 0.17 | 10/34 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.21× | +3.0 | 0.17 | 6/34 (SW 900, HOP62, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.548×** | -9.3 | 1e-17 | 19/31 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -6.1 | 3e-07 | 20/34 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.566×** | -6.0 | 5e-07 | 18/34 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Artesunate (drug)]] 5 µM |  | **0.690×** | -5.7 | 2e-06 | 20/34 (SW480, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.620×** | -5.2 | 2e-05 | 16/34 (MIA PaCa-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.693×** | -4.0 | 0.006 | 14/30 (PANC-1, J82, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.695×** | -4.0 | 0.006 | 14/34 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.697×** | -3.9 | 0.006 | 11/34 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.698×** | -3.9 | 0.006 | 10/34 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -3.4 | 0.038 | 11/32 (A-427, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.087 | 13/33 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 41.7 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0956× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.03× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -10.8) |
| [[SHP-77 (line)]] | alt | 36.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -14.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.0 | 0 | 2 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0745× (z -9.9) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.100× (z -9.1) |
| [[A-427 (line)]] | wt | 12.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -10.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[A498 (line)]] | wt | 7.96 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +9.8) ⚠ cell-cycle shift, explains ~83% of this change | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -10.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 10.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -17.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 3.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.118× (z -8.5) |
| [[HOP62 (line)]] | alt | 9.66 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.84× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 5.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 6.14 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0757× (z -9.0) |
| [[SW1417 (line)]] | alt | 6.77 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0919× (z -8.9) |
| [[SW480 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLFNL1-AS1]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 | same gene group |
| [[ZNF876P]] | +0.64 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[KCNQ5]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[BEND3]] | +0.59 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ZNF718]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PRDM15]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[LRRK1]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[WNT5B]] | +0.57 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[TIMM23B-AGAP6]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RANBP17]] | +0.57 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HADHB]] | -0.59 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[OPTN]] | -0.56 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SLC50A1]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SKAP2]] | -0.55 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[ANG]] | -0.54 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[THAP8]] | -0.53 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[FIG4]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[RNASE4]] | -0.52 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[RAB30]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ALAD]] | -0.51 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ZFYVE1]] | -0.51 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TBC1D17]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX1]] | B | DLX1 activity raises GBX2-AS1's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without DLX1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[RFLNB]] | B | RFLNB activity raises GBX2-AS1's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without RFLNB | 0.020 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[GALNT14]] | B | GALNT14 activity lowers GBX2-AS1's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.54× higher at baseline in the lines without GALNT14 | 0.045 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[FAR2]] | B | FAR2 activity lowers GBX2-AS1's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.54× higher at baseline in the lines without FAR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[MGAT5B]] | C | MGAT5B activity raises GBX2-AS1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.72× lower at baseline in the lines without MGAT5B | 0.006 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[ENTPD1-AS1]] | C | ENTPD1-AS1 activity raises GBX2-AS1's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 3.36× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[KHDC1-AS1]] | C | KHDC1-AS1 activity raises GBX2-AS1's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 2.37× lower at baseline in the lines without KHDC1-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFLNB]] | B | GBX2-AS1 activity raises RFLNB's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without GBX2-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[C16orf95]] | B | GBX2-AS1 activity raises C16orf95's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without GBX2-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[CFAP36]] | B | GBX2-AS1 activity raises CFAP36's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without GBX2-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[ADCY3]] | B | GBX2-AS1 activity raises ADCY3's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without GBX2-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[L3HYPDH]] | B | GBX2-AS1 activity raises L3HYPDH's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without GBX2-AS1 | 0.077 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[MBD3]] | B | GBX2-AS1 activity raises MBD3's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without GBX2-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[TTL]] | B | GBX2-AS1 activity raises TTL's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without GBX2-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[SCHIP1]] | B | GBX2-AS1 activity raises SCHIP1's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 2.94× lower at baseline in the lines without GBX2-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[FANCC]] | B | GBX2-AS1 activity raises FANCC's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.35× lower at baseline in the lines without GBX2-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[ARMC6]] | B | GBX2-AS1 activity raises ARMC6's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without GBX2-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[MGAT5B]] | C | GBX2-AS1 activity raises MGAT5B's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 3.32× lower at baseline in the lines without GBX2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B; co-absent with the target |
| [[KHDC1-AS1]] | C | GBX2-AS1 activity raises KHDC1-AS1's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without GBX2-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B; co-absent with the target |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.0, -35.5); signed map (3.9, -49.7). **Vector** length 73.0, 15.1% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.2 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Artesunate (drug)]] 5 µM |  | -2.6 | -5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.2 | -6.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | GBX2 and ASB18 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q37.2 — chr2:236,167,418-236,294,927 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AC079135.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55714) · Entrez [121853074](https://www.ncbi.nlm.nih.gov/gene/121853074) · Ensembl [ENSG00000233611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233611)

## Data

Gene col 13913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13913); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13913]; `tensor/DDL_lfc|DDL_z.npy` [13913]; `embed/gene_vectors.npy` [13913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13913 or target_col == 13913). Every well: [[GBX2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GBX2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
