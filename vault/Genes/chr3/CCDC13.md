---
symbol: "CCDC13"
type: "gene"
col: 14410
ensembl_id: "ENSG00000244607"
name: "coiled-coil domain containing 13"
location: "3p22.1"
module: 37
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 47
n_dd_down: 1
n_dd_up_clean: 37
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CCDC13

*coiled-coil domain containing 13* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.96× (z +27.5, q 0e+00, up in 26 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Sodium Salicylate (drug)]] 5 µM: 0.741× (z -4.0, q 0.038, down in 8 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRC1]] (+0.79, fdr 7e-06), [[DCAF4L1]] (+0.77, fdr 7e-06), [[CMYA5]] (+0.73, fdr 7e-06); moves opposite to [[ZFAND4]] (-0.57, fdr 4e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[BAY1125976 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.96×** | +27.5 | 0e+00 | 26/27 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.95×** | +21.2 | 0e+00 | 30/32 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.61×** | +15.6 | 0e+00 | 15/19 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.55×** | +13.7 | 2e-40 | 25/31 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.81×** | +12.5 | 6e-34 | 24/28 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.56×** | +11.9 | 9e-31 | 39/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +11.5 | 9e-29 | 14/19 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.31×** | +11.1 | 1e-26 | 15/44 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.36×** | +10.9 | 5e-26 | 6/11 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.90×** | +10.0 | 1e-21 | 32/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.84×** | +9.8 | 7e-21 | 25/35 (SW480, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.83×** | +9.8 | 8e-21 | 33/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.79×** | +9.3 | 9e-19 | 0/0 | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.52×** | +8.6 | 2e-16 | 20/39 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.57×** | +8.5 | 6e-16 | 18/36 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.29×** | +7.7 | 3e-13 | 24/43 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.96×** | +6.3 | 8e-09 | 15/41 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +5.9 | 1e-07 | 18/44 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +5.6 | 5e-07 | 14/41 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.78×** | +5.4 | 2e-06 | 8/35 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.741×** | -4.0 | 0.038 | 8/44 (SK-MEL-2, LoVo, …) | rises with dose | position effect removed |
| [[Canagliflozin (drug)]] 5 µM |  | 0.715× | -3.0 | 0.59 | 5/26 (BT-474, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.81 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.9× (z +15.2) | — |
| [[NCI-H460 (line)]] | wt | 3.33 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 6.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +8.7) | — |
| [[A498 (line)]] | wt | 1.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 0.917 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.0× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 3.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.23× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 1.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 5.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.08× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 1.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +9.1) | — |
| [[SW48 (line)]] | wt | 4.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +8.5) | — |
| [[SW480 (line)]] | alt | 2.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +12.6) | — |
| [[A-172 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.606 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.644 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.848 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRC1]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[DCAF4L1]] | +0.77 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[CMYA5]] | +0.73 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.73 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[MCF2]] | +0.71 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[LINC02955]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[LINC02763]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[OVGP1]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[COLEC11]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SNX31]] | +0.69 | +0.73 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND4]] | -0.57 | -0.41 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST8SIA5]] | B | ST8SIA5 activity raises CCDC13's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without ST8SIA5 | 0.078 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[BAY1125976 (drug)]] 0.5 µM | C | CCDC13's natural level lowers the cells' numbers under BAY1125976 0.5 µM (makes them more sensitive) | CCDC13's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.033 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM | C | CCDC13's natural level lowers the cells' numbers under Sivelestat (sodium tetrahydrate) 0.5 µM (makes them more sensitive) | CCDC13's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.051 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, -15.5); signed map (13.7, 4.5). **Vector** length 52.5, 6.67% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +27.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.5 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +3.4 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.2 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +9.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.8 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.5 | +6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,705,756-42,773,253 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25467 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYE1](https://www.uniprot.org/uniprotkb/Q8IYE1) (Coiled-coil domain-containing protein 13):

> Required for primary cilia formation and promotes the localization of the ciliopathy protein BBS4 to both centriolar satellites and cilia.

**Summary**, from NCBI Gene [152206](https://www.ncbi.nlm.nih.gov/gene/152206):

> Predicted to enable microtubule binding activity. Acts upstream of or within DNA damage response; cytoplasmic microtubule organization; and non-motile cilium assembly. Located in centriolar satellite. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26358) · Entrez [152206](https://www.ncbi.nlm.nih.gov/gene/152206) · UniProt [Q8IYE1](https://www.uniprot.org/uniprotkb/Q8IYE1) · Ensembl [ENSG00000244607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244607)

## Data

Gene col 14410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14410); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14410]; `tensor/DDL_lfc|DDL_z.npy` [14410]; `embed/gene_vectors.npy` [14410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14410 or target_col == 14410). Every well: [[CCDC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
