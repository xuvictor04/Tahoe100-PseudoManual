---
symbol: "SAP30-DT"
type: "gene"
col: 15748
ensembl_id: "ENSG00000272870"
name: "SAP30 divergent transcript"
location: "4q34.1"
module: 79
arm: "+"
pooled_cpm: 9.54
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# SAP30-DT

*SAP30 divergent transcript* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +9.1, q 4e-17, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.282× (z -18.0, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM3A]] (+0.82, fdr 7e-06), [[MXI1]] (+0.77, fdr 7e-06), [[PDK3]] (+0.76, fdr 7e-06); moves opposite to [[GPATCH4]] (-0.66, fdr 7e-06), [[MAK16]] (-0.66, fdr 7e-06), [[POGK]] (-0.66, fdr 7e-06).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[APLN]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BRWD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.1 | 4e-17 | 33/44 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.6 | 0.001 | 9/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.068 | 15/48 (NCI-H2347, CHP-212, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.5 | 0.068 | 12/44 (J82, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.068 | 14/36 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimitespib (drug)]] 5 µM |  | 1.85× | +3.2 | 0.11 | 6/34 (NCI-H1792, HOP62, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.38× | +3.2 | 0.13 | 9/42 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.282×** | -18.0 | 0e+00 | 42/45 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.221×** | -14.6 | 1e-45 | 41/46 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.321×** | -11.4 | 6e-28 | 37/44 (LS 180, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.388×** | -9.5 | 2e-19 | 37/48 (NCI-H1792, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.509×** | -6.8 | 1e-09 | 31/47 (HOP62, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -5.9 | 4e-07 | 26/39 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -5.8 | 6e-07 | 23/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.600×** | -4.9 | 6e-05 | 22/47 (MIA PaCa-2, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.648×** | -4.1 | 0.003 | 18/46 (SNU-423, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.668×** | -4.1 | 0.003 | 19/48 (A-172, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -4.1 | 0.003 | 16/48 (SNU-423, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.668×** | -3.8 | 0.006 | 18/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.495×** | -3.7 | 0.011 | 24/47 (MIA PaCa-2, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -3.5 | 0.016 | 14/43 (MIA PaCa-2, HCT15, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.781×** | -3.5 | 0.017 | 19/48 (LOX-IMVI, SNU-423, …) | rises with dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.706×** | -3.5 | 0.017 | 13/47 (A549, KATO III, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.523×** | -3.4 | 0.024 | 18/44 (H4, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.743×** | -3.0 | 0.091 | 12/44 (BT-474, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 19.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -17.3) |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -14.9) |
| [[A-172 (line)]] | wt | 27.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -22.4) |
| [[C32 (line)]] | wt | 24.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0277× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0746× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -9.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.293× (z -8.8) |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 8.27 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.4) |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -19.3) |
| [[J82 (line)]] | alt | 8.08 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -9.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 8.23 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.79× (z +8.6) ⚠ position not correctable | [[Harringtonine (drug)]] 5 µM 0.0710× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 8.62 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.109× (z -11.1) |
| [[SW480 (line)]] | alt | 8.32 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.3) |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.140× (z -8.5) |
| [[H4 (line)]] | wt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.9) |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 7.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -9.8) |
| [[HT-29 (line)]] | alt | 4.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -9.8) |
| [[LS 180 (line)]] | wt | 6.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0435× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 7.98 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.208× (z -8.5) |
| [[PANC-1 (line)]] | alt | 6.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.0) |
| [[SHP-77 (line)]] | alt | 6.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -11.1) |
| [[A-427 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM3A]] | +0.82 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[MXI1]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[PDK3]] | +0.76 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[RBPJ]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.74 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[HERC3]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.72 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.72 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[NARF]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | +0.71 | +0.64 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | -0.66 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[MAK16]] | -0.66 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[POGK]] | -0.66 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[UTP20]] | -0.65 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[DDX10]] | -0.64 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.63 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[FAM83H]] | -0.63 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.63 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[CHMP6]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[COA7]] | -0.62 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[RAD54L2]] | -0.62 | -0.51 / -0.71 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.61 | -0.62 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLN]] | B | APLN activity raises SAP30-DT's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.16× lower at baseline in the lines without APLN | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC03047]] | B | LINC03047 activity raises SAP30-DT's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without LINC03047 | 0.046 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRWD3]] | C | SAP30-DT's natural level strengthens BRWD3's drug response | SAP30-DT's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.11; direction clear | 0.074 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.849). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.3, -17.1); signed map (-34.9, 23.7). **Vector** length 102, 23.9% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.60 to 16); *hypoxia* (control, mean cos +0.67 to 5); *glycolysis* (hallmark, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -18.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -11.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -9.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | SAP30 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q34.1 — chr4:173,349,543-173,370,721 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000608794, MIRE |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54424) · Entrez [105377540](https://www.ncbi.nlm.nih.gov/gene/105377540) · Ensembl [ENSG00000272870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272870)

## Data

Gene col 15748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15748); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15748]; `tensor/DDL_lfc|DDL_z.npy` [15748]; `embed/gene_vectors.npy` [15748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15748 or target_col == 15748). Every well: [[SAP30-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAP30-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
