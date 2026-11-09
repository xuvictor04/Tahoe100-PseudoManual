---
symbol: "TPD52L2"
type: "gene"
col: 2079
ensembl_id: "ENSG00000101150"
name: "TPD52 like 2"
location: "20q13.33"
module: 2
arm: "+"
pooled_cpm: 64.62
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TPD52L2

*TPD52 like 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.47× (z +6.2, q 4e-07, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.654× (z -9.6, q 5e-19, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.792× (z -5.3, q 2e-05, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YKT6]] (+0.71, fdr 7e-06), [[DPP9]] (+0.70, fdr 7e-06), [[RER1]] (+0.66, fdr 1e-05); moves opposite to [[ZNF608]] (-0.72, fdr 7e-06), [[ZNF827]] (-0.63, fdr 1e-05), [[ARID2]] (-0.62, fdr 7e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HMGN5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +6.2 | 4e-07 | 32/48 (SW480, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +6.0 | 8e-07 | 32/48 (A-427, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +5.1 | 6e-05 | 31/48 (SW480, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 9e-05 | 32/48 (Panc 03.27, A-427, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.001 | 23/49 (NCI-H1573, A-427, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.4 | 0.001 | 24/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +3.5 | 0.043 | 22/47 (LS 180, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.12 | 22/48 (SW480, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.654×** | -9.6 | 5e-19 | 37/47 (A-427, A549, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.586×** | -8.2 | 5e-14 | 39/48 (LoVo, MIA PaCa-2, …) | top dose only | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -5.3 | 2e-05 | 28/48 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -5.1 | 4e-05 | 25/49 (NCI-H2347, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.755×** | -4.3 | 0.002 | 29/47 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.806×** | -3.5 | 0.048 | 19/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.072 | 25/49 (AsPC-1, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -3.3 | 0.072 | 18/48 (HOP62, A498, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.821×** | -3.2 | 0.087 | 16/48 (Panc 03.27, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 51.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -22.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 54.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.32× (z +9.6) | — |
| [[A498 (line)]] | wt | 82.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[CFPAC-1 (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -10.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.302× (z -11.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.329× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 90.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H661 (line)]] | alt | 57.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0961× (z -9.6) |
| [[RKO (line)]] | wt | 76.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW 1271 (line)]] | alt | 63.7 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0673× (z -9.8) |
| [[A-172 (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YKT6]] | +0.71 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DPP9]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[RER1]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CAPN10]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[GOLGA3]] | +0.64 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[SZT2]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SPRYD3]] | +0.63 | +0.74 / +0.39 | both halves | 5e-05 |  |
| [[WDR55]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[INTS11]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[HGS]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.61 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[DPH7]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF608]] | -0.72 | -0.71 / -0.68 | both halves | 7e-06 |  |
| [[ZNF827]] | -0.63 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ARID2]] | -0.62 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[SSH2]] | -0.62 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ATF7IP]] | -0.61 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[POGZ]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PLPP3]] | -0.61 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TET2]] | -0.61 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TGIF2]] | -0.61 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[NIPBL]] | -0.61 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NR2F1]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[SETD2]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN5]] | B | HMGN5 activity lowers TPD52L2's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.39× higher at baseline in the lines without HMGN5 | 0.050 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |
| [[NUAK1]] | B | NUAK1 activity raises TPD52L2's level | lines that do not express NUAK1 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without NUAK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TGFB1, DBN1, CAVIN1; its own permutation p |
| [[PSMB5]] | B | PSMB5 activity lowers TPD52L2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (10.1, -26.5); signed map (-50.0, 2.4). **Vector** length 122, 34.2% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.1 | +4.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.8 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.7 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +3.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.0 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.9 | -9.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -7.8 | -8.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | TPD52 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,865,228-63,891,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D54, hD54, TPD54 |
| Matched by | ensembl_id |

UniProt [O43399](https://www.uniprot.org/uniprotkb/O43399) carries no function annotation.

**Summary**, from NCBI Gene [7165](https://www.ncbi.nlm.nih.gov/gene/7165):

> This gene encodes a member of the tumor protein D52-like family. These proteins are characterized by an N-terminal coiled-coil motif that is used to form homo- and heteromeric complexes with other tumor protein D52-like proteins. Expression of this gene may be a marker for breast cancer and acute lymphoblastic leukemia. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 12. …

**Accessions** — [HGNC:12007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12007) · Entrez [7165](https://www.ncbi.nlm.nih.gov/gene/7165) · UniProt [O43399](https://www.uniprot.org/uniprotkb/O43399) · Ensembl [ENSG00000101150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101150)

## Data

Gene col 2079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2079); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2079]; `tensor/DDL_lfc|DDL_z.npy` [2079]; `embed/gene_vectors.npy` [2079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2079 or target_col == 2079). Every well: [[TPD52L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPD52L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
