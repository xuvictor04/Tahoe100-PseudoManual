---
symbol: "PCSK2"
type: "gene"
col: 4680
ensembl_id: "ENSG00000125851"
name: "proprotein convertase subtilisin/kexin type 2"
location: "20p12.1"
module: 61
arm: "+"
pooled_cpm: 3.67
n_lines_expressing: 23
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PCSK2

*proprotein convertase subtilisin/kexin type 2* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.32× (z +18.6, q 0e+00, up in 11 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC80]] (+0.67, fdr 7e-06), [[SLC35F1]] (+0.65, fdr 7e-06), [[SGCZ]] (+0.65, fdr 7e-06); moves opposite to [[WHAMMP1]] (-0.51, fdr 3e-05), [[WHAMMP2]] (-0.48, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[DACH2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.32×** | +18.6 | 0e+00 | 11/11 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.85×** | +12.6 | 9e-34 | 7/10 (A549, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.40×** | +11.1 | 2e-26 | 3/3 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.66×** | +11.0 | 5e-26 | 1/1 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.92×** | +9.7 | 3e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +8.1 | 8e-14 | 13/16 (NCI-H460, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.69×** | +6.5 | 5e-09 | 7/11 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +5.3 | 7e-06 | 10/14 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.7 | 2e-04 | 1/5 (NCI-H460) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +4.6 | 3e-04 | 13/16 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.3 | 7e-04 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +4.3 | 7e-04 | 10/15 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +4.3 | 8e-04 | 3/14 (SHP-77, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +4.2 | 0.001 | 1/4 (NCI-H460) | top dose only | cell-cycle shift (explains ~24% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.43×** | +4.2 | 0.001 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +4.1 | 0.001 | 3/14 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.003 | 2/12 (A549, HOP62) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +3.6 | 0.009 | 2/5 (HS-578T, NCI-H460) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.010 | 4/11 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.033 | 2/11 (C32, NCI-H460) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.043 | 3/16 (A549, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.84×** | +2.9 | 0.089 | 0/6 | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.616× | -3.2 | 0.41 | 1/13 (HS-578T) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.612× | -3.1 | 0.41 | 3/12 (C32, NCI-H460, …) | top dose only | position effect removed |
| [[Gallic acid (drug)]] 0.05 µM |  | 0.634× | -3.0 | 0.41 | 1/11 (BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.34 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 111× (z +19.9) | — |
| [[A549 (line)]] | wt | 1.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 215× (z +13.8) | — |
| [[C32 (line)]] | wt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.6× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 0.960 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 3.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +11.4) | — |
| [[A-172 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.935 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.720 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.897 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.753 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.955 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.982 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.838 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC80]] | +0.67 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.65 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CHST8]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ADAMTSL1]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SH3GL2]] | +0.63 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[FMN2]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[RALYL]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[HS6ST3]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.60 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[PDLIM3]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[STXBP5L]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMMP1]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[WHAMMP2]] | -0.48 | -0.45 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCSK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SCG3]] | C | SCG3 activity raises PCSK2's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.23× lower at baseline in the lines without SCG3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[LINC01287]] | C | LINC01287 activity raises PCSK2's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.24× lower at baseline in the lines without LINC01287 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DACH2]] | B | PCSK2 activity raises DACH2's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 1.68× lower at baseline in the lines without PCSK2 | 0.024 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |
| [[LDB2]] | B | PCSK2 activity raises LDB2's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without PCSK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |
| [[PLCL1]] | B | PCSK2 activity raises PLCL1's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without PCSK2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |
| [[SLC35F1]] | B | PCSK2 activity raises SLC35F1's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without PCSK2 | 0.060 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 32.7); signed map (33.5, 25.4). **Vector** length 30.6, 7.30% of its response variance represented; |z| ≥ 3 in 339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +18.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.7 | +0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.1 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | proprotein convertase subtilisin/kexin type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:17,226,107-17,484,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC2, SPC2; previously NEC2 |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 6 pathways, smallest: Insulin processing; Peptide hormone metabolism; HCMV Late Events |
| Matched by | ensembl_id |

**Function**, from UniProt [P16519](https://www.uniprot.org/uniprotkb/P16519) (Neuroendocrine convertase 2):

> Serine endopeptidase which is involved in the processing of hormone and other protein precursors at sites comprised of pairs of basic amino acid residues. Responsible for the release of glucagon from proglucagon in pancreatic A cells. Mediates the release of insulin from pro-insulin.

**Summary**, from NCBI Gene [5126](https://www.ncbi.nlm.nih.gov/gene/5126):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. The protein undergoes an initial autocatalytic processing event and interacts with a neuroendocrine secretory protein in the ER, exits the ER and sorts to secretory granules, where it is cleaved and catalytically activated during intracellular transport. The encoded …

**Accessions** — [HGNC:8744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8744) · Entrez [5126](https://www.ncbi.nlm.nih.gov/gene/5126) · UniProt [P16519](https://www.uniprot.org/uniprotkb/P16519) · Ensembl [ENSG00000125851](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125851)

## Data

Gene col 4680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4680); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4680]; `tensor/DDL_lfc|DDL_z.npy` [4680]; `embed/gene_vectors.npy` [4680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4680 or target_col == 4680). Every well: [[PCSK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCSK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
