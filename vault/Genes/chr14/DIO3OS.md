---
symbol: "DIO3OS"
type: "gene"
col: 15108
ensembl_id: "ENSG00000258498"
name: "DIO3 opposite strand upstream RNA"
location: "14q32.31"
module: 141
arm: "+"
pooled_cpm: 2.48
n_lines_expressing: 25
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 12
direction_downstream: 17
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# DIO3OS

*DIO3 opposite strand upstream RNA* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.91× (z +12.1, q 8e-31, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +5.6, q 4e-06, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.456× (z -5.1, q 2e-04, down in 14 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02320]] (+0.79, fdr 7e-06, ⚠ read-through risk), [[FGF19]] (+0.66, fdr 7e-06), [[NTSR1]] (+0.63, fdr 7e-06), [[ETV4]] (+0.61, fdr 1e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[BCAN-AS2]] → it (grade B ⚠); 17 go from it, the strongest it → [[TBC1D8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.91×** | +12.1 | 8e-31 | 3/4 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.29×** | +9.5 | 9e-19 | 2/6 (NCI-H2030, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.36×** | +7.0 | 5e-10 | 3/6 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.6 | 4e-06 | 2/13 (HEC-1-A, A549) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.6 | 5e-04 | 1/10 (NCI-H2030) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.0 | 0.006 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +4.0 | 0.006 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.008 | 2/18 (BT-474, A549) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.010 | 5/20 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +3.7 | 0.012 | 2/14 (SW1417, LoVo) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.85×** | +3.6 | 0.020 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.79×** | +3.1 | 0.081 | 3/15 (NCI-H1573, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.1 | 0.081 | 0/10 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.94×** | +3.1 | 0.088 | 1/8 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.456×** | -5.1 | 2e-04 | 14/21 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.473×** | -4.0 | 0.015 | 5/21 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.556×** | -3.9 | 0.016 | 8/21 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.565×** | -3.5 | 0.054 | 9/16 (SW480, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.481×** | -3.5 | 0.054 | 4/21 (SW480, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.639×** | -3.4 | 0.054 | 10/18 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.608×** | -3.2 | 0.097 | 9/21 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.2 | 0 | 13 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0550× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 4.29 | 0 | 2 | — | [[Decitabine (drug)]] 0.5 µM 0.0517× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 7.32 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0465× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 5.35 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0120× (z -12.9) |
| [[A-172 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.717 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.833 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.614 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02320]] | +0.79 | +0.71 / +0.84 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 14.1 kb 3′ of LINC02320 on the same strand (can correlate by spillover, not regulation) |
| [[FGF19]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[NTSR1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ETV4]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[IGFL4]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[VSIG1]] | +0.60 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[TNS4]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LINC00460]] | +0.58 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[LINC00659]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[LCK]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CACNA2D4]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PTPRN2]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[LINC00467]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAN-AS2]] | B | BCAN-AS2 activity raises DIO3OS's level | lines that do not express BCAN-AS2 (9) vs lines expressing it (41) | 1.72× lower at baseline in the lines without BCAN-AS2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS1, ARHGAP18 |
| [[GPSM3]] | B | GPSM3 activity raises DIO3OS's level | lines that do not express GPSM3 (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without GPSM3 | 0.040 | ⚠ within organs, on part of the lines; also absent: NAV1, CDK15, PAMR1 |
| [[MAP2K2]] | B | MAP2K2 activity raises DIO3OS's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[BCAN-AS1]] | B | BCAN-AS1 activity raises DIO3OS's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without BCAN-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[IGFL4]] | C | IGFL4 activity raises DIO3OS's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without IGFL4 | 0.026 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent; co-absent with the target |
| [[SCAT1]] | C | SCAT1 activity raises DIO3OS's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without SCAT1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent; co-absent with the target |
| [[PIWIL1]] | C | PIWIL1 activity raises DIO3OS's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 2.02× lower at baseline in the lines without PIWIL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises DIO3OS's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 1.82× lower at baseline in the lines without GJB1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[TNS4]] | C | TNS4 activity raises DIO3OS's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without TNS4 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6; co-absent with the target |
| [[PDE9A]] | C | PDE9A activity raises DIO3OS's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without PDE9A | 0.080 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748; co-absent with the target |
| [[SH2D3A]] | C | SH2D3A activity raises DIO3OS's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without SH2D3A | 0.084 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3; co-absent with the target |
| [[VSIG1]] | C | VSIG1 activity raises DIO3OS's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.60× lower at baseline in the lines without VSIG1 | 0.093 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 11, C 6. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | DIO3OS activity raises TBC1D8's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.56× lower at baseline in the lines without DIO3OS | 5e-04 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[ITGB5]] | B | DIO3OS activity raises ITGB5's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without DIO3OS | 0.011 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[LINC02842]] | B | DIO3OS activity raises LINC02842's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without DIO3OS | 0.012 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[LINC02320]] | B | DIO3OS activity strengthens LINC02320's drug response | lines that do not express DIO3OS (10) vs lines expressing it (19) | the lines without DIO3OS respond 0.58× as strongly (z diff +2.91); strongest at Homoharringtonine 5 µM: 0.51x vs 0.18x (z diff +4.6) | 0.013 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3; target measured in part of the lines; artifact flags |
| [[NPAS2]] | B | DIO3OS activity raises NPAS2's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 1.98× lower at baseline in the lines without DIO3OS | 0.021 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[COL4A3]] | B | DIO3OS activity raises COL4A3's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without DIO3OS | 0.032 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[TBC1D8]] | B | DIO3OS activity strengthens TBC1D8's drug response | lines that do not express DIO3OS (20) vs lines expressing it (24) | the lines without DIO3OS respond 0.76× as strongly (z diff +1.81); strongest at Idarubicin (hydrochloride) 5 µM: 0.88x vs 0.51x (z diff +5.5) | 0.032 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3; target measured in part of the lines; artifact flags |
| [[ABCC3]] | B | DIO3OS activity raises ABCC3's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.91× lower at baseline in the lines without DIO3OS | 0.039 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[GTF2IP7]] | B | DIO3OS activity raises GTF2IP7's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without DIO3OS | 0.060 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[ITGA6]] | B | DIO3OS activity raises ITGA6's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.08× lower at baseline in the lines without DIO3OS | 0.066 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[PTPRN2]] | B | DIO3OS activity raises PTPRN2's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.33× lower at baseline in the lines without DIO3OS | 0.067 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[LINC02320]] | C | DIO3OS activity raises LINC02320's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 3.82× lower at baseline in the lines without DIO3OS | 4e-04 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3; co-absent with the target |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.5, 42.8); signed map (6.8, 37.9). **Vector** length 52.9, 15.8% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +3.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | DIO3 opposite strand upstream RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q32.31 — chr14:101,552,221-101,620,355 (-) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00041, DIO3-AS1; previously C14orf134 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [64150](https://www.ncbi.nlm.nih.gov/gene/64150):

> The mouse and human DIO3OS and DIO3 (MIM 601038) genes overlap and are transcribed in opposite directions. The mouse Dio3 gene is imprinted from the paternal allele during fetal development, suggesting that DIO3OS is a noncoding gene that may have a role in maintaining monoallelic expression of DIO3 (Hernandez et al., 2004 [PubMed 14962667]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20348) · Entrez [64150](https://www.ncbi.nlm.nih.gov/gene/64150) · Ensembl [ENSG00000258498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258498)

## Data

Gene col 15108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15108); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15108]; `tensor/DDL_lfc|DDL_z.npy` [15108]; `embed/gene_vectors.npy` [15108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15108 or target_col == 15108). Every well: [[DIO3OS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIO3OS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
