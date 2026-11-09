---
symbol: "GDPD3"
type: "gene"
col: 2282
ensembl_id: "ENSG00000102886"
name: "glycerophosphodiester phosphodiesterase domain containing 3"
location: "16p11.2"
module: 30
arm: "+"
pooled_cpm: 2.2
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GDPD3

*glycerophosphodiester phosphodiesterase domain containing 3* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.27× (z +6.3, q 1e-07, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.84× (z +3.5, q 0.066, up in 8 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.373× (z -7.6, q 1e-11, down in 24 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA6C]] (+0.67, fdr 7e-06), [[SDHAP1-1]] (+0.66, fdr 1e-05), [[OSBPL7]] (+0.62, fdr 1e-05); moves opposite to [[IMMP2L]] (-0.54, fdr 4e-05), [[CHRAC1]] (-0.53, fdr 1e-05), [[PSME3]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +6.3 | 1e-07 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +4.5 | 0.002 | 3/12 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +3.8 | 0.028 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.5 | 0.066 | 8/20 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.4 | 0.075 | 2/3 (A498, A-172) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.082 | 8/21 (NCI-H2030, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.373×** | -7.6 | 1e-11 | 24/38 (HT-29, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.455×** | -6.3 | 7e-08 | 24/44 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.473×** | -6.0 | 3e-07 | 22/41 (NCI-H1573, NCI-H460, …) | two highest doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -5.8 | 9e-07 | 16/28 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.505×** | -5.5 | 4e-06 | 20/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.661×** | -4.7 | 2e-04 | 18/32 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.683×** | -4.3 | 0.001 | 16/31 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.595×** | -4.2 | 0.002 | 12/40 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.608×** | -4.0 | 0.004 | 16/41 (SNU-423, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.612×** | -3.9 | 0.005 | 11/19 (SW480, NCI-H1573, …) | two highest doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.625×** | -3.8 | 0.008 | 15/44 (HT-29, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.623×** | -3.7 | 0.012 | 11/25 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.639×** | -3.6 | 0.014 | 10/40 (HCT15, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.638×** | -3.5 | 0.021 | 12/33 (NCI-H460, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.756×** | -3.2 | 0.056 | 13/44 (SW1417, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -8.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HOP62 (line)]] | alt | 2.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -8.9) |
| [[A-427 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA6C]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP1-1]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MAPK3]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.6 kb, same strand: neighbours can correlate without regulation) |
| [[EGFL8]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[HDAC10]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LINC00674]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[USP35]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CLIP3]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[MAP2K2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZNF567-DT]] | +0.57 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[MPND]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMMP2L]] | -0.54 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[CHRAC1]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PSME3]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[SLC26A2]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[OMA1]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ADAT1]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[C6orf120]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SMIM15]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[AKAP11]] | -0.50 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TFAM]] | -0.50 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[SPOPL-DT]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GDPD3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.0, -17.9); signed map (-31.1, -1.2). **Vector** length 48.3, 5.99% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.5 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.0 | -6.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | glycerophosphodiester phosphodiesterase domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,104,810-30,113,537 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4171 |
| Reactome | 4 pathways, smallest: Glycerophospholipid catabolism; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5L3](https://www.uniprot.org/uniprotkb/Q7L5L3) (Lysophospholipase D GDPD3):

> Hydrolyzes lysoglycerophospholipids to produce lysophosphatidic acid (LPA) and the corresponding amines. Shows a preference for 1-O-alkyl-sn-glycero-3-phosphocholine (lyso-PAF), lysophosphatidylcholine (lyso-PC) and N-acylethanolamine lysophospholipids. Does not display glycerophosphodiester phosphodiesterase activity, since it cannot hydrolyze either glycerophosphoinositol or glycerophosphocholine.

**Summary**, from NCBI Gene [79153](https://www.ncbi.nlm.nih.gov/gene/79153):

> Enables phosphoric diester hydrolase activity. Involved in N-acylethanolamine metabolic process. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28638) · Entrez [79153](https://www.ncbi.nlm.nih.gov/gene/79153) · UniProt [Q7L5L3](https://www.uniprot.org/uniprotkb/Q7L5L3) · Ensembl [ENSG00000102886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102886)

## Data

Gene col 2282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2282); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2282]; `tensor/DDL_lfc|DDL_z.npy` [2282]; `embed/gene_vectors.npy` [2282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2282 or target_col == 2282). Every well: [[GDPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
