---
symbol: "KCNK3"
type: "gene"
col: 10087
ensembl_id: "ENSG00000171303"
name: "potassium two pore domain channel subfamily K member 3"
location: "2p23.3"
module: 13
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 20
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# KCNK3

*potassium two pore domain channel subfamily K member 3* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.22× (z +10.4, q 2e-22, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.06× (z +4.7, q 3e-04, up in 3 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.820× (z -4.8, q 8e-04, down in 4 of 16 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.490× (z -4.7, q 9e-04, down in 11 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RPMI-7951 0.0338×, HOP62 0.0993×, SHP-77 0.250×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.138×, RPMI-7951 0.119×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0325×, PANC-1 0.0302×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNDIG1]] (+0.74, fdr 7e-06), [[ITGA11]] (+0.74, fdr 7e-06), [[NAV1]] (+0.66, fdr 7e-06); moves opposite to [[NEXN]] (-0.54, fdr 5e-05), [[SRGN]] (-0.50, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02970]] → it (grade C ⚠); 3 go from it, the strongest it → [[FIBCD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.22×** | +10.4 | 2e-22 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.48×** | +7.2 | 2e-10 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +5.8 | 2e-06 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.95×** | +5.0 | 7e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +4.7 | 3e-04 | 3/13 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.7 | 3e-04 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.001 | 6/14 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.52×** | +4.3 | 0.001 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.3 | 0.001 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.0 | 0.003 | 1/10 (NCI-H460) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +4.0 | 0.004 | 3/14 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.19×** | +3.7 | 0.012 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.030 | 0/14 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.2 | 0.064 | 0/10 | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +3.1 | 0.071 | 0/3 | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.68×** | +3.0 | 0.092 | 0/10 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10087.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RPMI-7951 0.0338×, HOP62 0.0993×, SHP-77 0.250×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.138×, RPMI-7951 0.119×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0325×, PANC-1 0.0302×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.820×** | -4.8 | 8e-04 | 4/16 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -4.7 | 9e-04 | 11/13 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.551×** | -3.9 | 0.018 | 5/15 (HOP62, BT-474, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.629× | -3.0 | 0.33 | 5/14 (PANC-1, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 18.5 | 0 | 15 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0312× (z -14.2) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0993× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0338× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.159× (z -16.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0400× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 3.58 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0203× (z -9.8) |
| [[A498 (line)]] | wt | 19.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.3) |
| [[PANC-1 (line)]] | alt | 2.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0302× (z -11.1) |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.1) |
| [[A-172 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.804 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.766 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNDIG1]] | +0.74 | +0.77 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[NAV1]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PAEP]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LINC02813]] | +0.65 | +0.65 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[VSTM4]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[INSYN2B]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TRIM9]] | +0.63 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[GFPT2]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MIR493HG]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ADAMTS14]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SFRP1]] | +0.61 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEXN]] | -0.54 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[SRGN]] | -0.50 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02970]] | C | LINC02970 activity raises KCNK3's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 1.77× lower at baseline in the lines without LINC02970 | 0.016 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595; co-absent with the target |
| [[SYNDIG1]] | C | SYNDIG1 activity raises KCNK3's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without SYNDIG1 | 0.068 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises KCNK3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.08× lower at baseline in the lines without ITGA11 | 0.068 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[RARB]] | C | RARB activity raises KCNK3's level | lines that do not express RARB (28) vs lines expressing it (22) | 2.08× lower at baseline in the lines without RARB | 0.074 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |
| [[IQCA1]] | C | IQCA1 activity raises KCNK3's level | lines that do not express IQCA1 (31) vs lines expressing it (19) | 1.76× lower at baseline in the lines without IQCA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: NOL4, KCTD8, MAP6; maybe low, not absent; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises KCNK3's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without GPR173 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[SCUBE1]] | C | SCUBE1 activity raises KCNK3's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without SCUBE1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FIBCD1]] | B | KCNK3 activity raises FIBCD1's level | lines that do not express KCNK3 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without KCNK3 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, IGFN1 |
| [[SCUBE1]] | C | KCNK3 activity raises SCUBE1's level | lines that do not express KCNK3 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without KCNK3 | 0.052 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, IGFN1; co-absent with the target |
| [[PODXL]] | C | KCNK3 activity raises PODXL's level | lines that do not express KCNK3 (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without KCNK3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, IGFN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.1, 15.0); signed map (22.7, 47.1). **Vector** length 52.0, 16.4% of its response variance represented; |z| ≥ 3 in 452 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.7 | +4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.3 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.7 | +1.0 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.7 | +1.7 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Ferulic acid (drug)]] 0.5 µM |  | +0.7 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -2.4 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | potassium two pore domain channel subfamily K member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,692,722-26,733,420 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K2p3.1, TASK, TASK-1, TASK1 |
| Gene groups (HGNC) | Potassium two pore domain channel subfamily K |
| Reactome | 6 pathways, smallest: Tandem pore domain potassium channels; Phase 4 - resting membrane potential; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [O14649](https://www.uniprot.org/uniprotkb/O14649) (Potassium channel subfamily K member 3):

> K(+) channel that conducts voltage-dependent outward rectifying currents upon membrane depolarization. Voltage sensing is coupled to K(+) electrochemical gradient in an 'ion flux gating' mode where outward but not inward ion flow opens the gate. Changes ion selectivity and becomes permeable to Na(+) ions in response to extracellular acidification. Protonation of the pH sensor His-98 stabilizes C-type inactivation conformation likely converting the channel from outward K(+)-conducting, to inward …

**Summary**, from NCBI Gene [3777](https://www.ncbi.nlm.nih.gov/gene/3777):

> This gene encodes a member of the superfamily of potassium channel proteins that contain two pore-forming P domains. The encoded protein is an outwardly rectifying channel that is sensitive to changes in extracellular pH and is inhibited by extracellular acidification. Also referred to as an acid-sensitive potassium channel, it is activated by the anesthetics halothane and isoflurane. Although three transcripts are detected in northern blots, there is currently no sequence available to confirm …

**Accessions** — [HGNC:6278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6278) · Entrez [3777](https://www.ncbi.nlm.nih.gov/gene/3777) · UniProt [O14649](https://www.uniprot.org/uniprotkb/O14649) · Ensembl [ENSG00000171303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171303)

## Data

Gene col 10087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10087); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10087]; `tensor/DDL_lfc|DDL_z.npy` [10087]; `embed/gene_vectors.npy` [10087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10087 or target_col == 10087). Every well: [[KCNK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
