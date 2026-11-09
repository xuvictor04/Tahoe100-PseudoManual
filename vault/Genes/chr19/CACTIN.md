---
symbol: "CACTIN"
type: "gene"
col: 2579
ensembl_id: "ENSG00000105298"
name: "cactin, spliceosome C complex subunit"
location: "19p13.3"
module: 138
arm: "+"
pooled_cpm: 7.58
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# CACTIN

*cactin, spliceosome C complex subunit* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +20.0, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.689× (z -4.4, q 0.007, down in 21 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.775× (z -4.2, q 0.007, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMWD]] (+0.73, fdr 7e-06), [[ANAPC2]] (+0.73, fdr 7e-06), [[CD2BP2]] (+0.71, fdr 7e-06); moves opposite to [[SPOPL]] (-0.52, fdr 3e-05), [[FRG1CP]] (-0.50, fdr 2e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.36×** | +20.0 | 0e+00 | 42/44 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.15×** | +13.4 | 2e-38 | 45/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +11.5 | 2e-28 | 40/44 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +11.5 | 2e-28 | 45/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.38×** | +10.1 | 5e-22 | 39/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.23×** | +9.3 | 1e-18 | 42/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.56×** | +8.7 | 3e-16 | 32/43 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +7.9 | 3e-13 | 31/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.87×** | +7.3 | 2e-11 | 27/44 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +6.8 | 8e-10 | 26/46 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +6.5 | 3e-09 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.62×** | +5.4 | 3e-06 | 20/44 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +5.2 | 9e-06 | 20/47 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +5.1 | 1e-05 | 17/47 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.1 | 1e-05 | 15/48 (BT-474, J82, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +4.7 | 1e-04 | 19/47 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 3e-04 | 13/47 (A-427, PANC-1, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.006 | 13/47 (SW480, BT-474, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.006 | 7/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.689×** | -4.4 | 0.007 | 21/47 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -4.2 | 0.007 | 16/48 (SW48, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.740×** | -3.4 | 0.098 | 9/44 (RKO, NCI-H2030, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -3.4 | 0.098 | 9/46 (COLO 205, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled); position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.759× | -3.2 | 0.14 | 9/47 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 6.12 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +15.3) | — |
| [[A-172 (line)]] | wt | 8.35 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +9.4) | [[Orlistat (drug)]] 0.05 µM 0.0870× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 6.54 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +10.2) | [[Finasteride (drug)]] 0.05 µM 0.121× (z -9.7) |
| [[SW480 (line)]] | alt | 9.63 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.30× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 9.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 5.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 5.35 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0702× (z -10.2) |
| [[J82 (line)]] | alt | 7.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 7.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 9.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 6.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +9.6) | — |
| [[A-427 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMWD]] | +0.73 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[ANAPC2]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CD2BP2]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[KMT2B]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FBRS]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TEPSIN]] | +0.69 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.65 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[TAOK2]] | +0.65 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[USP19]] | +0.65 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[REXO1]] | +0.64 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[ZNF574]] | +0.63 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[BRD9]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOPL]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[FRG1CP]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CACTIN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.2, -22.9); signed map (1.9, -8.8). **Vector** length 58.5, 8.54% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.3 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +20.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.1 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.2 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.5 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.3 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +0.7 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.3 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cactin, spliceosome C complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,610,645-3,626,815 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-24, fSAPc; previously C19orf29 |
| Gene groups (HGNC) | Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUQ7](https://www.uniprot.org/uniprotkb/Q8WUQ7) (Splicing factor Cactin):

> Plays a role in pre-mRNA splicing by facilitating excision of a subset of introns. Required for the splicing of CDCA5/Sororin, a regulator of sister chromatid cohesion. Involved in the regulation of innate immune response. Acts as a negative regulator of Toll-like receptor, interferon-regulatory factor (IRF) and canonical NF-kappa-B signaling pathways. Contributes to the regulation of transcriptional activation of NF-kappa-B target genes in response to endogenous pro-inflammatory stimuli.

**Summary**, from NCBI Gene [58509](https://www.ncbi.nlm.nih.gov/gene/58509):

> Enables RNA binding activity. Involved in several processes, including cellular response to cytokine stimulus; negative regulation of cytokine production; and negative regulation of signal transduction. Located in nuclear speck. Part of catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29938) · Entrez [58509](https://www.ncbi.nlm.nih.gov/gene/58509) · UniProt [Q8WUQ7](https://www.uniprot.org/uniprotkb/Q8WUQ7) · Ensembl [ENSG00000105298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105298)

## Data

Gene col 2579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2579); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2579]; `tensor/DDL_lfc|DDL_z.npy` [2579]; `embed/gene_vectors.npy` [2579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2579 or target_col == 2579). Every well: [[CACTIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACTIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
