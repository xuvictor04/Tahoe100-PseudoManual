---
symbol: "FBLN2"
type: "gene"
col: 8708
ensembl_id: "ENSG00000163520"
name: "fibulin 2"
location: "3p25.1"
module: 100
arm: "+"
pooled_cpm: 3.82
n_lines_expressing: 25
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# FBLN2

*fibulin 2* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.02× (z +13.8, q 2e-40, up in 11 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.606× (z -4.4, q 0.005, down in 5 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0796×, SNU-1 0.190×; ⚠ cell-cycle shift, explains ~45% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.131×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.209×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.379×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN2]] (+0.53, fdr 1e-05), [[TMEFF2]] (+0.52, fdr 3e-05), [[CBFA2T3]] (+0.52, fdr 3e-05); moves opposite to [[TRAPPC13]] (-0.44, fdr 2e-04), [[TCEANC2]] (-0.41, fdr 2e-04), [[WDR53]] (-0.41, fdr 5e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[KLKP1-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.02×** | +13.8 | 2e-40 | 11/19 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.21×** | +12.2 | 1e-31 | 4/5 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.60×** | +11.3 | 3e-27 | 3/6 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.25×** | +9.6 | 1e-19 | 4/5 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +8.2 | 2e-14 | 13/21 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +7.9 | 2e-13 | 10/19 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +6.5 | 7e-09 | 10/21 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +6.2 | 4e-08 | 6/18 (RPMI-7951, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.06×** | +5.2 | 2e-05 | 1/4 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.1 | 2e-05 | 1/8 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.16×** | +4.8 | 7e-05 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.73×** | +4.6 | 2e-04 | 2/3 (NCI-H1792, NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +4.6 | 2e-04 | 6/21 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.01×** | +4.4 | 5e-04 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.2 | 9e-04 | 3/10 (NCI-H2347, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.003 | 3/18 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.54×** | +3.8 | 0.005 | 2/12 (NCI-H1792, HEC-1-A) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.2 | 0.035 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.043 | 0/13 | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.043 | 1/20 (NCI-H2347) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8708.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.0796×, SNU-1 0.190×; ⚠ cell-cycle shift, explains ~45% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.131×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 0.209×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.379×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -4.4 | 0.005 | 5/19 (hTERT-HPNE, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -4.0 | 0.021 | 7/21 (SNU-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.689× | -3.3 | 0.16 | 7/20 (NCI-H661, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.695× | -3.1 | 0.25 | 1/17 (BT-474) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 228 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -17.8) |
| [[A-172 (line)]] | wt | 2.42 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 78.4× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 2.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +11.0) | — |
| [[J82 (line)]] | alt | 1.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0796× (z -11.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.993 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.473 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.862 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN2]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TMEFF2]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CBFA2T3]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[RASSF5]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CRISPLD2]] | +0.50 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[TMCC2]] | +0.49 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[PREX1]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[GFRA1]] | +0.49 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[CLSTN2]] | +0.49 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[RRAD]] | +0.48 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[FSIP1]] | +0.48 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[SLC38A4]] | +0.48 | +0.32 / +0.43 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.44 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[TCEANC2]] | -0.41 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[WDR53]] | -0.41 | -0.23 / -0.42 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLKP1-1]] | B | FBLN2 activity raises KLKP1-1's level | lines that do not express FBLN2 (25) vs lines expressing it (25) | 1.78× lower at baseline in the lines without FBLN2 | 0.053 | ⚠ within organs, on part of the lines; also absent: MME, LINC01411, TLL1 |
| [[LUM]] | C | FBLN2 activity raises LUM's level | lines that do not express FBLN2 (25) vs lines expressing it (25) | 2.53× lower at baseline in the lines without FBLN2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MME, LINC01411, TLL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.398). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.7, 36.8); signed map (32.3, 23.3). **Vector** length 31.8, 5.27% of its response variance represented; |z| ≥ 3 in 476 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +11.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.5 | +1.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.5 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | fibulin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:13,549,125-13,638,422 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fibulins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P98095](https://www.uniprot.org/uniprotkb/P98095) (Fibulin-2):

> Its binding to fibronectin and some other ligands is calcium dependent. May act as an adapter that mediates the interaction between FBN1 and ELN.

**Summary**, from NCBI Gene [2199](https://www.ncbi.nlm.nih.gov/gene/2199):

> This gene encodes an extracellular matrix protein, which belongs to the fibulin family. This protein binds various extracellular ligands and calcium. It may play a role during organ development, in particular, during the differentiation of heart, skeletal and neuronal structures. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3601) · Entrez [2199](https://www.ncbi.nlm.nih.gov/gene/2199) · UniProt [P98095](https://www.uniprot.org/uniprotkb/P98095) · Ensembl [ENSG00000163520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163520)

## Data

Gene col 8708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8708); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8708]; `tensor/DDL_lfc|DDL_z.npy` [8708]; `embed/gene_vectors.npy` [8708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8708 or target_col == 8708). Every well: [[FBLN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBLN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
