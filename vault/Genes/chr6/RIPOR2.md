---
symbol: "RIPOR2"
type: "gene"
col: 3308
ensembl_id: "ENSG00000111913"
name: "RHO family interacting cell polarization regulator 2"
location: "6p22.3"
module: 98
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 41
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# RIPOR2

*RHO family interacting cell polarization regulator 2* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.94× (z +13.8, q 1e-40, up in 18 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Hs 766T 0.0739×, SNU-1 0.161×, A-172 0.129×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.194×, Hs 766T 0.154×); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.0481×; ⚠ cell-cycle shift, explains ~74% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.125×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA10]] (+0.70, fdr 7e-06), [[RTN4RL1]] (+0.69, fdr 7e-06), [[ATOH8]] (+0.68, fdr 1e-05); moves opposite to [[ADAMTS16]] (-0.52, fdr 3e-05), [[LIF]] (-0.52, fdr 1e-05), [[WNT7B]] (-0.52, fdr 2e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); 6 go from it, the strongest it → [[FRMD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +13.8 | 1e-40 | 18/27 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.38×** | +13.3 | 3e-38 | 10/15 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +10.9 | 2e-25 | 2/4 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.63×** | +9.9 | 9e-21 | 4/6 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.77×** | +9.2 | 4e-18 | 20/32 (SHP-77, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +7.2 | 5e-11 | 15/36 (J82, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.13×** | +6.8 | 7e-10 | 17/32 (SHP-77, H4, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.93×** | +5.9 | 2e-07 | 14/32 (SHP-77, SW 900, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.87×** | +5.6 | 1e-06 | 15/33 (SHP-77, SW 900, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.86×** | +5.6 | 1e-06 | 13/33 (SHP-77, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.54×** | +5.5 | 2e-06 | 15/35 (H4, SHP-77, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.1 | 1e-05 | 7/27 (LS 180, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.95×** | +5.1 | 2e-05 | 13/26 (SHP-77, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.75×** | +5.1 | 2e-05 | 11/34 (SHP-77, Hs 766T, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.9 | 3e-05 | 3/15 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.70×** | +4.8 | 6e-05 | 15/34 (SHP-77, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.4 | 4e-04 | 8/32 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.0 | 0.002 | 7/34 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.84×** | +3.9 | 0.003 | 2/14 (HEC-1-A, SW 900) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3308.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (Hs 766T 0.0739×, SNU-1 0.161×, A-172 0.129×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-1 0.194×, Hs 766T 0.154×); [[Panobinostat (drug)]] 5 µM in 1 line (SNU-1 0.0481×; ⚠ cell-cycle shift, explains ~74% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.125×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.642× | -3.6 | 0.15 | 11/35 (SNU-1, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 119 | 0 | 21 (14 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0481× (z -18.8) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.9) |
| [[SHP-77 (line)]] | alt | 6.57 | 9 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 35.0× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -18.0) |
| [[H4 (line)]] | wt | 3.45 | 4 | 0 | [[Triamcinolone (drug)]] 5 µM 30.6× (z +9.6) | — |
| [[A-172 (line)]] | wt | 6.53 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0399× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 2.65 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 10.2× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 9.07 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 14.0× (z +8.6) | — |
| [[A-427 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA10]] | +0.70 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[RTN4RL1]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ATOH8]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[ADGRG2]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[KLF9]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TMTC1]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[MAOA]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[KCNB1]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[LINC00607]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[VSTM2L]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[STXBP5-AS1]] | +0.61 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[SAMSN1]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS16]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[LIF]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[WNT7B]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SYNJ2]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[IGFN1]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ANXA10]] | -0.47 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CRLF2]] | -0.46 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[LINC00973]] | -0.46 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[NPTX1]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GPR39]] | -0.46 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[IGFBP3]] | -0.45 | -0.48 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises RIPOR2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD3]] | B | RIPOR2 activity raises FRMD3's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 2.28× lower at baseline in the lines without RIPOR2 | 0.026 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[SSBP2]] | B | RIPOR2 activity raises SSBP2's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 2.20× lower at baseline in the lines without RIPOR2 | 0.038 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[TMTC1]] | B | RIPOR2 activity raises TMTC1's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 3.89× lower at baseline in the lines without RIPOR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[B4GALT1]] | B | RIPOR2 activity raises B4GALT1's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without RIPOR2 | 0.081 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[TLR2]] | B | RIPOR2 activity raises TLR2's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 2.38× lower at baseline in the lines without RIPOR2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |
| [[SLC1A3]] | B | RIPOR2 activity raises SLC1A3's level | lines that do not express RIPOR2 (9) vs lines expressing it (41) | 3.01× lower at baseline in the lines without RIPOR2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GNA14, EPHA1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 16.8); signed map (18.7, 31.3). **Vector** length 64.9, 11.5% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +5.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.1 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +9.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.0 | +5.6 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.5 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RHO family interacting cell polarization regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:24,804,282-25,042,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0386, DIFF48, MYONAP; previously C6orf32, FAM65B |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4F9](https://www.uniprot.org/uniprotkb/Q9Y4F9) (Rho family-interacting cell polarization regulator 2):

> Acts as an inhibitor of the small GTPase RHOA and plays several roles in the regulation of myoblast and hair cell differentiation, lymphocyte T proliferation and neutrophil polarization. Inhibits chemokine-induced T lymphocyte responses, such as cell adhesion, polarization and migration. Involved also in the regulation of neutrophil polarization, chemotaxis and adhesion (By similarity). Required for normal development of inner and outer hair cell stereocilia within the cochlea of the inner ear …

**Summary**, from NCBI Gene [9750](https://www.ncbi.nlm.nih.gov/gene/9750):

> This gene encodes an atypical inhibitor of the small G protein RhoA. Inhibition of RhoA activity by the encoded protein mediates myoblast fusion and polarization of T cells and neutrophils. The encoded protein is a component of hair cell stereocilia that is essential for hearing. A splice site mutation in this gene results in hearing loss in human patients. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:13872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13872) · Entrez [9750](https://www.ncbi.nlm.nih.gov/gene/9750) · UniProt [Q9Y4F9](https://www.uniprot.org/uniprotkb/Q9Y4F9) · Ensembl [ENSG00000111913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111913)

## Data

Gene col 3308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3308); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3308]; `tensor/DDL_lfc|DDL_z.npy` [3308]; `embed/gene_vectors.npy` [3308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3308 or target_col == 3308). Every well: [[RIPOR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIPOR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
