---
symbol: "PPP1R32"
type: "gene"
col: 8486
ensembl_id: "ENSG00000162148"
name: "stabilizer of axonemal microtubules 4"
location: "11q12.2"
module: 37
arm: "+"
pooled_cpm: 4.48
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PPP1R32

*stabilizer of axonemal microtubules 4* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.46× (z +10.9, q 1e-24, up in 28 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.313× (z -13.5, q 1e-38, down in 33 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYPK]] (+0.77, fdr 7e-06), [[DRD4]] (+0.73, fdr 7e-06), [[CLEC4A]] (+0.69, fdr 7e-06); moves opposite to [[ZNF252P-1]] (-0.63, fdr 7e-06), [[AASDHPPT]] (-0.61, fdr 1e-05), [[SLX4IP]] (-0.60, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SYCP2L]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.46×** | +10.9 | 1e-24 | 28/42 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.3 | 0.004 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.004 | 9/37 (A498, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.008 | 8/36 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.030 | 4/44 (HEC-1-A, Hs 766T, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.313×** | -13.5 | 1e-38 | 33/41 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.435×** | -10.1 | 2e-21 | 32/45 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.551×** | -6.9 | 8e-10 | 19/41 (PANC-1, LoVo, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.726×** | -5.5 | 5e-06 | 22/36 (A498, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -5.5 | 5e-06 | 19/39 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.2 | 0.003 | 19/39 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.715×** | -4.1 | 0.004 | 12/46 (A-427, BT-474, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.722×** | -3.9 | 0.006 | 13/45 (SW 1271, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.732×** | -3.8 | 0.010 | 14/43 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.746×** | -3.6 | 0.022 | 8/46 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.758×** | -3.4 | 0.040 | 10/46 (SW 1271, CHP-212, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.764×** | -3.3 | 0.052 | 13/45 (KATO III, AN3 CA, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.766×** | -3.2 | 0.053 | 7/46 (H4, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 8.50 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -10.4) |
| [[A-172 (line)]] | wt | 4.78 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0689× (z -9.7) |
| [[A498 (line)]] | wt | 5.99 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.9) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A549 (line)]] | wt | 4.59 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0744× (z -9.1) |
| [[HOP62 (line)]] | alt | 4.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0974× (z -9.7) |
| [[HT-29 (line)]] | alt | 6.28 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -8.7) ⚠ cell-cycle shift, explains ~56% of this change |
| [[J82 (line)]] | alt | 5.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0970× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 5.57 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0955× (z -10.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 5.24 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0740× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 5.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0481× (z -9.5) |
| [[A-427 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYPK]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[DRD4]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[CLEC4A]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[LINC02935]] | +0.68 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[WDR49]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[TNXB]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[BNIPL]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.66 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GET1-SH3BGR]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[GRK3]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF252P-1]] | -0.63 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[AASDHPPT]] | -0.61 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.59 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[PABIR1]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.59 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[CEP41]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[RIF1]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CSTF2T]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[EPC2]] | -0.57 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[CENPS]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2L]] | B | SYCP2L activity raises PPP1R32's level | lines that do not express SYCP2L (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without SYCP2L | 0.063 | ⚠ within organs, on part of the lines; also absent: POGLUT2, BIVM, SPATA17 |
| [[PPP1R9A]] | B | PPP1R9A activity lowers PPP1R32's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.21× higher at baseline in the lines without PPP1R9A | 0.091 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[RBM44]] | C | RBM44 activity raises PPP1R32's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 1.84× lower at baseline in the lines without RBM44 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; its own permutation p |
| [[LINC02656]] | C | LINC02656 activity raises PPP1R32's level | lines that do not express LINC02656 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without LINC02656 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, MAP3K8, ENSG00000250842; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | PPP1R32's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | PPP1R32's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.018 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, -20.5); signed map (8.3, 6.0). **Vector** length 66.8, 10.3% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.4 | +1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +4.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +0.9 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.8 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -13.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -3.5 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | stabilizer of axonemal microtubules 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,481,120-61,490,931 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IIIG9, FLJ32771; previously C11orf66, PPP1R32 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Stabilizer of axonemal microtubules family |
| Matched by | ensembl_id |

UniProt [Q7Z5V6](https://www.uniprot.org/uniprotkb/Q7Z5V6) carries no function annotation.

**Summary**, from NCBI Gene [220004](https://www.ncbi.nlm.nih.gov/gene/220004):

> Enables phosphatase binding activity. Predicted to be involved in flagellated sperm motility. Located in ciliary basal body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28869) · Entrez [220004](https://www.ncbi.nlm.nih.gov/gene/220004) · UniProt [Q7Z5V6](https://www.uniprot.org/uniprotkb/Q7Z5V6) · Ensembl [ENSG00000162148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162148)

## Data

Gene col 8486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8486); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8486]; `tensor/DDL_lfc|DDL_z.npy` [8486]; `embed/gene_vectors.npy` [8486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8486 or target_col == 8486). Every well: [[PPP1R32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
