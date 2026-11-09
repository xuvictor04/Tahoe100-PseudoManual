---
symbol: "METTL17"
type: "gene"
col: 9184
ensembl_id: "ENSG00000165792"
name: "methyltransferase like 17"
location: "14q11.2"
module: 17
arm: "+"
pooled_cpm: 16.98
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# METTL17

*methyltransferase like 17* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.47× (z +5.3, q 8e-05, up in 21 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.56× (z +4.5, q 9e-04, up in 19 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.591× (z -10.7, q 9e-24, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC4]] (+0.77, fdr 7e-06), [[OSBPL7]] (+0.74, fdr 7e-06), [[MINDY3]] (+0.70, fdr 7e-06); moves opposite to [[SPON1-AS1]] (-0.62, fdr 1e-05), [[HIVEP2-DT]] (-0.59, fdr 3e-05), [[NPIPB5]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HACE1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.3 | 8e-05 | 21/42 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.8 | 4e-04 | 22/45 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +4.7 | 5e-04 | 21/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +4.5 | 9e-04 | 19/45 (SHP-77, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.76×** | +4.2 | 0.003 | 12/44 (LS 180, C32, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.005 | 19/48 (Panc 03.27, SW48, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.026 | 16/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.28×** | +3.6 | 0.026 | 18/40 (NCI-H460, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.28×** | +3.4 | 0.036 | 14/31 (MIA PaCa-2, KATO III, …) | all doses, flat | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.4 | 0.036 | 13/34 (KATO III, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.25×** | +3.2 | 0.080 | 12/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.080 | 6/46 (C32, A549, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.24×** | +3.1 | 0.080 | 11/47 (A-427, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -10.7 | 9e-24 | 38/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.016 | 18/47 (NCI-H661, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.761×** | -3.9 | 0.018 | 14/47 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.838× | -3.6 | 0.049 | 11/48 (A-427, Panc 03.27, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -3.5 | 0.061 | 5/48 (CHP-212, SK-MEL-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.796× | -3.1 | 0.15 | 18/46 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.805× | -3.1 | 0.16 | 12/47 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 16.4 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0599× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0864× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 9.57 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -13.7) |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0918× (z -14.4) |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.156× (z -8.6) |
| [[KATO III (line)]] | alt | 15.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.1000× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[RKO (line)]] | wt | 20.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.180× (z -9.8) |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0881× (z -11.9) |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.6) |
| [[A-172 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC4]] | +0.77 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[OSBPL7]] | +0.74 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[MRPL22]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[POT1]] | +0.68 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[THYN1]] | +0.68 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[HEATR6]] | +0.68 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TADA1]] | +0.68 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[PRPF39]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MRS2]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NDUFA12]] | +0.67 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPON1-AS1]] | -0.62 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | -0.59 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[NPIPB5]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[CRK]] | -0.58 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[GGPS1]] | -0.57 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[OSTM1]] | -0.57 | -0.60 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACE1]] | C | HACE1 activity raises METTL17's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-3.5, -9.4); signed map (-29.9, -12.1). **Vector** length 85.2, 17.5% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[NG25 (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.9 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase like 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,989,973-20,997,035 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20859; previously METT11D1 |
| Gene groups (HGNC) | 7BS orphan methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7H0](https://www.uniprot.org/uniprotkb/Q9H7H0) (Ribosome assembly protein METTL17, mitochondrial):

> Mitochondrial ribosome (mitoribosome) assembly factor. Binds at the interface of the head and body domains of the mitochondrial small ribosomal subunit (mt-SSU), occluding the mRNA channel and preventing compaction of the head domain towards the body. Probable inactive methyltransferase: retains the characteristic folding and ability to bind S-adenosyl-L-methionine, but it probably lost its methyltransferase activity.

**Summary**, from NCBI Gene [64745](https://www.ncbi.nlm.nih.gov/gene/64745):

> Enables 4 iron, 4 sulfur cluster binding activity. Involved in mitochondrial small ribosomal subunit assembly. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19280) · Entrez [64745](https://www.ncbi.nlm.nih.gov/gene/64745) · UniProt [Q9H7H0](https://www.uniprot.org/uniprotkb/Q9H7H0) · Ensembl [ENSG00000165792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165792)

## Data

Gene col 9184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9184); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9184]; `tensor/DDL_lfc|DDL_z.npy` [9184]; `embed/gene_vectors.npy` [9184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9184 or target_col == 9184). Every well: [[METTL17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
