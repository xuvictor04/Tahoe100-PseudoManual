---
symbol: "CCDC61"
type: "gene"
col: 2538
ensembl_id: "ENSG00000104983"
name: "coiled-coil domain containing 61"
location: "19q13.32"
module: 2
arm: "+"
pooled_cpm: 5.09
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CCDC61

*coiled-coil domain containing 61* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.37× (z +13.6, q 2e-39, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.666× (z -4.5, q 0.002, down in 16 of 39 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 0.0640×, HOP62 0.0670×; ⚠ toxic); [[Tucidinostat (drug)]] 0.5 µM in 1 line (HS-578T 0.0517×; ⚠ cell-cycle shift, explains ~5% of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (J82 0.0775×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (A-427 0.124×); [[Tomivosertib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD17A]] (+0.73, fdr 1e-05), [[NOP9]] (+0.68, fdr 9e-06), [[INTS11]] (+0.66, fdr 1e-05); moves opposite to [[LINC02307]] (-0.55, fdr 5e-05), [[LITAF]] (-0.51, fdr 8e-05), [[IRX5]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.37×** | +13.6 | 2e-39 | 45/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.17×** | +12.9 | 1e-35 | 43/45 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +9.6 | 1e-19 | 37/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +6.1 | 2e-07 | 17/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.9 | 8e-05 | 14/39 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.9 | 1e-04 | 3/10 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.33×** | +4.5 | 5e-04 | 8/46 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.7 | 0.016 | 6/27 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.6 | 0.021 | 4/28 (LS 180, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.031 | 10/47 (SW1417, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2538.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (LoVo 0.0640×, HOP62 0.0670×; ⚠ toxic); [[Tucidinostat (drug)]] 0.5 µM in 1 line (HS-578T 0.0517×; ⚠ cell-cycle shift, explains ~5% of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (J82 0.0775×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (A-427 0.124×); [[Tomivosertib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.666×** | -4.5 | 0.002 | 16/39 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.668×** | -4.5 | 0.002 | 16/46 (SNU-1, A-172, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -4.5 | 0.002 | 12/32 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.723×** | -3.6 | 0.043 | 5/47 (SNU-423, AN3 CA, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.736× | -3.3 | 0.11 | 13/44 (MIA PaCa-2, SW480, …) | rises with dose | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.18 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +8.6) | — |
| [[A-427 (line)]] | wt | 6.05 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.124× (z -8.7) |
| [[HOP62 (line)]] | alt | 3.96 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0670× (z -10.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 6.24 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0517× (z -12.0) ⚠ cell-cycle shift, explains ~5% of this change |
| [[J82 (line)]] | alt | 4.19 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0775× (z -9.2) |
| [[LoVo (line)]] | wt | 5.96 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0640× (z -12.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 6.62 | 0 | 1 | — | [[Tomivosertib (drug)]] 0.05 µM 0.105× (z -8.6) |
| [[SW1417 (line)]] | alt | 8.82 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0770× (z -9.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD17A]] | +0.73 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[NOP9]] | +0.68 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[INTS11]] | +0.66 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[LENG8]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[ANAPC2]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[NRBP2]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[FCHSD1]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.60 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NOC2L]] | +0.59 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CPSF1]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02307]] | -0.55 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[LITAF]] | -0.51 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[IRX5]] | -0.50 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[SMNDC1]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MPLKIP]] | -0.50 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[LINC02362]] | -0.49 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CCDC61's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF512]] | C | ZNF512 activity lowers CCDC61's level | lines that do not express ZNF512 (3) vs lines expressing it (47) | 1.58× higher at baseline in the lines without ZNF512 | 0.080 | ⚠ few lines (3 vs 47); across organs; co-occurs with MSH6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.2, -23.7); signed map (-38.0, -22.9). **Vector** length 48.0, 5.40% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +13.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +12.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.3 | +9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.0 | +1.5 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +0.9 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.3 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -2.7 | -3.3 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +2.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 61 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,995,461-46,021,318 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VFL3, hVFL3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6R9](https://www.uniprot.org/uniprotkb/Q9Y6R9) (Centrosomal protein CCDC61):

> Microtubule-binding centrosomal protein required for centriole cohesion, independently of the centrosome-associated protein/CEP250 and rootletin/CROCC linker. In interphase, required for anchoring microtubule at the mother centriole subdistal appendages and for centrosome positioning. During mitosis, may be involved in spindle assembly and chromatin alignment by regulating the organization of spindle microtubules into a symmetrical structure. Has been proposed to play a role in CEP170 …

**Summary**, from NCBI Gene [729440](https://www.ncbi.nlm.nih.gov/gene/729440):

> Enables identical protein binding activity and microtubule binding activity. Involved in centriole assembly and mitotic spindle assembly. Located in centriolar satellite and ciliary basal body. Part of centriolar subdistal appendage. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33629) · Entrez [729440](https://www.ncbi.nlm.nih.gov/gene/729440) · UniProt [Q9Y6R9](https://www.uniprot.org/uniprotkb/Q9Y6R9) · Ensembl [ENSG00000104983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104983)

## Data

Gene col 2538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2538); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2538]; `tensor/DDL_lfc|DDL_z.npy` [2538]; `embed/gene_vectors.npy` [2538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2538 or target_col == 2538). Every well: [[CCDC61 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC61.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
