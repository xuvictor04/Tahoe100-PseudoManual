---
symbol: "SNTG2"
type: "gene"
col: 10268
ensembl_id: "ENSG00000172554"
name: "syntrophin gamma 2"
location: "2p25.3"
module: 61
arm: "+"
pooled_cpm: 3.66
n_lines_expressing: 32
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SNTG2

*syntrophin gamma 2* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.88× (z +16.9, q 0e+00, up in 11 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-427 0.276×, SNU-1 0.107×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0952×; ⚠ cell-cycle shift, explains ~25% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.165×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.226×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.246×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERC2]] (+0.74, fdr 7e-06), [[TMEFF2]] (+0.67, fdr 8e-06), [[TMEM108]] (+0.65, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[RGS7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.88×** | +16.9 | 0e+00 | 11/20 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.83×** | +16.7 | 0e+00 | 13/22 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.72×** | +16.4 | 0e+00 | 25/27 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.50×** | +13.3 | 6e-38 | 2/7 (HOP62, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.48×** | +13.2 | 9e-38 | 23/28 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.55×** | +12.8 | 9e-36 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.06×** | +12.4 | 4e-33 | 20/27 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.77×** | +10.8 | 2e-25 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.03×** | +9.8 | 1e-20 | 17/24 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.76×** | +8.9 | 2e-17 | 12/23 (SNU-423, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +7.8 | 3e-13 | 9/19 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.31×** | +7.4 | 8e-12 | 20/27 (C-33 A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +6.5 | 3e-09 | 16/27 (A498, SHP-77, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +5.0 | 3e-05 | 6/26 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.3 | 6e-04 | 2/12 (A-172, HOP62) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +4.3 | 6e-04 | 9/25 (A-172, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +4.2 | 0.001 | 3/14 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.83×** | +3.8 | 0.004 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +3.6 | 0.008 | 9/24 (SHP-77, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10268.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-427 0.276×, SNU-1 0.107×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0952×; ⚠ cell-cycle shift, explains ~25% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.165×; ⚠ toxic); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.226×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.246×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.674× | -3.5 | 0.25 | 12/25 (NCI-H23, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.667× | -3.3 | 0.25 | 4/27 (LOX-IMVI, A-172, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.697× | -3.2 | 0.26 | 7/20 (A-427, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 77.4 | 0 | 8 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0952× (z -16.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.226× (z -10.6) |
| [[A498 (line)]] | wt | 4.11 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 21.5× (z +11.4) | — |
| [[A-172 (line)]] | wt | 2.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.7× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 6.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.64× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 1.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 27.0× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 1.33 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.3× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 1.07 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 20.2× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.49 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.4× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 2.13 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.3× (z +8.9) | — |
| [[A549 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.796 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERC2]] | +0.74 | +0.65 / +0.79 | both halves | 7e-06 |  |
| [[TMEFF2]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[TMEM108]] | +0.65 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[SGCZ]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 685 |
| [[ATP8A2]] | +0.63 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[FMN2]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GABRB3]] | +0.62 | +0.50 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[CDH18]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[VAT1L]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[NTRK3]] | +0.61 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[LINC02511]] | +0.60 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[RERG]] | +0.60 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNTG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GABRB3]] | B | GABRB3 activity raises SNTG2's level | lines that do not express GABRB3 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without GABRB3 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000244468, S100A9, FGG |
| [[GNAO1]] | B | GNAO1 activity raises SNTG2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without GNAO1 | 0.074 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[CTNNA2]] | B | CTNNA2 activity raises SNTG2's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 1.83× lower at baseline in the lines without CTNNA2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS7]] | B | SNTG2 activity raises RGS7's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without SNTG2 | 0.053 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent |
| [[LINC01933]] | B | SNTG2 activity raises LINC01933's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 1.40× lower at baseline in the lines without SNTG2 | 0.056 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent |
| [[HBG2]] | B | SNTG2 activity raises HBG2's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without SNTG2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent |
| [[MIR646HG]] | C | SNTG2 activity raises MIR646HG's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 3.10× lower at baseline in the lines without SNTG2 | 0.025 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent; co-absent with the target |
| [[NBEAP1]] | C | SNTG2 activity raises NBEAP1's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without SNTG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent; co-absent with the target |
| [[FMN2]] | C | SNTG2 activity raises FMN2's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without SNTG2 | 0.080 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 31.1); signed map (32.1, 24.0). **Vector** length 48.1, 8.35% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +16.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +16.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.3 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | syntrophin gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:950,849-1,367,613 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYN5, G2SYN |
| Gene groups (HGNC) | PDZ domain containing; Syntrophin family |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY99](https://www.uniprot.org/uniprotkb/Q9NY99) (Gamma-2-syntrophin):

> Adapter protein that binds to and probably organizes the subcellular localization of a variety of proteins. May link various receptors to the actin cytoskeleton and the dystrophin glycoprotein complex (By similarity).

**Summary**, from NCBI Gene [54221](https://www.ncbi.nlm.nih.gov/gene/54221):

> This gene encodes a protein belonging to the syntrophin family. Syntrophins are cytoplasmic peripheral membrane proteins that bind to components of mechanosenstive sodium channels and the extreme carboxy-terminal domain of dystrophin and dystrophin-related proteins. The PDZ domain of this protein product interacts with a protein component of a mechanosensitive sodium channel that affects channel gating. Absence or reduction of this protein product has been associated with Duchenne muscular …

**Accessions** — [HGNC:13741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13741) · Entrez [54221](https://www.ncbi.nlm.nih.gov/gene/54221) · UniProt [Q9NY99](https://www.uniprot.org/uniprotkb/Q9NY99) · Ensembl [ENSG00000172554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172554)

## Data

Gene col 10268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10268); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10268]; `tensor/DDL_lfc|DDL_z.npy` [10268]; `embed/gene_vectors.npy` [10268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10268 or target_col == 10268). Every well: [[SNTG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNTG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
