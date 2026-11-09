---
symbol: "TMEM139"
type: "gene"
col: 10964
ensembl_id: "ENSG00000178826"
name: "transmembrane protein 139"
location: "7q34"
module: 27
arm: "+"
pooled_cpm: 4.33
n_lines_expressing: 17
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 88
direction_downstream: 103
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# TMEM139

*transmembrane protein 139* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.47× (z +11.3, q 6e-27, up in 3 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +5.4, q 5e-06, up in 1 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.580× (z -4.3, q 0.010, down in 12 of 15 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Pravastatin (sodium) (drug)]] 5 µM: 0.610× (z -3.8, q 0.049, down in 3 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (KATO III 0.126×, SW480 0.187×, HEC-1-A 0.241×, SW1417 0.321×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.178×, SW480 0.309×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (HT-29 0.0382×, SW480 0.192×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.162×, LS 180 0.176×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLRN3]] (+0.82, fdr 7e-06), [[VIL1]] (+0.79, fdr 7e-06), [[EDAR]] (+0.77, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 88 arrows point to it, the strongest [[ZNF860]] → it (grade B ⚠); 103 go from it, the strongest it → [[SLC44A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10964.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.47×** | +11.3 | 6e-27 | 3/7 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +11.2 | 1e-26 | 3/9 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +8.1 | 1e-13 | 2/8 (KATO III, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.89×** | +8.0 | 2e-13 | 3/10 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.47×** | +7.1 | 1e-10 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.4 | 5e-06 | 1/14 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.12×** | +4.2 | 0.002 | 2/10 (HEC-1-A, Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.006 | 3/13 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.62×** | +3.8 | 0.011 | 1/13 (LS 180) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.054 | 6/14 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.079 | 3/15 (AsPC-1, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.1 | 0.086 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.086 | 1/10 (Panc 03.27) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10964.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (KATO III 0.126×, SW480 0.187×, HEC-1-A 0.241×, SW1417 0.321×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.178×, SW480 0.309×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (HT-29 0.0382×, SW480 0.192×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.162×, LS 180 0.176×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.580×** | -4.3 | 0.010 | 12/15 (SW480, SW1417, …) | inconsistent across doses | position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.610×** | -3.8 | 0.049 | 3/15 (HepG2/C3A, SK-MEL-2, …) | rises with dose | plate-row cell shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.650× | -3.4 | 0.13 | 0/15 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10964. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.2 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -15.1) |
| [[KATO III (line)]] | alt | 28.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0429× (z -16.4) |
| [[LS 180 (line)]] | wt | 19.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains <1% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -8.6) |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -9.8) |
| [[HT-29 (line)]] | alt | 6.70 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0382× (z -13.2) |
| [[LoVo (line)]] | wt | 4.12 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.105× (z -8.9) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.590 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.626 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10964), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLRN3]] | +0.82 | +0.78 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[VIL1]] | +0.79 | +0.80 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[KCNE3]] | +0.73 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[BMP4]] | +0.73 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[VWA2]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[AXIN2]] | +0.73 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.72 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[GJB1]] | +0.72 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[LINC00299]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[VSNL1]] | +0.70 | +0.70 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*88 arrows, 88 of them with an alert ⚠; grade A 0, B 7, C 81. Shown: the 12 strongest; 76 more arrows (76 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF860]] | B | ZNF860 activity raises TMEM139's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without ZNF860 | 0.021 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[MAP2K6]] | B | MAP2K6 activity raises TMEM139's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without MAP2K6 | 0.051 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises TMEM139's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without SHROOM3 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[SLC44A3]] | B | SLC44A3 activity raises TMEM139's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without SLC44A3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[MANSC1]] | B | MANSC1 activity raises TMEM139's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without MANSC1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TMEM139's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.07× lower at baseline in the lines without ELF3-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[VILL]] | B | VILL activity raises TMEM139's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without VILL | 0.092 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[LINC03040]] | C | LINC03040 activity raises TMEM139's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 3.50× lower at baseline in the lines without LINC03040 | 7e-04 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[ARHGEF38]] | C | ARHGEF38 activity raises TMEM139's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 4.27× lower at baseline in the lines without ARHGEF38 | 8e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises TMEM139's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 4.14× lower at baseline in the lines without GJB1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises TMEM139's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.50× lower at baseline in the lines without TMPRSS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises TMEM139's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 3.99× lower at baseline in the lines without NPSR1-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*103 arrows, 103 of them with an alert ⚠; grade A 0, B 15, C 88. Shown: the 12 strongest; 91 more arrows (91 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | TMEM139 activity raises SLC44A3's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without TMEM139 | 0.001 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[ELF3-AS1]] | B | TMEM139 activity raises ELF3-AS1's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 3.35× lower at baseline in the lines without TMEM139 | 0.003 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[FGD3]] | B | TMEM139 activity raises FGD3's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without TMEM139 | 0.004 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[VILL]] | B | TMEM139 activity raises VILL's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without TMEM139 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[MROH7]] | B | TMEM139 activity raises MROH7's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.45× lower at baseline in the lines without TMEM139 | 0.012 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[MANSC1]] | B | TMEM139 activity raises MANSC1's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.47× lower at baseline in the lines without TMEM139 | 0.020 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[SHROOM3]] | B | TMEM139 activity raises SHROOM3's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 3.10× lower at baseline in the lines without TMEM139 | 0.026 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[RSPH1]] | B | TMEM139 activity raises RSPH1's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.13× lower at baseline in the lines without TMEM139 | 0.026 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[FAAH]] | B | TMEM139 activity raises FAAH's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without TMEM139 | 0.036 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[ZNF703]] | B | TMEM139 activity raises ZNF703's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.75× lower at baseline in the lines without TMEM139 | 0.037 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[ZNF860]] | B | TMEM139 activity raises ZNF860's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without TMEM139 | 0.037 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[PHACTR3]] | B | TMEM139 activity raises PHACTR3's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 1.77× lower at baseline in the lines without TMEM139 | 0.040 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 46.9); signed map (62.7, 12.4). **Vector** length 52.2, 17.3% of its response variance represented; |z| ≥ 3 in 386 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +8.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 139 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:143,279,957-143,288,048 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90586 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV31](https://www.uniprot.org/uniprotkb/Q8IV31) (Transmembrane protein 139):

> May be involved in cellular trafficking of proteins such as SLC4A1.

**Summary**, from NCBI Gene [135932](https://www.ncbi.nlm.nih.gov/gene/135932):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22058) · Entrez [135932](https://www.ncbi.nlm.nih.gov/gene/135932) · UniProt [Q8IV31](https://www.uniprot.org/uniprotkb/Q8IV31) · Ensembl [ENSG00000178826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178826)

## Data

Gene col 10964: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10964); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10964, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10964]; `tensor/DDL_lfc|DDL_z.npy` [10964]; `embed/gene_vectors.npy` [10964]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10964 or target_col == 10964). Every well: [[TMEM139 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM139.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
