---
symbol: "ZFP41"
type: "gene"
col: 11202
ensembl_id: "ENSG00000181638"
name: "ZFP41 zinc finger protein"
location: "8q24.3"
module: 16
arm: "+"
pooled_cpm: 8.06
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZFP41

*ZFP41 zinc finger protein* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.10× (z +8.9, q 3e-16, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.380× (z -11.6, q 2e-28, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF252P-1]] (+0.72, fdr 7e-06), [[B3GALT9]] (+0.72, fdr 7e-06), [[TMEM185B]] (+0.70, fdr 7e-06); moves opposite to [[HIGD2A]] (-0.64, fdr 7e-06), [[SLC25A5]] (-0.63, fdr 1e-05), [[ETFDH]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +8.9 | 3e-16 | 38/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +7.4 | 4e-11 | 31/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +6.0 | 4e-07 | 22/47 (HOP62, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +5.0 | 1e-04 | 18/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.44×** | +4.4 | 0.001 | 13/44 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.2 | 0.003 | 15/42 (NCI-H2347, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +4.0 | 0.006 | 5/46 (LS 180, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.023 | 15/44 (NCI-H2347, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.023 | 12/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.037 | 5/46 (PANC-1, C-33 A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.3 | 0.057 | 6/15 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.380×** | -11.6 | 2e-28 | 38/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -9.4 | 2e-18 | 32/43 (SHP-77, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.813×** | -8.1 | 8e-14 | 37/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -6.9 | 9e-10 | 28/46 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.614×** | -5.9 | 5e-07 | 22/46 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.594×** | -5.0 | 6e-05 | 17/37 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -4.6 | 3e-04 | 20/47 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.686×** | -4.5 | 4e-04 | 16/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 0.609× | -3.1 | 0.12 | 15/39 (HT-29, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.775× | -3.1 | 0.12 | 10/45 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.5 µM 0.0872× (z -10.5) |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0934× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 8.28 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0887× (z -8.8) |
| [[Hs 766T (line)]] | wt | 6.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0836× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 9.02 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -8.7) |
| [[LoVo (line)]] | wt | 7.96 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 6.73 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -9.4) |
| [[PANC-1 (line)]] | alt | 8.97 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -9.4) |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0841× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF252P-1]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[B3GALT9]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[ZNF623]] | +0.67 | +0.75 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF252P]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 | same gene group |
| [[PURB]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 | same gene group |
| [[ZNF839]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 | same gene group |
| [[CEP41]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.65 | +0.79 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIGD2A]] | -0.64 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[SLC25A5]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[ETFDH]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ABHD18]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.60 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[NDUFA1]] | -0.60 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NARF]] | -0.60 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[NDUFA4]] | -0.59 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[HINT1]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[TESK2]] | -0.58 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[C9orf153]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[APTR]] | -0.58 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ZFP41's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.3, 17.6); signed map (-0.9, -31.5). **Vector** length 56.7, 8.12% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -11.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ZFP41 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,246,821-143,262,705 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38705, FLJ00028, ZNF753 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8Y5](https://www.uniprot.org/uniprotkb/Q8N8Y5) (Zinc finger protein 41 homolog):

> A putative DNA-binding regulatory protein associated with meiosis in spermatogenesis.

**Summary**, from NCBI Gene [286128](https://www.ncbi.nlm.nih.gov/gene/286128):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26786) · Entrez [286128](https://www.ncbi.nlm.nih.gov/gene/286128) · UniProt [Q8N8Y5](https://www.uniprot.org/uniprotkb/Q8N8Y5) · Ensembl [ENSG00000181638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181638)

## Data

Gene col 11202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11202); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11202]; `tensor/DDL_lfc|DDL_z.npy` [11202]; `embed/gene_vectors.npy` [11202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11202 or target_col == 11202). Every well: [[ZFP41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
