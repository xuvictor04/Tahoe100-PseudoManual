---
symbol: "VSTM4"
type: "gene"
col: 9154
ensembl_id: "ENSG00000165633"
name: "V-set and transmembrane domain containing 4"
location: "10q11.23"
module: 13
arm: "+"
pooled_cpm: 4.0
n_lines_expressing: 19
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 27
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# VSTM4

*V-set and transmembrane domain containing 4* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.54× (z +14.9, q 0e+00, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.64× (z +5.8, q 1e-06, up in 3 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.527× (z -5.3, q 7e-05, down in 11 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01411]] (+0.82, fdr 7e-06), [[SYNDIG1]] (+0.70, fdr 7e-06), [[INSYN2B]] (+0.67, fdr 7e-06); moves opposite to [[SRGN]] (-0.66, fdr 7e-06), [[PTX3]] (-0.49, fdr 8e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ADAMTS14]] → it (grade C ⚠); 27 go from it, the strongest it → [[LOXL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.54×** | +14.9 | 0e+00 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +9.2 | 1e-17 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +8.9 | 1e-16 | 1/6 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +5.8 | 1e-06 | 3/17 (C-33 A, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +5.7 | 1e-06 | 6/17 (NCI-H2347, A498, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.47×** | +5.3 | 1e-05 | 2/8 (NCI-H2030, A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.7 | 2e-04 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +4.2 | 0.002 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.003 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.56×** | +3.7 | 0.012 | 1/15 (C-33 A) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.56×** | +3.7 | 0.012 | 1/15 (SW 1088) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.7 | 0.012 | 0/13 | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.56×** | +3.6 | 0.012 | 0/11 | inconsistent across doses | low cells (technical?) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.020 | 5/16 (HS-578T, A-172, …) | two highest doses | low cells (technical?); position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.55×** | +3.3 | 0.030 | 1/12 (A498) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.030 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.047 | 3/17 (RPMI-7951, NCI-H2347, …) | inconsistent across doses |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.047 | 2/12 (C-33 A, NCI-H2030) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.054 | 2/12 (A-427, A498) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.069 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.074 | 0/17 | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.42×** | +2.9 | 0.078 | 2/13 (RPMI-7951, SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Silodosin (drug)]] 5 µM |  | **1.44×** | +2.9 | 0.082 | 1/13 (C-33 A) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.527×** | -5.3 | 7e-05 | 11/17 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.579×** | -4.2 | 0.007 | 1/17 (AN3 CA) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.607×** | -4.1 | 0.007 | 7/17 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.731×** | -3.7 | 0.035 | 1/17 (A-172) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -3.5 | 0.055 | 10/17 (SW 900, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Rucaparib (phosphate) (drug)]] 0.05 µM |  | 0.663× | -3.1 | 0.14 | 2/16 (H4, SW 900) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.766× | -3.1 | 0.14 | 10/17 (H4, SNU-423, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.668× | -3.1 | 0.14 | 2/17 (NCI-H2347, H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 39.1 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -15.8) |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -15.7) |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0950× (z -13.8) |
| [[HOP62 (line)]] | alt | 6.58 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 42.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 7.48 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.12 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0573× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.365 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.310 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01411]] | +0.82 | +0.78 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SYNDIG1]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ADAMTS14]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SIRLNT]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[EDNRA]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[KCNK3]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[MEG3]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[KIRREL3]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[NAV1]] | +0.63 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[GDNF]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MIR493HG]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 | **novel candidate** |
| [[PTX3]] | -0.49 | -0.56 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS14]] | C | ADAMTS14 activity raises VSTM4's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.42× lower at baseline in the lines without ADAMTS14 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[BOC]] | C | BOC activity raises VSTM4's level | lines that do not express BOC (21) vs lines expressing it (29) | 3.08× lower at baseline in the lines without BOC | 0.054 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2; co-absent with the target |
| [[FAM20C]] | C | FAM20C activity raises VSTM4's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 2.75× lower at baseline in the lines without FAM20C | 0.058 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises VSTM4's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.75× lower at baseline in the lines without EDNRA | 0.063 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises VSTM4's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.54× lower at baseline in the lines without PTGFR | 0.079 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises VSTM4's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.84× lower at baseline in the lines without COL5A1 | 0.083 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[GJA1]] | C | GJA1 activity raises VSTM4's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 3.37× lower at baseline in the lines without GJA1 | 0.088 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[CSMD2]] | C | CSMD2 activity raises VSTM4's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 3.55× lower at baseline in the lines without CSMD2 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[IL1B]] | C | IL1B activity raises VSTM4's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without IL1B | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises VSTM4's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 2.75× lower at baseline in the lines without NTNG2 | 0.095 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 7, C 20. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL2]] | B | VSTM4 activity raises LOXL2's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 4.67× lower at baseline in the lines without VSTM4 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[GSDME]] | B | VSTM4 activity raises GSDME's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.73× lower at baseline in the lines without VSTM4 | 0.030 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[ABCA1]] | B | VSTM4 activity raises ABCA1's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.32× lower at baseline in the lines without VSTM4 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[RAI14]] | B | VSTM4 activity raises RAI14's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 2.76× lower at baseline in the lines without VSTM4 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[COL7A1]] | B | VSTM4 activity raises COL7A1's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.61× lower at baseline in the lines without VSTM4 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[GPR68]] | B | VSTM4 activity raises GPR68's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without VSTM4 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| cells under [[(S)-Crizotinib (drug)]] 0.05 µM | B | VSTM4 activity lowers the cells' numbers under (S)-Crizotinib 0.05 µM (makes them more sensitive) | lines that do not express VSTM4 (31) vs lines expressing it (17) | the lines without VSTM4: 1.17× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[BOC]] | C | VSTM4 activity raises BOC's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without VSTM4 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2; co-absent with the target |
| [[FAM20C]] | C | VSTM4 activity raises FAM20C's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 5.63× lower at baseline in the lines without VSTM4 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2; co-absent with the target |
| [[SPOCD1]] | C | VSTM4 activity raises SPOCD1's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 2.77× lower at baseline in the lines without VSTM4 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2; co-absent with the target |
| [[COL6A2]] | C | VSTM4 activity raises COL6A2's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 5.61× lower at baseline in the lines without VSTM4 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2; co-absent with the target |
| [[PTGFR]] | C | VSTM4 activity raises PTGFR's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.49× lower at baseline in the lines without VSTM4 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.1, 16.5); signed map (23.8, 48.1). **Vector** length 60.1, 17.5% of its response variance represented; |z| ≥ 3 in 598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -5.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | V-set and transmembrane domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:49,014,236-49,115,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31737; previously C10orf72 |
| Gene groups (HGNC) | V-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW00](https://www.uniprot.org/uniprotkb/Q8IW00) (V-set and transmembrane domain-containing protein 4):

> Peptide Lv enhances L-type voltage-gated calcium channel (L-VGCC) currents in retinal photoreceptors.

**Summary**, from NCBI Gene [196740](https://www.ncbi.nlm.nih.gov/gene/196740):

> Predicted to act upstream of or within several processes, including endothelial cell proliferation; retina blood vessel maintenance; and vasculature development. Predicted to be located in extracellular region and plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26470) · Entrez [196740](https://www.ncbi.nlm.nih.gov/gene/196740) · UniProt [Q8IW00](https://www.uniprot.org/uniprotkb/Q8IW00) · Ensembl [ENSG00000165633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165633)

## Data

Gene col 9154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9154); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9154]; `tensor/DDL_lfc|DDL_z.npy` [9154]; `embed/gene_vectors.npy` [9154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9154 or target_col == 9154). Every well: [[VSTM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VSTM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
