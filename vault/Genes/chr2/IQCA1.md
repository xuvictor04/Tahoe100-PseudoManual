---
symbol: "IQCA1"
type: "gene"
col: 5297
ensembl_id: "ENSG00000132321"
name: "dynein regulatory complex subunit 11"
location: "2q37.2-q37.3"
module: 13
arm: "+"
pooled_cpm: 3.72
n_lines_expressing: 19
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# IQCA1

*dynein regulatory complex subunit 11* — 2q37.2-q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.00× (z +16.6, q 0e+00, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.75× (z +16.5, q 0e+00, up in 5 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Clopidogrel (drug)]] 0.05 µM: 0.645× (z -3.9, q 0.048, down in 2 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.175×, NCI-H1792 0.163×, HOP62 0.184×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.103×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1792 0.194×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.387×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGTR1]] (+0.64, fdr 1e-05), [[ADAMTS9-AS2]] (+0.62, fdr 1e-05), [[SPOCD1]] (+0.55, fdr 2e-05); moves opposite to [[LINC02099]] (-0.50, fdr 5e-05), [[BMP10]] (-0.46, fdr 1e-04, ⚠ BMP10 in the vector space only through flagged drug-doses).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NAV1]] → it (grade C ⚠); 4 go from it, the strongest it → [[ZNF404]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.00×** | +16.6 | 0e+00 | 2/6 (MIA PaCa-2, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.75×** | +16.5 | 0e+00 | 5/11 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.17×** | +12.6 | 3e-34 | 2/6 (MIA PaCa-2, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +8.9 | 5e-17 | 1/6 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +7.0 | 2e-10 | 1/12 (MIA PaCa-2) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.15×** | +6.7 | 1e-09 | 4/14 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.0 | 4e-05 | 2/9 (MIA PaCa-2, NCI-H1573) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.6 | 3e-04 | 1/11 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.002 | 2/12 (MIA PaCa-2, SNU-423) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.0 | 0.003 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.85×** | +3.9 | 0.005 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.9 | 0.005 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.011 | 0/8 | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.78×** | +3.6 | 0.011 | 0/5 | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.011 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.74×** | +3.5 | 0.017 | 1/9 (J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.41×** | +3.0 | 0.071 | 2/14 (SNU-423, SHP-77) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5297.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (CFPAC-1 0.175×, NCI-H1792 0.163×, HOP62 0.184×); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.103×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1792 0.194×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.387×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.645×** | -3.9 | 0.048 | 2/15 (J82, H4) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -3.8 | 0.048 | 5/14 (NCI-H1792, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (drug)]] 0.5 µM |  | 0.686× | -3.4 | 0.13 | 0/14 | inconsistent across doses |  |
| [[Relugolix (drug)]] 0.5 µM |  | 0.691× | -3.3 | 0.13 | 3/14 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.695× | -3.2 | 0.13 | 3/14 (MIA PaCa-2, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +13.9) | [[AZD2858 (drug)]] 0.5 µM 0.117× (z -8.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 34.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -14.9) |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.7) |
| [[HOP62 (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.9) |
| [[A-172 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.987 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.577 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGTR1]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS9-AS2]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SPOCD1]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[NLRP1]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[OR9Q1]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ZNF334]] | +0.53 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ZNF439]] | +0.52 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[HTRA3]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[STAC]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[ITGB3]] | +0.50 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[ADAM12]] | +0.50 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[KCNK3]] | +0.49 | +0.46 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02099]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[BMP10]] ⚠ | -0.46 | -0.44 / -0.33 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV1]] | C | NAV1 activity raises IQCA1's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without NAV1 | 0.052 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF404]] | B | IQCA1 activity strengthens ZNF404's drug response | lines that do not express IQCA1 (20) vs lines expressing it (14) | the lines without IQCA1 respond 0.59× as strongly (z diff +2.16); strongest at Dinaciclib 0.5 µM: 0.50x vs 0.21x (z diff +4.3) | 0.079 | ⚠ within organs, on part of the lines; also absent: NOL4, KCTD8, MAP6; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZNF439]] | B | IQCA1 activity raises ZNF439's level | lines that do not express IQCA1 (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without IQCA1 | 0.085 | ⚠ within organs, on part of the lines; also absent: NOL4, KCTD8, MAP6; maybe low, not absent |
| [[ADGRE2]] | C | IQCA1 activity raises ADGRE2's level | lines that do not express IQCA1 (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without IQCA1 | 0.029 | ⚠ within organs, on part of the lines; also absent: NOL4, KCTD8, MAP6; maybe low, not absent; co-absent with the target |
| [[KCNK3]] | C | IQCA1 activity raises KCNK3's level | lines that do not express IQCA1 (31) vs lines expressing it (19) | 1.76× lower at baseline in the lines without IQCA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: NOL4, KCTD8, MAP6; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.1, 23.6); signed map (30.9, 48.7). **Vector** length 28.7, 6.08% of its response variance represented; |z| ≥ 3 in 332 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -0.9 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.8 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein regulatory complex subunit 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.2-q37.3 — chr2:236,324,147-236,507,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22527; previously IQCA |
| Gene groups (HGNC) | AAA ATPases; Dynein regulatory complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XH1](https://www.uniprot.org/uniprotkb/Q86XH1) (Dynein regulatory complex subunit 11):

> Component of the nexin-dynein regulatory complex (N-DRC), a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes.

**Summary**, from NCBI Gene [79781](https://www.ncbi.nlm.nih.gov/gene/79781):

> The protein encoded by this gene is a member of the ATPases Associated with diverse cellular Activities (AAA) superfamily. Members of this superfamily, found in all organisms, participate in a large number of cellular processes and contain the ATPase module consisting of an alpha-beta-alpha core domain and the Walker A and B motifs of the P-loop NTPases. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:26195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26195) · Entrez [79781](https://www.ncbi.nlm.nih.gov/gene/79781) · UniProt [Q86XH1](https://www.uniprot.org/uniprotkb/Q86XH1) · Ensembl [ENSG00000132321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132321)

## Data

Gene col 5297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5297); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5297]; `tensor/DDL_lfc|DDL_z.npy` [5297]; `embed/gene_vectors.npy` [5297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5297 or target_col == 5297). Every well: [[IQCA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
