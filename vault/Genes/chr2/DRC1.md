---
symbol: "DRC1"
type: "gene"
col: 8107
ensembl_id: "ENSG00000157856"
name: "dynein regulatory complex subunit 1"
location: "2p23.3"
module: 37
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# DRC1

*dynein regulatory complex subunit 1* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 16.9× (z +33.1, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.629× (z -3.9, q 0.066, down in 10 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.117×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC13]] (+0.79, fdr 7e-06), [[MFSD2B]] (+0.78, fdr 7e-06), [[IMPA1P1]] (+0.77, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Hesperidin (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **16.9×** | +33.1 | 0e+00 | 29/29 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **15.3×** | +21.7 | 0e+00 | 30/31 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **14.7×** | +21.4 | 0e+00 | 24/26 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **5.21×** | +13.1 | 4e-37 | 10/12 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.37×** | +12.2 | 4e-32 | 39/46 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.62×** | +11.3 | 2e-27 | 23/31 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.02×** | +9.1 | 5e-18 | 30/41 (A498, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.06×** | +8.9 | 4e-17 | 0/1 | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.12×** | +8.8 | 1e-16 | 17/42 (BT-474, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +8.4 | 2e-15 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.48×** | +7.5 | 3e-12 | 23/39 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +7.4 | 8e-12 | 16/29 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.36×** | +7.1 | 6e-11 | 20/44 (A498, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.31×** | +6.9 | 2e-10 | 2/10 (NCI-H460, HOP62) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +6.5 | 3e-09 | 9/16 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +5.1 | 9e-06 | 11/42 (A498, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +5.1 | 1e-05 | 12/41 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.74×** | +4.6 | 2e-04 | 10/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.4 | 3e-04 | 7/43 (A498, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.001 | 13/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.69×** | +4.1 | 0.001 | 10/37 (A498, SW480, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.41×** | +3.8 | 0.003 | 3/13 (NCI-H460, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8107.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (A498 0.117×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (NCI-H460 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.629×** | -3.9 | 0.066 | 10/44 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.12 | 5 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.5× (z +17.5) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.117× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 3.65 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +15.1) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.130× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 5.37 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 1.81 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 3.00 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.0× (z +11.7) | — |
| [[SW480 (line)]] | alt | 1.60 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.2) | — |
| [[C32 (line)]] | wt | 2.62 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 2.27 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 3.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +9.7) | — |
| [[A-172 (line)]] | wt | 1.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 34.2× (z +12.7) | — |
| [[A549 (line)]] | wt | 1.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.9× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 0.922 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.6× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 2.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 46.6× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +8.6) | — |
| [[LoVo (line)]] | wt | 2.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 1.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 1.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 37.0× (z +10.3) | — |
| [[A-427 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.878 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.943 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.818 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC13]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MFSD2B]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.77 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.76 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[WDR49]] | +0.76 | +0.75 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SNX31]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.73 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[CORIN]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[MCF2]] | +0.73 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.72 | +0.79 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DRC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RBM44]] | C | RBM44 activity raises DRC1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 1.36× lower at baseline in the lines without RBM44 | 0.087 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Hesperidin (drug)]] 0.05 µM | C | DRC1's natural level raises the cells' numbers under Hesperidin 0.05 µM (protects the cells) | DRC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.383 over the table, 0.084 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | DRC1's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | DRC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.473 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.0, -16.4); signed map (13.5, 6.3). **Vector** length 61.3, 9.28% of its response variance represented; |z| ≥ 3 in 1,214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +33.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +21.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +21.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.1 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +4.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | dynein regulatory complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,401,920-26,456,711 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16372, FLJ32660, CILD21; previously C2orf39, CCDC164 |
| Gene groups (HGNC) | Dynein regulatory complex |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MC2](https://www.uniprot.org/uniprotkb/Q96MC2) (Dynein regulatory complex protein 1):

> Component of the nexin-dynein regulatory complex (N-DRC) a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes (By similarity). Plays a critical role in the assembly of N-DRC and also stabilizes the assembly of multiple inner dynein arms and radial spokes. Coassembles with DRC2 to form a central scaffold needed for assembly of the N-DRC and its attachment to the outer doublet …

**Summary**, from NCBI Gene [92749](https://www.ncbi.nlm.nih.gov/gene/92749):

> This gene encodes a central component of the nexin-dynein complex (N-DRC), which regulates the assembly of ciliary dynein. Mutations in this gene can cause ciliary dyskinesia. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:24245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24245) · Entrez [92749](https://www.ncbi.nlm.nih.gov/gene/92749) · UniProt [Q96MC2](https://www.uniprot.org/uniprotkb/Q96MC2) · Ensembl [ENSG00000157856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157856)

## Data

Gene col 8107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8107); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8107]; `tensor/DDL_lfc|DDL_z.npy` [8107]; `embed/gene_vectors.npy` [8107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8107 or target_col == 8107). Every well: [[DRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
