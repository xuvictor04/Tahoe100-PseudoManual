---
symbol: "IFI27"
type: "gene"
col: 9215
ensembl_id: "ENSG00000165949"
name: "interferon alpha inducible protein 27"
location: "14q32.12"
module: 32
arm: "+"
pooled_cpm: 108.01
n_lines_expressing: 29
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 51
direction_downstream: 77
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFI27

*interferon alpha inducible protein 27* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +5.9, q 2e-06, up in 20 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.378× (z -8.7, q 2e-15, down in 25 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI6]] (+0.93, fdr 7e-06), [[IFITM3]] (+0.88, fdr 7e-06), [[OAS1]] (+0.87, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 51 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 77 go from it, the strongest it → [[OAS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +5.9 | 2e-06 | 20/28 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.16×** | +4.9 | 2e-04 | 11/28 (J82, LS 180, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.21×** | +4.9 | 2e-04 | 9/24 (J82, LS 180, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +4.6 | 6e-04 | 22/27 (SHP-77, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +4.3 | 0.002 | 24/29 (SW1417, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.003 | 22/27 (SW1417, NCI-H2347, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.87×** | +4.0 | 0.006 | 19/27 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +3.3 | 0.080 | 18/27 (NCI-H1573, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.378×** | -8.7 | 2e-15 | 25/28 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.527×** | -5.7 | 3e-06 | 24/28 (LoVo, COLO 205, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.411×** | -5.6 | 4e-06 | 24/27 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.575×** | -4.9 | 1e-04 | 20/27 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.463×** | -4.9 | 1e-04 | 25/27 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.513×** | -4.2 | 0.002 | 23/27 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.534×** | -4.0 | 0.006 | 18/27 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.561×** | -3.6 | 0.019 | 24/28 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.566×** | -3.6 | 0.021 | 24/27 (A549, NCI-H1573, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.551×** | -3.5 | 0.022 | 23/27 (COLO 205, SK-MEL-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.352×** | -3.4 | 0.029 | 25/28 (J82, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -3.4 | 0.031 | 23/27 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -3.4 | 0.031 | 20/27 (NCI-H1792, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.569×** | -3.4 | 0.031 | 26/27 (SW 900, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.365×** | -3.3 | 0.033 | 22/28 (A-172, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.598×** | -3.2 | 0.043 | 24/27 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.603×** | -3.2 | 0.049 | 23/28 (LoVo, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 193 | 0 | 11 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.123× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 90.9 | 0 | 9 | — | [[Tofacitinib (drug)]] 5 µM 0.122× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 7 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0355× (z -14.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.145× (z -12.2) |
| [[A549 (line)]] | wt | 46.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.7) |
| [[KATO III (line)]] | alt | 443 | 0 | 6 | — | [[Tofacitinib (drug)]] 5 µM 0.197× (z -14.4) |
| [[COLO 205 (line)]] | alt | 349 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.159× (z -13.9) |
| [[A-172 (line)]] | wt | 89.2 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.165× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 64.0 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.147× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 54.1 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.180× (z -10.9) |
| [[J82 (line)]] | alt | 149 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 55.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.8) |
| [[A498 (line)]] | wt | 102 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.284× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 581 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.249× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.198× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 44.0 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.113× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 54.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 438 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.351× (z -9.1) |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.4) |
| [[SW 900 (line)]] | alt | 463 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.361× (z -8.6) |
| [[SW1417 (line)]] | alt | 142 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.319× (z -10.0) |
| [[A-427 (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 185 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 538 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.07 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI6]] | +0.93 | +0.87 / +0.96 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 882 |
| [[IFITM3]] | +0.88 | +0.82 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 829 |
| [[OAS1]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 937 |
| [[ISG15]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 970 |
| [[RSAD2]] | +0.86 | +0.87 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 958 |
| [[MX2]] | +0.86 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 664 |
| [[IFIT3]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 904 |
| [[IFI35]] | +0.85 | +0.80 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 781 |
| [[CMPK2]] | +0.85 | +0.84 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 623 |
| [[USP18]] | +0.85 | +0.82 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 771 |
| [[OAS2]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 866 |
| [[OASL]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 888 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 32, C 19. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IFI27's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RASGRP3]] | B | RASGRP3 activity raises IFI27's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without RASGRP3 | 0.010 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[FBXO39]] | B | FBXO39 activity raises IFI27's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 3.33× lower at baseline in the lines without FBXO39 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[IFIT3]] | B | IFIT3 activity raises IFI27's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 4.91× lower at baseline in the lines without IFIT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises IFI27's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.83× lower at baseline in the lines without PLAAT4 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[CASP10]] | B | CASP10 activity raises IFI27's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 4.20× lower at baseline in the lines without CASP10 | 0.012 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[UBA7]] | B | UBA7 activity raises IFI27's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 4.75× lower at baseline in the lines without UBA7 | 0.013 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises IFI27's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 4.47× lower at baseline in the lines without IFI44 | 0.014 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[CMPK2]] | B | CMPK2 activity raises IFI27's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.01× lower at baseline in the lines without CMPK2 | 0.017 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[ODF3B]] | B | ODF3B activity raises IFI27's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 3.17× lower at baseline in the lines without ODF3B | 0.017 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[CTSS]] | B | CTSS activity raises IFI27's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.78× lower at baseline in the lines without CTSS | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises IFI27's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.92× lower at baseline in the lines without GBP1 | 0.025 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 63, C 14. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS3]] | B | IFI27 activity raises OAS3's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.66× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[USP18]] | B | IFI27 activity raises USP18's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.42× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[SCO2]] | B | IFI27 activity raises SCO2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.41× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[N4BP1]] | B | IFI27 activity raises N4BP1's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.37× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[CMPK2]] | B | IFI27 activity raises CMPK2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[PLSCR1]] | B | IFI27 activity raises PLSCR1's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.74× lower at baseline in the lines without IFI27 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[IFI6]] | B | IFI27 activity raises IFI6's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.99× lower at baseline in the lines without IFI27 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[PARP10]] | B | IFI27 activity raises PARP10's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without IFI27 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[HELZ2]] | B | IFI27 activity raises HELZ2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.06× lower at baseline in the lines without IFI27 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[CASP10]] | B | IFI27 activity raises CASP10's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without IFI27 | 0.004 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[TMEM140]] | B | IFI27 activity raises TMEM140's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.16× lower at baseline in the lines without IFI27 | 0.005 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[MX2]] | B | IFI27 activity raises MX2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 4.04× lower at baseline in the lines without IFI27 | 0.006 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.884). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 51.9); signed map (65.4, 29.5). **Vector** length 111, 43.1% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.72 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.78 to 21); *ISG15 antiviral mechanism* (reactome, mean cos +0.78 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.8 | -8.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.3 | -3.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.0 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | interferon alpha inducible protein 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:94,104,836-94,116,695 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P27, FAM14D, ISG12 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 4 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Interferon alpha/beta signaling; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P40305](https://www.uniprot.org/uniprotkb/P40305) (Interferon alpha-inducible protein 27, mitochondrial):

> Probable adapter protein involved in different biological processes. Part of the signaling pathways that lead to apoptosis. Involved in type-I interferon-induced apoptosis characterized by a rapid and robust release of cytochrome C from the mitochondria and activation of BAX and caspases 2, 3, 6, 8 and 9. Also functions in TNFSF10-induced apoptosis. May also have a function in the nucleus, where it may be involved in the interferon-induced negative regulation of the transcriptional activity of …

**Summary**, from NCBI Gene [3429](https://www.ncbi.nlm.nih.gov/gene/3429):

> Enables several functions, including RNA polymerase II-specific DNA-binding transcription factor binding activity; identical protein binding activity; and lamin binding activity. Involved in several processes, including cell surface receptor signaling pathway; host-mediated perturbation of viral genome replication; and protein K48-linked ubiquitination. Acts upstream of or within negative regulation of transcription by RNA polymerase II and regulation of protein export from nucleus. Located in …

**Accessions** — [HGNC:5397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5397) · Entrez [3429](https://www.ncbi.nlm.nih.gov/gene/3429) · UniProt [P40305](https://www.uniprot.org/uniprotkb/P40305) · Ensembl [ENSG00000165949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165949)

## Data

Gene col 9215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9215); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9215]; `tensor/DDL_lfc|DDL_z.npy` [9215]; `embed/gene_vectors.npy` [9215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9215 or target_col == 9215). Every well: [[IFI27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
