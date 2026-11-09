---
symbol: "MCOLN1"
type: "gene"
col: 1635
ensembl_id: "ENSG00000090674"
name: "mucolipin TRP cation channel 1"
location: "19p13.2"
module: 122
arm: "+"
pooled_cpm: 4.49
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 30
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# MCOLN1

*mucolipin TRP cation channel 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.75× (z +24.8, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.760× (z -5.2, q 9e-05, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[EX229 (drug)]] 0.05 µM in 1 line (HOP62 0.0639×); [[ETC-206 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0717×); [[Resveratrol (drug)]] 0.5 µM in 1 line (C32 0.0746×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPNS1]] (+0.69, fdr 1e-05), [[CTNS]] (+0.69, fdr 7e-06), [[GET3]] (+0.67, fdr 1e-05); moves opposite to [[ZNF30]] (-0.45, fdr 3e-04), [[PCNX2]] (-0.42, fdr 0.003, ⚠ not reproduced), [[RPAP3]] (-0.41, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.75×** | +24.8 | 0e+00 | 40/40 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.86×** | +23.5 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.05×** | +20.9 | 0e+00 | 31/40 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.80×** | +20.9 | 0e+00 | 47/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.92×** | +18.1 | 0e+00 | 45/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +10.8 | 3e-25 | 25/39 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +10.4 | 2e-23 | 30/45 (SNU-423, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +10.2 | 2e-22 | 19/27 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +10.1 | 4e-22 | 22/37 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +9.0 | 1e-17 | 29/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +8.3 | 6e-15 | 24/40 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +8.2 | 2e-14 | 3/9 (LOX-IMVI, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +8.0 | 4e-14 | 6/13 (NCI-H2030, J82, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +7.7 | 6e-13 | 18/38 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.7 | 6e-13 | 20/48 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +7.6 | 1e-12 | 20/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +6.3 | 1e-08 | 19/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +5.7 | 3e-07 | 14/45 (A498, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1635.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[EX229 (drug)]] 0.05 µM in 1 line (HOP62 0.0639×); [[ETC-206 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0717×); [[Resveratrol (drug)]] 0.5 µM in 1 line (C32 0.0746×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -5.2 | 9e-05 | 17/47 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.698×** | -4.8 | 4e-04 | 15/44 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.11 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.32× (z +11.4) | — |
| [[A498 (line)]] | wt | 3.94 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.72× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 3.77 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +18.5) | — |
| [[SNU-423 (line)]] | alt | 9.65 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +13.4) | — |
| [[A-172 (line)]] | wt | 6.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +10.2) | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0746× (z -9.1) |
| [[HOP62 (line)]] | alt | 2.90 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0639× (z -9.5) |
| [[Hs 766T (line)]] | wt | 4.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +8.6) | — |
| [[J82 (line)]] | alt | 4.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +12.4) | — |
| [[LoVo (line)]] | wt | 3.11 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 1 | — | [[ETC-206 (drug)]] 0.05 µM 0.0717× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 6.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 4.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 7.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 5.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +9.5) | — |
| [[A-427 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPNS1]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[CTNS]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 | STRING 485 |
| [[GET3]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[CTSA]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 | STRING 575 |
| [[TPP1]] | +0.61 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[DVL2]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[GNPTG]] | +0.59 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[HEXA]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ZFYVE26]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TOLLIP]] | +0.57 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[WASHC2C]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ATP6V1C1]] | +0.55 | +0.60 / +0.43 | both halves | 3e-05 | pathway: Ion channel transport |

## Genes that move opposite

*3 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF30]] | -0.45 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[PCNX2]] | -0.42 | -0.10 / -0.47 | ⚠ not reproduced | 0.003 |  |
| [[RPAP3]] | -0.41 | -0.18 / -0.41 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MCOLN1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.2, -17.7); signed map (-9.8, -20.9). **Vector** length 51.2, 6.50% of its response variance represented; |z| ≥ 3 in 1,271 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +24.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +20.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.2 | +6.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.9 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | mucolipin TRP cation channel 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,522,624-7,534,009 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRPML1, ML4, MLIV, MST080, MSTP080, TRPM-L1 |
| Gene groups (HGNC) | Mucolipin TRP cation channel family |
| Reactome | 6 pathways, smallest: TRP channels; Transferrin endocytosis and recycling; Iron uptake and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZU1](https://www.uniprot.org/uniprotkb/Q9GZU1) (Mucolipin-1):

> Nonselective cation channel probably playing a role in the regulation of membrane trafficking events and of metal homeostasis. Acts as a Ca(2+)-permeable cation channel with inwardly rectifying activity. Proposed to play a major role in Ca(2+) release from late endosome and lysosome vesicles to the cytoplasm, which is important for many lysosome-dependent cellular events, including the fusion and trafficking of these organelles, exocytosis and autophagy. Required for efficient uptake of large …

**Summary**, from NCBI Gene [57192](https://www.ncbi.nlm.nih.gov/gene/57192):

> This gene encodes a memberof the transient receptor potential (TRP) cation channel gene family. The transmembrane protein localizes to intracellular vesicular membranes including lysosomes, and functions in the late endocytic pathway and in the regulation of lysosomal exocytosis. The channel is permeable to Ca(2+), Fe(2+), Na(+), K(+), and H(+), and is modulated by changes in Ca(2+) concentration. Mutations in this gene result in mucolipidosis type IV. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:13356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13356) · Entrez [57192](https://www.ncbi.nlm.nih.gov/gene/57192) · UniProt [Q9GZU1](https://www.uniprot.org/uniprotkb/Q9GZU1) · Ensembl [ENSG00000090674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090674)

## Data

Gene col 1635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1635); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1635]; `tensor/DDL_lfc|DDL_z.npy` [1635]; `embed/gene_vectors.npy` [1635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1635 or target_col == 1635). Every well: [[MCOLN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCOLN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
