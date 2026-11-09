---
symbol: "GUCY1A2"
type: "gene"
col: 7621
ensembl_id: "ENSG00000152402"
name: "guanylate cyclase 1 soluble subunit alpha 2"
location: "11q22.3"
module: 26
arm: "+"
pooled_cpm: 4.65
n_lines_expressing: 42
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# GUCY1A2

*guanylate cyclase 1 soluble subunit alpha 2* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.28× (z +18.8, q 0e+00, up in 25 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.686× (z -4.9, q 6e-04, down in 11 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 5 µM in 1 line (LOX-IMVI 0.0610×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.77, fdr 7e-06), [[SYNPO2]] (+0.75, fdr 7e-06), [[COL21A1]] (+0.73, fdr 7e-06); moves opposite to [[BRAT1]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[DLG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.28×** | +18.8 | 0e+00 | 25/29 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.94×** | +17.7 | 0e+00 | 25/28 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.11×** | +16.5 | 0e+00 | 30/34 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.89×** | +14.0 | 4e-42 | 2/5 (NCI-H2030, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.49×** | +13.7 | 7e-41 | 13/14 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.16×** | +12.0 | 2e-31 | 5/7 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.91×** | +9.8 | 1e-20 | 19/29 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +8.0 | 8e-14 | 22/37 (HS-578T, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.35×** | +7.5 | 4e-12 | 21/34 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.77×** | +7.4 | 8e-12 | 16/37 (HEC-1-A, J82, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +6.9 | 3e-10 | 14/38 (LOX-IMVI, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +6.0 | 9e-08 | 16/35 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +5.8 | 2e-07 | 10/28 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.3 | 5e-06 | 8/26 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +5.1 | 1e-05 | 15/33 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +4.8 | 6e-05 | 12/37 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.62×** | +4.2 | 8e-04 | 12/32 (H4, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.1 | 0.001 | 4/34 (C-33 A, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7621.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Naproxen (drug)]] 5 µM in 1 line (LOX-IMVI 0.0610×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.686×** | -4.9 | 6e-04 | 11/38 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.683× | -3.4 | 0.22 | 6/37 (CHP-212, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Rosiglitazone (drug)]] 0.05 µM |  | 0.696× | -3.1 | 0.41 | 3/36 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 1.92 | 2 | 0 | [[Auranofin (drug)]] 5 µM 30.7× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.84× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.69× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 2.88 | 1 | 0 | [[Auranofin (drug)]] 5 µM 27.6× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 3.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 4.55 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0610× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 4.24 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.4× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 2.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +9.6) | — |
| [[SW480 (line)]] | alt | 1.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.4) | — |
| [[A-172 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.77 | +0.75 / +0.70 | both halves | 7e-06 | pathway: Muscle contraction |
| [[SYNPO2]] | +0.75 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.71 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[CHODL]] | +0.71 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[LINC01933]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.70 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[LINC02889]] | +0.70 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.70 | +0.73 / +0.38 | both halves | 6e-05 |  |
| [[LINC01208]] | +0.69 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[LRRC4C]] | +0.69 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RFTN2]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.59 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GUCY1A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLG2]] | B | GUCY1A2 activity raises DLG2's level | lines that do not express GUCY1A2 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without GUCY1A2 | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF559, ENSG00000229195, LINC02456; maybe low, not absent |
| [[ATP9A]] | B | GUCY1A2 activity lowers ATP9A's level | lines that do not express GUCY1A2 (8) vs lines expressing it (42) | 1.33× higher at baseline in the lines without GUCY1A2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF559, ENSG00000229195, LINC02456; maybe low, not absent |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (25.4, 25.1); signed map (37.4, 15.0). **Vector** length 58.1, 9.63% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +16.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +17.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | guanylate cyclase 1 soluble subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:106,674,019-107,018,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GC-SA2; previously GUC1A2 |
| Gene groups (HGNC) | Soluble guanylate cyclases |
| Reactome | 5 pathways, smallest: Nitric oxide stimulates guanylate cyclase; Smooth Muscle Contraction; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P33402](https://www.uniprot.org/uniprotkb/P33402) (Guanylate cyclase soluble subunit alpha-2):

> Alpha subunit of soluble guanylate cyclase (sGC), a central enzyme in nitric oxide (NO) signaling. Functions as the main intracellular receptor for NO. Upon NO binding, catalyzes the conversion of GTP to cyclic GMP (cGMP) and thereby transducing NO signal into a ubiquitous intracellular second messenger.; [Isoform 2]: Acts as a negative regulator of guanylyl cyclase activity as it forms non-functional heterodimers with the beta subunit.

**Summary**, from NCBI Gene [2977](https://www.ncbi.nlm.nih.gov/gene/2977):

> Soluble guanylate cyclases are heterodimeric proteins that catalyze the conversion of GTP to 3',5'-cyclic GMP and pyrophosphate. The protein encoded by this gene is an alpha subunit of this complex and it interacts with a beta subunit to form the guanylate cyclase enzyme, which is activated by nitric oxide. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:4684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4684) · Entrez [2977](https://www.ncbi.nlm.nih.gov/gene/2977) · UniProt [P33402](https://www.uniprot.org/uniprotkb/P33402) · Ensembl [ENSG00000152402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152402)

## Data

Gene col 7621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7621); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7621]; `tensor/DDL_lfc|DDL_z.npy` [7621]; `embed/gene_vectors.npy` [7621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7621 or target_col == 7621). Every well: [[GUCY1A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUCY1A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
